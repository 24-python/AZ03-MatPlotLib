from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# # Укажите путь к вашему веб-драйверу
# driver_path = 'path/to/your/chromedriver'
#
# # Инициализация веб-драйвера
# service = Service(executable_path=driver_path)
driver = webdriver.Firefox()

# Открытие страницы
driver.get('https://www.divan.ru/krasnoyarsk/category/divany-i-kresla')

# Даем время странице загрузиться
try:
    # Ожидание, пока элементы с ценами станут видимыми
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//span[contains(@class, 'price__main-value')]"))
    )

    # Найти все элементы с ценами через XPath
    prices = driver.find_elements(By.XPATH, "//span[contains(@class, 'price__main-value')]")

    # Вывести все найденные цены
    for price in prices:
        print(price.text)
except TimeoutException:
    print("Не удалось загрузить элементы с ценами.")
finally:
    # Закрыть браузер
    driver.quit()