'''
В Англии валютой являются фунты стерлингов £ и пенсы p, и в обращении есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Сколькими разными способами можно составить £2, используя любое количество монет?
'''
coins = (200, 100, 50, 20, 10, 5, 2, 1)

count = 0

def getCountCoins(value, part):
    global count
    for i in range(0, 201, coins[value]):
        if part + i < 200 and value < 7:
            temp = getCountCoins(value + 1, part + i)
            count += temp
        elif part + i == 200 or value == 7:
            return 1
        else:
            return 0
temp = getCountCoins(0, 0)
count += temp
print(count)