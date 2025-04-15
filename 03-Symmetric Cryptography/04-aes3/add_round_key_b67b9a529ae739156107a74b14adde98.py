import numpy

def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    return b''.join(bytes(matrix[i]) for i in range(4))

def add_round_key(s, k):
    return numpy.bitwise_xor(s, k).tolist()

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

new_state = add_round_key(state, round_key)
print(new_state)
print(matrix2bytes(new_state))
