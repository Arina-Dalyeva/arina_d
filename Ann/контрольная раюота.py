x = int(input("введите 1 сторону треугольника"))
y = int(input("введите 2 сторону треугольника"))
z = int(input("введите 3 сторону треугольника"))
p = x + y + z
t = p/2
s = (t * (t - x) * (t - y) * (t - z))
print("площадь треугольника равна", s ** 0.5)
if x == y == z:
    print("треугольник равносторонний")
elif x != y and x != z and z != y:
    print("треугольник разносторонний")
else:
    print("nhteujkmybr hfdyj,tlhtyysq")
#x == y or x == z or y == z and x != y or x != z or y != z :
  #  print("треугольник равнобедренный")