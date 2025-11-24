from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_textinput():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("http://uitestingplayground.com/textinput")

    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    print(button.text)

    input("Нажмите Enter, чтобы закрыть браузер...")

    driver.quit()


if __name__ == "__main__":
    test_textinput()
