#coding=GBK
f=open('file_write_gbk_ydxgx.txt','w')
f.write('常熟理工学院计算机学院@cslg')
f.seek(0,2) 	     #把文件指针移到文件尾
length=f.tell()   #会返回文件尾的位置，其值刚好等于文件长度
f.close()
print ('文件长度=',length)
