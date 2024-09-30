#В филармонии К музыкальных инструментов (музыкантов) Т типов. Сформировать все возможные варианты трио. 
#Усложнение: доп. параметр - стоимость аренды инструментов.
import tkinter as tk
from tkinter import *
from tkinter import ttk
import itertools
import timeit
import random

#ф-я для цены
def generate_rent_price():
    return random.randint(300, 500)
#фильтр по цене
def filter_trios_by_rent(trios, optimal_price):
    trios_optimal = []
    for trio, rent_sum in trios:
        if rent_sum <= optimal_price:
            trios_optimal.append((trio, rent_sum))
    return trios_optimal
#алг. подход
def algoritm():
    
    T = int(entry_T.get())
    K = int(entry_K.get())
    optimal_price = int(entry_optimal_price.get())#cena
    selected_type=int(entry_selected_type.get())#type
    instruments_by_type = [list(range(i, K, T)) for i in range(T)]

    start_time = timeit.timeit()
    valid_trios = []
    for i in instruments_by_type[selected_type-1]:
        sumi = random.randint(300, 500)
        for j in instruments_by_type[selected_type-1]:
            sumj = random.randint(300, 500)
            for k in instruments_by_type[selected_type-1]:
                sumk = random.randint(300, 500)
                sumA=sumi+sumj+sumk
                if i < j < k and sumA <= optimal_price:
                    valid_trios.append((i, j, k, sumA))
    end_time = timeit.timeit()
    
    Alg_time = end_time - start_time

    output_text.delete('1.0', tk.END)  # Очистить текстовое поле перед выводом
    output_text.insert(tk.END, f"Список инструментов по типам :")
    for i, instruments in enumerate(instruments_by_type):
        output_text.insert(tk.END, f"\nТ{i + 1}={instruments}")
    output_text.insert(tk.END, f"\nВсего сформировано {len(valid_trios)} подходящих трио инструментов типа {selected_type}:")
    for trio in valid_trios:
        output_text.insert(tk.END, f"\nТрио: {trio[0], trio[1], trio[2]}, Сумма аренды: {trio[3]}")
    output_text.insert(tk.END, f"\nВремя усложненного подхода с помощью алгоритма: \n{abs(Alg_time)}")

#подход с помощью функций
def with_function():

    T = int(entry_T.get())
    K = int(entry_K.get())
    optimal_price = int(entry_optimal_price.get())#cena
    selected_type=int(entry_selected_type.get())#type

    instruments_by_type = [list(range(i, K, T)) for i in range(T)]
    instruments = instruments_by_type[selected_type-1]

    start_time = timeit.timeit()
    trios = list(itertools.combinations(instruments, 3))
    trios = [(trio, sum([generate_rent_price() for _ in range(3)])) for trio in trios if
             (trio[0] % K != trio[1] % K) and (trio[0] % K != trio[2] % K) and (trio[1] % K != trio[2] % K)]
    trios_optimal = [(trio, rent_sum) for trio, rent_sum in trios if rent_sum <= 3 * optimal_price]
    end_time = timeit.timeit()
    
    Funktime = end_time - start_time
    trios_optimal = filter_trios_by_rent(trios, optimal_price)

    output_text.delete('1.0', tk.END)  # Очистить текстовое поле перед выводом
    output_text.insert(tk.END, f"Список инструментов по типам:")
    for i, instruments in enumerate(instruments_by_type):
        output_text.insert(tk.END, f"\nТ{i + 1}={instruments}")
    output_text.insert(tk.END, f"\nВсего сформировано {len(trios_optimal)} подходящих трио инструментов типа {selected_type}:")
    for trio, rent_sum in trios_optimal:
        output_text.insert(tk.END, f"\nТрио: {trio}, Сумма аренды: {rent_sum}")
    output_text.insert(tk.END, f"\nВремя усложненного подхода с помощью функции: \n{abs(Funktime)}")

#фун-я для запуска
def run():
    approach = approach_var.get()
    if approach == 'algoritm':
        return algoritm()
    elif approach == 'with_function':
        return with_function()

#создание окна
root = tk.Tk()
root.title("Аренда музыкальных инструментов")
root.geometry("420x300+400+200")
# неизменяемый размер окна
root.resizable(False, False)
# количество
tk.Label(root, text="Введите колличество инструментов:").grid(row=0, column=0)
entry_K = tk.Entry(root)
entry_K.grid(row=0, column=1)
#типы
tk.Label(root, text="Введите колличество типов инструментов:").grid(row=1, column=0)
entry_T = tk.Entry(root)
entry_T.grid(row=1, column=1)
#цена
tk.Label(root, text="Введите оптимальную цену аренды:").grid(row=2, column=0)
entry_optimal_price = tk.Entry(root)
entry_optimal_price.grid(row=2, column=1)
#какие инструменты хотим
tk.Label(root, text="Выберете подходящий тип инструментов:").grid(row=3, column=0)
entry_selected_type = tk.Entry(root)
entry_selected_type.grid(row=3, column=1)

# выбор подхода(алгоритмический\функциональный)
approach_var = tk.StringVar(value='algorithmic')
tk.Radiobutton(root, text="Алгоритмический", variable=approach_var, value='algoritm').grid(row=4, column=0)
tk.Radiobutton(root, text="Функциональный", variable=approach_var, value='with_function').grid(row=4, column=1)

# запуск
run_button = tk.Button(root, text="Запустить алгоритм", command=run)
run_button.grid(row=5, column=0, columnspan=2)

# вывод
output_text = tk.Text(root, height=8, width=50)
scroll = ttk.Scrollbar(root, orient="vertical", command= output_text.yview)
output_text.configure(yscrollcommand=scroll.set)
output_text.grid(row=6, column=0, columnspan=2)
scroll.grid(column = 2, row = 6, sticky= NS)

root.mainloop()
