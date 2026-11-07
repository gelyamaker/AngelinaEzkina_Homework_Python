import pytest
import allure
from selenium import webdriver
from pages.calc_page import CalcPage
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity("critical")
@allure.title("Вычисление 7+8=15")
@allure.description("Вычисление результата сложения двух чисел")
def test_01_calc(driver: WebDriver):
    """
    Тест проверяет работу калькулятора с различными операциями.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    calc = CalcPage(driver)

    calc.open()
    delay = 45
    calc.fill_delay(delay)
    calc.calc_buttons("7", "+", "8", "=")

    expected_result = "15"
    actual_result = calc.output_result(expected_result, delay)

    with allure.step("Сравнение полученного результата с ожидаемым"):
        assert actual_result == expected_result, \
            (f"Ожидаемый результат {expected_result}, "
             f"фактический результат: {actual_result}")
