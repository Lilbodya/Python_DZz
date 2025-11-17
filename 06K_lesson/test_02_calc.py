import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = driver.find_element(By.ID, 'delay')
    delay.clear()
    delay.send_keys('45')

    driver.find_element(By.XPATH, "//span[contains(text(), '7')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(), '+')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(), '8')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(), '=')]").click()

    waiter = WebDriverWait(driver, 50)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), "15")
    )

    number_15 = driver.find_element(By.CSS_SELECTOR, '.screen').text
    assert number_15 == "15"
