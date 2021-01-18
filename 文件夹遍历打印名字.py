import os
rootdir = 'D:\Download'

def bianli(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            print(os.path.join(root,file))
        for dir in dirs:
            print(os.path.join(root,dir))
            bianli(dir)

bianli(rootdir)