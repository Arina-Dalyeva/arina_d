from random import randint
lst_1=[0]*20
for i in range(len(list)):
    lst_1=randint(0, 20)
print(lst_1)
for i in range(0, len(lst), 1):
    lst_1[i]= lst[i]*lst[i]
print(lst_1)