'''
215 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 21000?
'''

summ = 0

for char in str(2**1000):
    summ += int(char)

print(summ)