#Câu 11: Kiểm tra số nguyên tố
'''
Viết chương trình nhập vào một số, kiểm tra xem số này có phải là số nguyên tố
hay không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm.
'''
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    so = int(input("Nhập một số: "))

    if la_so_nguyen_to(so):
        print(so, "là số nguyên tố.")
    else:
        print(so, "không phải là số nguyên tố.")

    tiep_tuc = input("Bạn có muốn tiếp tục không? (y/n): ").strip().lower()
    if tiep_tuc != 'y':
        print("Thoát chương trình. Tạm biệt!")
        break
