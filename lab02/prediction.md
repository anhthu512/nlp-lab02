# Prediction trước experiment - PHẢI TỰ VIẾT, KHÔNG DÙNG AI

Không xem bảng/biểu đồ/output trong notebook trước khi điền phần này. Với mỗi câu, bắt buộc ghi đủ Prediction, Reason, Confidence. Confidence có thể dùng thang 0-100%.

## Prediction 1 - Vocabulary khi unigram -> bigram -> trigram

- Prediction:
- Reason: Tự phân biệt “vocabulary” (tập token) với “tập n-gram”.
- Confidence:

## Prediction 2 - Số lượng n-gram

- Prediction:
- Reason: Xét số vị trí tạo n-gram và khả năng tổ hợp độc nhất khi context dài hơn.
- Confidence:

## Prediction 3 - Zero probability

- Prediction:
- Reason: Liên hệ độ dài context với xác suất một context/continuation đã từng xuất hiện.
- Confidence:

## Prediction 4 - Training perplexity

- Prediction:
- Reason: Nghĩ về mức độ mô hình có thể khớp chính dữ liệu dùng để đếm; ghi rõ đang nói MLE hay smoothing.
- Confidence:

## Prediction 5 - Corpus nhỏ: trigram có chắc chắn tốt hơn bigram?

- Prediction:
- Reason: Cân bằng thông tin context với sparsity; tách train khỏi validation/test.
- Confidence:

## Đối chiếu sau experiment

Chỉ điền sau khi đã khóa phần dự đoán phía trên. Không sửa prediction gốc.

| Câu | Khớp kết quả? | Bằng chứng cụ thể từ output | Điều học được |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

