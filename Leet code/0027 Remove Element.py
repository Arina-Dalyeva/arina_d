nums = [4,5]
val = 4


def removeElement(nums, val):
    k = 0
    for i in range (len(nums)):
        if nums[i] != val:
            k =  k + 1
        else:
            nums[i] = '_'
    for j in range(len(nums)):
        for i in range(j, len(nums), 1):
            if nums[j] == '_' and nums[i] != '_':
                nums[j], nums[i] = nums[i], nums[j]
    return k


print(removeElement(nums, val))
print(nums)