from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    DELAY = (By.CSS_SELECTOR, "#delay")
    RESULT_TEXT = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

    def fill_delay(self, seconds):
        delay_input = self.wait.until(
            EC.element_to_be_clickable(self.DELAY)
                                       )
        delay_input.clear()
        delay_input.send_keys(seconds)

    def calc_buttons(self, *buttons):
        for btn in buttons:
            self.driver.find_element(
                By.XPATH, f"//span[text()='{btn}']").click()

    def output_result(self, result):
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_TEXT, result
                                             ))
        return self.driver.find_element(*self.RESULT_TEXT).text
