my_bytes = b'python'
print(my_bytes)

ascii_code = [hex(byte) for byte in my_bytes]
print(ascii_code)

mybyts2 = b'\x70\x79\x74\x68\x6f\x6e'
print(mybyts2)

mybyts3 = b'10'
print(mybyts3)

ascii_code2 = [hex(byte) for byte in mybyts3]
print(ascii_code2)
mybyts4 = b'\x31\x30'
print(mybyts4)

mybyts5 = "北京"
print(mybyts5)

ascii_code3 = [hex(ord(byte)) for byte in mybyts5]
print(ascii_code3)

mystr = '\u5317\u4eac'
print(mystr)

write_bytes = mybyts5.encode('utf-8')
print(write_bytes)

print(write_bytes.decode('utf-8'))



