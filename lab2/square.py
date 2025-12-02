# square.py
# Упражнение 3: квадрат

import turtle

turtle.shape('turtle')

side = 100  # длина стороны квадрата

for _ in range(4):
    turtle.forward(side)
    turtle.left(90)

turtle.done()
