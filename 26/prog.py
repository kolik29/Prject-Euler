'''
Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:

1/2	=	0.5
1/3	=	0.(3)
1/4	=	0.25
1/5	=	0.2
1/6	=	0.1(6)
1/7	=	0.(142857)
1/8	=	0.125
1/9	=	0.(1)
1/10	=	0.1
Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.

Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность цифр.
'''
def convert(numerator, denominator):
    ans = str(numerator//denominator) + "."
    l = {}
    index = 0
    numerator = numerator%denominator
    l[numerator] = index
    t = False
    while t == False:
        if numerator == 0:
            break
        digit = numerator*10 // denominator
        numerator = numerator * 10 - (numerator * 10 // denominator) * denominator
        if numerator not in l:
            ans += str(digit)
            index += 1
            l[numerator] = index
            t = False
        else:
            ans += str(digit) + ")"
            ans = ans[:l.get(numerator) + len(ans[:ans.index(".") + 1])] + "(" +  ans[l.get(numerator) + len(ans[:ans.index(".") + 1]):]
            t = True
    return ans

max = 0

for d in range(2, 1000):
    num = convert(1, d)
    if max < len(str(convert(1, d))):
        print(d)
        max = len(str(convert(1, d)))