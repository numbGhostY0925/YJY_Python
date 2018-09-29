import struct
buffer=struct.pack("ihb",2,6,7)#将二进制数据分装位字符串
print(repr(buffer))
print(struct.unpack("ihb",buffer))#  将字符串反解析为数据
data=[1,2,3]
buffer=struct.pack('!ibh',*data)#将数据按照大端格式转换
print(repr(buffer))
print(struct.unpack("!ihb",buffer))