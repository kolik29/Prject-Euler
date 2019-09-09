'''
Перестановка - это упорядоченная выборка объектов. К примеру, 3124 является одной из возможных перестановок из цифр 1, 2,
 3 и 4. Если все перестановки приведены в порядке возрастания или алфавитном порядке, то такой порядок будем называть словарным. Словарные перестановки из цифр 0, 1 и 2 представлены ниже:

012   021   102   120   201   210

Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?
'''
import itertools
stuff = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numList = []
for subset in itertools.permutations(stuff, 10):
    numList.append(''.join(str(x) for x in subset))
    print(''.join(str(x) for x in subset))

print(numList[999999:1000002])