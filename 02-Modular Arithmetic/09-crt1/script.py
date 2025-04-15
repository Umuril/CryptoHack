N = 5 * 11 * 17

l = [(2, 5), (3, 11), (5, 17)]

print(sum([x[0] * N // x[1] * pow(N // x[1], -1, x[1]) for x in l]) % N)