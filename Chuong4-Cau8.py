import math

def loga_x(a, x):
    """Tính loga cơ số a của x: log_a(x) = ln(x) / ln(a)"""
    return math.log(x) / math.log(a)

# --- Chương trình chính ---
print("=== CHƯƠNG TRÌNH TÍNH log_a(x) ===")

a = float(input("Nhập cơ số a (a > 0, a != 1): "))
x = float(input("Nhập giá trị x (x > 0): "))

# Kiểm tra điều kiện hợp lệ
if a <= 0 or a == 1:
    print("❌ Lỗi: Cơ số a phải > 0 và khác 1.")
elif x <= 0:
    print("❌ Lỗi: x phải > 0.")
else:
    kq = loga_x(a, x)
    print(f"\nlog_{a}({x}) = {kq:.4f}")
