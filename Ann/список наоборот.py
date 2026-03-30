from random import randint
lst = [0]*20
for i in range(len(lst)):
    lst[i] = randint(0,100)
print(lst)
for i in range(0, len(lst)//2):
    lst[i], lst[len(lst)-1-i]=lst[len(lst)-1-i], lst[i]
    #x = lst[i]
    #lst[i] = lst[len(lst)-1-i]
    #lst[len(lst)-1-i] = x
print(lst)
