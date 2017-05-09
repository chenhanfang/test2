#coding=utf-8
import threading
from time import ctime,sleep

class mythread(threading.Thread ):
    def __init__(self,func,args,name):
        threading .Thread .__init__(self)
        self.func=func
        self.args=args
        self.name=name

    def run(self):
#        apply(self.func,self.args )
        self.func(*self.args)
def superplayer(file,time):
    for i in range(2):
        print('start playing: %s ! %s' %(file,ctime()))
        sleep(time)

lists={'aijiujianrenxin.mp3':3,'yanyuan.mp4':5,'guiji.mp3':2}
threads=[]
files=range(len(lists ))

for file,time in lists.items():
    t=mythread (superplayer,(file,time),superplayer.__name__ )
    threads.append(t)

if __name__=='__main__':
    for i in files:
        threads [i].start()
    for i in files:
        threads [i].join()
    print('end:%s' %ctime())
