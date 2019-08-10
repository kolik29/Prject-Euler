'''
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
'''

import math

max = 0

def pal(x):
    x = str(x)

    for i in range(0, int(len(x) / 2)):
        if x[i] != x[-i - 1]:
            break
    else:
        return int(x)

for i in range(100, 1000):
    for j in range(100, 1000):
        try:
            if pal(i * j) > max:
                max = pal(i * j)
        except:
            continue

print(max)