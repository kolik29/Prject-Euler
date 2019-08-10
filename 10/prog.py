'''
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.
'''
import math

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

summ = 0
start = 2

while True:
    if isPrime(start):
        if start <= 2000000:
            summ += start
            print(start)
        else:
            break
    start += 1

print(summ)