from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_firstname(self, firstname):
        self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME)).send_keys(firstname)

    def fill_lastname(self, lastname):
        self.wait.until(EC.element_to_be_clickable(self.LASTNAME)).send_keys(lastname)

    def fill_zip(self, zipcode):
        self.wait.until(EC.element_to_be_clickable(self.ZIP)).send_keys(zipcode)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self):
        total_text = self.driver.find_element(*self.TOTAL).text
        return total_text.replace("Total: $", "")
