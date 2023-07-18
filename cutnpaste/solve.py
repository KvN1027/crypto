from pwn import *

r = remote('127.0.0.1', 20000)


r.sendlineafter('user = ', 'A' * 11 + 'admin' + 'A' * 11 + 'A' * 10 )
token = r.recvline().strip().partition(b' = ')[2].decode()
token = bytes.fromhex(token)
token = token[:16] + token[32:48] + token[16:32] + token[48:]
print("mytoken==>",token)
r.sendlineafter('cookie = ', token.hex())

r.interactive()
