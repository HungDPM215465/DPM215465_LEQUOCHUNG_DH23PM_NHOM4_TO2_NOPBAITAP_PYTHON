import math

def can_long_nhau(n):
    """Tính S(n) = sqrt(2 + sqrt(2 + ... + sqrt(2))) với n dấu căn."""
    s = 0
    for i in range(n):
        s = math.sqrt(2 + s)
    return s

# --- Chương trình chính ---
print("=== CHƯƠNG TRÌNH TÍNH CĂN BẬC 2 LỒNG NHAU ===")
n = int(input("Nhập số n (số dấu căn lồng nhau): "))

if n <= 0:
    print("❌ Lỗi: n phải là số nguyên dương!")
else:
    kq = can_long_nhau(n)
    print(f"\nGiá trị S({n}) = {kq:.6f}")
