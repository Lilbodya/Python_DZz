import pytest
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):

    calc = SlowCalculatorPage(driver)
    calc.open()

    calc.set_delay(45)

    calc.press_button("7")
    calc.press_button("+")
    calc.press_button("8")
    calc.press_button("=")

    calc.wait_for_result("15")
    assert calc.get_result() == "15", "Ожидали результат 15"