from random import randint
lst = [0]*20
for i in range(len(lst)):
    lst[i] = randint(-100,100)
print(lst)
x = 0
y = 19
for i in range(0, len(lst) - 1):
    x = lst[i]
    lst[i] = lst[y]
    lst[y] = x
    y = y - 1
print(lst)

