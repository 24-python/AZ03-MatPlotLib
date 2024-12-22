import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Опционально: задаём размер графика
plt.hist(data, bins=30, edgecolor='black')  # bins определяет количество столбцов в гистограмме
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')

# Отображение графика
plt.show()