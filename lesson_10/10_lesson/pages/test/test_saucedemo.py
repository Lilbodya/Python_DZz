import pytest
import allure
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации WebDriver.

    Создаёт экземпляр Firefox, разворачивает окно.
    После выполнения теста — закрывает браузер.

    Returns:
        WebDriver: объект Selenium WebDriver.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий")
@allure.title("Проверка успешного оформления заказа из 3 товаров")
@allure.description("""
Тест полностью проходит путь оформления заказа на сайте saucedemo:
1. Авторизация пользователем standard_user
2. Добавление 3 товаров в корзину
3. Проверка содержимого корзины
4. Заполнение формы Checkout
5. Проверка итоговой суммы заказа

Ожидаемый результат:
- Все 3 товара отображаются в корзине
- Итоговая сумма равна 58.29
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_order(driver):
    """
    Тест оформляет заказ на сайте saucedemo.com и проверяет итоговую сумму.

    Детализированные шаги перечислены в описании через allure.description.
    """

    # -----------------------------
    # 1. Авторизация
    # -----------------------------
    with allure.step("Авторизация на сайте"):
        login = LoginPage(driver)
        login.open()
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

    # -----------------------------
    # 2. Добавление товаров в корзину
    # -----------------------------
    with allure.step("Добавляем товары в корзину"):
        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.add_tshirt()
        inventory.add_onesie()
        inventory.go_to_cart()

    # -----------------------------
    # 3. Проверка товаров в корзине
    # -----------------------------
    with allure.step("Проверяем товары в корзине"):
        cart = CartPage(driver)
        items = cart.get_cart_items()

        assert "Sauce Labs Backpack" in items
        assert "Sauce Labs Bolt T-Shirt" in items
        assert "Sauce Labs Onesie" in items

    # -----------------------------
    # 4. Заполнение данных Checkout
    # -----------------------------
    with allure.step("Заполняем данные покупателя"):
        checkout = CheckoutPage(driver)
        checkout.fill_firstname("Иван")
        checkout.fill_lastname("Петров")
        checkout.fill_zip("123456")
        checkout.click_continue()

    # -----------------------------
    # 5. Проверка итоговой суммы
    # -----------------------------
    with allure.step("Проверяем итоговую сумму заказа"):
        total = checkout.get_total()
        allure.attach(total, "Сумма заказа", allure.attachment_type.TEXT)

        assert total == "58.29", f"Ожидали 58.29, получили {total}"
