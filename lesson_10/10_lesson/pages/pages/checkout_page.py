import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    """
    Страница оформления заказа (Checkout Page) для заполнения данных пользователя и получения общей суммы заказа.

    Атрибуты:
        driver: Selenium WebDriver.
        wait: WebDriverWait для ожидания элементов на странице.
    """

    def __init__(self, driver):
        """
        Инициализация страницы CheckoutPage.

        Входные значения:
            driver: экземпляр Selenium WebDriver.

        Выходные значения:
            None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы элементов
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполняем имя: {firstname}")
    def fill_firstname(self, firstname: str):
        """
        Ввод имени пользователя.

        Входные значения:
            firstname (str): Имя пользователя.

        Выходные значения:
            None
        """
        self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME)).send_keys(firstname)

    @allure.step("Заполняем фамилию: {lastname}")
    def fill_lastname(self, lastname: str):
        """
        Ввод фамилии пользователя.

        Входные значения:
            lastname (str): Фамилия пользователя.

        Выходные значения:
            None
        """
        self.wait.until(EC.element_to_be_clickable(self.LASTNAME)).send_keys(lastname)

    @allure.step("Заполняем почтовый индекс: {zipcode}")
    def fill_zip(self, zipcode: str):
        """
        Ввод почтового индекса пользователя.

        Входные значения:
            zipcode (str): Почтовый индекс.

        Выходные значения:
            None
        """
        self.wait.until(EC.element_to_be_clickable(self.ZIP)).send_keys(zipcode)

    @allure.step("Нажимаем кнопку Continue")
    def click_continue(self):
        """
        Клик по кнопке Continue для перехода к следующему шагу оформления заказа.

        Входные значения:
            None

        Выходные значения:
            None
        """
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    @allure.step("Получаем общую сумму заказа")
    def get_total(self) -> str:
        """
        Получение общей суммы заказа.

        Входные значения:
            None

        Выходные значения:
            total (str): Сумма заказа без текста и символа '$', например "58.29"
        """
        total_text = self.driver.find_element(*self.TOTAL).text  # "Total: $58.29"
        return total_text.replace("Total: $", "")
