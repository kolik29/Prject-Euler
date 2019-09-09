'''
Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

Можно убедиться, что сумма чисел в диагоналях равна 101.

Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?
'''
l = 1001

topRight = []
topLeft = []
bottomLeft = []
bottomRight = []

for i in range(3, l + 1, 2):
    topRight.append(i ** 2)
    topLeft.append(i ** 2 - i + 1)
    bottomLeft.append(i ** 2 - i * 2 + 2)
    bottomRight.append(i ** 2 - i * 3 + 3)

print(sum(topRight) + sum(topLeft) + sum(bottomRight) + sum(bottomLeft) + 1)