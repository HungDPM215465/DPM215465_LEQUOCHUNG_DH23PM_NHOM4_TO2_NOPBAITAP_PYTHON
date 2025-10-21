# Hàm đệ quy trả về số Fibonacci tại vị trí N
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Hàm trả về danh sách dãy Fibonacci từ 1 đến N
def day_fibonacci(n):
    day = []
    for i in range(1, n + 1):
        day.append(fibonacci(i))
    return day

# --- Chương trình chính ---
print("=== CHƯƠNG TRÌNH TÍNH DÃY SỐ FIBONACCI ===")
N = int(input("Nhập số N: "))

# Tính số Fibonacci tại vị trí N
print(f"Số Fibonacci tại vị trí {N} là: {fibonacci(N)}")

# In ra danh sách dãy Fibonacci từ 1 → N
print(f"Dãy Fibonacci từ 1 đến {N}: {day_fibonacci(N)}")
