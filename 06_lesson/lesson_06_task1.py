from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_ajax():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
        )

    driver.get("http://uitestingplayground.com/ajax")

    driver.find_element(By.ID, "ajaxButton").click()

    wait = WebDriverWait(driver, 25)
    green_box = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    print("Текст плашки:", green_box.text)

    driver.quit()


if __name__ == "__main__":
    test_ajax()
