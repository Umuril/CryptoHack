from pwn import *

s = "label"

i = 13

x = xor(s, i)

print(x)