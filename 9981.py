ceng = 1
while ceng <= 9:
    num = 1
    while num <= ceng:
        print('{}*{}={}'.format(ceng, num, ceng*num), end=' ')
        num += 1
    print()
    ceng += 1