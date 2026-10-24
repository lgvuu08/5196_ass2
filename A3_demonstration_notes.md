# FIT5196 A3 — Demonstration Notes (Group005)

**Phạm vi:** (A) EDA & ML question của A1 · (B) A2: Seasonal delivery charge **spec 3.5**, **section 1.3**, **3.1, 3.2, 3.5**.
**Nguồn bằng chứng:** `Group005_solution_A3_revised.ipynb` (mọi con số bên dưới lấy từ output đã lưu trong notebook, trừ khi ghi "tự tính lại"), `ass2_spec.md` / A2 spec PDF, A3 specification + rubric.

---

## 0. Đọc trước: giả định và những gì CHƯA grounded

| # | Vấn đề | Cách tôi xử lý | Việc bạn cần làm |
|---|---|---|---|
| 1 | **A1 không có trong repo** (không notebook, không output A1). | Phần A chỉ là **khung (scaffold)** bám đúng yêu cầu A3 cho A1; không bịa finding/số liệu. A2 spec PDF (Section 4, cuối Task 3) nhắc "ten-findings / five-ML-questions" nên tôi suy ra A1 có 10 EDA findings + 5 ML questions. | Gửi A1 notebook/output → tôi điền Phần A với cùng cấu trúc như Phần B. |
| 2 | **Slide của unit không có trong repo.** Notebook chỉ trích 3 nhóm slide cụ thể. | Chỉ dùng slide số mà notebook đã trích (đánh dấu ✔). Chỗ khác ghi **⚠ slide # cần điền**, kèm tên khái niệm/phương pháp để bạn tra nhanh. Không tự bịa số slide. | Điền số slide ở mục 11 (≈10 phút). |
| 3 | "3.1, 3.2, 3.5" mà bạn ghi có thể là **Task 3** (3.1 customer copy, 3.2 original scales, 3.5 recommendation) hoặc **spec 3.1/3.2** (giá & làm tròn). | Chính = Task 3 (cùng danh sách với "spec 3.5, section 1.3"). **§10 (Phụ lục)** phủ spec 3.1/3.2 phòng trường hợp bạn muốn. | Cho tôi biết nếu cần mở rộng. |
| 4 | Số cell dùng 0-based (chỉ số trong file `.ipynb`). Jupyter không hiển thị chỉ số này. | **Check ID là locator chính** (Ctrl-F `DELIV-07`); cell idx là phụ. | — |

**Số tôi tự tính lại độc lập** (từ CSV gốc, không dùng code notebook) được đánh dấu 🔁. Chúng khớp notebook: 80 ô blank (10 × 8 trường), 8 tên warehouse sai, 8 vĩ độ dương, 8 định dạng ngày lạ, hệ số 4 mô hình mùa trên 420 dòng.

---

## 1. Rubric crosswalk — "HD" cần gì và notes này đáp ứng ở đâu

| Tiêu chí | HD cần (rubric §2) | Notes đáp ứng bằng | Mục |
|---|---|---|---|
| **G** (nhóm, 10đ) | Câu chuyện A1/A2 mạch lạc; exec summary có finding + recommendation + limitation; evidence **dễ tìm, nhãn chính xác**; chuyển tiếp trong thời gian | Exec-summary seed; "storyline" nối B1→B5; bảng evidence locator; core-vs-reserve để không vượt giờ | §2, §7 |
| **P** (cá nhân, 10đ) | Giải thích rõ, nhịp tốt, dùng notes/evidence **có chủ đích**, đóng góp substantive, bàn giao mượt | Mỗi phần có "kịch bản nói" (ý chính, không đọc nguyên văn), thứ tự mở evidence, câu signpost | §3, từng mục B |
| **Q** (cá nhân, 20đ) | Tự giải thích **how & why**, diễn giải evidence đúng **grain–units–limits**; biện minh một **independent check** và kết quả của nó; **thích ứng changed condition**, đề xuất check khả thi, nêu trade-off/uncertainty | Mỗi phần có hộp *Grain–Units–Limits*, *Independent check: establishes / does NOT establish*, và **Q&A drills gồm changed-condition** | từng mục B, §8 |
| Spec §4 (demonstration) | (1) input/source record + quyết định xử lý; (2) output/finding/so sánh; (3) cách ra kết quả + ý nghĩa giá trị; (4) supporting check làm được/không làm được gì. "Chỉ nói file tồn tại ≠ demonstration" | Mỗi phần có **Demo script 4 bước** đúng 4 gạch đầu dòng này | từng mục B |
| Spec §2 | Nếu cải tiến cho A3: nêu thay đổi vật chất, lý do, check đã làm; thừa nhận vấn đề chưa giải quyết | **A3 revision disclosure** + danh sách limitation chủ động nêu | §4, §9 |

---

## 2. Khung thời gian & phân vai (điều chỉnh theo kế hoạch nhóm)

Cả nhóm có **15–20 phút** trình bày + demo, assessor dùng timer (spec §6). Ngân sách đề xuất cho các phần của bạn (≈ 12–13 phút nếu một người làm hết; chia cho nhiều người thì chia theo hàng):

| Phần | Core (nói) | Reserve (chỉ mở khi bị hỏi) |
|---|---|---|
| B1 Spec 3.5 model | 3 phút | alternatives (d)(e), DELIV-10, complementary coding, pooled-model check 🔁 |
| B2 Section 1.3 outlier | 3.5 phút | DELIV-07b, per-season τ, CLAIMS-13, AUDIT_CONFIDENCE |
| B3 Task 3.1 customer copy | 2 phút | PROF-01f chi tiết, lineage 184 decisions |
| B4 Task 3.2 original scales | 2 phút | BASE-02 extremes, pair-by-pair identity |
| B5 Task 3.5 recommendation | 3 phút | DIST-01 đầy đủ, total_paid supplementary |
| A (A1 EDA & ML) | 3 phút | (điền sau) |

> **Nguyên tắc P:** mỗi phần ≤ 5 ý chính trên một "cue card"; mọi con số nói ra phải là con số **đang hiển thị trên màn hình**. Đọc nguyên văn bị coi là bằng chứng yếu (rubric "Notes and explanation").
>
> **Spec §4:** demo **bắt đầu bằng tóm tắt đóng góp/vai trò/task từng thành viên**. Điền: `[Tên] — [vai trò] — [task]` ×N trước khi vào nội dung.

**Exec-summary seed** (spec §3 yêu cầu ≥1 finding về data/results, 1 finding về cleaning/validation/transformation, 1 recommendation, 1 limitation):

- *Finding (results):* Delivery charge là **biểu giá tuyến tính theo mùa**: held-out R² ≥ 0.9999996 và MAE 0.0022–0.0025 AUD ≈ sàn làm tròn cent (0.0025). → "Charge lớn" ≠ bất thường; "residual lớn" mới là bất thường.
- *Finding (validation/transformation):* 24/500 đơn outlier bị loại bằng residual rule; cả 24 đều **mâu thuẫn với chính `order_total` của chúng** bằng đúng 4 mức phụ phí (6.25/9.50/14.75/22.00). Quy tắc thô (Tukey) xóa nhầm 13 đơn hợp lệ và bỏ sót 9.
- *Recommendation:* Với customer profiling: **không** biến đổi phi tuyến, **z-score** cả 3 thuộc tính (`order_count`, `mean_order_value`, `mean_delivery_distance`).
- *Limitation:* Quyết định loại outlier dựa trên batch guarantee "chỉ `delivery_charges` bị hỏng"; τ chỉ gấp 1.7× residual hợp lệ lớn nhất nên độ vững đến từ *plateau*, không từ biên của τ.

---

## 3. Mẫu "một phần = một vòng lập luận" (dùng cho mọi mục B)

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

## 5. PHẦN A — EDA & ML question của A1 (SCAFFOLD — chờ A1 notebook)

> ⚠ **Tôi không có dữ liệu A1.** Phần này chỉ cố định *cấu trúc trình bày* và *câu hỏi cần trả lời được*. Điền vào chỗ `[...]` từ A1 notebook của bạn; đừng nói bất cứ điều gì chưa được notebook chứng minh.

**Yêu cầu A3 cho A1 (spec §3):** *"Explain a representative path from JSON/XML to a standardised table and a finding. Include a parsing/reconciliation decision, a text-processing decision and how you checked the result."* Đây là điều assessor sẽ đối chiếu.

| Lớp | Cần có | Điền từ A1 |
|---|---|---|
| ① Anchor | Phương pháp EDA/ML từ slide (⚠ slide #) → code section tương ứng | `[EDA step: ...]` `[ML method: ...]` |
| ② Decisions | Với mỗi quyết định: *what / why (theo đặc điểm dữ liệu A1) / how (cell, check) / alternative bị loại + evidence* | parsing JSON/XML: `[...]` · reconciliation: `[...]` · text-processing: `[...]` |
| ③ Demo 4 bước | 1 record nguồn (JSON/XML) → bảng chuẩn hóa → 1 finding → 1 check | `[record id]` `[finding]` `[check]` |
| ④ Boundary | Grain của bảng; đơn vị; limit; **A1 prices không authoritative cho A2** (spec §2) | `[...]` |

**Câu hỏi ML/EDA "chung" assessor có thể hỏi (chuẩn bị câu trả lời từ A1 của bạn):**
1. Metric nào, baseline nào, vì sao? Held-out hay cross-validation, split có seed/stratify không?
2. Có leakage không (feature suy ra từ target; fit scaler/vectorizer trước khi split)?
3. Finding nào của EDA đã *thay đổi* một quyết định (làm sạch / chọn feature / chọn model)?
4. Check độc lập nào xác nhận kết quả, và nó **không** xác nhận điều gì?
5. *Changed condition:* nếu dữ liệu có thêm 20% bản ghi lỗi / một lớp hiếm hơn / feature mới, bạn đổi gì và kiểm tra thế nào?

→ Khi gửi A1 notebook, tôi sẽ viết Phần A với đúng định dạng của Phần B (≈ cùng độ sâu).

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
| **Modified z-score / Hampel identifier** (Iglewicz & Hoaglin 1993; Hampel 1974 ✔ notebook references): `|e − median| / (1.4826·MAD) > 3.5` | `residual_threshold` → τ = 3.5 × 1.4826 × MAD |
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
EDA: raw charge KHÔNG phân biệt được lỗi (charge ~ khoảng cách, mùa, cờ)  [EDA-1]
   → B1: mô hình hóa điều kiện: 4 OLS theo mùa, held-out R² ≈ 1, MAE = sàn cent     (thước đo "kỳ vọng")
   → B2: residual = thước đo bất thường; τ từ residual sạch; 24 đơn; plateau + total identity
   → output: outlier_clean 476 đơn + audit 24 `high`
   → B3: gộp 3 CSV đã nộp → 477 khách, 1,476 đơn; truy vết Task 1 → Task 3 (đều `high`)
   → B4: raw units ⇒ 99.9996% chi tiêu thống trị (đơn vị, không phải tầm quan trọng)
   → B5: z-score, không phi tuyến — đo bằng thay đổi láng giềng; RERUN từ đĩa 16/16
```

**Câu chuyển tiếp mẫu (EN):** *"So far the model told us what a delivery charge should be; the next step shows how that decision flows into the customer profiles we compare."*

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

Khi có số slide, thêm vào cột "① Anchor" của từng mục. **Quy tắc:** nói "slide X" chỉ khi bạn đã mở slide đó và xác nhận nội dung.

---

## 12. Pre-flight checklist (spec §6, §8, §9, rubric §4)

- [ ] Mở sẵn: notebook (đã Run All, output hiển thị), `Group005_*_clean.csv`, `audit_log.csv`; **bản local + backup** (file không trình chiếu được = không được tính).
- [ ] Màn hình demo thấy được với assessor; tắt AI, messaging, thiết bị khác (cấm *live AI* trong presentation/Q&A).
- [ ] Mỗi người: có cue card ≤ 5 ý; biết cell nào cần mở (Ctrl-F check ID); nói con số *đang hiển thị*.
- [ ] Mỗi người trả lời câu hỏi được chỉ định; đồng đội chỉ trả lời khi được mời. Nếu im lặng 1 phút, assessor sẽ chuyển câu.
- [ ] Có mặt đúng slot (Thứ Hai 2 / Thứ Ba 3/11/2026, giờ Melbourne); vắng không phép = **0/40**.
- [ ] **Moodle trước 23:55 AEDT thứ Tư 4/11/2026:** nếu dùng thêm slide/notebook sửa đổi/file demo ngoài A1/A2 đã nộp ⇒ nộp *đúng phiên bản đã dùng khi trình bày* (một zip `Group005_A3_submission.zip`). Không nộp lại A1/A2 không đổi.
- [ ] **AI record (spec §8):** nếu dùng AI (kể cả file notes này) để tạo/sửa tài liệu trình bày thì cần lịch sử/khai báo AI bằng tiếng Anh theo cách A1/A2. Nếu chỉ dùng notebook A2 đã nộp và không tạo tài liệu mới, không cần.

---

*Ghi chú nguồn số liệu: các số trong B1–B5 được trích từ output đã lưu của `Group005_solution_A3_revised.ipynb` (DELIV-01…11, PROF-01…03, BASE-01…03, SCALE-01…03, NONLIN-01, EVID-01, DIST-01, REC-01, RERUN-01). Những số đánh dấu 🔁 do tôi tự tính lại độc lập bằng NumPy từ CSV gốc; chúng không thay thế evidence trong notebook.*
