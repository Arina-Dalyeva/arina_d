nums = [0,0,1,1,1,2,2,3,3,4]


def removeDuplicates(nums):
    k = 1
    for i in range (len(nums)-1):
        if nums[i] != nums[i+1]:
            k = k + 1
    for i in range (k, len(nums, 1)):
        nums[i] = '_'
    return k


print(removeDuplicates(nums))
