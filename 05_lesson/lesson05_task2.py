from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main() -> None:

    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--disable-web-security")

    driver = webdriver.Chrome(options=options)

    driver.get("http://uitestingplayground.com/dynamicid")

    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
    )

    button.click()

    time.sleep(2)

    driver.quit()


if __name__ == "__main__":
    main()
