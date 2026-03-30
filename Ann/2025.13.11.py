lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#s = 0
#for x in lst:
    #s = s + x
#print(s)
s = 0
for x in lst:
    if x % 2 == 1:
        s = s + x
print(s)
for i in range (0, len (lst)):
    if i % 2 == 1 :
        s =  s + lst[i]




