#Натуральные нечетные числа.
#Менять местами каждые два соседних числа пока не встретится
#число из 3 подряд идущих нулей. После чего менять только каждую вторую пару.
#Последнее число вывести словами.
import re

def h(n):
    count = 0
    for i in range(len(str(n))):
        if str(n)[i] == '0':
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

book = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}

regex = re.compile(r'[13579]$')

with open('test.txt', 'r') as f:
    r = f.read().split()
    lexemes = []
    for i in range(len(r)):
        try:
            if regex.search(r[i]):
                lexemes.append(int(r[i]))
            else:
                print(r[i], '- Не подходит условию')
                continue
        except ValueError:
            print(r[i], '- Не подходит условию')
            continue
    i = 0
    print(lexemes)
    while not(h(lexemes[i])) and not(h(lexemes[i+1])):
        if 0 <= i <= len(lexemes)-2:
            a = lexemes[i]
            b = lexemes[i+1]
            lexemes[i] = b
            lexemes[i + 1] = a
            i += 2
            if not(0 <= i <= len(lexemes)-2):
                break
        else:
            break
    else:
        while 0 <= i <= len(lexemes)-3:
            a = lexemes[i]
            b = lexemes[i+1]
            lexemes[i] = b
            lexemes[i + 1] = a
            i += 4
    print(lexemes)
    if lexemes:
        for i in range(len(str(lexemes[-1]))):
            print(book[str(lexemes[-1])[i]])
