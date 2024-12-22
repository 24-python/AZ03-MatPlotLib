from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Инициализация драйвера
driver = webdriver.Firefox()

url = "https://www.divan.ru/krasnoyarsk/category/divany-i-kresla"

# Открытие страницы
driver.get(url)

# Подождем, чтобы страница полностью загрузилась
time.sleep(5)  # Время ожидания может быть скорректировано

# Получение цен
prices = driver.find_elements(By.CLASS_NAME, 'price__main-value')

# Создание и открытие CSV файла для записи
with open('divan.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Запись заголовка

    # Запись цен в файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()