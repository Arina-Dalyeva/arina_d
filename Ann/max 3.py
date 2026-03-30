from random import randint
lst=[0]*20
for i in range(len(lst)):
    lst[i]= randint(0,30)
print(lst)
max_el=0
for i in range (0, len(lst), 1):
    if lst[i]%3 ==0 and lst[i]>max_el:
        max_el=lst[i]
print(max_el)