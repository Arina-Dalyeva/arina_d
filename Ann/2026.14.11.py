from random import randint
lst=[0]*20
for i in range(len(lst)):
    lst[i]= randint(0,100)
print(lst)
nums=[0]*20
for i in range (0, len(lst), 1):
    if lst[i]%2 ==0 :
        nums[i] = lst[i]
    else :
        nums[i]= lst[i]*lst[i]
print(nums)
