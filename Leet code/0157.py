m = 9
lst = [0] * m


def treygolnik (lst):
    for i in range (len(lst)-1):
        lst[0] = [1]
        print(lst)
        lst[i+1] = [1] * (i+1)
        print(lst)
    for i in range (len(lst)-1):

    return lst


print(treygolnik(lst))