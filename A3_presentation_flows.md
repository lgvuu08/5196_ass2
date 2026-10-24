# Group005 — Hai flow thuyết trình A3 và câu chuyện phía sau

**Phân công dùng để thiết kế**
- **A1:** Minh = Task 1 (parse/profile, mapping) + Task 3 (text/regex) · Tim & Tiansheng = Task 2 (bảng, reconcile) + Task 4 (validation) · Sally & Riley = EDA + ML questions.
- **A2:** Minh = Block 1 + 1.1 + 2.1 · Tim = 1.0 + 3.2–3.3 · Tiansheng = 1.2 + 3.4 · Sally = Block 4 (+ 1.3) + 3.1 + 3.5 · Riley = Block 5 + 1.4 + 2.2.
- **Giả định (xin xác nhận):** Sally giữ 1.3; "Block 1a" = toàn bộ Block 1; Tim nói A1 cấp tập (Task 2 + 4); Tim 3.2 + 3.3, Tiansheng 3.4; ≈ 18 phút nói.

---

## 1. Câu chuyện chung (hai flow đều kể cùng một câu chuyện, chỉ khác cách dẫn)

> **"Mỗi con số chỉ có nghĩa khi đọc đúng *grain*, đúng *kỳ vọng* và đúng *thang đo* — và phải kiểm chứng lại từ file trên đĩa."**

| Nhịp | Câu hỏi khán giả đang nghĩ | Trả lời bằng | Ai |
|---|---|---|---|
| 1. **Kết luận** | "Dự án này tìm ra gì?" | Exec summary + finding A1 (review chọn lọc theo giá: 44.5% item vs 80.3% order; 27.0% → 63.6%) | Riley |
| 2. **Tin được bảng không (grain)** | "Số đó đúng nếu bảng đúng — bảng đáng tin không?" | A1: cấp bản ghi (parse, normalise, text) + cấp tập (reconcile 7,000, 0 xung đột, check 7,000/7,000) | Minh, Tim |
| 3. **Dữ liệu A2 sai ở đâu** | "Dữ liệu mới có vấn đề gì?" | A2 1.0: 80 ô trống, 8 warehouse sai, 8 vĩ độ dương, 8 ngày lạ, "charge thô ≠ outlier" | Tim |
| 4. **Mỗi lỗi một cách xử lý (kỳ vọng)** | "Vì sao ba batch xử lý khác nhau?" | dirty (quy tắc → sửa một trường) → missing (quy tắc → đại số → mô hình) → outlier (mô hình là detector) | Minh, Tiansheng, Sally |
| 5. **Dùng cho khách hàng (thang đo)** | "Rồi dùng thế nào?" | Task 3: 477 khách; raw units: chi tiêu chiếm 99.9996% → z-score cả 3 thuộc tính, không biến đổi phi tuyến | Sally, Tim, Tiansheng |
| 6. **Chứng minh & phản tư (proof)** | "Chắc chắn đúng không?" | Read-back: changed cells = logged cells; Reflection | Riley |

**Vì sao câu chuyện này hợp với marking criteria:**
- **G (mạch lạc):** một luận điểm, bốn từ khóa lặp trên màn hình (*Grain → Expectation → Scale → Proof*); A1 và A2 nối bằng *cùng kỷ luật*, không ép hợp nhất dữ liệu (A3 spec §2 cảnh báo hai tập không tự nhiên so sánh được).
- **A3 spec §3 (5 phần):** Exec summary = nhịp 1; A1 = nhịp 2; A2-data cleansing = nhịp 3–4; A2-Transformation = nhịp 5; Reflection = nhịp 6.
- **Rubric Q:** mỗi nhịp là một cặp *grain/units/limits* + một check độc lập, đúng thứ giám khảo hỏi.
- **Ba câu "tại sao" cố định xuyên suốt:** *vì sao chọn cách này* (so với phương án khác), *kiểm tra thế nào*, *giới hạn ở đâu*.

**Ba lựa chọn thiết kế chung cho cả hai flow:**
1. **Cleansing theo thứ tự spec (dirty → missing → outlier).** Block 1 của Minh phải đứng trước Block 4 của Sally *và* Minh sở hữu dirty, nên để Minh một chương liền (rules → dirty → audit) ít phân mảnh hơn là giải thích mô hình trước. Mô hình được nhắc trước bằng *một câu*.
2. **Task 3 là một chương có panel:** Sally 3.1 → Tim 3.2–3.3 → Tiansheng 3.4 → Sally 3.5. Sally bọc ngoài nên khán giả thấy một câu chuyện, không phải bốn mục.
3. **Riley mở và đóng.** Mở bằng kết luận; đóng bằng read-back + Reflection — **callback**: số ở đầu bài được kiểm lại từ file trên đĩa.

---

## 2. FLOW A — "Trace-back": từ kết luận truy ngược về bản ghi gốc *(9 lượt, ~18:10)*

### Câu chuyện
Mở bằng **kết luận** (hook), rồi hỏi "bảng này có đáng tin không?" — Tim trả lời ở **cấp tập** (7,000 review, 0 xung đột). Sau đó Minh **theo một bản ghi từ nguồn đến dòng đó** (cấp bản ghi) và đi thẳng vào **Block 1 của A2** (cùng kiểu quy tắc theo bản ghi), nên A1 → A2 nối bằng *mức lập luận*, không bằng "chuyển phần".

### Lịch và hand-over

| # | Giờ | Người nói | Nội dung | Câu hỏi chuyển giao |
|---|---|---|---|---|
| 1 | 0:00–2:00 | **Riley** | Roster (30 s) · Exec summary (30 s) · **A1 finding** (60 s): 44.5% vs 80.3%; 27.0% → 63.6% | *"Số này chỉ đúng nếu bảng đúng — bảng có đáng tin không? — Tim."* |
| 2 | 2:00–4:45 | **Tim** | **A1 cấp tập** (1:30): reconcile 3,850 + 3,850 − 700 = 7,000, 0 xung đột; check `VAL-FLOW`, `VAL-TEXT-01/02`, `T3-TEXT-05` · **1.0 của A2** (1:15) | *"Một bản ghi đi từ nguồn tới dòng đó thế nào — và quy tắc cùng kiểu trong A2? — Minh."* |
| 3 | 4:45–8:45 | **Minh** | **A1 cấp bản ghi** (1:15): parse, normalise (day-first = 31), text (marker list, near-match) · **Block 1** (0:45) · **1.1 dirty** (1:15) · **2.1** (0:45; 184 = 80 + 80 + 24) | *"Quy tắc không giúp khi ô **trống** — Tiansheng."* |
| 4 | 8:45–10:15 | **Tiansheng** | **1.2 missing**: đại số (10 charge, `high`) → mô hình (10 cờ expedited, `medium`) | *"Bậc cao nhất là phán đoán bằng mô hình — Sally."* |
| 5 | 10:15–13:30 | **Sally** | **Block 4 / spec 3.5** · **1.3 outlier** · **3.1** (1,476 đơn → 477 khách) | *"Với 477 khách, đơn vị có chi phối khoảng cách không? — Tim."* |
| 6 | 13:30–14:35 | **Tim** | **3.2 + 3.3**: raw units 99.9996%; z-score 1/3 vs min-max 38/16/46% | *"Phi tuyến thì sao? — Tiansheng."* |
| 7 | 14:35–15:20 | **Tiansheng** | **3.4**: log làm skew 0.49 → −1.94 | *"Vậy khuyến nghị gì? — Sally."* |
| 8 | 15:20–16:10 | **Sally** | **3.5**: không phi tuyến + z-score; DIST-01 | *"Tất cả có khớp file trên đĩa? — Riley."* |
| 9 | 16:10–18:10 | **Riley** | **Block 5 + 1.4 + 2.2** (1:30) · **Reflection** (0:30) | — |

### Lý do phía sau
- **Hook trước, bằng chứng sau:** finding mạnh nhất đứng đầu (Exec summary), phần còn lại là "vì sao tin được".
- **Mỗi người một chương liền:** Minh = *quy tắc theo bản ghi* (A1 record → Block 1 → dirty → audit); Tim = *bảng/grain* (A1 reconcile → 1.0). Không ai phải quay lại hai lần ở nửa đầu.
- **Thang xử lý tăng dần phụ thuộc mô hình:** dirty (quy tắc) → missing (đại số, rồi mô hình cho cờ) → outlier (mô hình là detector). Confidence phản ánh đúng thang này (`high` → `medium`).
- **Callback đóng bài:** Riley nhắc lại con số mở đầu và chứng minh từ file trên đĩa.

### Ưu / nhược
- **Ưu:** 9 lượt (ít nhất); Minh và Tim đều liền một chương; mở bài mạnh.
- **Nhược:** A1 kể ngược → người nghe có thể khựng. *Cách giảm:* Riley nói đúng một câu *"We start from the finding, verify the table, then follow one record back to its source."* Minh dùng **một** review duy nhất (ví dụ HREV004637) xuyên suốt phần A1 của mình.

---

## 3. FLOW B — "Forward path": theo chiều dữ liệu chảy *(10 lượt, ~17:55)*

### Câu chuyện
Cũng mở bằng kết luận, nhưng A1 kể **xuôi** như pipeline: một **bản ghi** JSON/XML (Minh) → trở thành một **bảng** đáng tin (Tim) → rồi mới sang A2. Đây là chiều tự nhiên nhất cho người chưa biết dữ liệu: *"nguồn → giá trị → bảng → kết luận"*.

### Lịch và hand-over

| # | Giờ | Người nói | Nội dung | Câu hỏi chuyển giao |
|---|---|---|---|---|
| 1 | 0:00–2:00 | **Riley** | Roster · Exec summary · **A1 finding** (44.5% vs 80.3%; 27.0% → 63.6%) | *"Một review JSON/XML trở thành một dòng đáng tin như thế nào? — Minh."* |
| 2 | 2:00–3:15 | **Minh** | **A1 cấp bản ghi**: parse, normalise (day-first = 31), text (marker list, near-match) trên *một* review | *"Nhiều bản ghi thành một bảng ra sao — Tim."* |
| 3 | 3:15–5:45 | **Tim** | **A1 cấp tập** (1:15): reconcile 7,000, 0 xung đột; `VAL-FLOW`, `T3-TEXT-05` · **1.0 của A2** (1:15) | *"Bắt đầu bằng quy tắc cho một đáp án duy nhất — Minh."* |
| 4 | 5:45–8:30 | **Minh** | **Block 1** (0:45) · **1.1 dirty** (1:15) · **2.1** (0:45) | *"Khi ô trống — Tiansheng."* |
| 5 | 8:30–10:00 | **Tiansheng** | **1.2 missing** | *"Bậc cao nhất — Sally."* |
| 6 | 10:00–13:15 | **Sally** | **Block 4 / 3.5** · **1.3** · **3.1** | *"477 khách, đơn vị có chi phối không? — Tim."* |
| 7 | 13:15–14:20 | **Tim** | **3.2 + 3.3** | *"Phi tuyến? — Tiansheng."* |
| 8 | 14:20–15:05 | **Tiansheng** | **3.4** | *"Khuyến nghị? — Sally."* |
| 9 | 15:05–15:55 | **Sally** | **3.5** | *"Khớp file trên đĩa? — Riley."* |
| 10 | 15:55–17:55 | **Riley** | **Block 5 + 1.4 + 2.2** · **Reflection** | — |

### Lý do phía sau
- **A1 đi theo chiều đọc tự nhiên:** người nghe thấy bản ghi trước, bảng sau, nên "bảng đáng tin" là kết quả chứ không phải khẳng định.
- **A1 trọn vẹn trong cùng một cụm:** lượt 1–3 là chương A1 liền (finding → bản ghi → bảng), rồi mới sang A2.
- **Phần A2 và Task 3 y hệt Flow A:** cùng thang xử lý, cùng panel, cùng callback.

### Ưu / nhược
- **Ưu:** dễ theo dõi nhất với giám khảo chưa quen dữ liệu; hand-over A1 rất tự nhiên.
- **Nhược:** **10 lượt**; Minh nói hai lần cách nhau Tim (A1 rồi A2); lượt 2 của Minh chỉ 1:15 nên dễ bị cắt nếu trượt giờ. *Cách giảm:* Minh mở sẵn đúng hai tab (A1 `T1-P4` / `T3-TEXT-02` và A2 `DIRTY-01`), và dùng đúng một review làm ví dụ.

---

## 4. So sánh và cách chọn

| Tiêu chí | Flow A (trace-back) | Flow B (forward) |
|---|---|---|
| Số lượt | **9** | 10 |
| Minh | **một chương liền** | hai lượt |
| Chiều kể A1 | ngược (kết luận → bảng → bản ghi) | **xuôi** (bản ghi → bảng → kết luận đã nêu) |
| Rủi ro người nghe khựng | Trung bình | **Thấp** |
| Mở bài | giống nhau | giống nhau |
| Panel Task 3, cleansing, đóng bài | giống nhau | giống nhau |
| Tổng thời lượng | ~18:10 | ~17:55 |

**Nên chọn Flow A** nếu nhóm muốn ít phân mảnh và mỗi người một chương liền; **chọn Flow B** nếu muốn ưu tiên sự dễ theo dõi của A1. Vì hai flow chỉ khác ở lượt 2–4, **có thể quyết định muộn** sau khi tập thử một lần.

---

## 5. Hai điểm cần chốt trước khi tập
1. **Tiansheng chưa có lượt A1** và đang có lượt A2 ngắn nhất (2:15). Hoặc giữ nguyên (chỉ trong roster và Q&A), hoặc chia phần cấp tập: **Tim nói reconcile (Task 2) 0:45, Tiansheng nói check (Task 4) 0:45**, rồi Tim tiếp 1.0 (thêm một lượt, Tiansheng lên ~3:00).
2. **Minh (2.1) và Riley (Block 5) chồng nhau** ở confidence và export audit. Đề xuất: *Minh = nội dung và ý nghĩa của log (định nghĩa high/medium/low một câu, 184 dòng); Riley = máy ghi và toàn vẹn (recorder 9 cột, rule `medium`, smoke test, export, read-back)*. Riley nhắc lại, không định nghĩa lại.
