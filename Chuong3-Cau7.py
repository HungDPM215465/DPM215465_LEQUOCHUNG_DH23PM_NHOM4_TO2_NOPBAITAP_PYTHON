#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return 0  

def ngay_ke_tiep(ngay, thang, nam):
    ngay += 1
    if ngay > so_ngay_trong_thang(thang, nam):
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
            nam += 1
    return ngay, thang, nam

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

ngay_moi, thang_moi, nam_moi = ngay_ke_tiep(ngay, thang, nam)
print(f"Ngày kế tiếp là: {ngay_moi}/{thang_moi}/{nam_moi}")
