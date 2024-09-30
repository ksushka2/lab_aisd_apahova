# Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
# Вариант 2: F(0) = 5; F(1) = 1; F(n) =(-1)n*( 2F(n-1)/n! + F(n-2) /(2n)!)

import matplotlib.pyplot as plt
import math
import time


def factorial(n):
    if n == 0:
        return 1
    q = 1
    for j in range(1, n + 1):
        q *= j
    return q

sign=1
# рекурсивный подход
def recursive_F(n):
    if n == 0:
        return 5
    elif n == 1:
        return 1
    else:
        global sign
        sign *= -1
        return sign * (2 * recursive_F(n - 1) / factorial(n) + recursive_F(n - 2) / (2 * n * factorial(n)))


sign = 1
fpred2 = 1
fpred = 1
# итерация подход
def iterative_F(n):
    f0 = 5
    f1 = 1
    global fpred2, fpred, sign
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        for i in range(2, n + 1):
            sign *= -1
            fi = sign * ((2 * fpred // factorial(i)) + (fpred2 // factorial(2 * i)))
            fpred2, fpred = fpred, fi
        return fpred


# сравнение времени выполнения
n = 20
recursive_start_time = time.time()
recursive_result = recursive_F(n)
recursive_time = time.time() - recursive_start_time

iterative_start_time = time.time()
iterative_result = iterative_F(n)
iterative_time = time.time() - iterative_start_time

print("| n | Recursive time | Iterative time |")
print("|---|---------------|----------------|")
for n in range(1, 21):
    recursive_start_time = time.perf_counter()
    recursive_F(n)
    recursive_time = time.perf_counter() - recursive_start_time

    iterative_start_time = time.perf_counter()
    iterative_F(n)
    iterative_time = time.perf_counter() - iterative_start_time

    print("|", n, "|", round(recursive_time, 5), "|", round(iterative_time, 5), "|")

n_values = list(range(1, 21))
recursive_times = []
iterative_times = []
for n in n_values:
    recursive_start_time = time.perf_counter()
    recursive_F(n)
    recursive_time = time.perf_counter() - recursive_start_time
    recursive_times.append(recursive_time)

    iterative_start_time = time.perf_counter()
    iterative_F(n)
    iterative_time = time.perf_counter() - iterative_start_time
    iterative_times.append(iterative_time)

# вывод графика
plt.plot(n_values, recursive_times, label='Recursive time')
plt.plot(n_values, iterative_times, label='Iterative time')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
