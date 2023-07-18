def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


print(xor(b'22',xor(b'5',b'')))