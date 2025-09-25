#Câu 10: Tính dãy số
'''
Cho biểu thức toán học sau:
Viết chương trình cho phép nhập x, n và xuất ra kết quả của biểu thức
'''
import math

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))

s = x 

for i in range(2, n + 1):
    s += x**i / math.factorial(i)

print("S({0}, {1}) = {2}".format(x, n, s))
