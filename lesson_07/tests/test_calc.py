import pytest
from selenium import webdriver
from pages.calc_page import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_01_calc(driver):

    calc = CalcPage(driver)

    calc.open()
    calc.fill_delay("45")
    calc.calc_buttons("7", "+", "8", "=")

    assert calc.output_result("15") == "15", "Результат 15 не отобразился"
