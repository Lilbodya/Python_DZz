import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Страница логина (Login Page) для авторизации пользователя на сайте SauceDemo.

    Атрибуты:
        driver: Selenium WebDriver.
        wait: WebDriverWait для ожидания элементов на странице.
    """

    def __init__(self, driver):
        """
        Инициализация страницы LoginPage.

        Входные значения:
            driver: экземпляр Selenium WebDriver.

        Выходные значения:
            None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы элементов
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Открываем страницу логина")
    def open(self):
        """
        Переход на страницу логина.

        Входные значения:
            None

        Выходные значения:
            None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Вводим имя пользователя: {username}")
    def enter_username(self, username: str):
        """
        Ввод имени пользователя в поле логина.

        Входные значения:
            username (str): имя пользователя.

        Выходные значения:
            None
        """
        self.wait.until(EC.element_to_be_clickable(self.USERNAME)).send_keys(username)

    @allure.step("Вводим пароль: {password}")
    def enter_password(self, password: str):
        """
        Ввод пароля пользователя.

        Входные значения:
            password (str): пароль пользователя.

        Выходные значения:
            None
        """
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD)).send_keys(password)

    @allure.step("Нажимаем кнопку Login")
    def click_login(self):
        """
        Клик по кнопке входа на сайт.

        Входные значения:
            None

        Выходные значения:
            None
        """
        self.driver.find_element(*self.LOGIN_BUTTON).click()
