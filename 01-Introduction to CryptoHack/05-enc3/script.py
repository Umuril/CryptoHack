import base64

s = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

h = bytes.fromhex(s)

print(base64.b64encode(h))