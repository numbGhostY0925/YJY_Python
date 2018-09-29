#coding=UTF-8
import pickle
#创建一个二进制文件，如果没有的话，会创建出来
f=open('yjy_file_binary_write_pickle_dump_teach.dat','wb')
n=7
i =102400000
a=10.24
s='中国云南昆明石林'
lst=[[1,2,3],[4,5,6],[7,8,9]]
tu=(5,10,8)
coll={4,5,6}
dic={'a':'apple','b':'banana','c':'collect','d':'dist','e':'egg'}
try:
    pickle.dump(n,f)
    pickle.dump(i,f)
    pickle.dump(a,f)
    pickle.dump(s,f)
    pickle.dump(lst,f)
    pickle.dump(tu,f)
    pickle.dump(coll,f)
    pickle.dump(dic,f)
except:
    print('写入的文件出错')
f.close()