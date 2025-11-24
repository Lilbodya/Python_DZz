import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_saucedemo_order(driver):
    # Страница входа
    login = LoginPage(driver)
    login.open()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    # Страница товаров
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.add_tshirt()
    inventory.add_onesie()
    inventory.go_to_cart()

    # Страница корзины
    cart = CartPage(driver)
    items = cart.get_cart_items()
    cart.click_checkout()

    # Проверяем, что 3 товара действительно попали в корзину
    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Bolt T-Shirt" in items
    assert "Sauce Labs Onesie" in items

    # Страница Checkout
    checkout = CheckoutPage(driver)
    checkout.fill_firstname("Иван")
    checkout.fill_lastname("Петров")
    checkout.fill_zip("123456")
    checkout.click_continue()

    # Получаем итоговую сумму
    total = checkout.get_total()

    # Проверка суммы
    assert total == "58.29", f"Ожидали 58.29, получили {total}"
