nums = [3,3]
target = 6
def twoSum(nums, target: int):
    for i in range (len(nums)-1):
        for j in range(i + 1, len(nums), 1):
            if nums[j] + nums[i] == target:
                return [i, j]
print(twoSum(nums, target))