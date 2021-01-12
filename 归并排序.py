def merge(arr, left, mid, right):
    # 创建一个临时数组存放排序结果
    temp_arr = []
    # 标记左半区第一个未排序的元素
    l_pos = left
    # 标记右半区第一个未排序的元素
    r_pos = mid + 1
    # 合并左右半区
    while l_pos <= mid and r_pos <= right:
        if arr[l_pos] <= arr[r_pos]:
            temp_arr.append(arr[l_pos])
            l_pos += 1
        else:
            temp_arr.append(arr[r_pos])
            r_pos += 1
    # 如果有剩余元素，直接放入temp_arr, 注意边界
    while l_pos <= mid:
        temp_arr.append(arr[l_pos])
        l_pos += 1
    while r_pos <= right:
        temp_arr.append(arr[r_pos])
        r_pos += 1
    # 一定要标明临时数组在原数组中代表的位置
    arr[left:right+1] = temp_arr
    del temp_arr


def msort(arr, left, right):
    if left < right:
        mid = (left + right)//2
        # 对左半区进行划分
        msort(arr, left, mid)
        # 对右半区进行划分
        msort(arr, mid+1, right)
        # 将左右分区合并
        merge(arr, left, mid, right)


if __name__ == '__main__':
    arr = [9, 5, 2, 7, 12, 4, 3, 1, 11]
    msort(arr, 0, len(arr)-1)
    print(arr)