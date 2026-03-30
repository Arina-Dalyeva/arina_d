x = int(input("введите число:"))
x = x + 1
for i in range(2, x):
        if x % i == 0:
            print(x+1)
            break
        elif x % i != 0:
            print(x+1)
            break