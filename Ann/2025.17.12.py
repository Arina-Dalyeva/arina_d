from random import randint
lst=[0]*20
for i in range(len(lst)):
    lst[i]=randint(0, 20)
print(lst)
for i in range(0,len(lst),1):
    lst[i]=i, i-1,i+1
print(lst)