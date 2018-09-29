#这个程序是使用readlines对文件进行读写#
f=open('E:\\txtopen.txt','r')
data=[line.strip() for line in f.readlines()]#line.strip()用来删除换行符
f.close()
