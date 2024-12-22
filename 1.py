from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# # Путь к вашему драйверу Chrome
# CHROME_DRIVER_PATH = "path/to/chromedriver"
#
# # Настройки Selenium
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Если вы хотите запускать браузер в фоновом режиме
#
# # Инициализация драйвера
# service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Firefox()

try:
    # Открытие сайта
    url = "https://www.divan.ru/krasnoyarsk/category/divany"
    driver.get(url)

    # Небольшая пауза для загрузки страницы
    time.sleep(5)

    # Поиск карточек товаров
    products = driver.find_elements(By.CLASS_NAME, "WdR1o")

    # Парсинг цен
    for product in products:
        try:
            price = product.find_element(By.CLASS_NAME, "pY3d2").text
            name = product.find_element(By.CLASS_NAME, "ui-GPFV8").text
            print(f"Название: {name}, Цена: {price}")
        except Exception as e:
            print(f"Ошибка при обработке карточки: {e}")

finally:
    # Закрытие браузера
    driver.quit()