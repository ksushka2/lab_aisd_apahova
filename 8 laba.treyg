#Задание на л.р. №8 ООП 24
#Требуется написать объектно-ориентированную программу с графическим интерфейсом в соответствии со своим вариантом.
#В программе должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
#Ввод данных из файла с контролем правильности ввода.
#Базы данных использовать нельзя. При необходимости сохранять информацию в виде файлов, разделяя значения запятыми или пробелами.
#Для GUI использовать библиотеку tkinter.
#Вариант 2
#Объекты – треугольники
#Функции:  проверка пересечения
#визуализация
#раскраска
#перемещение на плоскости

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

def turn(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
def intersect(A, B, C, D):
    return turn(A, C, D) != turn(B, C, D) and turn(A, B, C) != turn(A, B, D)
class Triangle:
    def __init__(self, canvas, dots, color):
        self.dots = dots
        self.color = color
        self.canvas = canvas
        self.triangle_id = self.draw()

    def get_bounding_box(self):
        x_coords, y_coords = zip(*self.dots)
        return (min(x_coords), min(y_coords), max(x_coords), max(y_coords))

    def intersects_with(self, other_triangle):
        for i in range(3):
            for j in range(3):
                A, B = self.dots[i], self.dots[(i + 1) % 3]
                C, D = other_triangle.dots[j], other_triangle.dots[(j + 1) % 3]
                if intersect(A, B, C, D):
                    return True
        return False
    def draw(self):
        return self.canvas.create_polygon(self.dots, fill=self.color, outline='black')

    def move(self, dx, dy):
        self.canvas.move(self.triangle_id, dx, dy)
        self.dots = [(x + dx, y + dy) for x, y in self.dots]

    def change_color(self, color):
        self.color = color
        self.canvas.itemconfig(self.triangle_id, fill = color)

    def on_double_click(self, event):
        chosen_color = colorchooser.askcolor(title="Выберите цвет")[1]
        if chosen_color:
            self.change_color(chosen_color)

    def bind_events(self):
        self.canvas.tag_bind(self.triangle_id,'<B1-Motion>', self.on_drag)
        self.canvas.tag_bind(self.triangle_id, '<Double-1>', self.on_double_click)

    def on_drag(self, event):
        dx = event.x - self.canvas.coords(self.triangle_id)[0]
        dy = event.y - self.canvas.coords(self.triangle_id)[1]
        self.move(dx, dy)

class Start:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Треугольники")
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()
        self.triangles = []
        self.file_path = None
        self.current_pos = 0

        load_triangles_button = tk.Button(text="Загрузить треугольники", command=self.selected_triangle_file)
        load_triangles_button.pack(side=tk.LEFT)

        add_triangle_button = tk.Button(text="Добавить треугольник",
                                        command=lambda: self.add_triangle(self.canvas, self.triangles))
        add_triangle_button.pack(side=tk.LEFT)


        check_intersections_button = tk.Button(text="Проверить пересечения", command=self.check_intersections)
        check_intersections_button.pack(side=tk.LEFT)


    def check_intersections(self):
        for i, triangle_1 in enumerate(self.triangles):
            for triangle_2 in self.triangles[i + 1:]:
                if triangle_1.intersects_with(triangle_2):
                    triangle_1.change_color('grey')
                    triangle_2.change_color('grey')
                    messagebox.showinfo("Пересечение", "Обнаружено пересечение треугольников!")
                    return
        messagebox.showinfo("Пересечение", "Пересечений не обнаружено.")
    def mainloop(self):
        self.root.mainloop()

    def selected_triangle_file(self):
        self.file_path = filedialog.askopenfilename(title="Выберите файл с координатами треугольника")
        if not self.file_path:
            messagebox.showerror("Ошибка", "Файл не выбран")
            return False
        return True

    def read_triangle_dots(self):
        if not self.file_path:
            messagebox.showerror("Ошибка", "Файл не был выбран.")
            return None
        try:
            with open(self.file_path, 'r') as file:
                for _ in range(self.current_pos * 3):
                    next(file)
                vertices = [tuple(map(float, file.readline().strip().split(','))) for _ in range(3)]
            if len(vertices) != 3 or not all(vertices):
                messagebox.showerror("Ошибка", "Недостаточно данных для формирования треугольника.")
                return None
            self.current_pos += 1
            return vertices
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при чтении файла: {e}")
            return None


    def add_triangle(self, canvas, triangles):
        dots = self.read_triangle_dots()
        if dots:
            color = 'grey'
            triangle = Triangle(canvas, dots, color)
            triangle.bind_events()
            triangles.append(triangle)

if __name__ == "__main__":
    start = Start()
    start.mainloop()

