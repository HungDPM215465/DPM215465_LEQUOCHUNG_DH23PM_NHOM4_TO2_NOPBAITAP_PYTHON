def oscillate(start, count):
    a = start
    for i in range(count):
        yield a
        yield -a
        a += 1 if a < 0 else -1

# Kiểm tra:
for n in oscillate(-3, 5):
    print(n, end=' ')