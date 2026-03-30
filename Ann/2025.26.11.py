from random import randint
lst = [0]*10
for i in range (len(lst)):
    lst[i] = randint(0, 10)
print(lst)
max_el = 0
for i in range (0,len(lst)-1, 1):
    if lst[i + 1] %2 == 0 and lst[i] > max_el:
        max_el = lst[i]
print(max_el)
