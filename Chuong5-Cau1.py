while True:
    chuoi = input("\nNhập vào một chuỗi: ")

    # Kiểm tra chuỗi đối xứng
    if chuoi == chuoi[::-1]:
        print("==> Chuỗi này là chuỗi đối xứng.")
    else:
        print("==> Chuỗi này KHÔNG phải là chuỗi đối xứng.")

    # Hỏi người dùng có tiếp tục không
    tiep_tuc = input("Bạn có muốn tiếp tục không? (y/n): ").lower()
    if tiep_tuc != 'y':
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
