import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginShopPage:
    USERNAME_INPUT_SELECTOR = (By.ID, "user-name")
    PASSWORD_INPUT_SELECTOR = (By.ID, "password")
    LOGIN_BUTTON_SELECTOR = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса LoginShopPage. Переменная self.wait обозначает явное ожидание.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы авторизации магазина")
    def open(self):
        """
        Открывает страницу авторизации магазина.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизациия пользователя")
    def login(self, username: str, password: str):
        """
        Вводит поля авторизации и нажимает кнопку "Login".

        :param username: str — имя пользователя.
        :param password: str — пароль.
        """
        with allure.step(f"Ввод имени пользователя '{username}'"):
            user_name_input = self.wait.until(
                EC.element_to_be_clickable(self.USERNAME_INPUT_SELECTOR))
            user_name_input.send_keys(username)

        with allure.step(f"Ввод пароля '{password}'"):
            password_input = self.driver.find_element(
                *self.PASSWORD_INPUT_SELECTOR)
            password_input.send_keys(password)

        with allure.step(f"Нажатие кнопки 'Login'"):
            login_button = self.wait.until(
                EC.element_to_be_clickable(self.LOGIN_BUTTON_SELECTOR))
            login_button.click()
