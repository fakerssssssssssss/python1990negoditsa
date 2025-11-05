Запишите выражение, заданное формулой, в виде, подходящем для языка Python. И найдите его значения в точках 1, 10, 1000.



формула
y = x² - x - 6


Решение task1.py


import numpy as np

# Алгебраическое выражение: y = x^2 - x - 6 Т
def calculate_y(x):
    return x**2 - x - 6

# Точки для вычисления А
points = [1, 10, 1000]

# Вычисление и вывод Д
for x in points:
    y = calculate_y(x)
    print(f"Для x = {x}, y = {y}")
	
	
библиотеки matplotlib
$ pip install matplotlib

	
