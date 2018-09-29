#Exp7_8.py
f=open('yjy_file_txt_write_gbk_ydxgx.txt','r')
while True:
    line=f.readline()
    if line=='':
        break
    print(line),
#逗号不会产生换行符，但文件中有换行符，因此会换行
f.close()
