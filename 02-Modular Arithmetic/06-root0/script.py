p = 29
ints = [14, 6, 11]


q = (p-1) // 2
i = 0

for a in ints:
    if pow(a, q, p) == 1:
        i = a
        break

for x in range(p):
    if pow(x, 2, p) == i:
        print(x)
        break
