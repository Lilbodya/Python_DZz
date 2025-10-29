from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main() -> None:

    driver = webdriver.Firefox()

    driver.get("http://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))

    username.send_keys("tomsmith")

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("🔹 Кнопка Login нажата.")

    message = wait.until(EC.presence_of_element_located((By.ID, "flash")))

    print("✅ Сообщение на странице:")
    print(message.text.strip())

    time.sleep(2)

    driver.quit()


if __name__ == "__main__":
    main()
