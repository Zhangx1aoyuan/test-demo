print('9*9乘法表')
ceng = 1
while ceng <= 9:
    num = 1
    while num <= ceng:
        print('{}*{}={}'.format(ceng, num, ceng*num), end=' ')
        num += 1
    print()
    ceng += 1