def print_arr(arr):
    print('[', end='')
    for i in range(len(arr)):
        print(arr[i], end=',')
    print(']')


# 选择排序 O(N**2) 稳定性看判断条件
def selection_sort(arr, n):
    # 初始化最小值下标
    min = 0
    for i in range(n):
        min = i
        for j in range(i+1, n):
            # 找出最小值下标赋值给min
            if arr[min] < arr[j+1]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


if __name__ == '__main__':
    arr = [-1, -6, -5, 10, 5, 4, 6, 3, 1, 2, 8]
    print(selection_sort(arr, len(arr)))
