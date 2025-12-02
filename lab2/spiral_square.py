import turtle

turtle.shape('turtle')

length = 10  # начальная длина
step = 5     # увеличение длины каждый раз
angle = 90   # прямой угол

for _ in range(50):
    turtle.forward(length)
    turtle.left(angle)
    length += step

turtle.done()
