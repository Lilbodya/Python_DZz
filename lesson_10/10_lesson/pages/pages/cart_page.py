import allure
from selenium.webdriver.common.by import By


@allure.feature("Корзина")
class CartPage:
    """
    Page Object для страницы корзины сайта saucedemo.com.

    Содержит методы:
    - переход к оформлению заказа (Checkout)
    - получение списка товаров, добавленных в корзину
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        """
        Инициализация CartPage.

        Args:
            driver (WebDriver): Экземпляр Selenium WebDriver.
        """
        self.driver = driver

    @allure.title("Переход к оформлению заказа")
    @allure.description("Нажимает кнопку 'Checkout' на странице корзины.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Нажимаем кнопку Checkout")
    def click_checkout(self):
        """
        Кликает по кнопке Checkout.

        Входные данные:
            нет

        Возвращает:
            None
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    @allure.title("Получение списка товаров из корзины")
    @allure.description("Возвращает список названий всех товаров, находящихся в корзине.")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("Получаем список товаров из корзины")
    def get_cart_items(self):
        """
        Возвращает список названий товаров, добавленных в корзину.

        Входные данные:
            нет

        Returns:
            list[str]: список строк — названий товаров.
        """
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]
