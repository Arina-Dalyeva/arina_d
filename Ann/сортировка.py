from random import randint
lst = [0]*20
for i in range(len(lst)):
    lst[i] = randint(0,100)
print(lst)
for i in range(len(lst)):
        for i in range(0, len(lst) - i - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)
