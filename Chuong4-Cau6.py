import random

print("=== MINH HỌA HÀM random.randrange(0, 100) ===")

# In ra 10 giá trị ngẫu nhiên để quan sát
for i in range(10):
    so = random.randrange(0, 100)
    print(f"Lần {i+1}: {so}")
    
#✅ Có thể xuất hiện:
#0: ✅ (giá trị bắt đầu của khoảng)
#34: ✅ (nằm trong khoảng 0–99)
#99: ✅ (giá trị cuối cùng có thể được chọn)