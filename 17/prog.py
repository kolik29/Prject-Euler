'''
Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.

Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?


Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского английского.
'''

from num2words import num2words

summ = 0

for n in range(1, 1001):
    num = num2words(n, lang='en').replace(' ', '').replace('-', '')
    print([num, len(num)])
    summ += len(num)

print(summ)