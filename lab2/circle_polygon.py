# circle_polygon.py
# Упражнение 4: окружность через многоугольник

import turtle
import math

turtle.shape('turtle')

n = 60        # количество сторон многоугольника
radius = 100  # радиус "окружности"

side = 2 * math.pi * radius / n  # вычисление длины стороны

for _ in range(n):
    turtle.forward(side)
    turtle.left(360 / n)

