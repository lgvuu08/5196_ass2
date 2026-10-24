# FIT5196 A3 — Demonstration Notes (Group005)

**Phạm vi:** (A) A1 — EDA & ML questions (kèm *representative path* JSON/XML → bảng → finding) · (B) A2 — Seasonal delivery charge **spec 3.5**, **section 1.3**, **Task 3: 3.1, 3.2, 3.5**.
**Nguồn bằng chứng:**
- A1: `Group005_EDA.ipynb`, `Group005_EDA.pdf`, `Group005_solution.ipynb`, `Group005_source_to_target_mapping.csv`, 6 CSV chuẩn hóa (`Group005_A1_submission.zip`).
- A2: `Group005_solution_A3_revised.ipynb`, `ass2_spec.md` / A2 spec PDF.
- A3: specification + marking rubric.
- Mọi con số lấy từ output đã lưu trong notebook/PDF, trừ khi đánh dấu 🔁 (tôi tự tính lại độc lập từ dữ liệu).

**Cấu trúc mỗi phần:** *anchor lý thuyết/phương pháp trong môn → what–why–how của từng quyết định theo case → demo 4 bước → grain–units–limits → Q&A (kể cả changed-condition).*

---

## 0. Đọc trước: giả định và những gì CHƯA grounded

| # | Vấn đề | Cách tôi xử lý | Việc bạn cần làm |
|---|---|---|---|
| 1 | ~~A1 không có trong repo~~ → **đã có** gói A1 (EDA notebook + PDF, solution notebook, mapping, 6 CSV). | Phần A (§5) được viết từ chính gói đó: 8 figures, 10 findings, 5 MLQ + một path JSON/XML → bảng → finding. Con số chủ chốt được 🔁 kiểm lại từ 6 CSV. | Đọc hai cảnh báo ở đầu §5 (PDF vs notebook về "rerun"; hai môi trường Python khác nhau). |
| 2 | **Slide của unit không có trong repo.** Notebook A2 chỉ trích 3 nhóm slide (Week 7, 8, 11); notebook A1 chỉ trích *applied sessions* Week 2/3/4. | Chỉ dùng số slide/session mà notebook đã trích (✔). Chỗ khác ghi **⚠ slide # cần điền**, kèm tên khái niệm để bạn tra nhanh. Không tự bịa số slide. | Điền số slide ở §11 (≈10 phút). |
| 3 | "3.1, 3.2, 3.5" mà bạn ghi có thể là **Task 3** (3.1 customer copy, 3.2 original scales, 3.5 recommendation) hoặc **spec 3.1/3.2** (giá & làm tròn). | Chính = Task 3 (cùng danh sách với "spec 3.5, section 1.3"). **§10 (Phụ lục)** phủ spec 3.1/3.2 phòng trường hợp bạn muốn. | Cho tôi biết nếu cần mở rộng. |
| 4 | Số cell dùng 0-based (chỉ số trong file `.ipynb`). Jupyter không hiển thị chỉ số này. | **Check ID là locator chính** (Ctrl-F `DELIV-07`); cell idx là phụ. | — |

**Số tôi tự tính lại độc lập** (từ CSV gốc, không dùng code notebook) được đánh dấu 🔁. Chúng khớp notebook: 80 ô blank (10 × 8 trường), 8 tên warehouse sai, 8 vĩ độ dương, 8 định dạng ngày lạ, hệ số 4 mô hình mùa trên 420 dòng.

---

## 1. Rubric crosswalk — "HD" cần gì và notes này đáp ứng ở đâu

| Tiêu chí | HD cần (rubric §2) | Notes đáp ứng bằng | Mục |
|---|---|---|---|
| **G** (nhóm, 10đ) | Câu chuyện A1/A2 mạch lạc; exec summary có finding + recommendation + limitation; evidence **dễ tìm, nhãn chính xác**; chuyển tiếp trong thời gian | Exec-summary seed; "storyline" nối A1 → B1…B5; bảng evidence locator; core-vs-reserve để không vượt giờ | §2, §7 |
| **P** (cá nhân, 10đ) | Giải thích rõ, nhịp tốt, dùng notes/evidence **có chủ đích**, đóng góp substantive, bàn giao mượt | Mỗi phần có "kịch bản nói" (ý chính, không đọc nguyên văn), thứ tự mở evidence, câu signpost | §3, từng mục B |
| **Q** (cá nhân, 20đ) | Tự giải thích **how & why**, diễn giải evidence đúng **grain–units–limits**; biện minh một **independent check** và kết quả của nó; **thích ứng changed condition**, đề xuất check khả thi, nêu trade-off/uncertainty | Mỗi phần có hộp *Grain–Units–Limits*, *Independent check: establishes / does NOT establish*, và **Q&A drills gồm changed-condition** | từng mục B, §8 |
| Spec §4 (demonstration) | (1) input/source record + quyết định xử lý; (2) output/finding/so sánh; (3) cách ra kết quả + ý nghĩa giá trị; (4) supporting check làm được/không làm được gì. "Chỉ nói file tồn tại ≠ demonstration" | Mỗi phần có **Demo script 4 bước** đúng 4 gạch đầu dòng này | từng mục B |
| Spec §2 | Nếu cải tiến cho A3: nêu thay đổi vật chất, lý do, check đã làm; thừa nhận vấn đề chưa giải quyết | **A3 revision disclosure** + danh sách limitation chủ động nêu | §4, §9 |

---

## 2. Khung thời gian & phân vai (điều chỉnh theo kế hoạch nhóm)

> **Chia phần cho 5 người: xem §13 (hai flow đề xuất).** Bảng dưới là ngân sách theo *nội dung*, không theo người.

Cả nhóm có **15–20 phút** trình bày + demo, assessor dùng timer (spec §6). Dưới đây là **tổng ngân sách nếu một người làm hết (≈ 18 phút)** — thực tế nhóm sẽ chia theo hàng, và các thành viên khác còn Executive summary, A2-data cleansing, Reflection. **Chỉ chọn phần được giao**; phần "Reserve" dành cho Q&A.

| Phần | Core (nói) | Reserve (chỉ mở khi bị hỏi) |
|---|---|---|
| B1 Spec 3.5 model | 3 phút | alternatives (d)(e), DELIV-10, complementary coding, pooled-model check 🔁 |
| B2 Section 1.3 outlier | 3.5 phút | DELIV-07b, per-season τ, CLAIMS-13, AUDIT_CONFIDENCE |
| B3 Task 3.1 customer copy | 2 phút | PROF-01f chi tiết, lineage 184 decisions |
| B4 Task 3.2 original scales | 2 phút | BASE-02 extremes, pair-by-pair identity |
| B5 Task 3.5 recommendation | 3 phút | DIST-01 đầy đủ, total_paid supplementary |
| A.3 A1 representative path (JSON/XML → bảng → Finding 4–5) | 3 phút | D4–D11, `T3-TEXT-02` (65 ca), Q&A path |
| A.4–A.6 A1 EDA figure + MLQ (chọn *một* figure và *một* MLQ theo phân công) | 2.5 phút | A.5 (10 findings), toàn bộ MLQ-1…5, A.8 cầu nối A1↔A2 |

> **Nguyên tắc P:** mỗi phần ≤ 5 ý chính trên một "cue card"; mọi con số nói ra phải là con số **đang hiển thị trên màn hình**. Đọc nguyên văn bị coi là bằng chứng yếu (rubric "Notes and explanation").
>
> **Spec §4:** demo **bắt đầu bằng tóm tắt đóng góp/vai trò/task từng thành viên**. Điền: `[Tên] — [vai trò] — [task]` ×N trước khi vào nội dung.

**Exec-summary seed** (spec §3 yêu cầu ≥1 finding về data/results, 1 finding về cleaning/validation/transformation, 1 recommendation, 1 limitation):

- *Finding (results):* Delivery charge là **biểu giá tuyến tính theo mùa**: held-out R² ≥ 0.9999996 và MAE 0.0022–0.0025 AUD ≈ sàn làm tròn cent (0.0025). → "Charge lớn" ≠ bất thường; "residual lớn" mới là bất thường.
- *Finding (validation/transformation):* 24/500 đơn outlier bị loại bằng residual rule; cả 24 đều **mâu thuẫn với chính `order_total` của chúng** bằng đúng 4 mức phụ phí (6.25/9.50/14.75/22.00). Quy tắc thô (Tukey) xóa nhầm 13 đơn hợp lệ và bỏ sót 9.
- *Recommendation:* Với customer profiling: **không** biến đổi phi tuyến, **z-score** cả 3 thuộc tính (`order_count`, `mean_order_value`, `mean_delivery_distance`).
- *Limitation:* Quyết định loại outlier dựa trên batch guarantee "chỉ `delivery_charges` bị hỏng"; τ chỉ gấp 1.7× residual hợp lệ lớn nhất nên độ vững đến từ *plateau*, không từ biên của τ.

**Seed cho phần A1** (nếu bạn phụ trách exec summary hoặc nối A1 → A2):
- *Finding (data/results):* Review **chọn lọc theo giá**: 80.3% order có review nhưng chỉ 44.5% item line (7,000/15,739); coverage tăng **27.0% → 63.6%** theo tứ phân vị giá và đúng chiều ở 10/10 category (Finding 4–5).
- *Finding (validation):* 5,000 orders / 15,739 items / 7,000 reviews được dựng từ hai export tự lặp *và* chồng lấn (ví dụ reviews 3,850 + 3,850 − 700 = 7,000) với **0 xung đột sau normalise**; SKU/order-ref trích từ text khớp khóa có cấu trúc **7,000/7,000**.
- *Recommendation / next step:* MLQ-2 — dự đoán item nào ít có khả năng được review **≤ 30 ngày sau giao**, trên cohort giao hàng theo thời gian đã "chín", loại mọi thuộc tính từ review.
- *Limitation:* 44.5% là *export-observed coverage* (cutoff trích xuất chưa xác minh), không phải tỉ lệ phản hồi 30 ngày; 🔁 chỉ ≈ 65% review đến trong ≤ 30 ngày sau giao.

---

## 3. Mẫu "một phần = một vòng lập luận" (dùng cho mọi mục A và B)

```
① ANCHOR      Lý thuyết/phương pháp từ slide → code làm gì tương ứng      (≈20% thời gian)
② DECISIONS   What – Why (theo case cụ thể) – How (check ID) – Alternative bị loại + bằng chứng   (≈40%)
③ DEMO        4 bước theo spec §4: input → output → cách ra/ý nghĩa → check (establishes / does NOT)  (≈30%)
④ BOUNDARY    Grain – Units – Limits, và 1 câu "nếu điều kiện thay đổi thì…"  (≈10%)
```

Câu signpost gợi ý (EN): *"Let me anchor this in the method from the unit, then show the decision we made for our data, then the evidence."* / *"This check establishes X, but it does not establish Y."*

---

## 4. A3 revision disclosure (spec §2: "identify material changes, reasons and checks")

Nói ngắn gọn (≤30 giây) trước hoặc trong phần liên quan. Notebook A3 **không ghi đè** bản A2 đã nộp; chỉ sửa 1.3 (+ phần 1.0 và 2.1 liên quan) và Task 3.1, 3.2, 3.5.

**A1:** gói `Group005_A1_submission` được cung cấp không chứa ghi chú nào về thay đổi cho A3 (EDA PDF cũng ghi *"The full pipeline was not rerun for this summary"*). Nếu bạn có sửa gì ở A1 cho A3 thì thêm một dòng vào bảng dưới (thay đổi, lý do, check); nếu không, nói rõ **"A1 is presented as submitted"**.

| Phần | Thay đổi vật chất | Lý do | Check chứng minh | Quyết định có đổi? |
|---|---|---|---|---|
| **1.3** | Confidence của removal so với *các cent charge mà total cho phép* (tìm kiếm MISS-03), cổng = held-out error của mùa | Cổng cũ 0.005 so với charge không làm tròn bỏ qua làm tròn của total → CORD001200 bị `medium` | cả 24 removal `high`; 2.2 tái tính cùng kết quả | **Không** — vẫn 24 đơn |
| 1.3 | Sensitivity thêm τ riêng từng mùa và τ+1 cent | τ chỉ hơn 1 cent một chút; scale được gộp | cùng 24 id | Không |
| 1.3 | `residual_threshold` từ chối residual từ split khác; CLAIMS-13 tái kiểm các con số trong text (sửa 2 câu "nửa cent") | τ phụ thuộc state; text chưa có kiểm tự động | tất cả claim PASS | Không |
| 1.3 | DELIV-09 thêm support check (extrapolation) | Có quyết định nào là ngoại suy không? | 4 đơn vượt ≤ 0.56 km, giữ lại, residual ≤ 0.0034 | Không |
| **3.1** | PROF-01f (địa lý theo khách), PROF-02 (đối soát đơn/khách/tiền + truy vết Task 1 → Task 3), PROF-03 (1 khách → 1 dòng) | "No unresolved input problem" trước đó chỉ *tuyên bố*, chưa *chứng minh* | 22 khách khác nhau địa lý ở raw → 0 ở output; 36 thay đổi + 24 removal đều `high` | Không |
| **3.2** | BASE-01/02 thêm đếm miền giá trị + ai là khách extreme | 3.3/3.4 cần loại trừ 0/âm/hằng; extreme cần nguyên nhân | không missing/0/âm; 6 khách bị fence có 1–2 đơn | Không |
| **3.5** | EVID-01 tính lại mọi số REC-01 dẫn; DIST-01 **đo** tác động lên láng giềng; đối chiếu sqrt(`total_paid`) vs "none"(`mean_order_value`); RERUN-01 tái tạo từ đĩa | Tác động lên khoảng cách trước chỉ *mô tả*; hai kết luận trông mâu thuẫn | raw giữ 7% láng giềng, min-max 71%; sqrt skew −0.02 vs −0.50; 16/16 check pass | Không |

---

## 5. PHẦN A — A1: EDA & ML questions (đã grounded từ gói A1 của nhóm)

**Nguồn bằng chứng A1:** `Group005_EDA.ipynb` (8 figures, 10 findings, 5 MLQ, output đã lưu), `Group005_EDA.pdf` (13 trang; phần chấm = trang 3–12), `Group005_solution.ipynb` (Task 1–4: parse, reconcile, text, validation `VAL-*`), `Group005_source_to_target_mapping.csv` (111 dòng `MAP-*`), 6 CSV chuẩn hóa trong `outputs/`.
🔁 = tôi tự tính lại từ 6 CSV chuẩn hóa (không dùng code notebook) và **khớp** notebook/PDF: 5,000 orders / 15,739 item lines / 7,000 reviews / 500 customers; mean–median AUD 2,858–2,410; top-10% orders 26.2% vs customers 17.5%; Gini 0.38 vs 0.22; review phủ 4,017/5,000 orders (80.3%) và 7,000/15,739 item (44.5%); ≤2 sao 1,197 (17.1%); OTIF Nickolson 828/898 = 92.2%, Bakers 88.9%, Thompson 88.6%, failure prevalence 10.62%; coverage theo tứ phân vị giá 27.0% → 38.9% → 48.4% → 63.6%; fan-out ngây thơ làm tổng paid ×**3.54**; SKU/order-ref trích từ text khớp cấu trúc **7,000/7,000**.

> ⚠ **Hai chỗ lệch cần tránh nói sai:**
> 1. PDF ghi *"The full pipeline was not rerun for this summary"*, còn `Group005_EDA.ipynb` (ô 1.2) ghi *"reruns end to end from a fresh kernel with 145 of 145 register checks PASS"*. Khi trình bày chỉ nói **"saved PASS results in the solution notebook"** trừ khi bạn vừa Restart & Run All và thấy 145/145.
> 2. `Group005_solution.ipynb` in ra Python 3.10 / pandas 2.0.1, còn `Group005_EDA.ipynb` in ra Python 3.13.9 / pandas 2.3.3. Hai notebook chạy ở hai môi trường khác nhau (`requirements.txt` chỉ ghi min-version). Nếu bị hỏi về reproducibility: "6 CSV chuẩn hóa là hợp đồng giữa hai notebook; EDA đọc lại đúng 6 CSV".

### A.1 Yêu cầu A3 cho A1 và cách ta đáp ứng

Spec A3 (§3): *"Explain a representative path from JSON/XML to a standardised table and a finding. Include a parsing/reconciliation decision, a text-processing decision and how you checked the result."* Bảng sau là bản đồ nội dung → yêu cầu:

| Yêu cầu | Đáp ứng bằng | Mục |
|---|---|---|
| Đường đi đại diện JSON/XML → bảng chuẩn hóa → finding | **Path "một review → `product_reviews` → coverage theo giá → Finding 4–5 → MLQ-2"** | A.3 |
| Quyết định parsing/reconciliation | Parse có cấu trúc (không regex) + normalise-trước-khi-so-sánh + reconcile theo business key, **không** precedence | A.3 D1–D3 |
| Quyết định text-processing | Xóa marker bằng danh sách tường minh, từ chối near-match, emoji theo Unicode block, giữ đa ngôn ngữ | A.3 D4–D7 |
| Cách kiểm tra kết quả | `T3-TEXT-01/02/04/05`, `VAL-FLOW-*`, `VAL-CONFLICT-01`, `VAL-TEXT-01/02`, `VAL-FK-06`, join audit | A.3 |
| EDA + ML question (phần bạn chọn) | 8 figures → 10 findings → 5 MLQ, mỗi bước nêu grain/denominator/join/limitation | A.4–A.6 |

### A.2 Anchor — phương pháp từ môn học → code A1

| Khái niệm | Nguồn trong môn | Trong code A1 |
|---|---|---|
| Đọc JSON: `json.load`, làm phẳng `json_normalize(record_path=…)` | ✔ **Week 3 applied session** (notebook ghi rõ) | `T1-P1/P2` |
| Đọc XML: `BeautifulSoup(…, "lxml-xml")`, `pandas.read_xml(xpath, dtype=str)` | ✔ **Week 2 applied session** | `T1-P1/P2` |
| Regex dạng verbose `(?x)`, chỉ áp dụng *sau* khi parser đã trả giá trị | ✔ **Week 4 applied session** | `T1-P8`, `Group005_text_functions.py` |
| Data cleansing / missing-code: giữ sentinel, không đổi nghĩa của missing | ✔ **Week 7 *Data Cleansing*** (slides 27–30, 38–45; notebook A2 dẫn cho missing data — nguyên tắc "missing ≠ giá trị thật" được dùng lại ở A1) | quy ước literal `NaN`, `ASM-05/06/13` |
| Data validation: structural / content / logical | ✔ **Week 11 *Data Validation*** (slides 4, 22, 27; notebook A2 dẫn — cùng khung structural/content/logical được dùng ở A1) | `VAL-SCHEMA/PK/FK/FLOW/ARITH/TIME/TEXT` |
| EDA: phân phối, tập trung (Lorenz, Gini), skew, bảng chéo, grain & denominator | ⚠ Week ? slide ? | Figure 1–8 |
| Ước lượng bất định: Wilson, Newcombe, Bonferroni, bootstrap, Cliff's δ | tài liệu trích trong notebook: Wilson 1927; Newcombe 1998; Dunn 1961; Efron & Tibshirani 1993; Cliff 1993 ✔ · slide ⚠ | Fig 4, 5, 7 |
| Thiết kế ML question: target, decision-time predictors, validation theo thời gian, baseline, leakage | ⚠ Week ? slide ? | MLQ-1…5 |

---

### A.3 REPRESENTATIVE PATH — từ JSON/XML đến một finding

**Tên path:** *một review* (JSON `$.productReviews[*]` + XML `/OperationsExport/ProductReviews/Review`) → `product_reviews_standardised.csv` → *review coverage theo giá* → **Finding 4–5** → **MLQ-2**.
**Vì sao chọn path này:** nó đi qua đủ ba thứ assessor đòi (parsing/reconciliation, text-processing, kiểm tra), và finding của nó (review chọn lọc theo giá) là finding mạnh nhất của báo cáo.

**Dòng chảy số liệu (đọc từ trái sang phải; mỗi bước có ID để mở):**

```
JSON  3,946 review rows (3,850 distinct)  ┐                                   ┌ Finding 4: 44.5% item có review
                                          ├─ normalise ─ reconcile ─ text ─ ┤ Finding 5: coverage 27.0% → 63.6%
XML   3,946 review rows (3,850 distinct)  ┘   T1-P4      T2-R1     T3-TEXT   └ theo tứ phân vị giá (Fig 4)
                   700 key dùng chung → 3,850 + 3,850 − 700 = 7,000 reviews (VAL-FLOW)
```

#### ① Bước 1–2 — Parse và reconcile (what / why / how / alternative)

| # | Quyết định | What | Why (theo dữ liệu này) | How / evidence | Alternative bị loại |
|---|---|---|---|---|---|
| **D1** | **Parse bằng parser có cấu trúc, regex chỉ sau parser** | `json.load` + `json_normalize`; `BeautifulSoup lxml-xml` + `read_xml(dtype=str)` | Spec cấm "parse JSON/XML như text bằng regex". `dtype=str` giữ leading zero và định dạng gốc (XML không có kiểu: 100% `object`; JSON có `bool/int/float`) — **chính sự khác kiểu này là một finding** (`T1-P4`) | `T1-P1`: SHA-256 khớp manifest (JSON 14,139,534 B; XML 17,811,170 B). Ô "regex stays inside its boundary": **chỉ `T1-P8`** dùng regex; `T1-P1/P2` sạch | Regex quét file: mong manh, vi phạm spec |
| **D2** | **Normalise rồi mới so sánh** | Cùng một đơn viết `AUD 5,287.78` / `14/10/2018 09:28:00` / `Y` (XML) và `5287.78` / `2018-10-14 09:28:00` / `true` (JSON) | So giá trị thô sẽ báo *xung đột giả* ở mọi dòng | Day-first được **chứng minh, không giả định**: thành phần ngày thứ nhất của XML tới **31** (`ASM-01`); `coupon_discount` là *percentage points* (`15%` ≠ `0.15`, `ASM-02`); `""` (JSON) và `<Coupon_Code/>` (XML) là cùng một "không có coupon" (`ASM-04`) | Giả định tháng/ngày hoặc so chuỗi thô |
| **D3** | **Reconcile theo business key, không có precedence JSON/XML** | `T2-R1 reconcile_canonical`: một giá trị populated có thể điền chỗ trống của bản kia; **hai giá trị populated khác nhau → ghi log và từ chối**, không chọn âm thầm | Cả hai export *tự lặp* (96 cặp review lặp mỗi bên, giống hệt nhau) **và** chồng lấn (700 key chung) ⇒ phải xử lý lặp trong-nguồn *trước*, rồi chồng lấn | 3,850 + 3,850 − 700 = **7,000** (`VAL-FLOW`); **0 xung đột** trong JSON, trong XML, và giữa hai nguồn (`VAL-CONFLICT-01`); file log rỗng là *bằng chứng* vì chạy cùng code path sẽ ghi xung đột | "JSON thắng": che giấu xung đột thật nếu có; concat rồi `drop_duplicates` không kiểm tra |

#### ② Bước 3 — Text-processing (what / why / how / alternative)

| # | Quyết định | What | Why | How / evidence | Alternative bị loại |
|---|---|---|---|---|---|
| **D4** | **Xóa marker bằng danh sách tường minh** | Chỉ 7 marker spec công bố (`[SYSTEM]`, `[CATALOGUE]`, `[VERIFIED_PURCHASE]`, `[SOURCE: …]`, `[RATING: …]`, `#verified-buyer`, `@store_support`) | Lời khách như `[NOTE]`/`[URGENT]` phải sống sót | `TXT-18`: `[NOTE] Keep bracketed customer wording` → `[note] keep bracketed customer wording` (chỉ đổi chữ hoa) | Regex chung `\[.*?\]` xóa nhầm lời khách |
| **D5** | **Từ chối near-match, không cắt cụt** | `_search_bounded` kiểm ký tự hai bên; `-` và `_` thuộc về token | `\b` thôi chưa đủ: trong `SKU-ABC123-extra` dấu `-` là ranh giới → trả `SKU-ABC123` (*lỗi dữ liệu im lặng*) | `TXT-12`: `SKU-ABC123-extra` → `NaN`. Nhóm `near-match` là lớn nhất: **21/65** ca của nhóm | `\bSKU-\w+\b` đơn thuần |
| **D6** | **Emoji theo Unicode block/sequence, không theo category `So`** | Gồm cờ tag (England/Scotland/Wales = `U+1F3F4` + tag chars + `U+E007F`), variation selector, keycap | `So` còn chứa `©`, `®`, `™`, `°` — ký hiệu văn bản hợp lệ | `Product™` và `25°` sống sót; nhóm `symbol` 10 ca; xóa nguyên chuỗi cờ nên không còn ký tự vô hình | `unicodedata.category == "So"` |
| **D7** | **Giữ đa ngôn ngữ; Latin-analysis là trường dẫn xuất riêng** | `review_body_clean` giữ chữ không-Latin; `review_body_latin_analysis` = phần Latin; `contains_non_latin_script` theo *Unicode Script property* | Spec: *"A non-ASCII character is not automatically non-Latin"* | `café niño über` → `False` (không phải ngoại ngữ); 🔁 **276** review có chữ không-Latin (ja 61, ar 60, zh 58, hi 50, ru 47) và cờ khớp 276/276 (`VAL-TEXT-11`) | Loại ASCII-only; suy ngôn ngữ từ text (ASM-09: dùng `language_code` có cấu trúc) |
| **D8** | **Trích tham chiếu *trước* khi làm sạch** | `extract_order_reference`, `extract_product_sku` chạy trên *raw body do parser trả về* | Làm sạch xóa wrapper `Reference: … \| SKU: …`; trích sau sẽ mất nguồn | Wrapper có trong **7,892/7,892** raw body (`T1-P8`) | Trích từ body đã làm sạch |

#### ③ Bước 4 — Từ bảng đến finding (join và denominator)

| # | Quyết định | What | Why | How / evidence |
|---|---|---|---|---|
| **D9** | **Aggregate rồi mới join; mọi join đều audit** | `join_audit(left, right, key, validate=…)`: kiểm số dòng vào = ra, 0 unmatched | Order→items là one-to-many: join ngây thơ nhân paid value | Fan-out ngây thơ **×3.54** (EDA §1.3 *Executable EDA safeguards*; 🔁 3.54); mọi join của Fig 2, 3, 5, 7, 8 báo `unmatched = 0` |
| **D10** | **Đúng denominator cho từng câu hỏi** | Order-level (4,017/5,000 = 80.3%) vs item-level (7,000/15,739 = 44.5%) | Hai mẫu số trả lời hai câu hỏi khác nhau; order-level che khoảng trống ở item-level | `reviews.order_item_id` duy nhất (🔁 max 1 review/item) nên presence-flag không nhân dòng |
| **D11** | **Làm tròn bằng Python `round`, không phải numpy** | `ASM-14` | numpy `Series.round(2)` bất đồng trên giá trị đúng nửa cent | ≈ **1%** đơn sẽ trượt hợp đồng `order_total` nếu dùng numpy (cùng *họ* bài học với phát hiện Decimal vs float ở A2, §10: biểu diễn nhị phân của nửa cent) |

#### ④ Demo script (4 bước theo spec §4)

1. **Input/source record + quyết định:** hiển thị ca public **TXT-03** (trong `T3-TEXT-01`):
   `[SOURCE: mobile-app] <p>Caf&eacute; setup was easy 😊</p> Reference: HORD… | SKU: …` → **`café setup was easy`**. Nói: *"entity được decode trước khi strip tag nên `é` sống sót; marker có tham số, emoji, wrapper và social token bị loại; chữ Latin có dấu không bị coi là ngoại ngữ."* Rồi chiếu **TXT-12** (`SKU-ABC123-extra` → `NaN`) làm ví dụ cho D5.
2. **Output:** một dòng thật của bảng chuẩn hóa — 🔁 review **HREV004637**: `order_id = HORD003326`, `order_item_id = HITM0010461`, `product_id = PRD0986`, `rating = 5`, `value_experience = good_value`, **`extracted_order_reference = HORD003326`**, **`extracted_product_sku = SKU-VEL00986`**; item đó có `unit_price = AUD 419.88` thuộc **tứ phân vị giá 2** (234.12–543.69), nơi coverage là **38.95%**.
3. **Cách ra & ý nghĩa:** "Tham chiếu trích từ *chữ trong review* trùng với khóa *có cấu trúc* (`order_id`, `product_sku` của `product_id`) — hai đường độc lập cho cùng một liên kết. Item này nằm ở tứ phân vị giá nào quyết định nó thuộc cột nào của Fig 4; cả 15,739 item được gán tứ phân vị bằng `qcut` trên `unit_price` (cutpoints 234.12 / 543.69 / 1,062.27)."
4. **Supporting check:**
   - *Establishes:* (i) hàm trích tái tạo **đúng** các số đếm của `T1-P8` qua code path khác (`T3-TEXT-04`: 315 / 7,892 / 7,892 / 2,103 đều khớp); (ii) `T3-TEXT-05`: **7,892/7,892** SKU trích được đúng là SKU của sản phẩm được review — hàm trích *không có quyền truy cập catalogue*, nên khớp hoàn toàn nghĩa là đúng chứ không chỉ "đúng định dạng"; (iii) `VAL-TEXT-01/02`: 7,000/7,000 (🔁 tôi tự kiểm lại 7,000/7,000); (iv) 18/18 ca public + 65/65 ca tự thiết kế.
   - *Does NOT establish:* ngữ nghĩa của review (PDF: *"Measurement checks do not validate text semantics"*); không chứng minh review đại diện; đường sentinel `NaN` của `clean_narrative_text` **không được dữ liệu thực kích hoạt** (không review nào làm sạch ra rỗng — `ASM-13`), chỉ được các ca test kích hoạt.

#### ⑤ Grain – Units – Limits

- **Grain:** review (7,000) — một review ↔ đúng một `order_item` (grain item line 15,739) ↔ một order (5,000). **Units:** sao 1–5, AUD (giá item), ngày/giờ ISO.
- **Limits:** Latin-analysis của review *không-Latin có tên sản phẩm Latin* vẫn giữ dấu câu ASCII — 🔁 ví dụ **HREV000008** (ru): `candle edge 428 , . , , . , …` (`ASM-15` chỉ loại dấu câu *wide/fullwidth*); đây là giới hạn đã biết của trường dẫn xuất, không ảnh hưởng `review_body_clean` hay Finding 4–5. Review timestamps đến 2019-02-20 (hợp lệ, `ASM-10`) nên "coverage" là *đã quan sát được trong export*, không phải tỉ lệ phản hồi cuối cùng.

#### ⑥ Q&A drills cho path

| Câu hỏi | Trả lời mẫu |
|---|---|
| Vì sao không để JSON ưu tiên hơn XML? | Sau normalise có **0 xung đột** nên precedence là thừa; nếu có xung đột, precedence sẽ che giấu nó. Ta ghi log và từ chối chọn âm thầm (`T2-R1`, `VAL-CONFLICT-01`). |
| Check nào *độc lập* với code làm sạch? | `T3-TEXT-05`: SKU trích từ text so với `product_sku` của catalogue (7,892/7,892) — hàm trích không biết catalogue. Và `T3-TEXT-04`: đối chiếu với số đếm đo ở `T1-P8` bằng code path khác. |
| **Changed:** nếu một review có hai wrapper khác nhau hoặc SKU lệch product? | Trích trả `NaN` cho near-match (D5) và `VAL-TEXT-01/02` sẽ FAIL ⇒ giữ dòng nhưng ghi log, không sửa im lặng; check khả thi: đếm review có `extracted_* != structured` (hiện 0/7,000). |
| **Changed:** nếu XML dùng `MM/DD/YYYY`? | `ASM-01` sẽ sai, nhưng bằng chứng "ngày thứ nhất tới 31" sẽ không còn ⇒ `pd.to_datetime(format="%d/%m/%Y")` raise; vì ta parse với format tường minh nên lỗi lộ ra thay vì đảo âm thầm. |
| **Changed:** thêm nguồn thứ ba chồng lấn? | `reconcile_canonical` tổng quát hóa (coalesce theo key, log xung đột); phải chạy lại `VAL-FLOW` (số key = số phần tử của hợp các tập key) và đảm bảo hai nguồn mới normalise về cùng quy ước. |
| Vì sao text-processing quan trọng cho finding? | Nó không đổi phép đếm coverage (dựa trên `order_item_id` có cấu trúc) — nó **xác nhận liên kết** và bảo vệ các phép đo review khác (độ dài, đa ngôn ngữ). Không nói quá. |

---

### A.4 EDA — 8 figures: grain, denominator, join, kết quả, giới hạn

Cả 8 figure đều khai báo **question / observation unit & denominator / tables & join keys / interpretation / limitation** (đúng mẫu — cứ dùng mẫu này để nói).

| Fig | Loại | Grain / denominator | Join | Kết quả chính | Giới hạn nêu sẵn | Finding |
|---|---|---|---|---|---|---|
| 1 | Univariate | order n=5,000; panel khách n=500 | không join (khách = aggregate) | mean 2,858 > median 2,410; top-10% orders **26.2%** vs khách **17.5%**; Gini **0.38 → 0.22** | 1 năm; paid ≠ profit | F1 |
| 2 | Multivariate | order n=5,000; mỗi ô: median + n | items→order one-to-one | median gross 627 → 8,739 giữa hai góc; log-variance: giá gia quyền **57.0%**, số lượng **32.1%**, 2·cov **10.9%** | đồng nhất thức đại số, không phải độ quan trọng; không có bất định | F2 |
| 3 | Composition | item lines theo category | items→products→orders (many-to-one; 15,739 vào/ra, 0 unmatched) | doanh số 512k (Accessory) → 2.57M (Laptop) ≈ 5×; contribution-rate **28.6–33.1%** | proxy; GST/cost basis chưa xác minh | F3 |
| 4 | Multivariate/review | A: order trong strata số dòng; B: item theo tứ phân vị giá | aggregate trước, join one-to-one | 3-line orders: **74.2% → 92.0%**; item: **27.0% → 63.6%**; đúng chiều ở **10/10** category | hai kiểm tra riêng, không phải điều chỉnh đồng thời | F4, F5 |
| 5 | Bivariate/review | review (7,000), cluster theo order | reviews→orders, reviews→deliveries many-to-one | ≥4 sao **65.85% vs 65.87%** nhưng 5 sao **34.5% vs 21.8%** (+12.7 pp); mean gap **0.179** (CI [0.092, 0.267]); Cliff's δ **0.093** | nhãn value đồng thời với rating; không xử lý phụ thuộc khách lặp | F6, F7 |
| 6 | Temporal | đơn/ngày (kể cả ngày 0), 365 ngày | không join | weekday **13.50–13.85**; tháng **12.80 (Sep) – 14.94 (Aug)**; SD ngày **3.55**, IQR 5 | 1 chu kỳ năm; trung bình phẳng ≠ có thể dự báo | F8 |
| 7 | Delivery ops | giao hàng n=5,000 | deliveries→orders one-to-one | Nickolson **92.2%** (n=898) vs **88.8%** (4,102): **+3.44 pp**, khoảng đồng thời [0.77, 5.70]; omnibus p=0.0096 | `nearest_warehouse` ≠ nơi xuất kho; chưa hiệu chỉnh khoảng cách/địa lý | F9 |
| 8 | Delivery ops | giao hàng n=5,000; recovery = Σcharge/Σcost | one-to-one | cả 5,000 có contribution ≥ 0; tổng AUD 15,095, median 2.74; Standard **1.27×**, Express **1.28×** | chi phí ghi nhận thiếu (nhân công, đóng gói, hoàn, overhead) | F10 |

#### A.4.1 Hai figure đáng "đứng nói" (chọn theo phân công của bạn)

**Fig 1 / Finding 1 — "Giao dịch lớn ≠ phụ thuộc vào nhóm khách tinh hoa"**

| Lớp | Nội dung |
|---|---|
| ① Anchor | Phân phối lệch phải → báo cả mean *và* median; Lorenz + Gini là thước đo **tập trung**; tập trung phụ thuộc **grain** |
| ② Decisions | **Grain**: đơn (n=5,000) vs khách (n=500) — *"đúng mẫu số cho câu hỏi resilience là khách, không phải đơn"*. Gini bằng công thức `2Σ i·xᵢ /(nΣx) − (n+1)/n` trên mảng đã sắp xếp (🔁 0.38 / 0.22). `order_total` = paid (net coupon, gồm delivery và GST) — không phải doanh thu hàng hóa. |
| ③ Demo | Input: bảng `orders` (5,000). Output: panel (a) mean 2,858 vs median 2,410, skew; panel (b) hai đường Lorenz. Cách ra: sắp xếp tăng dần, tích lũy. Ý nghĩa: **26.2% → 17.5%** — biến thiên giao dịch không nên bị diễn giải thành chiến lược VIP. Check: results register tính lại từ CSV trong notebook (🔁 khớp). *Không chứng minh:* tính bền theo thời gian; 1 năm. |
| ④ Boundary | Grain = order / customer; unit = AUD paid; limit = 1 năm, paid ≠ profit |
| ⑤ Q&A | *"Gini 0.22 là thấp hay cao?"* → Không có ngưỡng tuyệt đối; so *cùng dữ liệu hai grain* (0.38 vs 0.22) là ý chính. **Changed:** *"Nếu 5% khách chiếm một nửa doanh thu?"* → Gini khách sẽ tăng mạnh, top-10% share lên cao; kết luận F1 đảo; check: tính lại `c_top10` và Lorenz khách. *"Có dùng log?"* → Chỉ để *nhìn* phân phối; Gini tính trên giá trị gốc vì nó đo bất bình đẳng của AUD. |

**Fig 7 / Finding 9 — OTIF theo kho**

| Lớp | Nội dung |
|---|---|
| ① Anchor | Tỉ lệ nhị phân → **khoảng Wilson**; so hai tỉ lệ → **Newcombe**; so *nhiều* nhóm với "phần còn lại" → **Bonferroni** (z tại α/(2·3)); omnibus **χ²** |
| ② Decisions | Mỗi kho vs *tất cả còn lại*, Newcombe = hiệu hai cận Wilson, **Bonferroni làm rộng khoảng** cho họ 3 so sánh (z = Φ⁻¹(1 − 0.05/6)). Kiểm tra case-mix: OTIF trong từng ô kho×service + chuẩn hóa theo cơ cấu service chung (Bakers 0.8891, **Nickolson 0.9221**, Thompson 0.8862 sau chuẩn hóa). Ghi rõ OTIF = "không trễ" trong export này (assert `ontime == (delay_days ≤ 0)`). |
| ③ Demo | Input: `deliveries` ⨝ `orders.nearest_warehouse` (5,000 vào, 5,000 ra, 0 unmatched). Output: Fig 7 ba panel + bảng. Ý nghĩa: Nickolson hơn **3.44 điểm %**; chỉ khoảng của Nickolson **không chứa 0** (Bakers −0.76 [−2.96, 1.36]; Thompson −1.33 [−3.49, 0.77]); lợi thế còn trong Express (+4.54 pp) và Standard (+3.21 pp). Check: service-mix standardisation hầu như không đổi tỉ lệ. *Không chứng minh:* nhân quả/hiệu quả vận hành của Nickolson. |
| ④ Boundary | Grain = giao hàng; limit: `nearest_warehouse` ≠ nơi xuất kho; khoảng cách (`shipping_distance_km`) **có sẵn nhưng chưa hiệu chỉnh**; khách lặp vi phạm độc lập |
| ⑤ Q&A | *"Tại sao Bonferroni?"* → 3 so sánh "kho vs phần còn lại" được nhìn cùng lúc nên kiểm soát family-wise; nhưng nó **không** xử lý confounding hay selection. **Changed:** *"Nếu Nickolson gần khách hơn?"* → khoảng cách là confounder chưa hiệu chỉnh — đúng là hạn chế đã nêu; check khả thi: phân tầng theo tứ phân vị `shipping_distance_km` hoặc logistic regression OTIF ~ kho + service + distance, so sánh hệ số kho; đây là chính nội dung **MLQ-5**. *"Tại sao không dùng chỉ p-value?"* → p=0.0096 chỉ nói *có khác nhau ở đâu đó*; ta cần *kho nào, bao nhiêu, bất định ra sao*. |

> Nếu cần mở rộng, Fig 4 (coverage) đã được trình bày trọn trong **A.3** (path); Fig 5 xem A.5 Finding 6.

---

### A.5 Mười findings — bảng tra nhanh cho Q&A

| # | Phát biểu (rút gọn) | Số liệu đỡ | Evidence | MLQ |
|---|---|---|---|---|
| 1 | Giao dịch lớn không chứng minh phụ thuộc vào nhóm khách ít người | 26.2% vs 17.5%; Gini 0.38 → 0.22 | Fig 1 | 1 |
| 2 | Giá gia quyền là phần cấu trúc lớn hơn của biến thiên giá trị giỏ — nhưng đây là đồng nhất thức | 57.0 / 32.1 / 10.9% | Fig 1–2 | 1 |
| 3 | Tầm quan trọng thương mại = quy mô × tỉ suất; không cái nào đứng riêng | 5× về doanh số; rate 28.6–33.1% | Fig 2–3 | 1 |
| 4 | Coverage cấp order (80.3%) che khoảng trống cấp item (44.5%) | 4,017/5,000; 7,000/15,739; export-observed, chưa phải tỉ lệ phản hồi cuối | Fig 4 | 2 |
| 5 | Review chọn lọc theo giá, qua hai kiểm tra riêng | 74.2% → 92.0% (3-line); 27.0% → 63.6%; 10/10 category | Fig 4 | 2 |
| 6 | Nhị phân "hài lòng" che dịch chuyển ordinal | ≥4 sao 65.85% vs 65.87%; 5 sao 34.5% vs 21.8%; gap 0.179; δ 0.093 | Fig 5 | 3 |
| 7 | Chọn lọc review và cường độ rating là hai target khác nhau | ≤2 sao: 17.1% của review nhưng 7.6% của item mua | Fig 4–5 | 2, 3 |
| 8 | Trung bình weekday phẳng ≠ khối lượng dự báo được | 13.50–13.85; SD 3.55; IQR 5 | Fig 6 | 4 |
| 9 | Chênh OTIF theo kho còn sau kiểm tra cơ cấu service → ưu tiên điều tra | +3.44 pp; [0.77, 5.70]; +4.54/+3.21 | Fig 7 | 5 |
| 10 | Thu hồi chi phí giao hàng và độ tin cậy là hai chiều khác nhau | 15,095; 1.27× vs 1.28× | Fig 7–8 | 5 |

**Ba chủ đề (Conclusion của báo cáo):** (i) tập trung nhẹ đi ở grain khách/danh mục (F1–3); (ii) bằng chứng review **chọn lọc có hệ thống** — đại diện, không phải rating trung bình, là rủi ro phân tích chính (F4–7); (iii) vận hành giao hàng có hai chiều tách biệt; chênh theo kho là *liên hệ*, chưa phải hiệu ứng cơ sở (F8–10).

---

### A.6 Năm ML questions — thiết kế và bảo vệ

Mỗi MLQ có đủ 7 phần: **EDA evidence → business decision → problem type & unit → target → decision-time predictors → validation & metric → leakage/deployment risk**. Năm câu phủ **4 loại bài toán** (hồi quy MLQ-1; phân loại nhị phân MLQ-2, MLQ-5; ordinal hai giai đoạn MLQ-3; dự báo chuỗi thời gian đếm MLQ-4). Ghi nhớ nguyên tắc chung: **chỉ dùng predictor có sẵn tại thời điểm quyết định; validation theo thời gian; baseline tường minh; chỉ số theo ngân sách can thiệp**. *A1 EDA không huấn luyện model* (limitation "Prediction untested").

| MLQ | Loại / unit | Target | Validation | Leakage guard chính |
|---|---|---|---|---|
| 1 | Hồi quy / customer-month | tổng paid tháng kế (kể cả 0) | rolling monthly origin; MAE & bias vs *previous-month* và *trailing-3-month mean*; precision@K cho "top-decile" | loại giao dịch tương lai; 🔁 **2,587/6,000** customer-month = 0 (zero-heavy) |
| 2 | Nhị phân / item line đã giao | có review ≤ 30 ngày sau giao | cohort giao hàng theo thời gian, mỗi order trong một partition, label đã "chín"; log-loss, calibration, PR-AUC vs prevalence | không gán nhãn "không phản hồi" cho quan sát chưa chín; loại mọi thuộc tính từ review |
| 3 | Hai giai đoạn: A = MLQ-2, B = rating ordinal | rủi ro joint = P(review ≤30d) × P(rating ≤ 2 \| review) | RPS cho ordinal; calibration, PR-AUC cho ≤2 sao | stage B chỉ huấn luyện trên người review ⇒ rủi ro *quan sát được*, không phải bất mãn tiềm ẩn; loại `value_experience`, rating, text |
| 4 | Chuỗi thời gian đếm / ngày | số đơn ngày kế + khoảng dự báo | expanding window 1 bước; MAE vs *historical mean* và *weekly seasonal-naive*; coverage & độ rộng khoảng (vd 90%) | không random split, không cửa sổ căn giữa; 1 năm không xác lập mùa vụ |
| 5 | Nhị phân / order lúc dispatch | OTIF failure (`False`) | rolling theo thời gian; PR-AUC vs prevalence **10.62%**; so có/không `warehouse` | loại `delay_days`, `delivered_date`; `nearest_warehouse` có thể không là nơi xuất kho |

#### A.6.1 MLQ-2 (gắn với path A.3) và MLQ-5 (gắn với Fig 7) — đào sâu

| Lớp | MLQ-2: item lines nào ít khả năng được review ≤ 30 ngày? | MLQ-5: dispatch-time info có nhận diện OTIF failure? |
|---|---|---|
| ① Anchor | Bài toán phân loại nhị phân mất cân bằng + selection; **PR-AUC & calibration** thay vì accuracy | Phân loại nhị phân, imbalance 10.62%; kiểm tra *giá trị tăng thêm* của một feature bằng so sánh có/không feature |
| ② Decisions | **Unit = item line** (vì review gắn với item, không phải order); **label** = review ≤30 ngày sau giao (neo vào *giao hàng*, không phải ngày đặt: median lag 29.0 ngày vs **23.5 ngày**); **chỉ** predictor tại lúc giao (giá, category, quantity, line count, order value, service, warehouse, delivery outcome); câu hỏi con *"giá có cải thiện dự đoán vượt basket size và category không?"* ⇒ so có/không giá | **Unit = order lúc dispatch**; target `on_time_in_full = False`; predictors dispatch-time (service, shipping distance, promised lead time, basket, order value, warehouse); câu hỏi con *"warehouse có thêm giá trị ổn định sau khi hiệu chỉnh case mix?"* |
| ③ Evidence & numbers | Fig 4: 27.0% → 63.6%, 10/10 category; **44.5% không phải tỉ lệ 30 ngày**. 🔁 Chỉ ≈ **64.9%** review đến trong ≤ 30 ngày sau giao (p90 = 41.6 ngày, max 45.8) ⇒ prevalence 30 ngày tối đa ≈ 0.649 × 44.5% ≈ **29%** của item line (*phép tính của tôi, nhãn "derived"*) | Fig 7: +3.44 pp, khoảng [0.77, 5.70]; lợi thế còn trong cả hai service; **khoảng cách chưa được hiệu chỉnh** ở Fig 7 |
| ④ Validation | Cohort giao theo thời gian; **label chín** (cần đã xác minh *extraction cutoff*). Dữ liệu: giao đến 2019-01-10, review đến 2019-02-20 ⇒ *nếu* cutoff ≥ 2019-02-20 thì mọi giao hàng đều có đủ 30 ngày (2019-01-10 + 30 = 2019-02-09) — nhưng cutoff **chưa được xác minh**, nên báo cáo không gán nhãn "non-response" | Rolling chronological; định nghĩa quy ước thời điểm dispatch (trường giao hàng chỉ có *ngày*); so sánh với/không warehouse; PR-AUC vs prevalence từng kỳ; recall/precision tại ngân sách can thiệp |
| ⑤ Leakage & rủi ro | Loại thuộc tính từ review; mỗi order ở một partition (item cùng order tương quan); low propensity ≠ responsiveness | Loại delay thực tế, ngày giao, sự kiện sau dispatch; `nearest_warehouse` ≠ nơi xuất kho; hiệu quả không bằng nhân quả |

**Q&A drills cho ML:**

| Câu hỏi | Trả lời mẫu |
|---|---|
| Vì sao không random split? | Dữ liệu là chuỗi thời gian + item cùng order phụ thuộc nhau; random split làm rò thông tin tương lai và các item cùng order ở hai phía. Dùng cohort theo thời gian, mỗi order một partition. |
| Vì sao PR-AUC thay vì ROC-AUC/accuracy? | OTIF failure chỉ 10.62%: accuracy 89.4% đạt được bằng cách luôn đoán "đúng hạn" 🔁 (1 − 0.1062). PR-AUC nhạy với lớp hiếm; thêm calibration và recall/precision tại ngân sách vì quyết định kinh doanh là *xếp hạng trong ngân sách*. |
| 44.5% có dùng làm baseline được không? | Không: đó là tỉ lệ *đã quan sát trong export*, không phải response 30 ngày; 🔁 chỉ ≈65% review đến ≤30 ngày nên prevalence 30 ngày thấp hơn (~29%); phải xác minh cutoff trước khi gán nhãn. |
| **Changed:** nếu cutoff trích xuất sớm hơn (ví dụ 2019-01-31)? | Các giao hàng cuối kỳ chưa đủ 30 ngày → loại khỏi tập huấn luyện (hoặc dùng survival/censoring) thay vì gán nhãn 0; kiểm tra: phân phối lag theo tuần giao. |
| **Changed:** nếu thêm text của review làm feature? | Rò: review text chỉ tồn tại *sau* sự kiện; chỉ hợp lệ cho mô hình hậu-review (stage B không áp dụng cho quyết định tại giao hàng). |
| **Changed:** nếu muốn kiểm tra tác động nhân quả của warehouse? | Không thể từ dữ liệu quan sát này: cần xác minh dispatch lineage và hiệu chỉnh case-mix; hoặc thí nghiệm/natural experiment. Chỉ có thể nói "association". |
| MLQ-1 có nhiều số 0 — xử lý thế nào? | Target gồm cả tháng không chi (2,587/6,000), nên so với baseline "tháng trước" và "trung bình 3 tháng"; có thể tách hai giai đoạn (có mua? → bao nhiêu?) nếu MAE bị zero-inflation chi phối. |

---

### A.7 Limitations chủ động nêu cho A1 (chọn 1–2)

1. **Review chọn lọc + follow-up chưa xác minh**: 44.5% là *observed coverage*, không phải response cuối cùng; ≤2 sao = 17.1% của review nhưng 7.6% của item mua — *không* phải tỉ lệ bất mãn.
2. **Warehouse effect là liên hệ**: `nearest_warehouse` ≠ nơi xuất kho; chưa hiệu chỉnh khoảng cách; khách lặp ⇒ khoảng bất định tối thiểu; Bonferroni xử lý đa so sánh, không xử lý confounding.
3. **Chỉ số thương mại là proxy**: contribution = revenue thực sau phân bổ coupon − `unit_cost × quantity`; GST/chi phí chưa xác minh (phần dư làm tròn gộp AUD 0.136).
4. **Một năm dữ liệu (2018)**: không tách được mùa vụ, xu hướng, khuyến mãi.
5. **EDA không huấn luyện model**: 5 MLQ là *đề xuất leakage-safe*, chưa kiểm chứng hiệu năng.
6. **Dependence**: bootstrap theo order, chưa theo khách ⇒ khoảng tin cậy có thể hẹp hơn thực tế.

### A.8 Cầu nối A1 ↔ A2 (để G có "một câu chuyện", nhưng không nói quá)

A3 spec §2: *nếu so sánh/kết hợp A1 và A2 phải kiểm tra key, grain, kỳ, đơn vị, nghĩa trước; batch A1 và A2 không tự nhiên là quần thể so sánh được; giá catalogue A1 không phải giá A2.* Vì vậy cầu nối là **kỷ luật phương pháp**, không phải số liệu hợp nhất:

| A1 (lịch sử 2018) | A2 (hiện tại 2019) | Cùng một nguyên tắc |
|---|---|---|
| Aggregate trước join, `join_audit` (fan-out ×3.54) | Gộp 3 CSV đã nộp rồi mới aggregate sang khách; `PROF-02` đối soát đơn–khách–tiền | **Đúng grain trước khi kết luận** |
| 44.5% order-level vs item-level; denominator khác câu hỏi khác | Residual vs raw charge: "charge lớn" ≠ "residual lớn" | **Đúng đại lượng so sánh** |
| `T3-TEXT-05` (đối chiếu độc lập với catalogue) | `DELIV-08` (đối chiếu độc lập với `order_total`), `PROF-01f` | **Check độc lập với code sửa/làm sạch** |
| Validation register 145 check; `VAL-CONFLICT-01` | `READBACK`, `AUDIT_EXPORT`, `CLAIMS-13` | **Validation tách khỏi transformation** |
| MLQ: validation theo thời gian, predictor tại thời điểm quyết định | DELIV: split có seed, held-out ≠ in-sample | **Không rò thông tin khi đánh giá** |

*Q&A:* **"Bạn có thể áp mô hình biểu giá A2 lên đơn A1 không?"** → Không tự động: khác kỳ (2018 vs 2019), tập khách/đơn khác, A1 không cung cấp cùng bộ trường biểu giá được xác nhận cho A2, và spec cảnh báo giá/quần thể không so sánh được. Check khả thi: so sánh theo *key, grain, kỳ, đơn vị* trước; nếu muốn thử, chỉ như kiểm tra thăm dò, không dùng để kết luận.

---

## 6. PHẦN B — A2

### Bản đồ evidence (mở theo thứ tự này khi demo)

| Check ID | Nội dung | Cell idx |
|---|---|---|
| EDA-01…04, Fig EDA-1/2 | Chẩn đoán thô | 15–19 |
| DELIV-01 → 05, 10 | Train rows → encoding → split → 4 model → held-out | 45–63 |
| (Alternatives) | 5 cách train khác | 64–66 |
| DELIV-06 → 09, 07b | Residual, rule, sensitivity, model-free check, retained | 89–108 |
| AUDIT_CONFIDENCE / CLAIMS-13 / decision | Log & kiểm text | 110, 117–119 |
| PROF-01 → 03 | Analysis copy, đối soát, aggregation | 137–141 |
| BASE-01 → 03 | Baseline & thống trị theo đơn vị | 142–145 |
| SCALE-01 → 03, NONLIN-01 | z-score vs min-max; phi tuyến | 146–158 |
| EVID-01, DIST-01, REC-01, RERUN-01 | Recommendation | 159–167 |

---

## B1. Spec 3.5 — Seasonal delivery-charge model (the "ML" của A2)

### ① Anchor: phương pháp → code

| Khái niệm (⚠ slide #) | Trong code |
|---|---|
| Multiple linear regression, OLS với intercept: `y = β0 + β1·distance + β2·expedited + β3·happy + ε` | `LinearRegression(fit_intercept=True)` mỗi mùa (`fit_seasonal_models`, cell 53) |
| Điều kiện nhận dạng được hệ số (full-rank design) | `np.linalg.matrix_rank(design) < 4` → raise |
| Train / held-out evaluation, split tái lập (seed), stratified | `train_test_split(random_state=5196, test_size=0.25, stratify=season×exp×happy)` |
| Metric: R² + absolute-error (MAE) | `r2_score`, `mean_absolute_error`; thêm RMSE, max\|e\| |
| Residual `e = observed − predicted` là công cụ chẩn đoán | `delivery_residuals` (nền cho 1.3) |
| Mã hóa biến nhị phân 0/1 nhất quán | `_to_binary` (1 = True; từ chối `'Yes'`, `'T'`) |

*Spec 3.5 bắt buộc:* 4 model (mỗi mùa), báo cáo Training n / Held-out n / R² / absolute-error, **đánh giá trên held-out**, R² ≳ 0.99, khuyến cáo điều tra nếu yếu.

### ② Decisions — what / why / how / alternative

| Quyết định | What | Why (theo case này) | How / evidence | Alternative bị loại |
|---|---|---|---|---|
| **Train rows** (DELIV-01) | 420 dòng đầy đủ của *missing batch* | Batch guarantee: giá trị quan sát được của missing batch là đúng; outlier batch chứa chính các charge bị nghi nên train trên đó "kéo" hệ số về phía bất thường; dirty batch chưa sửa, trường sai có thể chính là 1 trong 5 trường model | 500 − 80 dòng thiếu (mỗi dòng đúng 1 ô trống, 10 ô × 8 trường). Mùa: Summer 111, Autumn 93, Winter 117, Spring 99 | (c) 450 dòng đủ 5 trường model: hệ số lệch < 0.001 → lựa chọn chặt không tốn gì · (d) dirty: lệch tới **1.30**, MAE trên held-out sạch **0.32** · (e) outlier: lệch **1.30**, MAE **0.60** (>100× tệ hơn 0.0023) |
| **Bốn model, không gộp** | 1 OLS/mùa | Spec nêu rõ quan hệ tuyến tính *riêng từng mùa*; hệ số khác thật: intercept ≈10 (14 ở Winter), per-km 0.70–0.85, expedited +10 → +13, happy −2 → −4 | DELIV-04 bảng hệ số | 🔁 Gộp 1 model + dummy mùa (chỉ đổi intercept): R² **0.988 < 0.99**, MAE **0.48** (so 0.0024); gộp không dummy: R² 0.886. *(tự tính lại với split ngẫu nhiên khác, không phải kết quả notebook — dùng như "extra check" khi bị hỏi)* |
| **Split** (DELIV-03) | seed 5196, 25% held-out, stratify season×expedited×happy | Tổ hợp hiếm nhất (expedited & unhappy) chỉ 4–5 dòng/mùa; stratify đảm bảo nó nằm ở cả fit lẫn held-out để *mọi hệ số được thử* | 16 strata, nhỏ nhất 4 dòng; 315 fit + 105 held-out; Summer 83/28, Autumn 70/23, Winter 88/29, Spring 74/25; tái chạy cùng seed → id giống hệt, rời nhau, phủ đủ 420 | Random thuần: có thể không có "expedited+unhappy" ở held-out |
| **Encoding** (DELIV-02) | 1 = True cho cả 2 cờ | β2 = phụ phí expedited, β3 = điều chỉnh happy; token lạ → raise (cờ sai lệch cả một phụ phí) | Crosstab: expedited 330/90, happy 79/341 (False/True) | Mã hóa "unhappy" tương đương: `b0' = b0 + b3`, `b_unhappy = −b3` (đã kiểm: Summer 7.9992 / 2.0002) |
| **Metric & ngưỡng nghi ngờ** (DELIV-05) | R², MAE, RMSE, max\|e\| theo mùa | R² ≥ 0.99 *cần nhưng chưa đủ* | R² held-out: 0.9999996 / 0.9999996 / 0.9999997 / 0.9999996 (Summer/Autumn/Winter/Spring). MAE 0.0022 / 0.0023 / 0.0023 / 0.0025. Max\|e\| 0.0052 / 0.0060 / 0.0048 / 0.0058 | In-sample R² chỉ để đối chiếu, **không** là evidence (spec) |

**Vì sao R² ≈ 1 không đáng ngờ — "sàn làm tròn cent".** Charge được ghi tới cent. Nếu mô hình hoàn hảo, sai số chỉ còn do làm tròn ~ Uniform(−0.005, +0.005): `E|e| = 0.0025`, `RMSE = 0.01/√12 ≈ 0.0029`. Held-out MAE 0.0022–0.0025 và RMSE 0.0028–0.0030 **nằm đúng ở sàn đó**. Phần dư ≤ 0.001 thêm là sai số ước lượng hệ số. Đây là lập luận *vì sao fit quá tốt vẫn hợp lý*, và là cơ sở cho τ ở 1.3.

### ③ Demo script (4 bước spec §4)

1. **Input/problem:** mở DELIV-01 → "500 dòng missing batch → 420 dòng đủ; 80 dòng bị loại, mỗi dòng thiếu đúng 1 trường; outlier & dirty batch không dùng để train" (bảng `sources`).
2. **Output:** DELIV-04 (bảng hệ số) và DELIV-05 (bảng 4 mùa: n_train, n_holdout, R², MAE). Chỉ vào Winter: *"base ≈ 14, 0.85 AUD/km, +13 nếu expedited, −4 nếu happy."*
3. **Cách ra & ý nghĩa:** "Hệ số là OLS fit trên 75%, đánh giá trên 25% chưa từng thấy. +13 nghĩa là: cùng khoảng cách, cùng mức hài lòng, đơn expedited mùa đông trả thêm 13 AUD."
4. **Supporting check:** DELIV-05 cell kế (residual structure) + DELIV-10.
   - *Establishes:* không còn cấu trúc hệ thống — mean residual theo cờ ≤ 0.23 cent, trend theo khoảng cách ≤ 0.51 cent trên toàn dải; cờ expedited/happy sai sẽ để lại residual ≥ **1,680×** / **336×** residual lớn nhất (0.0060) ⇒ không dòng train nào mang cờ sai.
   - *Does NOT establish:* mô hình đúng với dữ liệu *ngoài* 2019 / ngoài dải khoảng cách đã thấy; không chứng minh dirty/outlier batch sạch (đó là việc 1.1 & 1.3).

### ④ Grain – Units – Limits

- **Grain:** 1 dòng = 1 đơn hàng; mô hình ở mức đơn. **Units:** AUD, AUD/km, cờ 0/1. **Phạm vi khoảng cách train:** 0.02–10.39 km.
- **Limits (nêu chủ động):** (i) held-out 105 dòng vừa dùng đánh giá (DELIV-05) vừa thiết lập τ (1.3) — kiểm tra nhất quán, không phải độc lập; (ii) biểu giá có vẻ *xác định + làm tròn cent* — dữ liệu thật nhiễu hơn sẽ không đạt R² này; (iii) 4 đơn outlier-batch nằm ngoài dải khoảng cách fit tới 0.56 km (đã kiểm: residual ≤ 0.0034).

### ⑤ Q&A drills

| Câu hỏi | Trả lời mẫu (ý chính) |
|---|---|
| Tại sao R² 0.9999996 mà bạn không nghi overfit? | Held-out R² gần bằng in-sample (0.9999996 vs 0.9999996); MAE ≈ sàn làm tròn 0.0025; residual không có cấu trúc; 4 tham số/≈70–88 dòng — không có dư địa overfit. Nguồn của "độ hoàn hảo" là biểu giá tất định. |
| Tại sao 4 model chứ không 1 model có `season`? | Hệ số khác nhau thật (base 10 vs 14; slope 0.70–0.85; phụ phí 10–13). Mô hình gộp chỉ đổi intercept để lại residual hàng AUD (🔁 R² 0.988, MAE 0.48). |
| Vì sao không dùng dirty/outlier batch train cho "nhiều dữ liệu hơn"? | Hệ số lệch tới 1.30 AUD và sai số held-out tăng >100× (alt d/e). Dữ liệu bẩn làm hỏng thước đo dùng để phát hiện bẩn. |
| **Changed:** Nếu một mùa có R² = 0.93? | Không dùng; điều tra trước (spec). Check: residual theo từng cờ/khoảng cách (có tương tác/phi tuyến?), phân phối khoảng cách, có dòng sai cờ/khoảng cách trong train không (DELIV-10-style), rồi mới cân nhắc robust regression (Huber) hoặc loại có căn cứ. |
| **Changed:** Nếu train có 20 dòng mỗi mùa? | 4 tham số/15 fit → ước lượng không vững; ưu tiên cross-validation thay vì 1 split, báo khoảng bất định của hệ số; cân nhắc gộp các mùa có hệ số gần nhau *chỉ khi* kiểm định cho phép. |
| **Changed:** Thêm interaction distance×expedited? | Residual theo cờ đã ≤ 0.23 cent → không có bằng chứng cần; thêm tham số khi không có tín hiệu chỉ tăng phương sai. Check: hệ số interaction ≈ 0 và held-out MAE không giảm dưới sàn. |
| Giải thích hệ số β3 âm? | Khách *happy* (VADER ≥ 0.05, hoặc "No review submitted") được giảm 2–4 AUD tùy mùa; đây là mô tả biểu giá, không phải quan hệ nhân quả. |

---

## B2. Section 1.3 — Outlier data: nhận diện & loại các dòng bất thường

### ① Anchor

| Khái niệm (⚠ slide #) | Trong code |
|---|---|
| **Contextual (conditional) outlier**: bất thường *tùy theo ngữ cảnh* (mùa, khoảng cách, cờ), không phải giá trị thô | Dùng **residual** từ mô hình mùa thay vì charge thô |
| Outlier score từ **linear model residual** | `delivery_residuals` |
| **Modified z-score / Hampel identifier** (Iglewicz & Hoaglin 1993; Hampel 1974 ✔ notebook references): `\|e − median\| / (1.4826·MAD) > 3.5` | `residual_threshold` → τ = 3.5 × 1.4826 × MAD |
| Ước lượng robust (median/MAD) để outlier không tự làm phồng thang đo | m, MAD tính **chỉ từ 105 residual held-out sạch** |
| Validation: structural, content, logical checks (Week 11 *Data Validation*, slides 4, 22, 27 ✔) | DELIV-08 (logical: order_total identity), DELIV-09 (retained), read-back 2.2 |

### ② Decisions — what / why / how / alternative

| Quyết định | What | Why | How / evidence | Alternative bị loại |
|---|---|---|---|---|
| **Score bằng residual** | Điểm = `e = observed − expected(season model)` | Charge cao có thể hợp lệ (đơn Winter expedited tới 32.00 AUD, residual 0.0015); charge sai có thể nằm trong dải thường (10/24 outlier ≤ P95 = 28.38) | Fig 2: corr(raw charge, \|e\|) = 0.52 — liên quan nhưng *kích thước không tách được*; residual tách thành 2 nhóm cách **×1,021** (476 dòng \|e\| ≤ 0.00612; 24 dòng 6.247–22.001) | Boxplot/3σ trên charge thô (xem benchmark dưới) |
| **Hiệu chuẩn τ chỉ từ held-out sạch** (DELIV-07) | m = −0.000024; MAD = 0.002012; σ_robust = 0.002984; **τ = 0.010442** | Không để charge đang bị xét tự đặt ngưỡng cho nó; two-sided vì undercharge cũng phá biểu giá | n = 105; kết quả 24 loại (24 dương, 0 âm) | Hiệu chuẩn trên chính outlier batch (xem DELIV-07b) |
| **Biện minh τ** | 3.5·1.4826 là quy ước Gauss; nhiễu thật ở đây là **làm tròn cent** (bị chặn ≤ 0.006) | Ngưỡng an toàn đến từ *plateau* chứ không từ xác suất đuôi Gauss | **Plateau:** mọi τ ∈ (0.00614, 6.2472) cho đúng 24 id — dải **×1,017**. τ chọn = 1.7× residual hợp lệ lớn nhất, 598× dưới anomaly nhỏ nhất | τ=0.005 (biên làm tròn): flag **43** (xóa nhầm 19 hợp lệ); τ=0.006: flag **25** |
| **Robustness của τ** | Đổi cutoff/scale | Chứng minh kết quả không phụ thuộc lựa chọn tùy ý | cutoff 3 → τ = 0.0090 → cùng 24; τ riêng từng mùa (0.0105–0.0140) → cùng 24; τ + 1 cent = 0.0204 → cùng 24 (chịu được 1 cent lệch của charge hợp lệ) | — |
| **Cross-check tự hiệu chuẩn** (DELIV-07b) | Iterative trimming trên chính outlier batch, không dùng dòng sạch, không τ | Kiểm tra lựa chọn thang nhiễu | Hội tụ sau 2/2/3/3 vòng (Summer/Autumn/Winter/Spring) → **cùng 24** | — |
| **Model-free corroboration** (DELIV-08) | `c* = order_total − order_price·(1 − coupon/100)` | Trong outlier batch, `order_price`, `coupon`, `order_total` đúng ⇒ có thể suy charge thực sự đã tính | 24 dòng mâu thuẫn với total, **trùng hoàn toàn** tập residual-rule; vượt đúng **{6.25, 9.50, 14.75, 22.00}** AUD; model tái tạo charge đã tính trong ≤ 0.0054; **476/476** charge giữ lại là charge mà total cho phép (5 total cho phép 2 cent liền kề) | Dùng `c*` làm *detector*: bị loại vì nó chỉ đúng khi `order_total` đáng tin — là bằng chứng bổ trợ, không phải detector chính |
| **Remove, không repair** | Loại 24 dòng, giữ nguyên 476 | Spec 1.3: remove; sửa charge rồi giữ dòng là sai yêu cầu. 1.1 (dirty) *repair* trường gốc; 1.2 (missing) *recover* theo thứ bậc deterministic → algebraic → model; 1.3 *remove* vì không có nguồn để biết "charge đúng" ngoài chính model | DELIV-09: 500 = 476 + 24 rời nhau | — |

**Benchmark (DELIV-08) — vì sao quy tắc thô sai:** nhãn model-free = 24 bất thường / 476 hợp lệ.

| Quy tắc | Flag | Xóa nhầm hợp lệ | Bỏ sót |
|---|---|---|---|
| Tukey fence trên charge thô (27.38) | 28 | **13** | **9** |
| \|z\| > 3 trong mùa trên charge thô | 8 | 0 | **16** |
| **Residual \|e − m\| > τ (chọn)** | 24 | **0** | **0** |

*Giải thích sự khác nhau về cách xử lý:* dirty ≠ missing ≠ outlier vì **mức độ biết "giá trị đúng"** khác nhau — dirty có batch guarantee ≤1 trường sai + quy tắc kiểm chéo ⇒ sửa được; missing có ô trống ⇒ khôi phục theo thứ bậc bằng chứng; outlier chỉ biết "charge này không khớp biểu giá" ⇒ loại.

### ③ Demo script (4 bước)

1. **Source record:** mở bảng DELIV-07 (cell 96). Chọn **CORD001276** (Autumn, 5.1835 km, không expedited, happy; charge **17.29**): *"Charge 17.29 chỉ ở percentile 74 của batch — nhìn thô thì bình thường."*
2. **Output/so sánh:** model kỳ vọng **11.0429**, residual **+6.2471**, modified z ≈ 2,094. Rồi chọn **CORD001338** (Winter, expedited, unhappy, charge **32.00** — cao nhất giữ lại): residual **0.0015** → *giữ*. Cùng 1 cột raw charge nhưng quyết định ngược nhau.
3. **Cách ra & ý nghĩa:** "τ = 3.5 × 1.4826 × MAD của 105 residual sạch = 0.0104 AUD. Residual 6.25 gấp ≈ 600 lần τ; residual hợp lệ lớn nhất 0.006 chỉ ≈ 0.6τ." Ý nghĩa: 6.25 là **phụ phí cố định** cộng thêm vào charge đã tính, không phải nhiễu.
4. **Supporting check:** DELIV-08 (+ Figure 3) và plateau.
   - *Establishes:* 24 id của residual-rule = 24 đơn mà charge mâu thuẫn với chính total; bốn mức phụ phí rời rạc; quy tắc chọn không xóa nhầm (0) hay bỏ sót (0) so với nhãn model-free; kết quả ổn định theo τ, cutoff, thang theo mùa, và thuật toán tự hiệu chuẩn.
   - *Does NOT establish:* (i) một charge bị sửa *đồng thời* với total sẽ **lọt** DELIV-08 — vì vậy residual rule là detector chính; (ii) không chứng minh batch guarantee "chỉ `delivery_charges` hỏng" — đó là giả định công bố; (iii) không phải khoảng dự đoán thống kê.

### ④ Grain – Units – Limits

- **Grain:** dòng/đơn; quyết định theo mùa (4 model). **Units:** AUD (residual, τ), z không đơn vị. **Hậu quả audit:** 24 dòng `ROW_REMOVED`, `field_name = delivery_charges`, `issue_type = outlier_row`, **cả 24 `high`** (cổng: margin > max(0.005, max\|e\| held-out mùa); charge phải khác mọi cent total cho phép > 0.01 và model tái tạo một cent đó trong cổng).
- **Limits nêu chủ động:** τ chỉ gấp 1.7× residual hợp lệ lớn nhất ⇒ *quyết định dựa vào plateau, không dựa vào biên τ*; một charge hợp lệ lệch 1 cent (|e − m| tới 0.016) sẽ bị loại bởi τ=0.0104 — τ+0.01 chịu được nhưng không đổi kết quả hôm nay, chỉ quan trọng với dữ liệu tương lai; mọi outlier ở đây là **overcharge** (24/24 dương) nên khả năng bắt undercharge chưa được thử bằng dữ liệu thật.

### ⑤ Q&A drills

| Câu hỏi | Trả lời mẫu |
|---|---|
| Vì sao không dùng IQR/boxplot? | Charge phụ thuộc mùa, khoảng cách, cờ ⇒ outlier là *có điều kiện*. Tukey xóa nhầm 13 đơn hợp lệ (đơn đắt thật) và bỏ sót 9; 3σ theo mùa bỏ sót 16. Residual không xóa nhầm/bỏ sót nào. |
| Vì sao 3.5? Có phải con số tùy ý? | Là cutoff modified-z chuẩn (Iglewicz–Hoaglin), nhưng bảo chứng thật là **plateau ×1,017**: 3 → τ = 0.0090, vẫn 24 id; bất kỳ τ nào từ 0.0061 đến 6.2 cho cùng kết quả. |
| Ngưỡng 0.08 trong spec thì sao? | Là *marking tolerance* cho giá trị đã sửa, **không** phải ngưỡng outlier (spec §3.5). Em vẫn chỉ ra τ=0.08 cho cùng 24 id để cho thấy không nhạy. |
| Held-out vừa dùng đánh giá vừa dùng đặt τ — có vòng tròn không? | Có phần nhất quán chứ không độc lập; vì thế evidence độc lập là plateau, DELIV-07b (không dùng dòng sạch) và DELIV-08 (dùng total, không dùng model). Em đã ghi rõ trong notebook. |
| **Changed:** Nếu `order_total` cũng có thể sai? | DELIV-08 mất giá trị làm bằng chứng độc lập; residual rule vẫn dùng được (nó không đọc total). Check khả thi: DELIV-07b (tự hiệu chuẩn), và so sánh với total trên các dòng mà cart-price + coupon ổn. Trade-off: độ tin cậy giảm từ `high` xuống `medium`. |
| **Changed:** Nếu anomaly chỉ là +0.05 AUD? | τ=0.0104 vẫn bắt, nhưng lúc đó phải xét rounding/1-cent artefact (τ+0.01) và nhiều khả năng cần thêm bằng chứng — ngưỡng 0.05 nằm trong plateau nên chưa đủ để phân biệt hai trường hợp nếu nhiễu thật lớn hơn. Đề xuất: đo lại nhiễu sạch trên batch mới. |
| **Changed:** Nếu nhiễu nền lớn hơn (R² ≈ 0.95)? | MAD tăng ⇒ τ tăng tự động (robust scale), nhưng plateau thu hẹp; phải xem phân phối residual, dùng robust regression/iterative trimming (DELIV-07b) và báo cáo precision/recall dựa trên nhãn độc lập nếu có. |
| **Changed:** Muốn sửa thay vì loại? | Chỉ khi có charge "đúng" tái tạo được: ở đây `c*` cho charge đã tính — nhưng spec yêu cầu *remove*, và việc dùng `c*` làm đáp án sửa dựa vào chính giả định về total. Em giữ remove + audit. |
| Vì sao giữ 4 đơn ngoài dải khoảng cách? | Ngoại suy ≤ 0.56 km, residual ≤ 0.0034, không đơn nào bị loại — quyết định không phụ thuộc ngoại suy. |

---

## B3. Task 3.1 — Build the customer-level analysis copy

### ① Anchor

| Khái niệm (⚠ slide #) | Trong code |
|---|---|
| **Grain** & aggregation: đổi grain order → customer bằng `groupby` | `build_customer_profiles` (cell 140) |
| **Data integration** (concat nhiều nguồn giữ nhãn nguồn) & kiểm toàn vẹn khóa | `analysis_orders = concat(...assign(source_batch=...))` |
| **Redundancy / correlation analysis** khi chọn thuộc tính (Han, Kamber & Pei §3.5 ✔ trích trong notebook) | `axis_shares` (eigenvalue của ma trận tương quan) |
| Validation: structural/content/logical (Week 11 slides 4, 22, 27 ✔) | PROF-01a–f |

### ② Decisions

| Quyết định | What | Why | How / evidence |
|---|---|---|---|
| **Chỉ đọc 3 CSV đã nộp** (PROF-01) | Task 3 đọc file trên đĩa, không dùng frame trong bộ nhớ hay raw | Spec: "read and concatenate the three cleaned CSVs you are submitting" | 6 check PASS: schema 16 cột; 1,476 dòng/1,476 order_id duy nhất; dirty 500/500, missing 500/500, outlier = 500 − 24 ROW_REMOVED; không ô trống, `order_total > 0`, `distance ≥ 0`; file = frame vừa export; địa lý khách |
| **Không khôi phục outlier, không thêm A1** | Giữ 1,476, không về 1,500 | Spec | PROF-02: 1,500 − 24 = 1,476 đơn; 478 − 1 (CUS00317, đơn duy nhất là outlier) = **477 khách**; 333 khách có đơn ở >1 batch (nên không profile theo từng batch) |
| **Đối soát tiền & truy vết Task 1 → Task 3** | Chỉ `order_total`, `distance` và *tập đơn giữ lại* ảnh hưởng thuộc tính | Cho biết quyết định cleaning nào có thể đổi kết quả Task 3 và độ tin cậy của chúng | 184 audit entry: 36 chạm `order_total`/`distance` đều `high`; 24 removal đều `high`; 18 `medium` (cờ expedited) **không được Task 3 đọc**; tổng tiền AUD **5,467,474.08** khớp tổng order_total |
| **PROF-01f: một địa chỉ/khách** | Mỗi khách có đúng 1 lat/long/warehouse/distance | Kiểm tra **độc lập với hàm haversine**: nếu repair 1.1 sót, một khách sẽ có 2 giá trị | 22 khách khác nhau ở raw (8 mất dấu lat, 8 sai tên warehouse, 7 distance phồng) → **0** ở output. *Không thấy được lỗi của khách chỉ có 1 đơn* ⇒ chỉ thấy 7/8 repair distance |
| **Chọn 3 thuộc tính** | `order_count`, `mean_order_value`, `mean_delivery_distance`; **bỏ `total_paid`** | Một thuộc tính / một chiều hành vi (activity, spending/order, geography). `total_paid = order_count × mean_order_value` (sai khác tối đa **3.6e−12** AUD) và corr 0.86 với `order_count` ⇒ đếm trùng chi tiêu trong khoảng cách Euclid | Redundancy (sau z-score, thành phần chính 1/2/3): chọn → **0.358 / 0.332 / 0.311** (≈ 1/3 mỗi trục = không dư thừa); count+total+mean → **0.674 / 0.314 / 0.012** (3 cột nhưng ≈ 2 chiều); mọi tập chứa `total_paid` dồn 50–67% lên 1 trục |

*Trade-off phải nói:* bỏ `total_paid` không mất thông tin tổng chi tiêu vì nó là tích của hai thuộc tính đã chọn; đổi lại hai khách cùng tổng chi tiêu nhưng khác thói quen (1 đơn lớn vs nhiều đơn nhỏ) **vẫn tách xa nhau** — phù hợp mục tiêu so sánh hành vi.

### ③ Demo script (4 bước)

1. **Source:** PROF-03 ví dụ **CUS00114** — 9 đơn đã giữ, từ 3 batch (dirty/missing/outlier), `distance` đều **3.8912**, tổng AUD 25,034.22.
2. **Output:** 1 dòng profile: `order_count = 9`, `mean_order_value = 2,781.58`, `mean_delivery_distance = 3.8912` (và `total_paid = 25,034.22`).
3. **Cách ra & ý nghĩa:** `groupby(customer_id)`: count distinct `order_id`; mean `order_total`; mean distance. Lưu ý `mean_delivery_distance` thực ra là **một khoảng cách cố định/khách** (PROF-01f) — là thuộc tính *vị trí*, không phải trung bình các lần giao.
4. **Check:** bảng PROF-01 + PROF-02. *Establishes:* tách batch/đối soát số đơn–khách–tiền khép kín; không khách nào có 2 địa chỉ. *Does NOT establish:* không phải customer lifetime value (profile chỉ phủ 1,476 đơn A2 năm 2019, 2019-01-01 → 2019-12-31); PROF-01f không bắt được lỗi của khách chỉ có 1 đơn.

### ④ Grain – Units – Limits

- **Grain:** 1 dòng = 1 `customer_id` (477), `customer_id` không bao giờ bị transform. **Units:** orders, AUD (gồm giao hàng sau giảm giá, *không* là lợi nhuận/merchandise), km. **Limits:** 24 đơn bị loại làm hụt activity của 23 khách (CUS00024 mất 2 đơn); CUS00317 không có profile.

### ⑤ Q&A drills

| Câu hỏi | Trả lời mẫu |
|---|---|
| Vì sao bỏ `total_paid`? | Là tích của 2 thuộc tính khác (sai khác 3.6e−12) → counting spending hai lần trong Euclid; bảng redundancy: count+total+mean để trục thứ 3 chỉ còn **1.2%** phương sai. |
| **Changed:** Nếu phải dùng `total_paid` + `order_count`? | Chấp nhận hai chiều "volume" và "frequency" nhưng không thêm `mean_order_value`; corr 0.86 nên kỳ vọng ~62% khoảng cách dồn một trục; hoặc dùng weighting/PCA. Check: `axis_shares` cho tập đó (count+total+distance = 0.621/0.333/0.046). |
| **Changed:** Nếu muốn giữ outlier đã loại? | Spec cấm khôi phục để về 1,500 dòng. Về nội dung: các dòng đó có `delivery_charges` không khớp biểu giá nên không phải quan sát sạch. Em không khẳng định tác động lên profile nếu giữ (chưa tính); check khả thi là chạy lại PROF-03 với/không có 24 dòng để so sánh, và nêu rõ tác động 24 đơn/23 khách như một limitation. |
| Vì sao có 477 khách thay vì 478? | CUS00317 chỉ có 1 đơn và đó là outlier bị loại; không có dữ liệu giữ lại để profile. |
| Check nào độc lập với cleaning code? | PROF-01f: tính nhất quán địa lý *giữa các đơn của cùng khách* — không dùng haversine; cho thấy 22 → 0. Giới hạn: khách 1 đơn. |

---

## B4. Task 3.2 — Original scales, distributions and relationships

### ① Anchor

| Khái niệm (⚠ slide #) | Trong code |
|---|---|
| EDA 1 biến: min, median, mean, SD, IQR, **skew, kurtosis**, tail (1.5·IQR fence) | `describe_attributes` (BASE-01) |
| EDA 2 biến: Pearson & Spearman, scatter | Fig 4 d–f; `corr` bảng PROF-03 |
| **Euclidean distance bị chi phối bởi thang đo** (lý do cần transformation theo *mục đích*; Week 8 *Data Transformation (I)* slides 3 & 17 ✔) | `distance_shares`, `pairwise_distances` (BASE-03) |

### ② Decisions & findings

| Câu hỏi | Cách trả lời | Kết quả |
|---|---|---|
| Đơn vị & thang? | BASE-01 | `order_count` (đơn): 1–9, median 3, SD 1.64 · `mean_order_value` (AUD): 138.99–10,916.77, median 3,516, SD **1,446** · `mean_delivery_distance` (km): 0.021–10.39, median 5.10, SD 2.32. SD chênh nhau ≈ 3 bậc độ lớn |
| Hình dạng? | skew, kurtosis, Fig 4a–c | `order_count` rời rạc 9 giá trị, skew 0.75 (86 khách = 18% chỉ có 1 đơn) · `mean_order_value` skew 0.49 nhưng **kurtosis dư 1.6** (đuôi nặng) · `mean_delivery_distance` đối xứng (skew −0.05), kurtosis −0.86 |
| Miền giá trị (cần cho log/sqrt/scale) | đếm missing/0/âm/hằng | **không** missing, zero, âm, hằng ⇒ cả 2 scaler, sqrt, log, log1p đều xác định |
| Extreme có phải lỗi? | BASE-02 | 6 khách vượt fence trên `mean_order_value` (AUD 7,349–10,917), *mỗi người chỉ 1–2 đơn*; SD của `mean_order_value` giảm khi nhiều đơn (2,084 ở 1 đơn → 913 ở 4 đơn) ⇒ extreme là **trung bình ít quan sát**, hành vi thật; mỗi đơn đã qua read-back (cart-price, total, haversine) ⇒ **giữ**, không trim/winsorise |
| Quan hệ giữa thuộc tính? | corr | \|r\|, \|ρ\| ≤ 0.09 giữa 3 thuộc tính ⇒ không trùng lặp thông tin |
| **Nếu dùng raw units trong khoảng cách thì cái nào thống trị?** (BASE-03) | Phân rã Σ khoảng cách² trên **113,526 cặp khách** | `mean_order_value` chiếm **99.999615%**; `order_count` 0.000128%; distance 0.000257%. Khoảng cách raw tương quan **+1.000** với chênh lệch chi tiêu; **99.4%** trong 10 láng giềng gần nhất trùng với láng giềng chỉ-theo-chi-tiêu ⇒ so sánh raw = so sánh chi tiêu, vì *AUD số lớn*, không vì chi tiêu quan trọng hơn |

**Lập luận nền (nói được bằng lời):** với Euclid, `Σ_{i<j}(x_i − x_j)² = n² · Var(x)` — mỗi thuộc tính đóng góp vào khoảng cách² *tỉ lệ thuận với phương sai của nó* (đã kiểm từng cặp bằng assert). Vì vậy kết luận "scaling bắt buộc" là hệ quả toán học, không phải ý kiến.

### ③ Demo script

1. **Source:** `profiles` (477 khách × 3 thuộc tính), bảng BASE-01.
2. **Output:** BASE-03 — hàng `share of squared distance`: 0.000128% / **99.999615%** / 0.000257%.
3. **Cách ra & ý nghĩa:** "Mọi cặp khách (113,526 cặp) → khoảng cách Euclid; chia nhỏ theo từng thuộc tính. Thuộc tính nào có SD lớn nhất thì thống trị. Vậy cần đưa 3 thuộc tính về cùng thang trước khi so sánh."
4. **Check:** assert đối chiếu *từng cặp* với công thức phương sai. *Establishes:* thống trị theo thang đo là chính xác, không xấp xỉ. *Does NOT establish:* chưa nói thang nào *đúng* (đó là 3.3–3.5), cũng không chứng minh tồn tại cụm.

### ④ Grain – Units – Limits

- **Grain:** khách; **Units:** orders / AUD / km (khác nhau — lý do của cả Task 3). **Limits:** `order_count` rời rạc 9 mức ⇒ nhiều tie; `mean_order_value` của khách 1–2 đơn nhiễu; profile chỉ là mẫu A2 đã giữ.

### ⑤ Q&A drills

| Câu hỏi | Trả lời mẫu |
|---|---|
| Vì sao skew 0.49 vẫn nói đuôi nặng? | Skew chỉ đo bất đối xứng; **kurtosis dư 1.6** và 6 khách vượt fence cho thấy đuôi nặng. Đây là lý do không dùng min-max và cũng là lý do kiểm log (3.4). |
| **Changed:** Nếu `mean_order_value` tính theo USD? | Đổi đơn vị chỉ nhân thang với một hằng số; SD vài trăm AUD vẫn ≫ 1.6 orders nên raw vẫn bị chi tiêu áp đảo. Sau z-score kết quả **bất biến** với đổi đơn vị — một lý do thực tế để chọn z-score. |
| **Changed:** Nếu thêm 1 khách chi tiêu AUD 200,000? | Raw: thống trị càng nặng; min-max: mọi khách khác bị nén về ≈ 0 (range bị 1 điểm quyết định, SCALE-03 cho thấy range −33% khi bỏ 5 điểm vs SD chỉ −7%); z-score: SD tăng, các khách khác nén nhưng ít hơn. Check: tái chạy SCALE-02/03. Nếu extreme đó là *thật* ⇒ cân nhắc robust scaling như phân tích độ nhạy. |
| Có nên loại 6 khách extreme? | Không: đã qua read-back, là hành vi thật; loại sẽ che đúng nhóm mà segmentation khám phá nên thấy. Nêu rõ: họ chỉ có 1–2 đơn ⇒ mean nhiễu — là limitation chứ không phải lỗi dữ liệu. |

---

## B5. Task 3.5 — Recommendations, boundaries and limitations

(Dựa trên 3.3 *scaling* và 3.4 *phi tuyến* làm evidence đầu vào.)

### ① Anchor

| Khái niệm (⚠ slide #) | Trong code |
|---|---|
| **z-score** `(x − μ)/σ`; **min-max** `(x − min)/(max − min)` (Han, Kamber & Pei §3.5.2 ✔) | `zscore`, `compare_scaling` (SCALE-01/02) |
| **Transformation phụ thuộc mục đích**, không "lệch → log" tự động (Week 8 slides 3 & 17 ✔: purpose-specific transformation, log scaling) | NONLIN-01 (sqrt/log/log1p rồi z-score) |
| Thứ tự phép biến đổi: *phi tuyến → rồi scale* | REC-01: "none → z-score" (nêu thứ tự dù không dùng phi tuyến) |
| Standardisation trong clustering không có phương pháp tốt nhất tuyệt đối (Milligan & Cooper 1988 ✔) | Phần Limitations của 3.5 |

### ② Decisions — bảng recommendation (đúng cấu trúc yêu cầu)

| Attribute | Nonlinear | Scaling | Evidence then justification (rút gọn) |
|---|---|---|---|
| `order_count` | **none** | **z-score**, `z = (x − 3.094)/1.636` | Rời rạc, 9 giá trị, skew 0.75, đuôi vừa (top 1% = 13% tổng z², max z 3.6). log/sqrt hạ xuống 5%/8% nhưng làm bước 1→2 đơn nặng gấp **3.1×/1.8×** bước 4→5 (NONLIN-01); log đổi **26%** láng giềng (DIST-01). Tuyến tính giữ mỗi đơn thêm = một bước như nhau. |
| `mean_order_value` | **none** | **z-score**, `z = (x − 3,653.690)/1,445.783` | min-max còn 16% trọng số vì 1 khách AUD 10,917 quyết định range (−33% range vs −7% SD khi bỏ 5 điểm, SCALE-03). **log over-correct:** skew 0.49 → **−1.94**, min z **−6.2**, 5/5 khách extreme trở thành người mua rẻ 1 đơn, top-1% share 0.14 → 0.25. sqrt lật skew sang −0.50, đổi 12% láng giềng và mất nghĩa AUD. |
| `mean_delivery_distance` | **none** | **z-score**, `z = (x − 5.022)/2.319` | Đối xứng (skew −0.05). min-max cho nó **46%** trọng số (phân phối phẳng ⇒ SD lớn so với range). Mọi phi tuyến tạo "đuôi thấp giả" từ khách sát kho (min z: sqrt −3.5, log1p −3.6, **log −7.9**); log đổi **32%** láng giềng. |

**Vì sao z-score thắng min-max (SCALE-02, DIST-01):** z-score chia đều **1/3** khoảng cách² cho mỗi thuộc tính; min-max chỉ cân bằng *range* chứ không cân bằng *độ phân tán* ⇒ 38% / 16% / 46%. Min-max giữ 71% láng giềng, robust scaling 83%, nhưng đều re-weight theo hình dạng phân phối.

**Đo tác động lên so sánh khách (DIST-01, so với "none → z-score"):**

| Cách biểu diễn | 10-NN overlap | Rank corr của mọi khoảng cách cặp |
|---|---|---|
| raw units | **0.069** | 0.506 |
| log(distance) rồi z | 0.680 | 0.933 |
| min-max | 0.708 | 0.956 |
| robust (median/IQR) | 0.830 | 0.988 |
| sqrt(`mean_order_value`) rồi z | 0.879 | 0.984 |

→ **Scaler là quyết định lớn nhất**; phi tuyến chỉ quan trọng khi sai chỗ (log lên distance).

**Hai điểm dễ bị hỏi mâu thuẫn — giải trước:**
1. *"sqrt tốt cho `total_paid` nhưng bạn chọn none cho `mean_order_value`?"* Không mâu thuẫn: `total_paid` lệch phải (0.83) vì là tích count × value, sqrt gần đối xứng (−0.02); `mean_order_value` chỉ lệch 0.49 và sqrt làm nó over-correct (−0.50). Phân tích `total_paid` chỉ mang tính **bổ sung** vì thuộc tính này không được chọn (§B3).
2. *"z-score cho mỗi thuộc tính đúng 1/3 tổng nhưng sao trong láng giềng gần chỉ 26/39/34%?"* 1/3 là trên **mọi cặp** (toàn cục); với 10 láng giềng gần nhất, `order_count` chỉ có 9 mức nên hay hòa, đóng góp ít hơn. Đây là limitation đã đo, không phải lỗi.

**Thứ tự phép biến đổi:** nếu có cả hai thì **phi tuyến trước, scale sau** (z-score có giá trị âm nên log/sqrt không xác định trước khi scale; scale cuối giữ trọng số bằng nhau). Ở đây chỉ còn 1 bước (z-score) với tham số đóng băng để áp cho khách mới.

### ③ Demo script

1. **Input:** `profiles` + bảng SCALE-02 (trọng số 3 cách scale).
2. **Output:** bảng REC-01 (3 dòng) và DIST-01 (Fig 5).
3. **Cách ra & ý nghĩa:** "Mỗi lựa chọn được đo bằng *thay đổi khoảng cách giữa các khách*, không bằng độ chuẩn của phân phối. Sau recommendation, `order_count`, `mean_order_value`, `mean_delivery_distance` mỗi cái chiếm đúng 0.333 khoảng cách²."
4. **Check:** RERUN-01: tái đọc 3 CSV + audit từ đĩa, kiểm byte-identical, tái dựng profile + EVID-01 + REC-01, test 11 claim: **16/16 check PASS**. *Establishes:* các số trong bảng khớp với dữ liệu nộp; Task 3 không ghi CSV, không thêm audit entry. *Does NOT establish:* tồn tại cụm có nghĩa; "equal weighting" là lựa chọn mô hình khám phá, **không** bằng chứng 3 chiều quan trọng như nhau; chưa đánh giá segmentation.

### ④ Grain – Units – Limits (đọc to ở cuối)

1. Profile chỉ phủ 1,476 đơn A2 (2019); 24 đơn bị loại từ 23 khách làm *activity* thấp hơn thực; CUS00317 không có profile; **không phải lifetime value**.
2. Trung bình 1–2 đơn nhiễu — chính là các khách extreme.
3. `order_total` gồm giao hàng sau coupon — không phải lợi nhuận.
4. Khoảng cách là đường thẳng tới kho gần nhất trong 3 kho, bỏ qua hướng (hai khách ở hai phía một kho trông giống nhau); log không xác định cho khách tương lai có distance 0.
5. Tham số z-score là thống kê của mẫu này: **khách mới dùng μ, σ đóng băng**; nếu có held-out thì fit trên train.
6. DIST-01 đo mức dịch chuyển láng giềng, không chứng minh cụm.

### ⑤ Q&A drills

| Câu hỏi | Trả lời mẫu |
|---|---|
| Tại sao không log cho `mean_order_value` — nó lệch phải mà? | Lệch chỉ 0.49 — log làm nó −1.94, tạo đuôi *thấp* (min z −6.2) và biến 5/5 khách extreme thành người mua rẻ 1 đơn. Mục tiêu là so sánh khách theo khoảng cách, không phải chuẩn hóa phân phối; Tuyên bố "lệch ⇒ log" bị spec loại bỏ. |
| Min-max có lợi gì? | Bị chặn [0,1], dễ giải thích; nhưng trọng số theo *range* nên 1 khách quyết định thang (16% cho spending; 46% cho distance). Nếu cần đầu vào bị chặn (ví dụ mạng nơ-ron), đó là lý do dùng được; ở đây mục tiêu khác. |
| **Changed:** Nếu business muốn ưu tiên chi tiêu gấp đôi? | Áp trọng số **sau** z-score (ví dụ nhân `mean_order_value` ×√2 hoặc đổi trọng số ma trận khoảng cách). Check: DIST-01 lại; z-score cho điểm xuất phát công bằng, trọng số là quyết định kinh doanh tường minh. |
| **Changed:** Nếu có 5 khách chi tiêu AUD 100k+? | z-score vẫn được nhưng SD tăng và phần đông bị nén; xem thêm robust scaling (median/IQR) hoặc winsorise *có căn cứ*, và chạy lại SCALE-03/DIST-01. Trade-off: robust giảm ảnh hưởng extreme nhưng cũng re-weight theo hình dạng. |
| **Changed:** Dùng khoảng cách Manhattan/cosine thay Euclid? | Thang vẫn quan trọng với Manhattan (cộng tuyệt đối theo thuộc tính); cosine chỉ quan tâm hướng nên cần *center* trước — z-score vẫn phù hợp. Cần chạy lại DIST-01. |
| **Changed:** Nếu phân tích held-out? | Fit μ, σ trên train customers rồi áp cho held-out — tránh leakage (spec cũng yêu cầu). |
| "Equal weighting" có hợp lý không? | Là lựa chọn khám phá mặc định; không là bằng chứng ba chiều quan trọng như nhau — ghi rõ trong notebook. |

---

## 7. Storyline nối các phần (cho tiêu chí G: coherence)

```
A1: dựng bảng đáng tin (grain, khóa, đơn vị; reconcile 0 xung đột; join audit) → EDA cho thấy trung bình/tỉ lệ
    sai khi nhầm denominator (order 80.3% vs item 44.5%; order vs customer Gini) → MLQ validation theo thời gian
   ⇣ (cùng kỷ luật, không hợp nhất số liệu — A3 spec §2)
A2 EDA: raw charge KHÔNG phân biệt được lỗi (charge ~ khoảng cách, mùa, cờ)  [EDA-1]
   → B1: mô hình hóa điều kiện: 4 OLS theo mùa, held-out R² ≈ 1, MAE = sàn cent     (thước đo "kỳ vọng")
   → B2: residual = thước đo bất thường; τ từ residual sạch; 24 đơn; plateau + total identity
   → output: outlier_clean 476 đơn + audit 24 `high`
   → B3: gộp 3 CSV đã nộp → 477 khách, 1,476 đơn; truy vết Task 1 → Task 3 (đều `high`)
   → B4: raw units ⇒ 99.9996% chi tiêu thống trị (đơn vị, không phải tầm quan trọng)
   → B5: z-score, không phi tuyến — đo bằng thay đổi láng giềng; RERUN từ đĩa 16/16
```

**Câu chuyển tiếp mẫu (EN):**
- A1 → A2: *"In A1 we learned that the denominator and the grain decide what a number means. In A2 we apply the same discipline to a different question: which delivery charges are wrong given what they should be."*
- B2 → B3: *"So far the model told us what a delivery charge should be; the next step shows how that decision flows into the customer profiles we compare."*

---

## 8. Ngân hàng "changed-condition" nhanh (cross-cutting, cho Q 20 điểm)

Mẫu trả lời 4 bước: **(1)** nói điều gì thay đổi và nó phá giả định nào → **(2)** hệ quả dự đoán → **(3)** check khả thi (cell/ID nào chạy lại) → **(4)** trade-off/uncertainty.

| Thay đổi | Giả định bị phá | Check khả thi | Trade-off |
|---|---|---|---|
| Dùng A1 catalogue price thay vì giá suy ra | Giá hiện tại ≠ giá lịch sử (spec 3.1; README nêu giá hiện tại khác A1) | Giá suy ra từ A2 tái tạo `order_price` 200/200 chưa dùng và 490/490 missing batch; muốn so với A1 thì chạy `verify_price_vector` với giá A1 (em **chưa** chạy, nên không nêu kết quả) | A1 không authoritative cho A2 |
| Train model trên tất cả 1,500 đơn | Dirty/outlier chưa sạch | Alt (d)/(e): hệ số lệch 1.30, MAE ×100 | Nhiều dữ liệu nhưng nhiễm bẩn |
| Ngưỡng τ chọn 3 thay 3.5 | Cutoff | τ = 0.0090 → cùng 24 | Không đổi nhờ plateau |
| Bỏ held-out, dùng toàn bộ 420 để fit | Đánh giá độc lập | Alt (b): hệ số lệch < 0.001 nhưng mất evidence độc lập | Spec: in-sample không phải evidence |
| Khách mới xuất hiện | z-score refit | Dùng μ, σ đóng băng của REC-01 | Phân phối có thể trôi → theo dõi |
| Batch mới có nhiễu lớn hơn | Nhiễu = làm tròn cent | Tính lại MAD; xem phân phối residual; robust regression | τ lớn hơn, độ nhạy giảm |
| (A1) Chia train/test ngẫu nhiên cho MLQ-2/5 | Quan sát độc lập; không rò thời gian | Thay bằng cohort giao hàng theo thời gian, mỗi order một partition; so MAE/PR-AUC hai cách để *đo* mức rò | Số liệu đẹp hơn nhưng lạc quan |
| (A1) Cutoff trích xuất sớm hơn 2019-02-20 | Label 30 ngày đã chín cho mọi giao hàng | Loại giao hàng chưa đủ 30 ngày hoặc dùng censoring; xem lag theo tuần giao | Mất dữ liệu cuối kỳ nhưng không gán nhãn sai |
| (A1) Nguồn XML thứ ba / định dạng ngày khác | Quy ước chuẩn hóa dùng chung | Parse với `format` tường minh; chạy lại `VAL-FLOW`, `VAL-CONFLICT-01` | Chi phí normalise thêm một nguồn |

---

## 9. Limitations chủ động nêu (mục Reflection, spec §3) — chọn 1–2 để nói

1. **Hiệu chuẩn τ & đánh giá dùng cùng 105 dòng held-out** (consistency, không độc lập) ⇒ bù bằng plateau, DELIV-07b, DELIV-08.
2. **Biên τ mỏng (1.7×)**; kết quả vững nhờ khoảng cách cực lớn giữa hai nhóm residual (×1,021).
3. **Batch guarantee là giả định**: nếu `order_total` cũng bị sửa đồng bộ, DELIV-08 mất hiệu lực.
4. **24/24 overcharge** — khả năng bắt undercharge chưa được thử bằng dữ liệu thật.
5. **Profile là mẫu A2 2019**, không phải lịch sử đầy đủ; `mean_delivery_distance` là thuộc tính vị trí; trung bình ít đơn nhiễu.
6. **Học được gì từ một check:** PROF-01f cho thấy một check *độc lập với hàm sửa* (nhất quán địa lý giữa các đơn của cùng khách) tìm ra điều mà "tuyên bố sạch" không chứng minh; cũng cho thấy giới hạn (khách 1 đơn).

---

## 10. Phụ lục — nếu "3.1, 3.2" nghĩa là spec 3.1/3.2 (giá & làm tròn)

**Spec 3.1 — current unit prices.** Mỗi đơn là một phương trình tuyến tính `Σ q_ik · p_k = order_price_i`; hệ `Q·p = y` giải bằng least squares (`np.linalg.lstsq`), parse cart bằng `json.loads` (không `eval`).
- **Chọn bằng chứng:** chỉ dùng **outlier batch** — batch duy nhất bảo đảm `order_price`/cart không bị hỏng (dirty: `order_price` có thể là trường sai; missing: 10 đơn thiếu `order_price`). **Không dùng A1 hay giá của nhóm khác.**
- **Kết quả:** giải trên 60% (300 phương trình, 12 ẩn, **rank 12**); residual bình phương ≈ **1.6e−20**; snap-distance ≈ 4.6e−12 ⇒ giá là số hai chữ số thập phân *chính xác*. 12 giá, ví dụ Vela Halo 569 = 149.09, Candle Orbit 656 = 2,262.06.
- **Kiểm tra độc lập:** tái tạo `order_price` bằng quy tắc 3.2: **200/200** phương trình *chưa dùng*, **500/500** outlier batch, **490/490** đơn của missing batch (batch độc lập, không chung đơn nào). *Bằng chứng là tái tạo bằng quy tắc công bố trên dữ liệu chưa dùng, không phải R².*

**Spec 3.2 — rounding.** `order_total = round(order_price·(1 − coupon/100) + delivery, 2)`, không làm tròn trung gian, không GST.
- **Phát hiện:** `Decimal` + `ROUND_HALF_UP` chỉ tái tạo **412/420** dòng missing batch đầy đủ (8 dòng lệch +1 cent). Ví dụ CORD000526: `5309.70×0.85 + 14.61 = 4527.855`; số float gần nhất nằm ngay dưới ⇒ `round` của Python cho 4527.85 còn Decimal cho 4527.86. Dữ liệu gốc sinh bằng float ⇒ **theo nguồn** (và tính từng dòng bằng `round` built-in, không dùng `Series.round`/`np.round`).
- **Vì sao quan trọng:** nếu chọn Decimal, chính check của ta sẽ gắn cờ 8 dòng hợp lệ và 1.1 sẽ "đuổi" lỗi không tồn tại.

---

## 11. Slide-anchor map (điền số slide còn thiếu)

| Khái niệm | Slide trích trong notebook | Cần điền |
|---|---|---|
| Missing data & field-appropriate treatment | ✔ Week 7 *Data Cleansing*, slides 27–30, 38–45 | — |
| Data validation: structural / content / logical | ✔ Week 11 *Data Validation*, slides 4, 22, 27 | — |
| Purpose-specific transformation; log scaling | ✔ Week 8 *Data Transformation (I)*, slides 3, 17 | — |
| OLS / multiple linear regression, hệ số, R² | ⚠ | Week ? slide ? |
| Train–held-out split, đánh giá model | ⚠ | Week ? slide ? |
| Outlier detection (residual-based, modified z / robust stats) | ⚠ *(ngoài slide: Hampel 1974, Iglewicz & Hoaglin 1993 ✔ trong notebook)* | Week ? slide ? |
| EDA: skewness, kurtosis, IQR fence, correlation | ⚠ | Week ? slide ? |
| z-score vs min-max normalisation | ⚠ *(ngoài slide: Han, Kamber & Pei 2011 §3.5.2 ✔)* | Week ? slide ? |
| Feature redundancy / correlation analysis | ⚠ *(Han, Kamber & Pei ✔)* | Week ? slide ? |
| A1 — đọc JSON / XML, làm phẳng | ✔ Week 3 / Week 2 *applied sessions* (notebook A1 dẫn) | slide # nếu có |
| A1 — regex verbose, bounded patterns | ✔ Week 4 *applied session* (notebook A1 dẫn) | slide # nếu có |
| A1 — khoảng tin cậy Wilson / Newcombe / bootstrap, Cliff's δ | ⚠ *(ngoài slide: Wilson 1927; Newcombe 1998; Dunn 1961; Efron & Tibshirani 1993; Cliff 1993 ✔ trong notebook A1)* | Week ? slide ? |
| A1 — thiết kế ML question (target, leakage, validation theo thời gian, baseline, PR-AUC) | ⚠ | Week ? slide ? |

Khi có số slide, thêm vào cột "① Anchor" của từng mục. **Quy tắc:** nói "slide X" chỉ khi bạn đã mở slide đó và xác nhận nội dung.

---

## 12. Pre-flight checklist (spec §6, §8, §9, rubric §4)

- [ ] Mở sẵn **A2**: `Group005_solution_A3_revised.ipynb` (đã Run All, output hiển thị), `Group005_*_clean.csv`, `audit_log.csv`; **bản local + backup** (file không trình chiếu được = không được tính).
- [ ] Mở sẵn **A1**: `Group005_EDA.ipynb` (output hiển thị), `Group005_EDA.pdf` (trang 3–12 là phần chấm), `Group005_solution.ipynb` (ô `T1-P*`, `T2-R1`, `T3-TEXT-*`, `VAL-*`), `Group005_source_to_target_mapping.csv` (lọc `MAP-product_reviews-*`), 6 CSV `outputs/`. Chuẩn bị sẵn *vị trí cuộn* tới `T2-R1`, `T3-TEXT-01/02/04/05`, Figure 4/5/7 để không phải tìm.
- [ ] A1: quyết định *trước* sẽ nói gì về "rerun" (xem cảnh báo đầu §5). Chỉ nói "saved PASS results" trừ khi bạn vừa Restart & Run All và thấy 145/145.
- [ ] Màn hình demo thấy được với assessor; tắt AI, messaging, thiết bị khác (cấm *live AI* trong presentation/Q&A).
- [ ] Mỗi người: có cue card ≤ 5 ý; biết cell nào cần mở (Ctrl-F check ID); nói con số *đang hiển thị*.
- [ ] Mỗi người trả lời câu hỏi được chỉ định; đồng đội chỉ trả lời khi được mời. Nếu im lặng 1 phút, assessor sẽ chuyển câu.
- [ ] Có mặt đúng slot (Thứ Hai 2 / Thứ Ba 3/11/2026, giờ Melbourne); vắng không phép = **0/40**.
- [ ] **Moodle trước 23:55 AEDT thứ Tư 4/11/2026:** nếu dùng thêm slide/notebook sửa đổi/file demo ngoài A1/A2 đã nộp ⇒ nộp *đúng phiên bản đã dùng khi trình bày* (một zip `Group005_A3_submission.zip`). Không nộp lại A1/A2 không đổi.
- [ ] **AI record (spec §8):** nếu dùng AI (kể cả file notes này) để tạo/sửa tài liệu trình bày thì cần lịch sử/khai báo AI bằng tiếng Anh theo cách A1/A2. Nếu chỉ dùng notebook A2 đã nộp và không tạo tài liệu mới, không cần.


---

## 13. Hai flow đề xuất để chia phần thuyết trình (5 người, giảm phân mảnh)

*Cập nhật theo phân công mới: **Minh** Block 1 + 1.1 + 2.1 · **Tim & Tiansheng** cùng 3.2–3.4 · **Sally** Block 4 (+ 1.3) + 3.1 + 3.5 · **Riley** Block 5 + 1.4 + 2.2 (+ A1 EDA/ML).*

### 13.0 Ràng buộc từ marking criteria

| Ràng buộc | Nguồn | Hệ quả thiết kế |
|---|---|---|
| Mở đầu bằng **tóm tắt đóng góp, vai trò, task từng thành viên** | A3 spec §4 | Slide roster 30–40 s ở lượt đầu (§13.5) |
| Mọi thành viên phải **giải thích một decision / result / supporting check** (không chỉ giới thiệu hay đổi slide); ai cũng hiểu workflow chung | A3 spec §3 | Mỗi người có ≥ 1 lượt "substantive" mang quyết định của chính mình |
| 5 phần: Executive summary · A1 · A2-data cleansing · A2-Transformation · Reflection; **thứ tự được phép đổi** | A3 spec §3 | Đủ 5 phần, thứ tự điều chỉnh theo logic |
| **15–20 phút** trình bày + demo, có timer | A3 spec §6 | Thiết kế ≈ 18 phút, đệm ≥ 1.5 phút |
| P: chuyển giao mượt, tìm evidence không bị mất chỗ; **không cần chia đều giây** | Rubric P | Lượt dài/ngắn khác nhau được; chốt tab trước |
| G: câu chuyện A1/A2 mạch lạc; evidence dễ tìm; chuyển tiếp trong thời gian | Rubric G | Hand-over bằng *một câu hỏi* |
| Q: câu hỏi riêng cho từng người; đồng đội chỉ trả lời khi được mời | A3 spec §6, Rubric Q | Người không nói A1 vẫn cần "A1 one-pager" (§13.6) |

**Phụ thuộc kỹ thuật của A2 (quyết định thứ tự):**

```
Block 1 (rules: cart→giá, haversine, season, VADER)  [Minh]
      │  cung cấp predictor distance & happy cho model, và là "diagnostic matrix" của dirty
      ▼
Block 4 (model theo mùa, train chỉ trên 420 dòng missing đầy đủ)  [Sally]
      ▼  dùng bởi
1.1 dirty [Minh]   1.2 missing [Tiansheng]   1.3 outlier [Sally]
      ▼  ghi lại bởi
Block 5 (recorder 9 cột, confidence)  [Riley]  +  2.1 nội dung log [Minh]
      ▼  xuất & kiểm
1.4 export · 2.2 read-back  [Riley]   →   Task 3 đọc đúng 3 CSV đã nộp  [Sally 3.1 → Tim/Tiansheng 3.2–3.4 → Sally 3.5]
```

**Điểm dễ gây phân mảnh:**
1. **Tim** (1.0 ở đầu, 3.2–3.3 ở cuối) và **Tiansheng** (1.2 giữa, 3.4 cuối) mỗi người có hai chương xa nhau.
2. **Tim & Tiansheng** nay cùng sở hữu 3 mục Task 3 ⇒ không còn là "cameo 45 s": cần một **panel hai người** có khuôn cố định.
3. **Sally** có Block 4/1.3 (cleansing) và 3.1/3.5 (transformation) — 3.1 và 3.5 *bọc quanh* panel của Tim/Tiansheng.
4. **Minh (2.1) và Riley (Block 5) chồng nhau** ở "confidence level definitions" và "audit_log export" ⇒ cần chia rõ (§13.4).

**Giả định (đổi được, xin xác nhận):**
- **Sally** giữ Block 4 **và 1.3** (1.3 chưa được nêu trong phân công mới).
- **"Block 1a"** của Minh = toàn bộ Block 1 (cart parse, price vector, rounding/total, haversine, date/season, VADER, validation trên outlier batch). Nếu "1a" chỉ là nửa đầu thì nửa còn lại chưa có chủ.
- **Tim = 3.2 + 3.3** (baseline đơn vị → hai scaler), **Tiansheng = 3.4** (nonlinear). Nếu hai bạn chia khác, đổi dòng tương ứng.
- Người nói **A1 provenance** (parse → reconcile → text → check) là **Tim** (liền mạch với 1.0). Đổi theo §13.4 nếu khác.
- **Riley** nói A1 EDA/ML (Sally đã nặng A2).
- Tổng ≈ 18 phút nói.

### 13.1 Nguyên tắc chung

1. Mỗi lượt = một chương trả lời *một câu hỏi*; hand-over bằng câu hỏi, không bằng tên mục.
2. **Panel 3.2–3.4**: Tim (3.2 → 3.3) rồi Tiansheng (3.4), cùng khuôn *Question → Decision → Evidence on screen → "so what"*; Sally mở bằng 3.1 và đóng bằng 3.5 nên khán giả thấy một chương, không phải ba.
3. **Thread ribbon** lặp ở đầu mọi màn hình: *Grain → Expectation → Scale → Proof*.
4. ≤ 3–4 lần chuyển ngữ cảnh (A1 EDA PDF/NB → A1 solution NB → A2 NB); mở sẵn tab theo thứ tự nói.
5. Con số nói ra phải đang hiển thị; cue card ≤ 5 ý mỗi người.

---

### 13.2 FLOW A — "Engine-first, thang mơ hồ" (A1 nói trước; mô hình giải thích trước các xử lý)

**Luận điểm:** *"Biết một charge đáng là bao nhiêu thì mới biết xử lý dòng sai thế nào."* Cleansing đi từ **biết trường sai → không biết trường sai**: outlier (biết `delivery_charges` sai) → missing (biết ô trống) → dirty (phải chẩn đoán trường gốc). **Block 1 được nói *đúng lúc dùng***, như "diagnostic matrix" của dirty; Sally chỉ nhắc một câu khi giới thiệu predictor của mô hình.

| # | Giờ | Người nói | Nội dung (task) | Câu hỏi hand-over | Evidence mở sẵn |
|---|---|---|---|---|---|
| 1 | 0:00–2:15 | **Riley** | Roster (30 s) · Exec summary (45 s) · **A1 claim** (60 s): review chọn lọc theo giá, 44.5% item vs 80.3% order, 27.0% → 63.6% | *"Số này chỉ đúng nếu bảng đúng — một review JSON/XML thành một dòng ra sao?"* | A1 EDA PDF tr. 5, 8; `Group005_EDA.ipynb` Fig 4 |
| 2 | 2:15–5:00 | **Tim** | **A1 provenance** (1:30): parse, normalise (day-first = 31), reconcile 3,850+3,850−700 = 7,000, text (marker list, near-match), check 7,892/7,892 · **1.0** (1:15): 80 ô trống, 8 warehouse sai, 8 vĩ độ dương, 8 ngày lạ, "charge thô ≠ outlier" | *"Một charge đáng là bao nhiêu? — Sally."* | A1 `T2-R1`, `T3-TEXT-05`; A2 `EDA-02/03`, Fig EDA-1 |
| 3 | 5:00–8:00 | **Sally** | **Block 4 / spec 3.5** (1:30: DELIV-01…05, 10; một câu về predictor từ Block 1) · **1.3 outlier** (1:15: DELIV-07, plateau, 24 đơn; DELIV-08) | *"Outlier dễ vì ta biết trường sai. Khi ô **trống** thì sao? — Tiansheng."* | `DELIV-05`, `DELIV-07` + Fig 3, `DELIV-08` |
| 4 | 8:00–9:30 | **Tiansheng** | **1.2 missing**: deterministic > algebraic > model; 10 charge khôi phục *đại số* (`high`), 10 cờ expedited chọn bằng model (`medium`); MISS-05 | *"Khó nhất là khi ta **không biết** trường nào sai — Minh."* | `MISS-02…06` |
| 5 | 9:30–12:30 | **Minh** | **Block 1** như diagnostic matrix (1:00: ngày↔season, haversine, VADER, số học) · **1.1 dirty** (1:15: một trường gốc, sửa đúng một ô) · **2.1** (0:45: một quyết định = một dòng; 184 = 80 + 80 + 24; 166 `high`/18 `medium`; định nghĩa high/medium/low) | *"184 quyết định đó dẫn tới khách hàng nào? — Sally."* | `DIRTY-01…03`, `AUDIT_CONFIDENCE`, bảng lineage `PROF-02` |
| 6 | 12:30–13:15 | **Sally** | **3.1**: 1,476 đơn → 477 khách; chọn 3 thuộc tính, bỏ `total_paid` | *"Với dữ liệu thô, thuộc tính nào chi phối khoảng cách? — Tim."* | `PROF-02/03` |
| 7 | 13:15–14:20 | **Tim** | **3.2 + 3.3**: raw units, chi tiêu chiếm 99.9996% (`BASE-03`); z-score chia đều 1/3, min-max 38/16/46% (`SCALE-02`) | *"Biến đổi phi tuyến có giúp không? — Tiansheng."* | `BASE-01/03`, `SCALE-02/03` |
| 8 | 14:20–15:05 | **Tiansheng** | **3.4**: log làm skew 0.49 → −1.94, min z −6.2; sqrt/log1p lệch distance (`NONLIN-01`) | *"Vậy ta khuyến nghị gì? — Sally."* | `NONLIN-01` |
| 9 | 15:05–15:55 | **Sally** | **3.5**: none + z-score cả 3; DIST-01: raw giữ 7% láng giềng; limitation | *"Và tất cả khớp với file trên đĩa? — Riley."* | `REC-01`, `DIST-01` |
| 10 | 15:55–17:55 | **Riley** | **Block 5** (0:40: recorder 9 cột, quy ước giá trị, sửa rule `medium`, smoke test) · **1.4 + 2.2** (0:50: 16 cột, 500/500/476, changed cells = logged cells) · **Reflection** (0:30) | — | `READBACK_*`, `AUDIT_EXPORT`, `RERUN-01` |

**Tải:** Riley 4:15 · Sally 4:35 · Tim 3:50 · Minh 3:00 · Tiansheng 2:15 (tổng 17:55).
**Ưu điểm:** đúng thứ tự phụ thuộc kỹ thuật (model trước các xử lý); A1 nói sớm nên không bị timer cắt; Block 1 xuất hiện lúc nó thực sự là công cụ (dirty).
**Rủi ro & cách giảm:** 10 lượt (nhiều nhất) và Sally 3 lần xuất hiện → ribbon + hand-over bằng câu hỏi, chuẩn bị tab; cleansing khác thứ tự spec → nói câu *"we order the treatments by how much we know about the wrong field"* ở đầu chương; Task 3 có 4 giọng → khuôn panel cố định, nếu quá giờ giảm 3.2–3.4 xuống 1 câu/mục.

---

### 13.3 FLOW B — "Rules-first, thang bằng chứng" (đúng thứ tự spec/notebook; A1 xen vào A2)

**Luận điểm:** *"Ta chỉ dựa vào mô hình khi quy tắc không còn đủ — và confidence phản ánh điều đó."* Mức phụ thuộc mô hình tăng dần: dirty (quy tắc) → missing (quy tắc → đại số → mô hình) → outlier (mô hình là detector). Mỗi người sở hữu **một chương liền**: Minh (Block 1 → 1.1 → 2.1), Sally (Block 4 → 1.3 → 3.1).

| # | Giờ | Người nói | Nội dung (task) | Câu hỏi hand-over | Evidence mở sẵn |
|---|---|---|---|---|---|
| 1 | 0:00–1:30 | **Riley** | Roster · Exec summary (biểu giá tuyến tính theo mùa; 24 đơn bị loại; z-score; limitation) | *"Trước khi sửa gì: dữ liệu A2 sai ở đâu, và A1 đã dạy ta kiểm tra thế nào?"* | slide roster |
| 2 | 1:30–5:00 | **Tim** | **1.0** (1:30) → **A1 provenance** (2:00) kết bằng *finding* của đường đi (44.5% → 63.6%) | *"Bắt đầu bằng quy tắc cho một đáp án duy nhất — Minh."* | A2 `EDA-02/03`; A1 `T2-R1`, `T3-TEXT-05`, Fig 4 |
| 3 | 5:00–8:15 | **Minh** | **Block 1** (1:15) → **1.1 dirty** (1:15) → **2.1** (0:45; 184 = 80 + 80 + 24; high/medium/low) | *"Quy tắc không giúp khi ô trống — Tiansheng."* | `DIRTY-01…03`, `AUDIT_CONFIDENCE` |
| 4 | 8:15–9:45 | **Tiansheng** | **1.2 missing** + bậc thang: đại số (10 charge, `high`) → model (10 cờ expedited, `medium`); báo trước "mô hình giải thích ngay sau đây" | *"Bậc cao nhất là phán đoán bằng mô hình — Sally."* | `MISS-02…06` |
| 5 | 9:45–13:15 | **Sally** | **Block 4 / 3.5** (1:30) → **1.3 outlier** (1:15) → **3.1** (0:45: Task 3 đọc outlier_clean 476 + hai CSV kia) | *"Với 477 khách, đơn vị có chi phối không? — Tim."* | `DELIV-05/07/08`, `PROF-02/03` |
| 6 | 13:15–14:20 | **Tim** | **3.2 + 3.3** | *"Phi tuyến thì sao? — Tiansheng."* | `BASE-03`, `SCALE-02` |
| 7 | 14:20–15:05 | **Tiansheng** | **3.4** | *"Khuyến nghị? — Sally."* | `NONLIN-01` |
| 8 | 15:05–15:55 | **Sally** | **3.5** | *"Khớp file trên đĩa? — Riley."* | `REC-01`, `DIST-01` |
| 9 | 15:55–18:25 | **Riley** | **Block 5 + 1.4 + 2.2** (1:30) · **A1 MLQ-2 làm bước tiếp** (0:40) · **Reflection** (0:20) | — | `READBACK_*`, `RERUN-01`; A1 EDA PDF tr. 10 |

**Tải:** Riley 4:00 · Tim 4:35 · Sally 4:20 · Minh 3:15 · Tiansheng 2:15 (tổng 18:25).
**Ưu điểm:** 9 lượt; Minh và Sally mỗi người một chương liền; giải thích rõ nhất "vì sao ba xử lý khác nhau"; MLQ làm next step tự nhiên.
**Rủi ro & cách giảm:** mô hình được giải thích *sau* khi dirty/missing đã nhắc → forward-reference một câu ("expected charge — explained next"); A1 tách đôi (path ở lượt 2, MLQ ở lượt 9) → lượt 2 phải kết bằng finding, MLQ ở cuối là phần **cắt được**; chuyển ngữ cảnh 4 lần (A2 → A1 solution → A2 → EDA PDF).

---

### 13.4 So sánh, khuyến nghị và việc chia Minh ↔ Riley

| Tiêu chí | Flow A (engine-first) | Flow B (rules-first) |
|---|---|---|
| Thứ tự phụ thuộc kỹ thuật | **Đúng** (model trước xử lý) | Cần forward-reference |
| Thứ tự spec/notebook (dirty → missing → outlier) | Khác | **Đúng** |
| Số lượt nói | 10 (Sally 3 lần) | **9** (Minh, Sally mỗi người một chương liền) |
| A1 bị rủi ro timer cắt | **Thấp** | Trung bình (MLQ cuối, cắt được) |
| Mạch kể "vì sao ba xử lý khác nhau" | Tốt (thang mơ hồ) | **Rất tốt** (thang phụ thuộc mô hình) |
| Chuyển ngữ cảnh | 3 | 4 |
| Cần luyện tập | Cao (nhiều hand-over) | Vừa–cao |

**Khuyến nghị:** với phân công mới, **Flow B là mặc định hợp lý hơn** vì Block 1 → 1.1 → 2.1 (Minh) và Block 4 → 1.3 → 3.1 (Sally) mỗi cái là một chương liền, ít phân mảnh nhất. Dùng **Flow A** nếu nhóm coi trọng việc mô hình phải được giải thích trước và A1 nói sớm, chấp nhận 10 lượt.

**Chia Minh (2.1) ↔ Riley (Block 5):** *Minh = nội dung & ý nghĩa của log* (một quyết định = một dòng; định nghĩa high/medium/low bằng một câu; thống kê 184 dòng). *Riley = máy ghi & toàn vẹn* (recorder 9 cột, quy ước giá trị, sửa rule `medium`, smoke test, export, read-back khớp "changed cells = logged cells"). Minh nói trước nên đưa định nghĩa; Riley nhắc lại *không định nghĩa lại*.

**Nếu người sở hữu A1 reconcile/text khác giả định:** đổi vai provenance sang người đó, nhưng giữ **provenance và 1.0 liền nhau trong một lượt** để A1 → A2 không bị ngắt; nếu là Minh hoặc Tiansheng thì chuyển 1.0 (hoặc cắt 1.0 xuống 45 s) cho Tim làm mở đầu chương Task 3.

### 13.5 Slide roster (30–40 s, bắt buộc theo spec §4)

| Thành viên | Vai trò | A1 | A2 | Nói ở | Sẵn sàng trả lời |
|---|---|---|---|---|---|
| Riley | Verifier & integrator | EDA + ML questions | Block 5 · 1.4 export · 2.2 read-back | Mở/đóng | Fig 1–8, 10 findings, MLQ; recorder, `medium` rule, read-back |
| Tim | Data investigator | `[phần A1 của Tim]` | 1.0 EDA · 3.2–3.3 | Provenance + 1.0; panel Task 3 | JSON/XML → bảng; EDA; baseline đơn vị, z-score vs min-max |
| Sally | Modeller & analyst | EDA (đồng sở hữu) | Block 4 · 1.3 · 3.1 · 3.5 | Engine/outlier + 3.1; 3.5 | model, τ, outlier; customer copy, recommendation |
| Minh | Rules, cleaner & auditor | `[phần A1 của Minh]` | Block 1 · 1.1 · 2.1 | Rules + dirty + audit | root-field diagnosis, confidence |
| Tiansheng | Recoverer | `[phần A1 của Tiansheng]` | 1.2 missing · 3.4 | Missing; panel 3.4 | hierarchy, imputation; log/sqrt |

*(Điền cột A1 của Minh/Tim/Tiansheng theo thực tế; tôi không có phân công A1 của họ.)*

### 13.6 Q&A readiness

**A1 one-pager (ai cũng nhớ):** 5,000 orders / 15,739 item lines / 7,000 reviews / 500 customers · reconcile 3,850 + 3,850 − 700 = 7,000, **0 xung đột** · day-first vì ngày XML tới **31** · review phủ **80.3%** order nhưng **44.5%** item, **27.0% → 63.6%** theo giá · Nickolson OTIF **92.2%** vs 88.8% (+3.44 pp) · SKU trích từ text khớp **7,892/7,892** · MLQ-2: label ≤ 30 ngày, cohort theo thời gian, loại thuộc tính từ review · limitation: cutoff trích xuất chưa xác minh.

**Cross-cover:** mỗi người đọc phần *Grain – Units – Limits* của hai chương liền kề trong flow đã chọn.

**Người trả lời chính:** A1 path/reconcile/text → Tim (hoặc người đã chọn) · A1 EDA/MLQ → Riley, Sally · Block 1 & dirty & log content → Minh · missing → Tiansheng · Block 4 & outlier & customer copy & recommendation → Sally · 3.2–3.4 → Tim, Tiansheng · recorder, export, read-back → Riley.

### 13.7 Việc cần xác nhận
1. **"Block 1a"** nghĩa là toàn bộ Block 1 hay một phần? (phần còn lại ai giữ?)
2. **1.3 outlier** thuộc Sally (giả định)?
3. Cách chia **3.2–3.4** giữa Tim và Tiansheng (giả định: Tim 3.2 + 3.3, Tiansheng 3.4).
4. Phần A1 thực tế của Minh, Tim, Tiansheng → chọn người nói provenance.
5. Chọn **Flow A hay B**; ai mở/đóng (đề xuất Riley cả hai đầu).

---

*Ghi chú nguồn số liệu: các số trong B1–B5 được trích từ output đã lưu của `Group005_solution_A3_revised.ipynb` (DELIV-01…11, PROF-01…03, BASE-01…03, SCALE-01…03, NONLIN-01, EVID-01, DIST-01, REC-01, RERUN-01); các số trong Phần A từ `Group005_EDA.ipynb`/`Group005_EDA.pdf`/`Group005_solution.ipynb` (T1-P*, T2-R1, T3-TEXT-*, VAL-*, Fig 1–8, MLQ-1…5). Những số đánh dấu 🔁 do tôi tự tính lại độc lập (NumPy/pandas) từ CSV; chúng không thay thế evidence trong notebook. Các phép "derived" (ví dụ ≈29% item line được review ≤30 ngày) là suy luận của tôi từ số 🔁, không có trong notebook A1.*
