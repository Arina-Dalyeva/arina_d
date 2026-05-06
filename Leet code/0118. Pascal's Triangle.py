m = 7
lst = [0] * m


def treygolnik(lst):
    x = 0
    for i in range(len(lst) - 1):
        lst[0] = [1]
        print(lst)
        lst[i + 1] = [1] * (i + 2)
        print(lst)
    for i in range(len(lst)):
        for j in range(len(lst[i])-1):
            if len(lst[i]) > 2 and j != 0:
                lst[i][j] = i
    for item in lst:
        print(item)
    return lst


print(treygolnik(lst))


for i in range (len(lst)):
    print((' '* -(i-len(lst)) ), *lst[i])