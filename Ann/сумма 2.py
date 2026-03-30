from random import randint
lst = [0]*20
for i in range(len(lst)):
    lst[i] = randint(-100,100)
print(lst)
lst_1 = [0] * 20
for i in range (1, len(lst) - 2):
    lst_1[0] = 0 + lst[0]
    lst_1[-1] = lst[-2] + lst[-1]
    while i >= 18:
        lst_1[i + 1] = lst[i + 1] + lst[i + 2] + lst[i - 1]
        print(lst_1)
print(lst_1)