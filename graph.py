import numpy as np
import matplotlib.pyplot as plt

# Диапазон x: от -5 до +5 (чтобы увидеть корни)
x = np.arange(-5, 5.1, 0.01)

# Функция: y = x² - x - 6
y = x**2 - x - 6

# График
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='y = x² - x - 6')

# Ось X (y=0) — чтобы видеть корни
plt.axhline(0, color='black', linewidth=1)

# Оформление
plt.title('График функции y = x² - x - 6', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.grid(True)
plt.legend()

# Показать
plt.show()

