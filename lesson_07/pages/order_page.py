from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    FIRST_NAME_INPUT_SELECTOR = (By.ID, "first-name")
    LAST_NAME_INPUT_SELECTOR = (By.ID, "last-name")
    POSTAL_CODE_INPUT_SELECTOR = (By.ID, "postal-code")
    CONTINUE_BUTTON_SELECTOR = (By.ID, "continue")
    SUMMARY_SELECTOR = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        first_name_input = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT_SELECTOR))
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(
            *self.LAST_NAME_INPUT_SELECTOR)
        last_name_input.send_keys(last_name)

        postal_code_input = self.driver.find_element(
            *self.POSTAL_CODE_INPUT_SELECTOR)
        postal_code_input.send_keys(postal_code)

        continue_button = self.wait.until(EC.element_to_be_clickable(
            self.CONTINUE_BUTTON_SELECTOR))
        continue_button.click()

    def read_summary(self):
        summary_total = self.wait.until(EC.visibility_of_element_located(
                self.SUMMARY_SELECTOR))
        return summary_total.text
