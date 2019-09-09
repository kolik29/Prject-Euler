'''
Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.
'''
import math

def getSumDivisors(n):
    summ = [x for x in range(1, n + 1) if n % x == 0]
    return sum(summ[0:len(summ) - 1])

def gen_friendlys(n):
    res=[]
    for i in range(1,n):
        if i not in res:
            tmp=getSumDivisors(i)
            if i==getSumDivisors(tmp) and i!=tmp:
                res.append(i)
                res.append(tmp)
    return res

print(sum(gen_friendlys(10000)))