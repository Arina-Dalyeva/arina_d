x = int(input("введите свой процент "))
if x >= 90:
    print("у вас 5")
elif x < 90 and x >= 70:
    print("у вас 4")
elif x < 70 and x >= 40:
    print("у вас 3")
else:
    print(" у вас 2")