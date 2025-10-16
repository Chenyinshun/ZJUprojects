import os
import time
import sys
import io
import CBalance
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


def ctime(path):
    w = os.path.getctime(path)
    b = time.localtime(w)
    return time.strftime('%Y %m %d %H:%M:%S', b)
    pass


def mtime(path):
    w = os.path.getmtime(path)
    b = time.localtime(w)
    c = time.strftime('%Y %m %d %H:%M:%S', b)
    return c
    pass


def atime(path):
    w = os.path.getatime(path)
    b = time.localtime(w)
    return time.strftime('%Y %m %d %H:%M:%S', b)
    pass


def copy(patha, pathb):
    su = os.system('copy ' + patha + ' ' + pathb)
    if su == 0:
        return 'success'
    else:
        return 'fail'
    pass


def make(path):
    if not os.path.exists(path):
        os.mkdir(path)


class cys(object):
    """这个cys函数能够帮助变量名A中的变量a作为变量名B生成
    并赋值b"""

    def vv(self, b):

        return self + '=' + "'" + b + "'"
        pass

    def ll(self):
        c = ''
        for i in self:
            c = c + i + '=[];'
        return c

        pass

    def lv(self):
        c = ''
        for i in self:
            c = c + i + '=None;'
        return c
        pass

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
    while (temp!=0):
        p=q
        q=temp
        temp=p%q
    return q

def download(args):
    import pip
    import os
    return os.system('pip install '+args)

if __name__=="__main__":
    print(download('yt-dlp'))