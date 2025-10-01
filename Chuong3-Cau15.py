#Các trường hợp cụ thể:

#(a) range(5)

#Mặc định = range(0, 5, 1)

#Kết quả: 0, 1, 2, 3, 4

#(b) range(5, 10)

#Bắt đầu từ 5 đến trước 10, bước = 1.

#Kết quả: 5, 6, 7, 8, 9

#(c) range(5, 20, 3)

#Bắt đầu từ 5, tăng 3, đến trước 20.

#Kết quả: 5, 8, 11, 14, 17

#(d) range(20, 5, -1)

#Bắt đầu từ 20, giảm 1, dừng khi nhỏ hơn hoặc bằng 5.

#Kết quả: 20, 19, 18, …, 6

#(e) range(20, 5, -3)

#Bắt đầu từ 20, giảm 3, dừng khi nhỏ hơn hoặc bằng 5.

#Kết quả: 20, 17, 14, 11, 8

#(f) range(10, 5)

#Bước mặc định = 1 (dương). Nhưng start = 10 > stop = 5 → không chạy.

#Kết quả: rỗng

#(g) range(0)

#Nghĩa là từ 0 đến trước 0 → không chạy.

#Kết quả: rỗng

#(h) range(10, 101, 10)

#Bắt đầu từ 10, tăng 10, đến trước 101.

#Kết quả: 10, 20, 30, …, 100

#(i) range(10, -1, -1)

#Bắt đầu từ 10, giảm 1, dừng khi nhỏ hơn -1.

#Kết quả: 10, 9, 8, …, 1, 0

#(j) range(-3, 4)

#Bắt đầu từ -3, tăng 1, đến trước 4.

#Kết quả: -3, -2, -1, 0, 1, 2, 3

#(k) range(0, 10, 1)

#Bắt đầu từ 0, tăng 1, đến trước 10.

#Kết quả: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#✅ Tóm lại:

#range chỉ sinh ra dãy số nguyên.

#Điểm dừng không bao giờ được lấy.

#Nếu chiều bước nhảy (step) không phù hợp với quan hệ giữa start và stop → kết quả rỗng.