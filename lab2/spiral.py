import turtle

turtle.shape('turtle')

length = 5   # начальная длина шага
step = 2     # насколько увеличиваем шаг каждый раз
angle = 20   # угол поворота

for _ in range(100):
    turtle.forward(length)
    turtle.left(angle)
    length += step

turtle.done()
