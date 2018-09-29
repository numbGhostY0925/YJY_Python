#首先生成随机数，并写人文本文件中;
#接着打开文本文件，将里面的数字输出
#导入随机数生成的包
from random import randint

def main():
    #打开一个存放随机的文件
    randtxt=open('yjy_file_txt_writeread_random_teach.txt','w')
    for i  in range(20):
        randtxt.write(str(randint(0,9))+",")
    randtxt.close()

    #将存储在文本文件中的数字提取出来并显示
    randtxtread=open('yjy_file_txt_writeread_random_teach.txt','r')
    s=randtxtread.read()
    #使用split函数将随机数字符串按照,分割，并返回一个列表
    stringnumbers=s.split(',')
    #print(stringnumber)
    for number in stringnumbers:
        print (number ,end="  ")
    randtxtread.close()    
main()
