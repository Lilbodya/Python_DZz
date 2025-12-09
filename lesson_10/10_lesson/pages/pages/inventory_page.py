import allure
from selenium.webdriver.common.by import By

class InventoryPage:
    """
    Страница каталога товаров (Inventory Page) для добавления товаров в корзину и перехода в корзину.

    Атрибуты:
        driver: Selenium WebDriver.
    """

    def __init__(self, driver):
        """
        Инициализация страницы InventoryPage.

        Входные значения:
            driver: экземпляр Selenium WebDriver.

        Выходные значения:
            None
        """
        self.driver = driver

    @allure.step("Добавляем рюкзак в корзину")
    def add_backpack(self):
        """
        Клик по кнопке добавления рюкзака в корзину.

        Входные значения:
            None

        Выходные значения:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    @allure.step("Добавляем футболку в корзину")
    def add_tshirt(self):
        """
        Клик по кнопке добавления футболки в корзину.

        Входные значения:
            None

        Выходные значения:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    @allure.step("Добавляем комбинезон в корзину")
    def add_onesie(self):
        """
        Клик по кнопке добавления комбинезона в корзину.

        Входные значения:
            None

        Выходные значения:
            None
        """
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self):
        """
        Клик по кнопке перехода в корзину.

        Входные значения:
            None

        Выходные значения:
            None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
