#Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
pheptoan = input("Nhập phép toán (+, -, *, /): ")

if pheptoan == "+":
    ket_qua = a + b
elif pheptoan == "-":
    ket_qua = a - b
elif pheptoan == "*":
    ket_qua = a * b
elif pheptoan == "/":
    if b != 0:
        ket_qua = a / b
    else:
        ket_qua = "Lỗi: không thể chia cho 0"
else:
    ket_qua = "Phép toán không hợp lệ"


print("Kết quả:", ket_qua)
