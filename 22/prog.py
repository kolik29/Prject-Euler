'''
Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), текстовый файл размером 46 КБ, содержащий более пяти тысяч имен. Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
'''
f = open('p022_names.txt', 'r')

names = sorted(f.read().split(' '))
abc = sorted([x for x in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
namesScore = []
i = 1

for name in names:
    abcVal = 0
    for letter in name:
        abcVal += abc.index(letter) + 1

    print(abcVal * i)
    namesScore.append(abcVal * i)
    i += 1

print(sum(namesScore))