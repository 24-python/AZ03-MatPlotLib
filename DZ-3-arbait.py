import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('divan.csv')

print(f"Средняя цена - {data['Price'].mean()}")

prices = data['Price']

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Опционально: задаём размер графика
plt.hist(prices, bins=50, edgecolor='black')  # bins определяет количество столбцов в гистограмме
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Отображение графика
plt.show()
