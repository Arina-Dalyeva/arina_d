from random import randint
lst=[0]*5
for i in range(len(lst)):
    lst[i]= randint(0,100)
print(lst)
y=[0]*len(lst)
x=lst[-1]
for i in range(len(lst)):
    y[i]=lst[i-1]
y[0]=x
print(y)