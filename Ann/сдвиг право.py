from random import randint
lst1=[0]*5
lst2=[0]*5
for i in range(len(lst1)):
    lst1[i]= randint(0,100)
    lst2[i] = randint(0, 100)
print(lst1, lst2)
lst3=[0]*5
for i in range(0,len(lst1),1):
    if lst1[i]>lst2[i]:
        lst3[i]=lst2[i]
    if lst2[i]>lst1[i]:
        lst3[i]=lst1[i]
print(lst3)

