# Error analysis - PHẢI TỰ PHÂN TÍCH, KHÔNG DÙNG AI

Notebook tự động tìm và in các candidate đúng/sai; sinh viên tự chọn 2 đúng và 2 sai. Không chép một nhãn nguyên nhân chung chung: mỗi kết luận phải có bằng chứng count/probability hoặc ví dụ corpus.

## Quy trình cho từng trường hợp

1. Chép chính xác context, model prediction, expected và probability từ notebook.
2. Tra count của context và các continuation cạnh tranh trong `trigram.ngram_counts`.
3. Kiểm tra token có bị đổi thành `<unk>` không.
4. So sánh top-1 với expected: chênh lệch do count, smoothing hay context thiếu thông tin?
5. Chọn nguyên nhân chính và, nếu cần, một nguyên nhân phụ.
6. Đề xuất một kiểm tra phản chứng: tăng dữ liệu, đổi `n`, đổi preprocessing, hoặc kiểm tra domain khác.

## Prediction đúng 1

- Context:
- Model prediction:
- Expected:
- Probability:
- Count evidence:
- Nguyên nhân mô hình đúng:

## Prediction đúng 2

- Context:
- Model prediction:
- Expected:
- Probability:
- Count evidence:
- Nguyên nhân mô hình đúng:

## Prediction sai 1

- Context:
- Model prediction:
- Expected:
- Probability:
- Count evidence:
- Nguyên nhân chính (chọn và chứng minh): insufficient data / unseen n-gram / vocabulary / sparsity / context ngắn / domain mismatch / preprocessing / smoothing.
- Kiểm tra phản chứng:

## Prediction sai 2

- Context:
- Model prediction:
- Expected:
- Probability:
- Count evidence:
- Nguyên nhân chính:
- Kiểm tra phản chứng:

## Checklist chất lượng

- [ ] Đủ 2 đúng và 2 sai.
- [ ] Mỗi case có số liệu cụ thể, không chỉ nhận xét cảm tính.
- [ ] Không kết luận “model không biết ngôn ngữ” khi bằng chứng chỉ cho thấy n-gram chưa xuất hiện.
- [ ] Không so sánh probability giữa các model nếu preprocessing/vocabulary khác nhau.

