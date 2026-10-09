from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginShopPage:
    USERNAME_INPUT_SELECTOR = (By.ID, "user-name")
    PASSWORD_INPUT_SELECTOR = (By.ID, "password")
    LOGIN_BUTTON_SELECTOR = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        user_name_input = self.wait.until(
            EC.element_to_be_clickable(self.USERNAME_INPUT_SELECTOR
                                       ))
        user_name_input.send_keys(username)

        password_input = self.driver.find_element(
            *self.PASSWORD_INPUT_SELECTOR)
        password_input.send_keys(password)

        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON_SELECTOR
                                       ))
        login_button.click()
