'''
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

import math

num = 600851475143

def getDividers(num):
    return [divid for divid in range(2, int(math.sqrt(num) + 1)) if num % divid == 0 and not getDividers(divid)]

print(getDividers(num))