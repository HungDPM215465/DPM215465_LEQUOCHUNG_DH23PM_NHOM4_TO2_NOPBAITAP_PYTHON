#Câu 2: Viết Hàm để chơi Game Đoán Số
'''
Yêu cầu:
Máy ra 1 số trong đoạn [1...100]
Người chơi đoán số, chỉ được phép đoán sai 7 lần. Mỗi lần đoán sẽ thông báo số
người chơi đoán nhỏ hơn hay lớn hơn số của mày và hiển thị số lần đoán
Game kết thúc khi: Đoán sai quá 7 lần hoặc đoán trúng trước 7 lần.
Sau khi game kết thúc hỏi người chơi có tiếp tục hay không?
'''
import random

def choi_game():
    # Máy chọn số ngẫu nhiên từ 1 đến 100
    so_may = random.randint(1, 100)
    so_lan_doan = 0
    gioi_han = 7

    print("=== Game Đoán Số ===")
    print("Máy đã chọn 1 số trong khoảng [1..100]. Bạn có 7 lần đoán!")

    while so_lan_doan < gioi_han:
        try:
            doan = int(input(f"Nhập số bạn đoán (lần {so_lan_doan+1}): "))
        except ValueError:
            print("Vui lòng nhập số nguyên!")
            continue

        so_lan_doan += 1

        if doan == so_may:
            print(f"🎉 Chúc mừng! Bạn đã đoán đúng số {so_may} sau {so_lan_doan} lần!")
            break
        elif doan < so_may:
            print("👉 Số bạn đoán nhỏ hơn số của máy.")
        else:
            print("👉 Số bạn đoán lớn hơn số của máy.")

        print(f"Còn {gioi_han - so_lan_doan} lần đoán.")

    else:
        print(f"😢 Bạn đã đoán sai quá {gioi_han} lần. Số đúng là {so_may}.")

# Chương trình chính
while True:
    choi_game()
    tiep_tuc = input("Bạn có muốn chơi lại không? (c/k): ").lower()
    if tiep_tuc != "c":
        print("Cảm ơn bạn đã chơi game! 👋")
        break
