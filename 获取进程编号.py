import multiprocessing
import time
import os


# 唱歌
def sing(num, name):
    print("唱歌进程pid：", os.getpid())
    print('唱歌进程的父进程：', os.getppid())
    for i in range(num):
        print(name, '', '唱歌...')
        time.sleep(0.5)


# 跳舞
def dance(num, name):
    print("跳舞进程pid：", os.getpid())
    print('跳舞进程的父进程：', os.getppid())
    for i in range(num):
        print(name, '', '跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    print('主进程的父进程：', os.getpid())
    sing_process = multiprocessing.Process(target=sing, args=(3, "zzy"))
    dance_process = multiprocessing.Process(target=dance, kwargs={'name': "zzy1", 'num': 2})

    sing_process.start()
    dance_process.start()

