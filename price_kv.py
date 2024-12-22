import csv

# Чтение и обработка данных из существующего CSV файла
with open('prices.csv', mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Открытие нового CSV файла для записи обработанных данных
with open('processed_prices.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)

    # Запись заголовка
    writer.writerow(rows[0])  # Предполагается, что первая строка содержит заголовок

    # Обработка каждой строки, начиная со второй (где находятся данные)
    for row in rows[1:]:
        if row:  # Проверка, что строка не пустая
            price_str = row[0].replace('₽/мес.', '').replace(' ', '')  # Удаление символов и пробелов
            try:
                price = int(price_str)  # Преобразование в число
                writer.writerow([price])  # Запись в файл
            except ValueError:
                print(f"Ошибка преобразования значения: {row[0]}")