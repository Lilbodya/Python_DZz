from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

EDGE_DRIVER_PATH = r"C:\
    Users\BeGraphics\Desktop\driver chrome\msedgedriver.exe"


def test_shadow_dom_in_iframe():
    service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()

    try:
        driver.get(
            "https://bonigarcia.dev"
            "/selenium-webdriver-java/slow-calculator.html"
            )

        wait = WebDriverWait(driver, 60)  # увеличил таймаут

        # --- Ждём полной загрузки страницы ---
        wait.until(lambda d: d.execute_script(
            "return document.readyState === 'complete'"))

        # --- Пробуем найти iframe (если он есть) ---
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        if iframes:
            print(f"🧩 Найден iframe: {len(iframes)}")
            driver.switch_to.frame(iframes[0])
        else:
            print("⚠️ iframe не найден, работаем в основном документе")

        # --- Проверяем, что slow-calculator появился ---
        shadow_host = wait.until(
            lambda d: d.execute_script(
                "return document.querySelector('slow-calculator')")
        )
        shadow_root = driver.execute_script(
            "return arguments[0].shadowRoot", shadow_host)

        # --- Устанавливаем задержку ---
        delay_input = driver.execute_script(
            "return arguments[0].querySelector('#delay')", shadow_root)
        driver.execute_script("""
            arguments[0].value = '2';
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        """, delay_input)

        # --- Кликаем кнопки ---
        for val in ['7', '+', '8', '=']:
            print(f"🖱️ Кликаем {val}")
            driver.execute_script("""
                const root = arguments[0];
                const btn = root.querySelector(
                                  `button[value='${arguments[1]}']`);
                if (btn) btn.click();
            """, shadow_root, val)

        # --- Ждём результата ---
        wait.until(lambda d: d.execute_script(
            "return "
            "arguments[0].querySelector"
            "('#result').textContent.trim() === '15'",
            shadow_root
        ))

        result = driver.execute_script(
            "return arguments[0].querySelector('#result').textContent.trim()",
            shadow_root
        )

        print("✅ Результат:", result)
        assert result == "15", f"Ожидался 15, а получили {result}"

    finally:
        driver.quit()
