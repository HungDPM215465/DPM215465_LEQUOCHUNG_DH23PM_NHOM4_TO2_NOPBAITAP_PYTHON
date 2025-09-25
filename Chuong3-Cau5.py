#Câu 5: Hãy cho biết kết quả xuất ra màn hình
'''
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, ", j =", j, ", k =", k)
Hãy cho biết kết quả xuất ra màn hình nếu tuần tự 3 biến trên có các giá trị sau:
(a) i = 3, j = 5, and k = 7
(b) i = 3, j = 7, and k = 5
(c) i = 5, j = 3, and k = 7
(d) i = 5, j = 7, and k =3
(e) i = 7, j = 3, and k = 5
(f) i =7, j = 5, and k = 3
'''
def test_values(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print(f"i = {i}, j = {j}, k = {k}")

# Các bộ test (a) → (f)
cases = [
    (3, 5, 7),  # a
    (3, 7, 5),  # b
    (5, 3, 7),  # c
    (5, 7, 3),  # d
    (7, 3, 5),  # e
    (7, 5, 3)   # f
]

labels = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)"]

for label, (i, j, k) in zip(labels, cases):
    print(label, end=" ")
    test_values(i, j, k)
