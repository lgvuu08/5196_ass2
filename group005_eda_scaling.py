"""Group005 Task 1.0 exploratory analysis and Task 3.3 scaling comparison."""

from pathlib import Path
import json

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas as pd
from IPython.display import display


SCALING_ATTRIBUTES = ("order_count", "total_paid", "mean_delivery_distance")


def _display_eda_table(frame, *, show_index=True):
    """Show a high-contrast, lightly striped EDA table in the notebook."""
    edge = "1px solid #bac8d6"
    grid = [
        {"selector": "", "props": [("border-collapse", "collapse")]},
        {"selector": "thead th", "props": [("border", edge),
                                            ("background-color", "#243b53"),
                                            ("color", "#ffffff"),
                                            ("padding", "6px 9px")]},
        {"selector": "tbody th", "props": [("border", edge),
                                            ("background-color", "#e8f0f8"),
                                            ("color", "#102a43"),
                                            ("padding", "5px 9px")]},
        {"selector": "td", "props": [("border", edge),
                                      ("background-color", "#ffffff"),
                                      ("color", "#102a43"),
                                      ("padding", "5px 9px")]},
        {"selector": "tbody tr:nth-child(even) td",
         "props": [("background-color", "#f2f6fa")]},
    ]
    styled = frame.style.set_table_styles(grid)
    if not show_index:
        styled = styled.hide(axis="index")
    display(styled)


def initial_eda(batches, warehouses):
    """Inspect original strings without modifying any source batch."""
    raw = {name: frame.drop(columns="source_batch", errors="ignore")
           for name, frame in batches.items()}
    columns = tuple(next(iter(raw.values())).columns)
    valid_warehouses = set(warehouses["warehouse"].astype(str))
    domains = {
        "nearest_warehouse": valid_warehouses,
        "season": {"Summer", "Autumn", "Winter", "Spring"},
        "is_expedited_delivery": {"True", "False"},
        "is_happy_customer": {"True", "False"},
    }

    def cart_ok(value):
        try:
            cart = json.loads(value)
            return (isinstance(cart, list) and len(cart) > 0
                    and all(isinstance(item, dict)
                            and isinstance(item.get("product"), str)
                            and bool(item["product"])
                            and type(item.get("quantity")) is int
                            and item["quantity"] > 0 for item in cart))
        except (TypeError, ValueError, KeyError):
            return False

    key_rows, domain_rows, numeric_rows = [], [], []
    blank_columns = {}
    numeric_fields = ("order_price", "delivery_charges", "order_total",
                      "distance_to_nearest_warehouse", "customer_lat",
                      "customer_long", "coupon_discount")
    for name, frame in raw.items():
        blank = frame.eq("")
        blank_columns[name] = blank.sum()
        key_rows.append({
            "batch": name, "rows": len(frame), "columns": len(frame.columns),
            "schema_matches": tuple(frame.columns) == columns,
            "all_raw_fields_text": all(pd.api.types.is_string_dtype(t) for t in frame.dtypes),
            "blank_order_ids": int(blank["order_id"].sum()),
            "duplicate_order_ids": int(frame["order_id"].duplicated().sum()),
            "duplicate_rows": int(frame.duplicated().sum()),
            "rows_with_blanks": int(blank.any(axis=1).sum()),
            "blanks": int(blank.to_numpy().sum()),
            "invalid_carts": int((~frame["shopping_cart"].map(cart_ok)).sum()),
        })
        for field, allowed in domains.items():
            counts = frame[field].value_counts(dropna=False).sort_index()
            domain_rows.append({
                "batch": name, "field": field,
                "blank": int(counts.get("", 0)),
                "invalid_nonblank": int((~frame[field].isin(allowed | {""})).sum()),
                "observed_values": ", ".join(f"{value or '<blank>'}: {count}"
                                             for value, count in counts.items()),
            })
        for field in numeric_fields:
            values = pd.to_numeric(frame[field].replace("", np.nan), errors="coerce")
            observed = values.dropna()
            numeric_rows.append({
                "batch": name, "field": field, "n": len(observed),
                "parse_failures": int((values.isna() & frame[field].ne("")).sum()),
                "min": observed.min(), "q1": observed.quantile(.25),
                "median": observed.median(), "q3": observed.quantile(.75),
                "max": observed.max(),
            })

    keys = pd.DataFrame(key_rows).set_index("batch")
    missingness = pd.DataFrame(blank_columns).T
    categories = pd.DataFrame(domain_rows)
    numeric = pd.DataFrame(numeric_rows)
    all_ids = pd.concat([frame["order_id"] for frame in raw.values()], ignore_index=True)
    print("EDA-01 · Structure, keys and row-level missingness")
    _display_eda_table(keys)
    print(f"Cross-batch order-ID collisions: {int(all_ids.duplicated().sum())}")
    print("\nEDA-02 · Blank cells by batch and field (zero-only fields omitted)")
    _display_eda_table(missingness.loc[:, missingness.sum().gt(0)])
    print("\nEDA-03 · Categorical domains, including exact raw spellings")
    _display_eda_table(categories, show_index=False)
    print("\nCoupon levels (percent):")
    for name, frame in raw.items():
        print(f"  {name}: {frame['coupon_discount'].value_counts().sort_index().to_dict()}")
    print("\nEDA-04 · Raw numeric distributions; not yet cleaned")
    _display_eda_table(numeric.round(4), show_index=False)

    colors = {"dirty": "#2563a6", "missing": "#d97706", "outlier": "#7c3aed"}
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 4.1), layout="constrained")
    charges = [pd.to_numeric(raw[name]["delivery_charges"].replace("", np.nan),
                             errors="coerce").dropna() for name in raw]
    boxes = axes[0].boxplot(
        charges,
        tick_labels=[f"{name}\n(n={len(values)})"
                     for name, values in zip(raw, charges)],
        patch_artist=True,
        medianprops={"color": "#172b4d", "linewidth": 1.6},
        flierprops={"marker": "o", "markersize": 3,
                    "markerfacecolor": "none", "markeredgecolor": "#475569"},
    )
    for patch, name in zip(boxes["boxes"], raw):
        patch.set_facecolor(colors[name])
        patch.set_alpha(.22)
    axes[0].set(title="Raw delivery charges by batch", ylabel="Charge (AUD)")
    for name, frame in raw.items():
        if name == "dirty":
            continue
        distance = pd.to_numeric(frame["distance_to_nearest_warehouse"].replace("", np.nan), errors="coerce")
        charge = pd.to_numeric(frame["delivery_charges"].replace("", np.nan), errors="coerce")
        observed = distance.notna() & charge.notna()
        axes[1].scatter(distance[observed], charge[observed], s=15, alpha=.45,
                        color=colors[name], label=f"{name} (n={observed.sum()})")
    axes[1].set(title="Distance and charge (unadjusted)",
                xlabel="Distance (km)", ylabel="Charge (AUD)")
    axes[1].legend(frameon=False, fontsize=9)
    for ax in axes:
        ax.grid(axis="y", color="#dbe3eb", linewidth=.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    plt.show()

    distributions = (
        ("order_price", "Order price", "AUD"),
        ("order_total", "Order total", "AUD"),
        ("distance_to_nearest_warehouse", "Warehouse distance", "km"),
    )
    fig, axes = plt.subplots(1, 3, figsize=(12.8, 3.6), layout="constrained")
    for ax, (field, title, unit) in zip(axes, distributions):
        values_by_batch = {
            name: pd.to_numeric(frame[field].replace("", np.nan),
                                errors="coerce").dropna().to_numpy()
            for name, frame in raw.items()
        }
        pooled = np.concatenate(list(values_by_batch.values()))
        edges = np.linspace(pooled.min(), pooled.max(), 29)
        for name, values in values_by_batch.items():
            ax.hist(values, bins=edges, weights=np.full(len(values), 1 / len(values)),
                    histtype="step", linewidth=1.7, color=colors[name],
                    label=f"{name} (n={len(values)})")
        ax.set(title=title, xlabel=unit, ylabel="Share of observed orders")
        ax.yaxis.set_major_formatter(PercentFormatter(1))
        ax.grid(axis="y", color="#dbe3eb", linewidth=.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(frameon=False, fontsize=8)
    plt.show()
    return {"keys": keys, "missingness": missingness,
            "categories": categories, "numeric": numeric}


def scaling_profiles_from_cleaned(paths):
    """Build only the three Task 3.3 columns from submitted cleaned CSVs."""
    paths = [Path(path) for path in paths]
    absent = [str(path) for path in paths if not path.is_file()]
    if absent:
        raise FileNotFoundError("Task 3.3 requires all final cleaned CSVs: " + ", ".join(absent))
    frames = [pd.read_csv(path, dtype=str, keep_default_na=False) for path in paths]
    required = {"order_id", "customer_id", "order_total", "distance_to_nearest_warehouse"}
    for path, frame in zip(paths, frames):
        if not required.issubset(frame):
            raise ValueError(f"{path}: missing required columns {sorted(required - set(frame))}")
        if frame["order_id"].eq("").any() or not frame["order_id"].is_unique:
            raise ValueError(f"{path}: blank or duplicate order_id")
    orders = pd.concat(frames, ignore_index=True)
    if not orders["order_id"].is_unique:
        raise ValueError("Cleaned batches contain cross-batch duplicate order_id")
    if orders["customer_id"].eq("").any():
        raise ValueError("A cleaned customer_id is blank")
    for field in ("order_total", "distance_to_nearest_warehouse"):
        orders[field] = pd.to_numeric(orders[field], errors="raise")
        if not np.isfinite(orders[field]).all():
            raise ValueError(f"{field} contains non-finite values")
    profile = orders.groupby("customer_id").agg(
        order_count=("order_id", "size"),
        total_paid=("order_total", "sum"),
        mean_delivery_distance=("distance_to_nearest_warehouse", "mean"),
    )
    return profile


def compare_scaling(profile, attributes=SCALING_ATTRIBUTES):
    """Compare affine scalers on the same immutable customer-level baseline."""
    attributes = tuple(attributes)
    if len(attributes) != 3 or len(set(attributes)) != 3:
        raise ValueError("Choose exactly three distinct profile attributes")
    if len(profile) < 2:
        raise ValueError("At least two customer profiles are required")
    x = profile.loc[:, attributes].apply(pd.to_numeric, errors="raise").astype(float).copy()
    if x.isna().any().any() or not np.isfinite(x.to_numpy()).all():
        raise ValueError("Scaling requires complete finite attributes")
    mean, std, low, high = x.mean(), x.std(ddof=0), x.min(), x.max()
    span = high - low
    constant = [name for name in attributes if std[name] == 0 or span[name] == 0]
    if constant:
        raise ValueError(f"Constant attributes cannot be scaled meaningfully: {constant}")
    z = (x - mean) / std
    mm = (x - low) / span
    summary = pd.DataFrame({
        "original_min": low, "original_median": x.median(), "original_max": high,
        "original_std": std, "z_mean": z.mean(), "z_std": z.std(ddof=0),
        "z_min": z.min(), "z_max": z.max(),
        "minmax_min": mm.min(), "minmax_median": mm.median(),
        "minmax_max": mm.max(),
        "original_IQR": x.quantile(.75) - x.quantile(.25),
        "z_IQR": z.quantile(.75) - z.quantile(.25),
        "minmax_IQR": mm.quantile(.75) - mm.quantile(.25),
    })
    # Each variance's share equals its expected contribution to squared
    # Euclidean distance over independent random customer pairs.
    variance = pd.DataFrame({
        "original": x.var(ddof=0), "z_score": z.var(ddof=0),
        "min_max": mm.var(ddof=0),
    })
    contributions = variance.div(variance.sum(axis=0), axis=1)
    print(f"SCALE-01 · {len(x)} customers; attributes: {attributes}")
    print(summary.round(5).to_string())
    print("\nSCALE-02 · Variance share of expected squared Euclidean distance")
    print(contributions.round(4).to_string())
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), layout="constrained")
    for ax, (title, frame) in zip(axes, (("Original", x), ("Z-score", z), ("Min–max", mm))):
        ax.boxplot([frame[col] for col in attributes], tick_labels=attributes,
                   showfliers=True)
        ax.set_title(title)
        ax.tick_params(axis="x", rotation=28)
    plt.show()
    return {"baseline": x, "z_score": z, "min_max": mm,
            "summary": summary, "distance_contributions": contributions}
