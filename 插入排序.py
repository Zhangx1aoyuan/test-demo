# 插入排序
def insertion_sort(arr, n):
    for i in range(n):
        cur_idx = i
        while cur_idx - 1 >= 0 and arr[cur_idx] < arr[cur_idx - 1]:
            arr[cur_idx], arr[cur_idx - 1] = arr[cur_idx - 1], arr[cur_idx]
            cur_idx -= 1
    return arr


if __name__ == '__main__':
    arr = [10, 5, 4, 6, 3, 1, 2, 8]
    print(insertion_sort(arr, len(arr)))