# Reflection - PHẢI TỰ TRẢ LỜI, KHÔNG DÙNG AI

Mỗi câu nên trả lời 3-5 câu bằng lời của bạn, có ít nhất một liên hệ với output notebook. Các gợi ý dưới đây chỉ là checklist khái niệm, không phải câu trả lời để nộp.

## Câu 1 - Tăng n bổ sung thông tin gì?

Tự nêu chính xác số token quá khứ mà từng mô hình điều kiện hóa; minh họa bằng một context trong notebook.

## Câu 2 - Vì sao sparsity tăng?

Tự liên hệ số tổ hợp có thể có, số unique n-gram và số hapax trong bảng corpus statistics.

## Câu 3 - Vì sao cần smoothing?

Tự trình bày chuỗi nhân xác suất, hậu quả của một zero, và cách Laplace phân phối lại mass (không chỉ “cộng 1”).

## Câu 4 - Perplexity đo gì?

Tự diễn giải từ công thức average negative log-likelihood; nói rõ điều kiện so sánh hợp lệ: cùng dữ liệu, vocabulary, preprocessing và cách tính token.

## Câu 5 - PPL thấp có luôn đồng nghĩa văn bản tốt hơn với con người?

Tự tách đánh giá xác suất trên test distribution với các thuộc tính con người quan tâm như mạch lạc dài hạn, đúng sự thật, đa dạng và hữu ích.

## Câu 6 - N-gram thất bại ở đâu so với hiểu ngôn ngữ?

Chọn ít nhất hai giới hạn, mỗi giới hạn có một ví dụ cụ thể: phụ thuộc xa, nghĩa/tri thức, compositionality, hoặc generalization ngoài các chuỗi đã thấy.

## Câu 7 - Context 100 từ và trigram

Vẽ vị trí 100 token, đánh dấu chính xác phần context trigram thực sự dùng để dự đoán token tiếp theo, rồi tự kết luận về 97 token còn lại.

## Chuẩn bị individual learning check

Tự tập nói mỗi câu dưới 30-40 giây, không đọc tài liệu:

- Vì sao bigram có zero probability?
- Tại sao log probability tránh underflow?
- Perplexity thấp nghĩa là gì và không có nghĩa là gì?
- Vì sao trigram không nhất thiết tốt hơn bigram trên test?
- Nếu một bigram chưa xuất hiện, MLE và Laplace xử lý khác nhau thế nào?

