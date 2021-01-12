from time import sleep
import threading
from threading import Thread

# 小明要下载十部电影
tasks = ['movie1', 'movie2', 'movie3', 'movie4', 'movie5', 'movie6', 'movie7', 'movie8', 'movie9', 'movie10']


def download(movie):
    print('开始下载{}'.format(threading.current_thread().name))
    sleep(2)
    print('下载{}完成'.format(threading.current_thread().name))


t = threading.current_thread()
print(f'{t.name}-{t.ident}')


for task in tasks:
    t = threading.Thread(target=download, name=task, args=(task,))   # 创建线程
    # print('{}{}'.format(t.name, t.ident))
    t.start()   # 启动线程
    # t.join()
    # print(f'thread {t.name}{t.ident}')

