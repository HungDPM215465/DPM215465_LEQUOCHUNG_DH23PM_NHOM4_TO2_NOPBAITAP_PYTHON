def tinh_BMI(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao ** 2)
    return bmi

def phan_loai_BMI(bmi):
    if bmi < 18.5:
        return "Gầy", "Thấp"
    elif bmi < 25:
        return "Bình thường", "Trung bình"
    elif bmi < 30:
        return "Hơi béo", "Cao"
    elif bmi < 35:
        return "Béo phì cấp độ 1", "Cao"
    elif bmi < 40:
        return "Béo phì cấp độ 2", "Rất cao"
    else:
        return "Béo phì cấp độ 3", "Nguy hiểm"

# --- Chương trình chính ---
print("=== CHƯƠNG TRÌNH TÍNH CHỈ SỐ BMI ===")
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

bmi = tinh_BMI(can_nang, chieu_cao)
phan_loai, nguy_co = phan_loai_BMI(bmi)

print(f"\nChỉ số BMI của bạn là: {bmi:.2f}")
print(f"Phân loại cơ thể: {phan_loai}")
print(f"Nguy cơ phát triển bệnh: {nguy_co}")
