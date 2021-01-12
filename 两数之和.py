def twoSum(nums, target):
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind  # index 和 nums位置交换
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]

if __name__ == '__main__':
    nums = [1, 5, 6, 7]
    target = 7
    print(twoSum(nums, target))