from pwn import *
r = remote("host3.dreamhack.games", 11737)
for i in range(50):
    first_number = int(r.recvuntil(b'+', drop=True))
    second_number = int(r.recvuntil(b'=?\n', drop=True))
    r.sendline(str(first_number + second_number).encode())
r.interactive()