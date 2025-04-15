import math

n = 273246787654
pwr = 65536 # 2**16
mod = 65537

# Fermat's little theorem
# (a ** p === a) % p

# if a is coprime to p
# then (a ** (p-1) === 1) % p


if math.gcd(n, mod) == 1:
    print(1)