import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object для страницы логина на сайте https://www.saucedemo.com/.

    Атрибуты:
        driver (WebDriver): экземпляр WebDriver для работы с браузером.
        wait (WebDriverWait): объект ожидания Selenium (10 секунд).
    """

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        """
        Инициализация класса LoginPage.

        Args:
            driver (WebDriver): объект Selenium WebDriver.

        Returns:
            LoginPage: экземпляр класса.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем страницу логина")
    def open(self):
        """
        Открывает страницу https://www.saucedemo.com/.

        Входные данные: нет
        Выходные данные: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Вводим имя пользователя: {username}")
    def enter_username(self, username):
        """
        Вводит имя пользователя в поле логина.

        Args:
            username (str): Имя пользователя.

        Returns:
            None
        """
        element = self.wait.until(EC.element_to_be_clickable(self.USERNAME))
        element.send_keys(username)

    @allure.step("Вводим пароль: {password}")
    def enter_password(self, password):
        """
        Вводит пароль в поле ввода пароля.

        Args:
            password (str): Пароль пользователя.

        Returns:
            None
        """
        element = self.wait.until(EC.element_to_be_clickable(self.PASSWORD))
        element.send_keys(password)

    @allure.step("Нажимаем кнопку логина")
    def click_login(self):
        """
        Нажимает на кнопку логина.

        Входные данные: нет
        Выходные данные: None
        """
        self.driver.find_element(*self.LOGIN_BUTTON).click()
