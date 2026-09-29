# LAB 02 - N-gram Language Models

Thư mục này chứa phần cài đặt và thí nghiệm có thể chạy lại cho LAB 02.

## Cách chạy

1. Đặt `c4-train.00000-of-01024-30K.json.gz` ở thư mục cha của `lab02/`.
2. Mở terminal tại `lab02/`.
3. Chạy notebook từ đầu đến cuối bằng Jupyter, hoặc chạy file notebook đã có output.

Notebook hiện dùng `MAX_DOCUMENTS = 10_000`, seed 42, chia theo document 80% train / 10% validation / 10% test. Vocabulary chỉ được xây dựng từ train; token ngoài vocabulary được ánh xạ thành `<unk>`. Mỗi câu có `</s>`; bigram/trigram dùng lần lượt một/hai `<s>` làm context đầu câu.

## Tệp chính

- `ngram_lm.py`: cài đặt từ đầu unigram, bigram, trigram, MLE, Laplace, log-probability, perplexity, next-word prediction và continuation ranking.
- `experiments.ipynb`: notebook đã chạy; output, bảng và biểu đồ được lưu ngay trong notebook.
- `results.csv`: kết quả máy sinh ra từ lần chạy notebook gần nhất.
- `calculations.md`, `prediction.md`, `error_analysis.md`, `reflection.md`: worksheet để sinh viên tự hoàn thành theo chính sách AI của đề.
- `AI_ASSISTANCE.md`: khai báo đầy đủ việc sử dụng AI.

## Quy ước đánh giá

- Perplexity tính trên mọi token được dự đoán và một token `</s>` cho mỗi câu.
- MLE trả về `inf` khi tập đánh giá có ít nhất một n-gram chưa thấy.
- Laplace dùng cùng vocabulary và preprocessing cho mọi split/model.
- Candidate có độ dài khác nhau được xếp hạng bằng average log-probability (tương đương conditional perplexity); notebook vẫn lưu total log-probability để đối chiếu.

## Chính sách AI quan trọng

Đề cấm dùng AI cho bài tính ban đầu, prediction trước experiment, giải thích kết quả, error analysis, reflection và individual learning check. Vì vậy các file tương ứng chỉ có khung, công thức, checklist và câu hỏi gợi ý; không chứa đoạn trả lời hoàn chỉnh để nộp. Phần code và visualization do AI hỗ trợ được khai báo trong `AI_ASSISTANCE.md`.

