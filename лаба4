#С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
#состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
#случайным образом целыми числами в интервале [-10,10]. Для тестирования
#использовать не случайное заполнение, а целенаправленное.
#Для ИСТд-11 вид матрицы А
#B C
#D E
#Формируется матрица F следующим образом: скопировать в нее А и если
#в С количество положительных элементов в четных столбцах, чем количество
#отрицательных  элементов в нечетных столбцах, то поменять местами С и В
#симметрично, иначе С и Е поменять местами несимметрично. При этом матрица
#А не меняется. После чего если определитель матрицы А больше суммы диагональных
#элементов матрицы F, то вычисляется выражение: A*AT – K * F*A-1, иначе вычисляется
#выражение (К*A-1 +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.
#Выводятся по мере формирования А, F и все матричные операции последовательно.

import numpy as np
import matplotlib.pyplot as plt
K = int(input("Введите K: "))
N = int(input("Введите N: "))

# Создаем матрицу A
A = np.zeros((N, N), dtype=int)
n2 = N // 2
if N % 2 != 0:
    n2 += 1
A[:n2, :n2] = np.random.randint(-10, 10, size=(n2, n2)) # Подматрица B
A[:n2, n2:] = np.random.randint(-10, 10, size=(n2, N - n2)) # Подматрица C
A[n2:, :n2] = np.random.randint(-10, 10, size=(N - n2, n2)) # Подматрица D
A[n2:, n2:] = np.random.randint(-10, 10, size=(N - n2, N - n2)) # Подматрица E


print("Матрица A:")
print(A)
# Цветной график
def print_mat(mat, description):
    plt.matshow(mat)
    plt.title(description)
    plt.colorbar()
    plt.show()
print_mat(A, "Матрица A")
# Создаем матрицу F
F = A.copy()

# Подсчитываем количество положительных и отрицательных элементов в подматрице C
C = A[:n2, n2:]
c_pos = np.count_nonzero(C[:, ::2] > 0)
c_neg = np.count_nonzero(C[:, 1::2] < 0)

# Проверяем условие и меняем местами подматрицы C и В или C и Е
if c_pos > c_neg:
    B = F[:n2, :n2].copy()
    n3 = N - n2
    F[:n3, :n3] = F[n2:, n2:]
    F[n2:, n2:] = B
else:
    C = F[:n2, n2:].copy()
    n3 = N - n2
    F[:n3, n2:] = F[n2:, n2:]
    F[n2:, n2:] = C[::-1, ::-1]
#Линейный график
plt.plot(F)
plt.title("Matrix F")
plt.show()
print("Матрица F:")
print(F)

# Вычисляем определитель матрицы A и сумму диагональных элементов матрицы F
det_A = np.linalg.det(A)
print("Определитель матрицы А:")
print(det_A)

sum_diag_F = np.trace(F)
print("Сумма главной диагонали матрицы F:")
print(sum_diag_F)

# Вычисляем выражение AAT – K * FA-1 или (К*A-1 +G-FТ)*K в зависимости от условия
if det_A > sum_diag_F:
    G = np.tril(A)
    result = np.dot(A, A.T) - K * np.dot(F, np.linalg.inv(A))
else:
    G = np.tril(A)
    result = K * np.dot(np.linalg.inv(A), A - F.T) + G
#Цветной график
plt.imshow(G, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.show()

print(G)
# Выводим результат
print("Результат:")
print(result)
