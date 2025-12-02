import turtle

turtle.shape('turtle')

n = 12       # количество лап (лучей)
length = 100 # длина каждой лапы

for _ in range(n):
    turtle.forward(length)
    turtle.backward(length)
    turtle.left(360 / n)

turtle.done()
