from random import randint
lst=[0]*20
for i in range(len(lst)):
    lst[i]= randint(0,100)
print(lst)
x = lst[0]
for i in range(len(lst)-1):
    lst[i] = lst[i+1]
lst[-1] = x
print(lst)