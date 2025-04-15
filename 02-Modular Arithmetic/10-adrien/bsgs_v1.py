from math import ceil, sqrt
from tqdm import tqdm

# https://gist.github.com/0xTowel/b4e7233fc86d8bb49698e4f1318a5a73

def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in tqdm(range(N))}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in tqdm(range(N)):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None


g = 288260533169915
p = 1007621497415251

h = 67594220461269
h = p - h
print("H: ", h)

# solution = bsgs(g, h, p)
solution = 454362531787185
print("SOLUTION: ", solution)

if solution:
    print("WORKS: ", pow(g, solution, p) == h)