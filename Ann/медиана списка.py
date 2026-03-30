from random import randint
lst=[0]*20
for i in range(len(lst)):
    lst[i]= randint(0,30)
for i in range(len(lst)):
        for i in range(0, len(lst) - i - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)
if len(lst) % 2 == 0:
    x = len(lst)/2
    print(lst[x])
else:
    y = len(lst) + 1
    s = y/2
    d = lst[s] + lst[s-1]
    b = d/2
    print(lst[b])
