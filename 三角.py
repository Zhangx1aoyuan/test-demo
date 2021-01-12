'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''

for i in range(1, 7):
    for j in range(1, 7):
        if j <= i:
            print(j, end=' ')
    print()
print()
'''
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for i in range(1, 7):
    for j in range(1, 7):
        if j >= i:
            print(j, end=' ')
    print()
print()
'''
          1 
        2 1 
      3 2 1 
    4 3 2 1 
  5 4 3 2 1 
6 5 4 3 2 1
'''
for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= 7:
            print((7 - j), end=' ')
        else:
            print(' ', end=' ')
    print()
print()

'''
          1 
        2 1 
      3 2 1 
    4 3 2 1 
  5 4 3 2 1 
6 5 4 3 2 1
'''
for i in range(1, 7):
    for j in range(1, 7):
        if j + 1 > i:
            print((j - i + 1), end=' ')
        else:
            print(' ', end=' ')
    print()