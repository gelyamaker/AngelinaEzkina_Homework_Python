import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalcPage:
    DELAY = (By.CSS_SELECTOR, "#delay")
    RESULT_TEXT = (By.CLASS_NAME, "screen")

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса CalcPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

    def fill_delay(self, delay: int):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        """
        with allure.step(f"Установка задержки {delay} секунд"):
            delay_input = self.driver.find_element(*self.DELAY)
            delay_input.clear()
            delay_input.send_keys(str(delay))

    def calc_buttons(self, *buttons: str):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        :param buttons: tuple[str] — кортеж текстов на кнопках,
        которые нужно нажать.
        """
        with allure.step(f"Нажатие кнопок {buttons}"):
            for btn in buttons:
                with allure.step(f"Нажатие кнопки '{btn}'"):
                    self.driver.find_element(
                        By.XPATH, f"//span[text()='{btn}']").click()

    def output_result(self, result: str, delay: int) -> str:
        """
        Ожидает появления ожидаемого результата на экране калькулятора
        и возвращает текущий результат с экрана калькулятора.

        :param result: str — ожидаемый результат.
        :param delay: int — время задержки в секундах.

        :return: str — текст результата на экране калькулятора.
        """
        with allure.step(f"Ожидание результата вычисления '{result}' "
                         f"в течение {delay} секунд"):
            WebDriverWait(self.driver, delay+1).until(
                EC.text_to_be_present_in_element(self.RESULT_TEXT, result))
        with allure.step("Получение результата вычисления"):
            return self.driver.find_element(*self.RESULT_TEXT).text
