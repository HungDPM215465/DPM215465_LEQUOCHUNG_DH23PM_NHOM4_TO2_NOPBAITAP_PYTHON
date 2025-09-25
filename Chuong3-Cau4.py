#Câu 4: Hãy cho biết kết quả của Boolean Expression
'''
Cho x, y, z = 3, 5, 7. Hãy cho biết kết quả của Boolean Expression
'''

x, y, z = 3, 5, 7


expressions = {
    "(a) x == 3": x == 3,
    "(b) x < y": x < y,
    "(c) x >= y": x >= y,
    "(d) x <= y": x <= y,
    "(e) x != y - 2": x != y - 2,
    "(f) x < 10": x < 10,
    "(g) x >= 0 and x < 10": x >= 0 and x < 10,
    "(h) x < 0 and x < 10": x < 0 and x < 10,
    "(i) x >= 0 and x < 2": x >= 0 and x < 2,
    "(j) x < 0 or x < 10": x < 0 or x < 10,
    "(k) x > 0 or x < 10": x > 0 or x < 10,
    "(l) x < 0 or x > 10": x < 0 or x > 10,
}


for expr, result in expressions.items():
    print(f"{expr}  =>  {result}")
