#Написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
#В филармонии К музыкальных инструментов (музыкантов) Т типов. Сформировать все возможные варианты трио.
import time
from itertools import combinations

K = int(input("Введите количество инструментов: "))
T = int(input('Введите количество типов инструментов: '))

instruments = list(range(0, K))
# словарь частотных характеристик инструментов
frequencies = {i: i % T for i in instruments}

# словарь диапазонов частотных характеристик инструментов
ranges = {i: (i % T, (i % T) + T - 1) for i in instruments}

# алгоритмический подход
start_time = time.time()
trios = []
for i in range(K - 2):
    for j in range(i + 1, K - 1):
        for k in range(j + 1, K):
            trios.append((instruments[i], instruments[j], instruments[k]))
end_time = time.time()

for trio in trios:
    print(trio)

print("Время выполнения алгоритмического подхода:", end_time - start_time)

# с помощью функций
instruments = list(range(0, K ))

start_time = time.time()
trios = combinations(instruments, T)
end_time = time.time()

print("Время выполнения функционального подхода:", end_time - start_time)
print('Списки типов инструментов:')
for i in range(T):
    instruments_of_type = [j for j in instruments if frequencies[j] == i]
    range_of_type = ranges[instruments_of_type[0]]
    print('Тип', i+1, instruments_of_type, 'диапазон', range_of_type)

