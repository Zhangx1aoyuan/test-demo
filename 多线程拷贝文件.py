import time
import os
import threading

# 拷贝文件
def copy_file(file_name, source_dir, test_dir):
    # 1、拼接源文件路径和目标文件路径
    source_path = source_dir + '/' + file_name
    test_path = test_dir + '/' + file_name

    # 2、打开源文件和目标文件
    with open(source_path, "rb") as source_file:    # 读
        with open(test_path, "wb") as test_file:    # 写
            # 3、循环拷贝源文件到目标文件
            while True:
                data = source_file.read(1024)
                if data:
                    test_file.write(data)
                else:
                    break


if __name__ == '__main__':
    flag = 0
    t = time.time()
    # 1、定义源目录和目标目录
    source_dir = "C:\\Users\\LENOVO\\Desktop\\zzy"
    test_dir = "D:\\Python\\testzzy"

    # 2、创建目录如果目录不存在
    try:
        os.mkdir(test_dir)
        flag = 1
    except:
        print('目标已存在')

    if flag == 1:
        # 3、读取源文件列表
        file_list = os.listdir(source_dir)

        # 4、遍历列表获取源文件
        for file_name in file_list:
            # 5、创建子线程实现多任务拷贝
            # copy_file(file_name, source_dir, test_dir)    # 单任务方式
            sub_thread = threading.Thread(target=copy_file, args=(file_name, source_dir, test_dir))
            sub_thread.start()

        print(f"拷贝完成，耗时{round(time.time() - t, 2)}秒")