import math

def do_dai_AB(xa, ya, xb, yb):
    """Trả về độ dài đoạn AB."""
    return math.hypot(xb - xa, yb - ya)

def read_point(name):
    """
    Đọc toạ độ một điểm từ input.
    Hỗ trợ nhập: "1 2", "1,2", "1.5 2.3", ...
    """
    while True:
        s = input(f"Nhập toạ độ {name} (x y): ").strip()
        s = s.replace(',', ' ')
        parts = s.split()
        if len(parts) != 2:
            print("Vui lòng nhập đúng 2 giá trị (x y). Thử lại.")
            continue
        try:
            x = float(parts[0])
            y = float(parts[1])
            return x, y
        except ValueError:
            print("Giá trị không hợp lệ. Nhập lại (phải là số).")

# --- Chương trình chính ---
print("=== TÍNH ĐỘ DÀI ĐOẠN AB ===")
xa, ya = read_point("A")
xb, yb = read_point("B")

d = do_dai_AB(xa, ya, xb, yb)
print(f"\nToạ độ A: ({xa}, {ya})")
print(f"Toạ độ B: ({xb}, {yb})")
print(f"Độ dài đoạn AB = sqrt((xB - xA)^2 + (yB - yA)^2) = {d:.4f}")
