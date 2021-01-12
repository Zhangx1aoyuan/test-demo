from time import sleep
import threading
from threading import Thread


count = 0
thread_nums = 10    # 线程数
thread_task = 1000000  # 任务数


def download():
    global count
    for i in range(thread_task):
        lock.acquire()      # 锁
        count += 1
        lock.release()      # 释放

lock = threading.Lock()
threads = []

for i in range(thread_nums):
    t = threading.Thread(target=download)   # 创建线程
    t.start()   # 启动线程
    threads.append(t)

for t in threads:
    t.join()    # 当前线程等待线程t执行完毕以后再执行后面的代码

print(f'应该:{thread_task * thread_nums} \n实际：{count}')

print('下载完毕！')

