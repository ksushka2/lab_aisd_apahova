import re

def h(n):
    # Use a regular expression to find three consecutive zeros
    return re.search('000', str(n)) is not None

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

lexemes = []

with open('test.txt', 'r') as f:
    block = f.read(1024)
    while block:
        # Use regular expressions to split the block into words
        r = re.split(r'\s+', block.strip())

        for word in r:
            if word.isdigit():
                if int(word) % 2 == 1:
                    lexemes.append(word)
                else:
                    print(word, '- Не подходит условию')
            else:
                print(word, '- Не подходит условию')

        print(lexemes)
        i = 0
        while i < len(lexemes) - 1 and not h(lexemes[i]) and not h(lexemes[i + 1]):
            lexemes[i], lexemes[i + 1] = lexemes[i + 1], lexemes[i]
            i += 2

        if i < len(lexemes) - 1 and (h(lexemes[i]) or h(lexemes[i + 1])):
            i += 1
            while i < len(lexemes) - 1:
                lexemes[i], lexemes[i + 1] = lexemes[i + 1], lexemes[i]
                i += 4

        block = f.read(1024)

# Print the lexemes after processing
print(lexemes)

# Translate the digits of the last lexeme to words
if lexemes:
    for digit in lexemes[-1]:
        print(book[digit])