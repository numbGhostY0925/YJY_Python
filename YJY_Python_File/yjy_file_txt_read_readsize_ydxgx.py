#Exp7_6.py
f=open('yjy_file_txt_write_gbk_ydxgx.txt','r')
s=f.read(11)#读取文件的前11个字节
f.close()
print('s=',s)
print('字符串s的长度(字符个数)=', len(s))
