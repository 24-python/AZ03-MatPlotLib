import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Инициализация браузера
driver = webdriver.Chrome()

try:
    url = 'https://www.divan.ru/category/divany-i-kresla'
    driver.get(url)

    # Явное ожидание загрузки карточек
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
    )

    # Поиск всех карточек на странице
    elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
    prices: list[int] = []

    for element in elements:
        try:
            price = element.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content')
            price_text = price.replace('₽', '').replace(' ', '')  # Убираем символы и пробелы
            if price_text.isdigit():  # Проверка, что цена корректная
                prices.append(int(price_text))
        except Exception:
            print("Ошибка при обработке элемента.")

finally:
    # Закрываем драйвер
    driver.quit()

# Создание и открытие CSV файла для записи
with open('divan.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Запись заголовка

    # Запись цен в файл
    for price in prices:
        writer.writerow([price])

print("Данные успешно записаны в divan.csv")


