#Câu 1: Viết hàm để Tính diện tích tam giác
'''
Yêu cầu:
Nhập vào 3 cạnh của tam giác, kiểm tra tính hợp lệ của tam giác, Sau đó tính diện tích
theo công thức Herong:
'''
import math

# Hàm kiểm tra tam giác hợp lệ
def hop_le_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Hàm tính diện tích theo công thức Heron
def dien_tich_tam_giac(a, b, c):
    cv = a + b + c
    p = cv / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

# Chương trình chính
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if hop_le_tam_giac(a, b, c):
    S = dien_tich_tam_giac(a, b, c)
    print(f"Diện tích tam giác là: {S:.2f}")
else:
    print("Ba cạnh không tạo thành tam giác hợp lệ!")
