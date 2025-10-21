def tinh_ROI(doanh_thu, chi_phi):
    roi = (doanh_thu - chi_phi) / chi_phi
    return roi

# --- Chương trình chính ---
print("=== CHƯƠNG TRÌNH TÍNH ROI (Return On Investment) ===")
doanh_thu = float(input("Nhập Doanh thu (VNĐ): "))
chi_phi = float(input("Nhập Chi phí đầu tư (VNĐ): "))

roi = tinh_ROI(doanh_thu, chi_phi)
print(f"\nTỷ lệ ROI của bạn là: {roi:.2f}")

# --- Đánh giá mức độ đầu tư ---
if roi >= 0.75:
    print("=> ROI đạt mức tốt, bạn NÊN đầu tư.")
else:
    print("=> ROI thấp, bạn KHÔNG NÊN đầu tư.")
