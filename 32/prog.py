'''
Каждое n-значное число, которое содержит каждую цифру от 1 до n ровно один раз, будем считать пан-цифровым; к примеру, 5-значное число 15234 является пан-цифровым, т.к. содержит цифры от 1 до 5.

Произведение 7254 является необычным, поскольку равенство 39 × 186 = 7254, состоящее из множимого, множителя и произведения является пан-цифровым, т.е. содержит цифры от 1 до 9.

Найдите сумму всех пан-цифровых произведений, для которых равенство "множимое × множитель = произведение" можно записать цифрами от 1 до 9, используя каждую цифру только один раз.

ПОДСКАЗКА: Некоторые произведения можно получить несколькими способами, поэтому убедитесь, что включили их в сумму лишь единожды.
'''
def isPandigital(string):
    digits = len(string)

    if digits >= 10:
        return False

    for i in range(1, digits + 1):
        if str(i) not in string:
            return False
    return True

def pandigitalProduct(a, b):
    numbers = str(a) + str(b) + str(a*b)
    if len(numbers) != 9:
        return False
    return isPandigital(numbers)

products = []
for a in range(1, 100000):
    for b in range(a, 100000):
        if len(str(a*b) + str(a) + str(b)) > 9:
            break
        if pandigitalProduct(a, b):
            products.append(a * b)
            print(str(a) + ' * ' + str(b) + ' = ' + str(a * b))

print(sum(set(products)))