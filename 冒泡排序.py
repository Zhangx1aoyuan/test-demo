# 冒泡排序 Bubble Sort
def bubble_sort(arr, n):
    if n == 0:
        return None
    for i in range(n):
        for j in range(n-i-1):  # 最后一个不需要和j+1比较
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    arr = [2, 9, 5, 2, 11, 12, 4, 3, 1, 7]
    print(bubble_sort(arr, len(arr)))