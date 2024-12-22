import pandas as pd
import matplotlib.pyplot as plt

# Загрузите данные из CSV-файла
data = pd.read_csv('processed_prices.csv')

# Предположим, что столбец с ценами называется 'price'
prices = data['Price']

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Опционально: задаём размер графика
plt.hist(prices, bins=30, edgecolor='black')  # bins определяет количество столбцов в гистограмме
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Отображение графика
plt.show()