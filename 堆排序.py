def heapify(arr, n, i):     # 数组/长度(判断是否越界)/父节点
    # 分别记录父节点，左子节点，右子节点下标
    largest = i
    lson = 2 * i + 1
    rson = 2 * i + 2
    # 判断子节点是否大于父节点，是则交换下标
    if lson < n and arr[largest] <= arr[lson]:
        largest = lson
    if rson < n and arr[largest] <= arr[rson]:
        largest = rson
    # 如果父节点记录发生变化，则交换父节点和子节点
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def heap_sort(arr, n):      # 对列表进行堆排序
    i, a = 0, n//2
    for j in range(a):
        i = a - j - 1
        heapify(arr, n, i)
    print(arr)
    # 交换root至列表最后，并将列表长度减一
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [4, 10, 3, 5, 1, 6, 2, 7]
    heap_sort(arr, len(arr))
    print(arr)
