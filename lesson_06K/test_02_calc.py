from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    # Откройте страницу в Google Chrome.
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 45)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # В поле ввода по локатору #delay введите значение 45.
    delay_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay")
                                   ))
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажмите на кнопку: 7
    seven_btn = driver.find_element(By.XPATH, "//span[text()='7']")
    seven_btn.click()

    # Нажмите на кнопку: +
    plus_btn = driver.find_element(By.XPATH, "//span[text()='+']")
    plus_btn.click()

    # Нажмите на кнопку: 8
    eight_btn = driver.find_element(By.XPATH, "//span[text()='8']")
    eight_btn.click()

    # Нажмите на кнопку: =
    equal_btn = driver.find_element(By.XPATH, "//span[text()='=']")
    equal_btn.click()

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    result = wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"
                                         ))
    assert result, "результат 15 не отобразился через 45 секунд"

    driver.quit()
