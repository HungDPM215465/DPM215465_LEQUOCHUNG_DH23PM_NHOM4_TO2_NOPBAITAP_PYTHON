import time
import os

# Hàm xóa màn hình (Windows / Linux)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Các hình vẽ bằng dấu *
hinh1 = [
    "      *",
    "      * *",
    "      * * *",
    "* * * * * * *",
    "* * *",
    "* *",
    "*"
]

hinh2 = [
    "      *",
    "      * *",
    "      *   *",
    "* * * * * * *",
    "*   *",
    "* *",
    "*"
]

hinh3 = [
    "      * * * *",
    "      * * *",
    "      * *",
    "      *",
    "    * *",
    "  * * *",
    "* * * *"
]

hinh4 = [
    "      * * * *",
    "      *   *",
    "      * *",
    "      *",
    "    * *",
    "  *   *",
    "* * * *"
]

# Danh sách các hình
cac_hinh = [hinh1, hinh2, hinh3, hinh4]

# Hiển thị từng hình, mỗi hình cách nhau 5 giây
for i, hinh in enumerate(cac_hinh, 1):
    clear()
    print(f"Hình {i}:")
    for dong in hinh:
        print(dong)
    time.sleep(5)

clear()
print("Đã hiển thị xong 4 hình!")
