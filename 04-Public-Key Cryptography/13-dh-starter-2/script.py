p = 28151


for i in range(2, p):
    s = set()
    for j in range(p):
        new = pow(i ** j, -1, p)
        if new in s:
            break
        s.add(new)
    if len(s) == p - 1:

        print(i)