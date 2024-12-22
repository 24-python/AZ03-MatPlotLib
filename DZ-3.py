from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import csv

driver = webdriver.Firefox()

driver.get('https://www.divan.ru/krasnoyarsk/category/divany-i-kresla')

time.sleep(10)

prices = driver.find_elements(By.XPATH, "//span[@class='ui-LD-ZU KIkOH']")


for price in prices:
    print(price.text)

# Создание и открытие CSV файла для записи
with open('divan.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Запись заголовка

    # Запись цен в файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()