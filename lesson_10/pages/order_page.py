import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class OrderPage:
    FIRST_NAME_INPUT_SELECTOR = (By.ID, "first-name")
    LAST_NAME_INPUT_SELECTOR = (By.ID, "last-name")
    POSTAL_CODE_INPUT_SELECTOR = (By.ID, "postal-code")
    CONTINUE_BUTTON_SELECTOR = (By.ID, "continue")
    SUMMARY_SELECTOR = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса OrderPage. Переменная self.wait обозначает явное ожидание.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ввод полей формы")
    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Вводит поля формы и нажимает кнопку "Continue".

        :param first_name: str — имя покупателя.
        :param last_name: str — фамилия покупателя.
        :param postal_code: str — почтовый индекс покупателя.
        """
        with allure.step(f"Ввод имени покупателя '{first_name}'"):
            first_name_input = self.wait.until(
                EC.element_to_be_clickable(self.FIRST_NAME_INPUT_SELECTOR))
            first_name_input.send_keys(first_name)

        with allure.step(f"Ввод фамилии покупателя '{last_name}'"):
            last_name_input = self.driver.find_element(
                *self.LAST_NAME_INPUT_SELECTOR)
            last_name_input.send_keys(last_name)

        with allure.step(f"Ввод почтового индекса покупателя '{postal_code}'"):
            postal_code_input = self.driver.find_element(
                *self.POSTAL_CODE_INPUT_SELECTOR)
            postal_code_input.send_keys(postal_code)

        with allure.step(f"Нажатие кнопки 'Continue'"):
            continue_button = self.wait.until(EC.element_to_be_clickable(
                self.CONTINUE_BUTTON_SELECTOR))
            continue_button.click()

    @allure.step("Получение суммы покупки")
    def read_summary(self):
        """
        Возвращает сумму покупки.
        :return: str — сумма покупки.
        """
        summary_total = self.wait.until(EC.visibility_of_element_located(
                self.SUMMARY_SELECTOR))
        return summary_total.text
