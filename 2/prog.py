'''
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
'''

FSumm = 0
F = {0: 0, 1: 1}

while F[1] < 4000000:
    curNum = F[0] + F[1]
    F[0] = F[1]
    F[1] = curNum

    if curNum % 2 == 0:
        FSumm += curNum

print(FSumm)