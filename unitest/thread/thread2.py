#coding=utf-8
import multiprocessing
#import threading
from time import sleep,ctime

def super_player(file_,time):
    for i in range(2):
        print("start playing: %s! %s" %(file_, ctime()))
        sleep(3)

lists={'let it be.mp3':2,'try.mp4':5,'just want.mp3':3}

threads=[]
files=range(len(lists))

for file_,time in lists.items():
    t=multiprocessing.Process(target=super_player,args=(file_,time))
#    t=threading .Thread(target=super_player, args=(file_,time))
    threads.append(t)


if __name__=='__main__':
    for t in files:
        threads[t].start()

    for t in files:
        threads[t].join()

    print ('end:%s ' % ctime())


