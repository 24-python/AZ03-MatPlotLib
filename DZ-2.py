import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 5  # Количество точек

x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))  # Опционально: задаём размер графика
plt.scatter(x, y, c='blue', alpha=0.5, edgecolors='w', s=70)  # c - цвет точек, alpha - прозрачность, s - размер точек
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Отображение графика
plt.show()