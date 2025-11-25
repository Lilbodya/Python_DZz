import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

# Путь к geckodriver одной строкой
GECKODRIVER_PATH = r"C:\
    Users\BeGraphics\Desktop\driver firefox\geckodriver.exe"


@pytest.fixture
def driver():
    service = FirefoxService(executable_path=GECKODRIVER_PATH)
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    time.sleep(5)  # Даем посмотреть результат перед закрытием
    driver.quit()


def test_saucedemo_shopping(driver):
    wait = WebDriverWait(driver, 10)

    # Открываем сайт
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(
        "standard_user"
    )
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]
    for product_id in products_to_add:
        wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Заполняем форму
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))
               ).send_keys(
        "Иван"
    )
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Читаем итоговую сумму
    total_text = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text
    total_amount = total_text.split("$")[1]

    # Проверка суммы — разбиваем строку на части, линтеру нравится
    assert total_amount == "58.29", (
        f"Ожидалась сумма $58.29, "
        f"но получили ${total_amount}"
    )

    print("✅ Тест пройден: итоговая сумма равна $58.29")
