# Calculations - PHẢI TỰ LÀM, KHÔNG DÙNG AI

Theo mục 25 của đề, đây là phần tính toán ban đầu không được sử dụng AI. File này là worksheet hướng dẫn phương pháp, không điền đáp số cuối cùng. Hãy làm trên giấy trước, chụp/scan nếu giảng viên yêu cầu, rồi chỉ dùng code để tự kiểm tra sau khi đã chốt bài làm.

## Bài 1 - Unigram

1. Chép ba câu thành một dãy token, giữ nguyên từng lần lặp.
2. Lập bảng `token | count`.
3. Vocabulary là tập các token phân biệt; `N` là tổng tất cả count.
4. Với mỗi từ được hỏi, thay vào `P(w) = C(w) / N`.
5. Kiểm tra độc lập: cộng mọi count phải bằng `N`; cộng xác suất của **tất cả** từ trong vocabulary phải bằng 1.

| Token | C(w) | P(w) = C(w)/N |
|---|---:|---:|
| the |  |  |
| cat |  |  |
| fish |  |  |
| dog |  |  |

Tự ghi vocabulary: `__________________________________________`

Tự ghi tổng token `N = ______`; tổng xác suất `= ______`.

## Bài 2 - Bigram

Lập riêng danh sách mọi từ xuất hiện ngay sau từng context. Mẫu tính:

`P(next | context) = C(context, next) / C(context)`

Trong mẫu số, `C(context)` phải đếm số lần context có một từ kế tiếp trong cách xử lý hiện tại. Nếu thêm `</s>`, phải dùng quy ước đó nhất quán.

| Xác suất | Tử số | Mẫu số | Kết quả |
|---|---:|---:|---:|
| P(cat\|the) |  |  |  |
| P(dog\|the) |  |  |  |
| P(eats\|cat) |  |  |  |
| P(likes\|cat) |  |  |  |

Kiểm tra normalization: liệt kê **mọi** continuation quan sát được sau `the`, tính từng xác suất rồi cộng. Trong phần tự giải thích, phải nêu được lý do tử số của các continuation tạo thành một phân hoạch của count ở mẫu số.

## Bài 3 - Xác suất câu

1. Viết bốn thừa số đúng thứ tự đề cho.
2. Tính riêng từng thừa số từ count.
3. Nhân các phân số; giữ dạng phân số để tránh làm tròn sớm.
4. Tự trả lời câu hỏi về việc thêm một từ bằng cách xét miền giá trị của xác suất có điều kiện và trường hợp biên; sau đó liên hệ với thiên lệch theo độ dài.

`P(sentence) = ______ × ______ × ______ × ______ = ______`

## Bài 4 - Sentence ranking

Trước khi xem output notebook, đánh dấu dự đoán cá nhân và lý do dựa trên các bigram khác nhau giữa hai câu. Sau đó tính tích xác suất của hai câu theo **cùng một quy ước**.

- Dự đoán trước: `__________`
- Bigram quyết định sự khác biệt: `__________`
- Sau khi tự tính: `__________`

## Zero probability

Với corpus `I like NLP / I like AI / I study NLP`:

1. Tìm trực tiếp count của bigram được hỏi.
2. Chia cho count của context để có MLE.
3. Theo dõi tác động của một thừa số bằng 0 lên tích xác suất câu.
4. Trong diễn giải cá nhân, phân biệt “không quan sát trong mẫu hữu hạn” với “bất khả thi trong ngôn ngữ”.

## Laplace smoothing

Thay lần lượt hai giá trị count vào:

`P_Laplace(eats|cat) = (C(cat,eats)+1)/(C(cat)+V)`

Tự kiểm tra rằng tổng xác suất trên toàn vocabulary vẫn bằng 1. Khi giải thích tác động lên bigram khác, so sánh cả tử số và mẫu số trước/sau smoothing, không chỉ nói zero trở thành dương.

## Perplexity bằng tay

1. Tính `P(W)` bằng tích ba xác suất.
2. Với `N=3`, tính `PP(W) = P(W)^(-1/3)` hoặc công thức log tương đương.
3. Thay xác suất giữa bằng giá trị mới và lặp lại.
4. So sánh **tỉ lệ** hai tích và căn bậc ba của tỉ lệ đó; đây là kiểm tra số học tốt hơn chỉ nhìn số thập phân.

| Trường hợp | P(W) | PP(W) |
|---|---:|---:|
| Xác suất giữa ban đầu |  |  |
| Xác suất giữa thay đổi |  |  |

