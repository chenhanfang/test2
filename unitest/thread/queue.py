#coding=utf-8
import multiprocessing
import os,time

def inputq(queue):
    info=str(os.getpid())+'(put):'+str(time.ctime())
    queue.put(info)

def outputq(queue,lock):
    info=queue.get()
    lock.acquire()
    print((str(os.getpid())+'(get):'+info))
    lock.release()

if __name__=='__main__':
    record1=[]
    record2=[]
    lock=multiprocessing.Lock()
    queue=multiprocessing .Queue(3)
    for i in range(10):
        process=multiprocessing.Process (target= inputq,args=(queue,))
        process .start()
        record1 .append(process)

    for i in range(10):
        process=multiprocessing .Process (target= outputq,args= (queue,lock))
        process .start()
        record2 .append(process )

    for p in record1 :
        p.join()
    queue.close()
    for p in record2 :
        p.join()

