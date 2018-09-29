import struct
a=b'hello'
b=b'world!'
c=b'python'
d=45
datstruct=struct.pack('5s6s6si',a,b,c,d)
print (repr(datstruct))
