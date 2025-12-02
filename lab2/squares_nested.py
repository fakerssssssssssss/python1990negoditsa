# squares_nested.py
# Упражнение 5: 10 вложенных квадратов

import turtle

turtle.shape('turtle')

side = 20      # начальная длина стороны
step = 10      # насколько увеличивать каждый новый квадрат

for i in range(10):
    # рисуем квадрат
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

    # смещаемся назад и вниз, чтобы следующий квадрат был "вокруг" предыдущего
    turtle.penup()
    turtle.backward(step / 2)
    turtle.right(90)
    turtle.backward(step / 2)
    turtle.left(90)
    turtle.pendown()

    side += step  # увеличиваем размер квадрата

turtle.done()
