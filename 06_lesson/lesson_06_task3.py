import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_loading_images():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

    wait = WebDriverWait(driver, 55)
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "img")) >= 3)

    images = driver.find_elements(By.CSS_SELECTOR, "img")
    WebDriverWait(driver, 55).until(
        lambda d: images[2].get_attribute("naturalWidth") != "0"
        )

    print(images[2].get_attribute("src"))

    start = time.time()
    while time.time() - start < 5:
        pass

    driver.quit()


if __name__ == "__main__":
    test_loading_images()
