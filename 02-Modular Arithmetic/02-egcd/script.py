from egcd import egcd

p = 26513
q = 32321

gcd, u, v = egcd(p ,q)
print(min(u, v))