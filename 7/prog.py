'''
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?
'''
import math

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

i = 0
start = 0

while i <= 10001:
    while True:
        if isPrime(start):
            print(start)
            i += 1
            start += 1
            break
        start += 1