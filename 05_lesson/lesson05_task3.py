from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main() -> None:

    driver = webdriver.Firefox()

    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("Sky")
    time.sleep(1)

    input_field.clear()
    time.sleep(1)

    input_field.send_keys("Pro")

    time.sleep(2)

    driver.quit()


if __name__ == "__main__":
    main()
