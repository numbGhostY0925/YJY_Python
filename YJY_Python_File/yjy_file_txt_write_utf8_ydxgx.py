import codecs  	#自然语言编码转换模块NameError: name 'codecs' is not defined
#coding=UTF-8
s='常熟理工学院计算机学院@cslg'
f=codecs.open('file_write_utf8_ydxgx.txt','w','UTF-8') #UTF-8编码方式
f.write(s)
f.seek(0,2) 	#把文件指针移到文件尾
length=f.tell() #文件尾的位置，其值刚好等于文件长度（字节数）
f.close()
print('文件长度=',length)
f=open('file_write_utf8_ydxgx.txt','a+')
s='常熟在苏州\n苏州在江苏\n'
f.write(s)
f.close()
