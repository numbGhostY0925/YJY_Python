#Exp7_9.py
f=open('yjy_file_txt_write_gbk_ydxgx.txt','r')
s=f.readlines()
for line in s:
    print(line),
  #逗号不会产生换行符，但文件中有换行符，因此会换行
    f.close()
