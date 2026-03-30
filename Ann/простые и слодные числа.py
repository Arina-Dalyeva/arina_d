x = int(input("введите число:"))
for i in range(2, x):
        if x % i == 0:
            print("число составное")
            break
        else:
            print("число простое")
            break