from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# # Настройка опций браузера
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# Инициализация драйвера
driver = webdriver.Firefox()

url = "https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/"

# Открытие страницы
driver.get(url)

# Подождем, чтобы страница полностью загрузилась
time.sleep(5)  # Время ожидания может быть скорректировано

# Получение цен
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Создание и открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Запись заголовка

    # Запись цен в файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()