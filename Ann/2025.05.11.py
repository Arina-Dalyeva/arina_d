x = input('введите букву от a до h')
letters = 'abcdefgh'
z = letters. index(x) + 1
number = int(input('введите номер от 1 до 8'))
if (number + z)%2 == 0:
    print('это черная клетка')
else:
    print('это белая клетка')
