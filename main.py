import os,sys
import hashlib
import shutil
def File_list(file_path):
    file_list = []
    for root,dirs,files in os.walk(file_path):
        for file in files:
            file_list.append(root+r'\\'+file)
    return file_list
def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
def Calchash(filepath):
    ret = (CalcMD5(filepath),CalcSha1(filepath))
    return ret
if __name__ == '__main__':
    file_list = File_list(r'E:\01-zzy\04-库\01-手机导出\in')
    out_path = (r'E:\01-zzy\04-库\01-手机导出\repeat')
    id = 0
    lt = 0
    t = 0
    L = len(file_list)
    dic = {}
    for i in range(L):
        file = file_list[i]
        t = int((i+1)*100/L)
        if(t!=lt):
            lt = t
            print("%d%%"%(t))
        myhash = Calchash(file)
        if(myhash in dic):
            print(dic[myhash]+' equal to '+ file)
            shutil.copy(dic[myhash], out_path)
            shutil.copy(file, out_path)
            os.remove(file)
        else :
            dic[myhash] = file