import os
import time
import sys
import io

#from pandas.io.common import file_path_to_url


#import CBalance
def bianma(encoding):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding=encoding) #改变标准输出的默认编码

def now():
    month = time.strftime('%m')
    today = time.strftime('%d')
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    timenow = month + "-" + today + ' , ' + hour + "时" + minute + "分" + second + '秒'
    return timenow


def printk(self, number):
    c = len(self)
    for i in range(0, c, number):
        d = self[i:i + number]
        print(d, end='')
    pass

class timef:


    def __init__(self):
        pass

    @staticmethod
    def now():
        return time.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def create_time(path):
        """创建（属性修改）时间"""
        w = os.path.getctime(path)
        b = time.localtime(w)
        return time.strftime('%Y-%m-%d %H:%M:%S', b)

    @staticmethod
    def edit_time(path):

        """修改时间"""
        w = os.path.getmtime(path)
        b = time.localtime(w)
        c = time.strftime('%Y-%m-%d %H:%M:%S', b)
        return c

    @staticmethod
    def access_time(path):
        """访问时间"""
        w = os.path.getatime(path)
        b = time.localtime(w)
        return time.strftime('%Y-%m-%d %H:%M:%S', b)



def format_size(size_in_bytes):
    """将字节数转换为人类可读的格式"""
    for unit in ['B','KB','MB','GB','TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} PB"

def get_and_format_file_size(file_path):
    """获取并格式化文件大小"""
    file_size = os.path.getsize(file_path)
    formatted_size = format_size(file_size)
    return formatted_size


def copy(patha, pathb):
    su = os.system('copy ' + patha + ' ' + pathb)
    if su == 0:
        return 'success'
    else:
        return 'fail'



def make(path):
    if not os.path.exists(path):
        os.mkdir(path)


def hebin(list:list):
    newlist=[]
    for i in list:
        if i in newlist:
            pass
        else:
            newlist.append(i)
    return newlist

def zuidagongyshu(p,q):
    temp=p%q
    while temp!=0:
        p=q
        q=temp
        temp=p%q
    return q

def download(args):
    #import pip
    import os
    return os.system('pip install '+args)

if __name__=="__main__":
    print(timef.now())