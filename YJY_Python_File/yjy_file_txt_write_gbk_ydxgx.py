#coding=GBK
f=open('file_write_gbk_ydxgx.txt','w')
f.write('������ѧԺ�����ѧԺ@cslg')
f.seek(0,2) 	     #���ļ�ָ���Ƶ��ļ�β
length=f.tell()   #�᷵���ļ�β��λ�ã���ֵ�պõ����ļ�����
f.close()
print ('�ļ�����=',length)
