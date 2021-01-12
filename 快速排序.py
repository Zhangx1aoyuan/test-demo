#   划分函数
def partition(arr, low, high):
    i, j = low, high
    # 每次设置枢纽为数列最后一个进行划分
    pivot = arr[high]
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[i], arr[high] = arr[high], arr[i]
    return i


#   快速排序
def quick_sort(arr, low, high):
    if low < high:
        # 获取枢纽所在位置下标
        mid = partition(arr, low, high)
        # 对枢纽划分的左右半区递归调用快排
        quick_sort(arr, low, mid-1)
        quick_sort(arr, mid+1, high)


if __name__ == '__main__':
    arr = [9, 5, 2, 11, 12, 4, 3, 1, 7]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
