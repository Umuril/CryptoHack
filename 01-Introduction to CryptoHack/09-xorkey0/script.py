from pwn import *

b = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

def is_printable(s):
    for c in s:
        if c not in string.printable:
            return False
    return True


for key in range(0xFF):
    x = xor(b, key)

    if is_printable(x.decode(errors='replace')):
        print(hex(key), x)
