# **FIT5196 A2 — Explicit Assignment Pipeline and Task-by-Task Requirements**

The assignment is best treated as a **dependency-driven data-quality pipeline**, not as three independent cleaning exercises. You must first establish reliable business rules and reusable calculations, then clean the three batches, validate every modification, and only after that perform the customer-level transformation analysis.

The assessment is worth **20 marks**: Task 1 \= 15, Task 2 \= 2, Task 3 \= 3\. The three source batches contain 500 orders each and represent different orders rather than three versions of the same records.

---

# **1\. Overall Assignment Pipeline**

Stage 0  
Environment \+ input verification  
        ↓  
Stage 1  
Initial EDA and data-quality diagnosis  
        ↓  
Stage 2  
Reconstruct trusted business relationships  
    ├── current product prices  
    ├── order arithmetic  
    ├── date → season  
    ├── coordinates → nearest warehouse \+ distance  
    ├── review → happiness  
    └── seasonal delivery models  
        ↓  
Stage 3  
TASK 1A — Dirty-data cleansing  
        ↓  
Stage 4  
TASK 1B — Missing-value recovery  
        ↓  
Stage 5  
TASK 1C — Delivery-charge outlier removal  
        ↓  
Stage 6  
Write three cleaned CSVs  
        ↓  
Stage 7  
TASK 2 — Generate audit log  
        ↓  
Stage 8  
TASK 2 — Re-read outputs and validate  
        ↓  
Stage 9  
TASK 3 — Combine cleaned outputs for analysis only  
        ↓  
Stage 10  
Customer-level aggregation  
        ↓  
Stage 11  
Transformation/scaling comparison  
        ↓  
Stage 12  
Treatment recommendations  
        ↓  
Stage 13  
Full reproducibility \+ final submission checks

The dependency order matters because later decisions rely on quantities established earlier. For example:

shopping\_cart  
    ↓  
infer current product prices  
    ↓  
reconstruct order\_price  
    ↓  
check order\_total

date  
    ↓  
derive season  
    ↓  
select correct seasonal delivery model

coordinates  
    ↓  
nearest warehouse  
    ↓  
distance

latest\_customer\_review  
    ↓  
VADER  
    ↓  
is\_happy\_customer

distance \+ expedited \+ happiness \+ season  
    ↓  
expected delivery charge  
    ↓  
missing delivery recovery / residual outlier detection  
---

# **2\. Stage 0 — Setup and Input Verification**

## **Objective**

Establish that you are analysing the correct group package and that the input data satisfy the expected structural contract before attempting repairs.

## **Required checks**

Confirm:

* correct `GroupNNN` identifier;  
* three order datasets exist;  
* each contains 500 rows initially;  
* each uses the expected 16-column schema;  
* grain is one row per order;  
* `order_id` is unique;  
* IDs are distinct across the three batches;  
* `warehouses.csv` loads correctly;  
* local VADER resource files exist;  
* manifest/checksum information is available.

The specification states that the batches correspond to:

* dirty values;  
* missing values;  
* delivery-charge outliers.

## **Notebook section**

Recommended heading:

0\. Configuration and Input Verification  
0.1 Environment and dependency versions  
0.2 Group configuration and paths  
0.3 Input manifest verification  
0.4 Schema and grain checks  
0.5 VADER resource verification

## **Critical requirement**

Put `GROUP_ID`, input path and output path in one configurable location. Your notebook must work without changing cleaning logic, private Drive paths, internet downloads or manual file replacement. A fresh kernel \+ `Run All` must recreate the outputs offline.

---

# **3\. Stage 1 — Initial EDA and Diagnosis**

This is an explicit Task 1 requirement, not optional decoration.

You need **EDA that supports diagnosis**, rather than general charts included for presentation purposes.

The specification explicitly expects investigation of:

* schema and types;  
* missingness;  
* distributions;  
* categorical values;  
* key integrity;  
* relevant relationships;  
* observations suitable or unsuitable for later models.

## **Recommended structure**

1\. Initial Data Investigation

1.1 Shape, schema and datatype checks  
1.2 ID uniqueness and grain  
1.3 Missingness profile by batch  
1.4 Numeric ranges and distributions  
1.5 Categorical-domain checks  
1.6 Date-format inspection  
1.7 Coordinate/location plausibility  
1.8 Shopping-cart structure  
1.9 Arithmetic consistency  
1.10 Delivery-charge relationships

## **What the EDA should actually answer**

Instead of:

> “Here is a histogram of delivery charges.”

You need reasoning such as:

> “Delivery charge varies systematically with distance and operational/customer indicators, so raw charge magnitude cannot by itself identify outliers.”

Similarly, categorical tables should establish whether values violate known domains, and relationship checks should establish which variables can later reconstruct corrupted or missing fields.

---

# **4\. Stage 2 — Establish the Trusted Business Rules**

This is the analytical foundation for Task 1\.

You should ideally implement these as reusable functions because the same relationships will be used repeatedly for diagnosis, correction and validation.

---

## **4.1 Shopping Cart Parsing**

`shopping_cart` must be parsed as JSON.

Required approach:

json.loads(...)

Do not use `eval`.

The cart contains objects such as:

\[  
  {"product": "...", "quantity": 2}  
\]

Product names and quantities are guaranteed reliable and must be preserved.

---

# **5\. Stage 2A — Infer Current Product Prices**

This is one of the most important upstream reconstruction problems.

## **Requirement**

Within A2:

> each product has one current unit price across all three batches.

You must infer those prices from **reliable shopping-cart/order-price equations**.

You cannot use:

* A1 prices as authoritative;  
* another group's price vector;  
* manually supplied answer lists.

## **Conceptual formulation**

For order ii:

qi1p1+qi2p2+⋯+qikpk=order\_priceiq\_{i1}p\_1 \+ q\_{i2}p\_2 \+ \\cdots \+ q\_{ik}p\_k \= \\text{order\\\_price}\_i

Across reliable orders:

Qp=yQp \= y

where:

* QQ \= cart quantity matrix;  
* pp \= unknown current product-price vector;  
* yy \= reliable `order_price`.

## **Notebook evidence expected**

Show:

2.1 Price reconstruction  
\- observations included  
\- observations excluded and why  
\- equation construction  
\- solution method  
\- inferred price vector  
\- independent verification  
\- reconstruction error

## **Critical quality requirement**

Do not merely solve the system.

Also verify the inferred prices against **suitable unused or independently reliable orders**.

The specification explicitly expects explanation of:

* equations;  
* evidence selection;  
* checking of inferred prices.

---

# **6\. Stage 2B — Order Arithmetic**

Once prices are established, reconstruct:

### **`order_price`**

For each cart item:

item amount=round⁡(quantity×unit price,2)\\text{item amount} \= \\operatorname{round}(quantity\\times unit\\ price,2)

Then:

order\_price=round⁡(∑item amounts,2)\\text{order\\\_price} \= \\operatorname{round} \\left( \\sum \\text{item amounts}, 2 \\right)

### **`order_total`**

order\_total=round⁡\[order\_price(1−coupon\_discount100)+delivery\_charges,2\]\\text{order\\\_total} \= \\operatorname{round} \\left\[ \\text{order\\\_price} \\left(1-\\frac{\\text{coupon\\\_discount}}{100}\\right) \+ \\text{delivery\\\_charges}, 2 \\right\]

Important:

* coupon applies only to item price;  
* delivery is added after discount;  
* do not separately round the discounted subtotal;  
* do not add GST;  
* do not add A1 columns.

---

# **7\. Stage 2C — Date and Season Logic**

## **Date output**

All dates must ultimately be:

YYYY-MM-DD

Slash-formatted dates are interpreted day-first.

## **Season mapping**

| Months | Season |
| ----- | ----- |
| December, January, February | Summer |
| March, April, May | Autumn |
| June, July, August | Winter |
| September, October, November | Spring |

## **Dependency**

date  
 ↓  
month  
 ↓  
expected season

Therefore, if date and season disagree, do **not** automatically assume both are wrong.

Use batch guarantees and independent evidence to identify the single corrupted field.

---

# **8\. Stage 2D — Warehouse and Geographic Reconstruction**

For every customer coordinate:

1. calculate Haversine distance to all supplied warehouses;  
2. use Earth radius \= **6371 km**;  
3. choose the minimum;  
4. assign the corresponding `nearest_warehouse`.

Required reconstructed distance precision:

4 decimal places

Do not use:

* road networks;  
* shortest-path algorithms;  
* graph data.

Also inspect whether coordinates are plausible for Melbourne before trusting the distances.

## **Reusable output**

For each row you should effectively be able to derive:

expected\_nearest\_warehouse  
expected\_distance

These become independent evidence for detecting dirty geographic fields.

---

# **9\. Stage 2E — Customer Review → Happiness**

This transformation is tightly specified.

Apply the package-local NLTK VADER model to `latest_customer_review`.

is\_happy\_customer={Truecompound≥0.05Falsecompound\<0.05is\\\_happy\\\_customer \= \\begin{cases} True & compound \\ge 0.05 \\\\ False & compound \< 0.05 \\end{cases}

Exception:

"No review submitted" → True

The sentinel is not missing data.

Do not:

* translate reviews;  
* remove punctuation;  
* clean/rewrite text;  
* reproduce A1 language filtering;  
* download a substitute lexicon.

You must verify and use the supplied local lexicon and required NLTK version.

---

# **10\. Stage 2F — Seasonal Delivery-Charge Models**

This is another central analytical component.

There must be **four models**, one per season.

General relationship:

delivery\_charge=β0+β1(distance)+β2(expedited)+β3(happy)+ϵdelivery\\\_charge \= \\beta\_0 \+ \\beta\_1(distance) \+ \\beta\_2(expedited) \+ \\beta\_3(happy) \+ \\epsilon

Predictors:

distance\_to\_nearest\_warehouse  
is\_expedited\_delivery  
is\_happy\_customer

plus intercept.

---

## **Required modelling evidence**

For each season report:

Training n  
Held-out n  
R²  
Absolute-error metric

For example:

MAE

Evaluation must be on **held-out observations**.

An in-sample score alone does not satisfy this requirement.

Clean data should normally produce very strong fit, approximately:

R2≥0.99R^2 \\ge 0.99

A materially weaker fit should trigger further investigation.

---

# **11\. TASK 1A — Dirty-Data Cleansing**

## **Marks**

**6 marks for dirty outputs**, within Task 1's 15 marks.

## **Core objective**

Identify rows containing incorrect or inconsistently represented values and repair **only the genuinely incorrect field**.

All 500 order IDs must remain.

---

## **Critical guarantee**

A dirty-data row contains:

> at most one intentionally incorrect field.

A row may also be completely correct.

This guarantee should control your reasoning.

For example:

wrong date  
   ↓  
date-season check fails  
   ↓  
delivery-model consistency may also appear wrong

This does **not** imply both `date` and `season` should be changed.

You must identify the underlying corrupted field.

---

## **Recommended diagnostic matrix**

For every row create expected/check variables such as:

expected\_date\_format  
expected\_season  
expected\_order\_price  
expected\_order\_total  
expected\_nearest\_warehouse  
expected\_distance  
expected\_happy  
expected\_delivery

Then compare:

observed vs expected

This lets you distinguish a root error from downstream inconsistencies.

---

## **Dirty-data workflow**

### **1\. Detect candidates**

Use:

* domain validation;  
* arithmetic identities;  
* geographic reconstruction;  
* review/happiness reconstruction;  
* seasonal delivery relationship.

### **2\. Diagnose root field**

Ask:

> Which single corrupted field can explain the observed failures?

### **3\. Repair only that field**

Do not change dependent correct values merely to force consistency.

### **4\. Re-run all checks**

The repaired record should satisfy the broader business rules.

### **5\. Log change**

One audit entry per corrected field.

---

## **Mandatory preservation rule**

Several fields are explicitly guaranteed complete and correct:

order\_id  
customer\_id  
shopping\_cart  
customer\_long  
coupon\_discount  
latest\_customer\_review

Preserve their information.

---

# **12\. TASK 1B — Missing-Data Recovery**

## **Marks**

**3 marks.**

## **Core objective**

Recover missing fields using the strongest defensible evidence available.

The missing batch:

* contains missing values only;  
* all observed values are correct;  
* missing values are represented by empty CSV fields.

Therefore:

OBSERVED value \= trusted  
MISSING value \= needs reconstruction

Do not “clean” nonmissing cells in this batch.

---

## **Required decision hierarchy**

Use strongest available information first.

### **Level 1 — Deterministic reconstruction**

Examples:

date → season  
cart \+ inferred prices → order\_price  
order\_price \+ coupon \+ delivery → order\_total  
coordinates → warehouse/distance  
review → happiness

### **Level 2 — Algebraic reverse calculation**

When mathematically identifiable.

For instance, if everything except delivery is known:

delivery=order\_total−order\_price(1−discount100)delivery \= order\\\_total \- order\\\_price \\left(1-\\frac{discount}{100}\\right)

### **Level 3 — Model-based imputation**

For quantities not deterministically recoverable, such as a delivery charge in an appropriate situation.

Then document:

* training observations;  
* model;  
* validation;  
* estimate;  
* uncertainty/confidence.

---

## **Explicit prohibition**

Do not apply one blanket:

mean  
median  
mode

to all missing values.

---

## **Output requirement**

GroupNNN\_missing\_clean.csv

must retain **all original 500 IDs**.

---

# **13\. TASK 1C — Delivery-Charge Outlier Removal**

## **Marks**

**2 marks.**

## **Core objective**

Identify anomalous `delivery_charges` using the seasonal models and **remove the corresponding rows**.

Do not replace the anomalous charge and retain the row.

---

# **14\. Outlier Logic — What You Are Actually Detecting**

A large delivery charge is **not automatically an outlier**.

The correct concept is the residual:

ei=observed\_deliveryi−predicted\_deliveryie\_i \= observed\\\_delivery\_i \- predicted\\\_delivery\_i

You therefore need to identify **unexpected charges conditional on their predictors**, rather than extreme raw values.

The specification explicitly distinguishes:

large charge ≠ necessarily anomalous  
large residual \= potential anomaly  
---

## **Required pipeline**

Fit seasonal models  
        ↓  
Generate predictions  
        ↓  
Calculate residuals  
        ↓  
Inspect residual distributions  
        ↓  
Define justified decision rule  
        ↓  
Identify anomalous records  
        ↓  
Remove rows  
        ↓  
Refit/check retained population  
---

## **Decision rule**

The assignment does not prescribe one mandatory numerical threshold.

You must:

* select a residual-based rule;  
* explain why;  
* show evidence;  
* demonstrate that valid unusual orders are preserved.

Do not confuse output-marking tolerances with an outlier threshold.

---

# **15\. TASK 1 Methodology and Documentation**

Task 1 is not marked only on final CSV values.

Breakdown:

| Component | Marks |
| ----- | ----- |
| Dirty outputs | 6 |
| Missing outputs | 3 |
| Outlier outputs | 2 |
| Methodology | 3 |
| Documentation/reproducibility | 1 |
| Total | 15 |

Your notebook should therefore expose the reasoning chain:

diagnosis  
→ evidence  
→ decision  
→ correction/removal  
→ validation

Not:

load data  
→ mysterious cleaning function  
→ save final CSV  
---

# **16\. TASK 2 — Audit Trail**

## **Marks**

**2 marks total for Task 2: audit trail \+ validation.**

## **Required file**

audit\_log.csv

Required columns, exactly in this order:

source\_file  
record\_key  
field\_name  
issue\_type  
original\_value  
corrected\_value  
method  
evidence  
confidence  
---

# **17\. Audit Log Requirements**

## **One row for**

Every:

corrected dirty field  
missing value imputed  
outlier row removed

Do not log:

* unchanged values;  
* formatting-only CSV changes;  
* harmless quoting differences.

For missing values:

original\_value \= \<MISSING\>

For outlier removal:

field\_name \= delivery\_charges  
corrected\_value \= ROW\_REMOVED  
issue\_type \= outlier\_row  
---

# **18\. Confidence Levels**

You must define:

high  
medium  
low

in the notebook.

A defensible framework could be:

High  
Exact deterministic reconstruction from trusted business rule.

Medium  
Strong model-based estimate with validated relationship and small uncertainty.

Low  
Evidence supports a choice but meaningful uncertainty remains.

The precise definitions are yours, but they must be declared and used consistently.

---

# **19\. Audit Evidence**

The `evidence` field should contain a concise traceable reference.

Better:

CHECK-GEO-04: Haversine reconstruction uniquely identifies Thompson

rather than:

value looked wrong

Your notebook can define numbered checks such as:

PRICE-01  
ARITH-02  
DATE-01  
GEO-03  
VADER-01  
DELIV-WIN-02

Then use those IDs inside `audit_log.csv`.

The specification explicitly allows this approach.

---

# **20\. TASK 2 — Post-Output Validation**

This is separate from cleaning.

After writing the three CSVs and audit log:

> read the files back from disk.

Then test the **actual submitted files**.

---

## **Validation Block A — Structural integrity**

Check:

schema exactly 16 columns  
column order correct  
no index column  
parseability  
data types/representations valid  
---

## **Validation Block B — IDs and row counts**

Dirty:

500 IDs retained

Missing:

500 IDs retained

Outlier:

only intended IDs removed  
no additional IDs lost  
---

## **Validation Block C — Shopping cart and prices**

Verify:

valid JSON  
positive integer quantities  
product names preserved  
reconstructed price system still holds  
---

## **Validation Block D — Business rules**

Recheck:

date ↔ season  
coordinate ↔ warehouse  
coordinate ↔ distance  
review ↔ happiness  
order\_price arithmetic  
order\_total arithmetic  
---

## **Validation Block E — Delivery models**

For retained rows verify:

per-season fit remains strong  
residual behaviour sensible  
removed rows reconcile with outlier decisions  
---

## **Validation Block F — Preservation**

Compare original and output files.

For every modified cell:

must be present in audit\_log

For every unchanged source cell:

should remain semantically unchanged  
---

## **Validation Block G — Audit reconciliation**

You should be able to establish:

{actual changed cells}={logged changed cells}\\{\\text{actual changed cells}\\} \= \\{\\text{logged changed cells}\\}

and:

{removed IDs}={audit outlier rows}\\{\\text{removed IDs}\\} \= \\{\\text{audit outlier rows}\\}

The specification explicitly requires agreement between input/output differences and the audit log.

---

# **21\. TASK 3 — Customer Profiling and Transformation**

## **Marks**

**3 marks**

Split into:

Comparison and evidence        2 marks  
Recommendation/limitations     1 mark  
---

# **22\. Task 3 Purpose**

The purpose is specifically:

> prepare numeric customer-profile attributes for possible future **distance-based exploratory segmentation**.

You are investigating whether:

different units  
different scales  
different distributions

would dominate distance comparisons between customers.

You are **not required** to perform clustering.

Do not:

* choose number of clusters;  
* fit a segmentation model;  
* build a prediction model;  
* build a dashboard.

---

# **23\. Task 3 Dataset Construction**

Read your **three submitted cleaned CSVs**.

Concatenate:

dirty\_clean  
\+  
missing\_clean  
\+  
outlier\_clean

while retaining source-batch identity.

Important:

do not restore removed outliers  
do not append A1  
do not use another group's data

Report:

dirty output row count  
missing output row count  
outlier output row count  
combined distinct orders  
number of customers

Then aggregate:

one row per customer\_id  
---

# **24\. Select Exactly Three Customer Attributes**

Choose three from:

| Attribute | Definition |
| ----- | ----- |
| `order_count` | number of distinct orders |
| `total_paid` | sum of `order_total` |
| `mean_order_value` | mean `order_total` |
| `mean_delivery_distance` | mean warehouse distance |

---

# **25\. Feature-Selection Requirement**

Selection itself requires justification.

Think in terms of whether the variables represent distinct customer dimensions such as:

activity  
spending  
order intensity  
delivery geography

A critical warning applies if you choose:

order\_count  
total\_paid  
mean\_order\_value

because approximately:

total\_paid=order\_count×mean\_order\_valuetotal\\\_paid \= order\\\_count \\times mean\\\_order\\\_value

So those features are algebraically dependent and could double-count spending behaviour in Euclidean distance.

The specification explicitly requires discussion of this issue.

---

# **26\. Task 3 — Original Baseline**

Before transformation, show each selected attribute in its original form.

At minimum inspect:

units  
range  
mean/median  
spread  
skewness/distribution  
extreme values  
relationships among attributes

The actual analytical question is:

> If these raw features entered a distance calculation, would one feature dominate because of scale rather than because it represents more important behaviour?

---

# **27\. Required Scaling Comparison**

You must compare both:

## **Standardisation**

z=x−μσz=\\frac{x-\\mu}{\\sigma}

and

## **Min-max scaling**

x′=x−min⁡(x)max⁡(x)−min⁡(x)x'=\\frac{x-\\min(x)} {\\max(x)-\\min(x)}

on **all three selected attributes**.

You must interpret the consequences, rather than merely showing transformed columns.

Relevant issues:

relative distances  
sensitivity to extremes  
interpretability  
boundedness  
variance preservation  
---

# **28\. Required Nonlinear Transformation Comparison**

At least one selected attribute must also be compared against an applicable nonlinear transformation such as:

log  
log1p  
square root

You must explain:

* mathematical domain;  
* whether zeros exist;  
* suitability;  
* actual effect.

---

# **29\. Important Task 3 Reasoning Constraint**

Do not use this logic:

skewed → log transform automatically

The specification explicitly rejects that shortcut.

Neither:

normality  
lower skewness  
higher R²

is automatically the optimisation objective.

The real objective is whether the transformation is appropriate for **distance-based customer comparison**.

---

# **30\. Transformation Order**

If you combine nonlinear transformation and scaling, state the order explicitly.

For example:

raw total\_paid  
    ↓  
log1p  
    ↓  
standardisation

is not equivalent to an unspecified treatment.

---

# **31\. Required Final Recommendation Table**

Task 3 explicitly requires one concise table with one row per selected feature.

Recommended structure:

| Attribute | Methods compared | Observed effect | Recommended nonlinear transform | Recommended scaling | Justification / limitation |
| :---: | :---: | :---: | :---: | :---: | :---: |

The treatment may legitimately be:

none

For example:

no nonlinear transformation;  
standardisation

is perfectly valid if supported by evidence.

---

# **32\. Task 3 Must Remain Analysis-Only**

Do not create another deliverable CSV containing transformed customer profiles.

Do not replace values in the three clean CSVs.

Do not add Task 3 transformations to `audit_log.csv`.

Customer profiles and transformed values belong only in the notebook.

---

# **33\. Final Required CSV Outputs**

You must produce:

GroupNNN\_dirty\_clean.csv  
GroupNNN\_missing\_clean.csv  
GroupNNN\_outlier\_clean.csv

Requirements:

original 16 columns  
original column order  
original units  
no pandas index  
UTF-8  
IDs retained as strings

Dirty and missing outputs:

exactly 500 original IDs

Outlier output:

only retained original IDs  
---

# **34\. Numerical Accuracy Requirements**

For values that genuinely require correction/imputation:

| Field | Accepted absolute error |
| ----- | ----- |
| `order_price` | ≤ AUD 0.01 |
| `order_total` | ≤ AUD 0.01 |
| `delivery_charges` | ≤ AUD 0.08 |
| `distance_to_nearest_warehouse` | ≤ 0.0001 km |
| coordinates | ≤ 0.0000001 degrees |
| categorical/ID/date fields | correct value |

These are **marking tolerances**, not permission to replace already-correct source values with model estimates.

---

# **35\. Critical Zero-Credit Structural Risks**

An affected output can receive **zero output credit** if it has problems such as:

missing output  
unreadable output  
missing columns  
extra columns  
renamed columns  
wrong column order  
duplicate order IDs  
unexpected IDs  
missing dirty/missing batch IDs

Therefore structural validation should be treated as a high-priority final control, not an administrative afterthought.

---

# **36\. Recommended Notebook Architecture**

A strong submission could use this structure:

0\. Configuration and Environment  
   0.1 Group ID and paths  
   0.2 Python/package versions  
   0.3 Resource verification

1\. Data Loading and Input Validation  
   1.1 Manifest checks  
   1.2 Schema and grain  
   1.3 ID integrity  
   1.4 Batch guarantees

2\. Initial Data Investigation  
   2.1 Missingness  
   2.2 Numeric diagnostics  
   2.3 Categorical checks  
   2.4 Relationship diagnostics

3\. Shared Reconstruction Methods  
   3.1 Shopping-cart parser  
   3.2 Current product-price inference  
   3.3 Order arithmetic  
   3.4 Date and season  
   3.5 Haversine and nearest warehouse  
   3.6 VADER happiness reconstruction  
   3.7 Seasonal delivery models

4\. Task 1A — Dirty Data  
   4.1 Candidate detection  
   4.2 Root-field diagnosis  
   4.3 Repairs  
   4.4 Dirty-output validation

5\. Task 1B — Missing Data  
   5.1 Missing-field inventory  
   5.2 Deterministic recovery  
   5.3 Algebraic recovery  
   5.4 Model-based estimates  
   5.5 Missing-output validation

6\. Task 1C — Delivery Outliers  
   6.1 Residual diagnostics  
   6.2 Threshold/rule justification  
   6.3 Removed orders  
   6.4 Retained-order validation

7\. Task 2 — Audit Trail  
   7.1 Confidence definitions  
   7.2 Generate audit\_log.csv  
   7.3 Audit reconciliation

8\. Final Output Validation  
   8.1 Re-read CSVs  
   8.2 Schema checks  
   8.3 ID/row checks  
   8.4 Business-rule checks  
   8.5 Preservation tests  
   8.6 Model/residual checks  
   8.7 Audit consistency

9\. Task 3 — Customer Profiling  
   9.1 Build retained A2 analysis copy  
   9.2 Aggregate to customers  
   9.3 Select three attributes  
   9.4 Raw-scale comparison  
   9.5 Standardisation  
   9.6 Min-max scaling  
   9.7 Nonlinear transformation  
   9.8 Relationship/distance implications  
   9.9 Recommendation table  
   9.10 Limitations

10\. Reproducibility Summary  
    10.1 Write final outputs  
    10.2 Fresh Run All confirmation  
    10.3 Final file inventory

This structure closely follows the assessment logic while making rubric evidence easy for the marker to locate.

---

# **37\. Required Submission Package**

Your ZIP should contain one folder:

GroupNNN\_A2\_submission/

with at least:

GroupNNN\_dirty\_clean.csv  
GroupNNN\_missing\_clean.csv  
GroupNNN\_outlier\_clean.csv  
audit\_log.csv  
GroupNNN\_solution.ipynb  
GroupNNN\_solution.py  
requirements.txt  
GroupNNN\_AI\_declaration.pdf  
AI\_records/                    if applicable

The executed notebook is the **technical report**; no separate EDA/report PDF is required.

---

# **38\. Most Important Logical Dependencies to Protect**

The strongest way to think about the entire assignment is:

A. Establish trustworthy evidence  
       ↓  
B. Use evidence to diagnose  
       ↓  
C. Identify the root field/problem  
       ↓  
D. Make the smallest justified intervention  
       ↓  
E. Preserve everything known to be valid  
       ↓  
F. Log exactly what changed  
       ↓  
G. Re-read submitted files  
       ↓  
H. Independently validate them  
       ↓  
I. Only then use the clean outputs analytically

The three major principles running through the specification are therefore:

**Evidence before correction.** Do not infer that every inconsistency represents multiple errors.

**Minimal intervention.** Repair only dirty/missing information actually requiring intervention, while outlier records are removed rather than repaired.

**Validation must be independent of the repair itself.** A value is not validated merely because the same function that generated it says it is consistent.

That distinction between **diagnosis → intervention → independent validation** is likely the most important conceptual framework for organising the whole A2 pipeline.

