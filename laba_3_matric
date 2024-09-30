#С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных
# по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
# Для тестирования использовать не случайное заполнение, а целенаправленное.
#Для ИСТд-11 вид матрицы А
#B C
#D E
#Подматрицы имеют вид:
#  2
# 1 3
#  4
#Формируется матрица F следующим образом: если в С количество положительных элементов в четных
#столбцах в области 2 больше, чем количество отрицательных  элементов в нечетных столбцах в области 4,
# то поменять в С симметрично области 1 и 3 местами, иначе С и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение: (F+A)*AT – K * F.
# Выводятся по мере формирования А, F и все матричные операции последовательно.
import random

# Вводим K и N с клавиатуры
K = int(input("Введите значение K: "))
N = int(input("Введите значение N: "))

' Создаем матрицы B, C, D, E и заполняем их случайными числами'
B = [[random.randint(-10, 10) for j in range(N//2)] for i in range(N//2)]
C = [[random.randint(-10, 10) for j in range(N//2)] for i in range(N//2)]
D = [[random.randint(-10, 10) for j in range(N//2)] for i in range(N//2)]
E = [[random.randint(-10, 10) for j in range(N//2)] for i in range(N//2)]

'Создаем матрицу А'
A = [[0] * N for _ in range(N)]
for i in range(N // 2):
    for j in range(N // 2):
        A[i][j] = B[i][j]
for i in range(N // 2, N):
    for j in range(N // 2):
        A[i][j] = D[i - N // 2 -1][j]
for i in range(N // 2):
    for j in range(N // 2, N):
        A[i][j] = C[i][j - N // 2-1]
for i in range(N // 2, N):
    for j in range(N // 2, N):
        A[i][j] = E[i -N // 2-1][j - N // 2-1]

print("Матрица A:")
for row in A:
    print(row)

'Копируем А в F'
F = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        F[i][j] = A[i][j]
C_pos = 0
C_neg = 0

'2 область в С'
for i in range(N // 2+1):
    for j in range(i, N - i):
        if i < len(C) and j < len(C[i]):
            if C[i][j] > 0 and j%2==0:
                C_pos += 1
    '4 область в С'
for i in range(N // 2, N):
    for j in range(N - i - 1, i + 1):
        if i < len(C) and j < len(C[i]):
            if C[i][j]<0 and j%2!=0:
                C_neg+=1

if C_pos > C_neg:
    'Меняем в С области 1 и 3'
    for i in range(N):
        for j in range(i + 1):
            if j <= i and j <= N - 1 - i:
                if j <= N // 2:
                    F[i][j], F[N - 1 - i][j] = F[N - 1 - i][j], F[i][j]
                else:
                    F[i][j], F[N - 1 - i][N - 1 - j] = F[N - 1 - i][N - 1 - j], F[i][j]

else:
    'Меняем в F С и Е'
    for i in range(N//2):
        for j in range(N//2):
            F[i][j], F[i][j+N//2], F[i+N//2][j], F[i+N//2][j+N//2] = B[i][j], E[i][j], D[i][j], C[i][j]
print("Матрица F:")
for row in F:
    print(row)

AT = [[A[j][i] for j in range(N)] for i in range(N)]
result = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            result[i][j] += (F[i][k] + A[i][k]) * AT[j][k]
        result[i][j] -= K * F[i][j]
print("Результат выражения (F+A)*AT - K*F:")
for row in result:
    print(row)

