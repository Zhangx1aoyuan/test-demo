from time import sleep
import threading
from threading import Thread

# 小明要下载十部电影
tasks = ['movie1', 'movie2', 'movie3', 'movie4', 'movie5', 'movie6', 'movie7', 'movie8', 'movie9', 'movie10']


def download(movie):
    print('开始下载{}'.format(movie))
    sleep(2)
    print('下载{}完成'.format(movie))



for task in tasks:
    t = Thread(target=download, name=task, args=(task,), daemon=True)   # 创建线程 如果daemon=True，主线程运行完就结束，不管子线程
    t.start()   # 启动线程
    print(f'{t.name} is daemon :{t.isDaemon()}')    # 是否是主线程

print('完成下载')

