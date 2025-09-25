#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ. (vd: n=35 => Ba mươi lăm, n=5 => năm).
def doc_so(n):
    don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 10:
        return don_vi[n]

    chuc = n // 10
    dv = n % 10

   
    if chuc == 1:
        ket_qua = "mười"
    else:
        ket_qua = don_vi[chuc] + " mươi"

   
    if dv == 0:
        return ket_qua
    elif dv == 1 and chuc > 1:
        return ket_qua + " mốt"
    elif dv == 5 and chuc > 0:
        return ket_qua + " lăm"
    else:
        return ket_qua + " " + don_vi[dv]



n = int(input("Nhập số n (0 <= n < 100): "))

if 0 <= n < 100:
    print(f"{n} => {doc_so(n)}")
else:
    print("Vui lòng nhập số có tối đa 2 chữ số (0-99).")
