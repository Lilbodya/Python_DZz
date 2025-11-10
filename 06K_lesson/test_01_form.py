import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    edge_driver_path = r"C:\Users\BeGraphics\
        Desktop\driver chrome\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    """Тест формы: Zip code красный, остальные поля зелёные"""
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(lambda d: any(
        "is-valid" in el.get_attribute(
            "class") or "is-invalid" in el.get_attribute("class")
        for el in d.find_elements(By.CSS_SELECTOR, "input")
    ))

    zip_code = driver.find_element(By.NAME, "zip-code")
    assert "is-invalid" in zip_code.get_attribute(
        "class"), "Zip code должен быть красным"

    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_name in valid_fields:
        field = driver.find_element(By.NAME, field_name)
        assert "is-valid" in field.get_attribute(
            "class"), f"Поле {field_name} должно быть зелёным"

    print("✅ Тест пройден: Zip code красный, остальные зелёные")
    input("Нажмите Enter, чтобы закрыть браузер...")
