from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    DELAY_FIELD = (By.ID, "delay")
    RESULT_FIELD = (By.CSS_SELECTOR, "div.screen")
    BUTTON_XPATH_TEMPLATE = "//span[text() = '{}']"


    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.wait.until(EC.presence_of_element_located(self.DELAY_FIELD))

    def set_delay(self, seconds: int):
        delay_el = self.wait.until(EC.element_to_be_clickable(self.DELAY_FIELD))
        delay_el.clear()
        delay_el.send_keys(str(seconds))

    def press_button(self, value: str):
        xpath = self.BUTTON_XPATH_TEMPLATE.format(value)
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn.click()

    def wait_for_result(self, expected_value: str, timeout=None):
        if timeout is None:
            wait = self.wait
        else:
            wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.RESULT_FIELD, expected_value))

    def get_result(self) -> str:
        return self.wait.until(EC.presence_of_element_located(self.RESULT_FIELD)).text
