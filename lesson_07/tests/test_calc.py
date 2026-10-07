from selenium import webdriver
from pages.calc_page import CalcPage


def test_01_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    calc = CalcPage(driver)

    calc.open()
    calc.fill_delay("45")
    calc.calc_buttons("7", "+", "8", "=")

    assert calc.output_result("15"), \
        "результат 15 не отобразился через 45 секунд"

    driver.quit()
