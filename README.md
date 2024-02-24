# laba1.
from num2words import num2words #pip install num2words
#Натуральные нечетные числа.
#Менять местами каждые два соседних числа пока не встретится
#число из 3 подряд идущих нулей. После чего менять только каждую вторую пару.
#Последнее число вывести словами.
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

with open('test.txt', 'r') as f:
    block = f.read(1024)
    r = block.split()
    lexemes = []
    while block:
        for i in range(len(r)):
            try:
                if int(r[i]) % 2 == 1:
                    int(r[i])
                    lexemes.append(r[i])
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
            print(i)
            while 0 <= i <= len(lexemes)-3:
                a = lexemes[i]
                b = lexemes[i+1]
                lexemes[i] = b
                lexemes[i + 1] = a
                i += 4

print(lexemes)
print(num2words(int(lexemes[-1]), lang='ru'))
block = f.read()
