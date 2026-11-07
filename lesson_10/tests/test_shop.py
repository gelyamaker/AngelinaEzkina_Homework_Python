import pytest
import allure
from selenium import webdriver
from pages.login_shop_page import LoginShopPage
from pages.main_shop_page import MainShopPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Магазин")
@allure.severity("critical")
@allure.title("Заказ товаров авторизованным пользователем")
@allure.description("Проверка работы магазина от пользователя 'standard_user' "
                    "с товарами 'Sauce Labs Backpack', "
                    "'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie' с вводом "
                    "данных формы - имени, фамилии и почтового индекса.")
def test_02_shop(driver: WebDriver):
    """
    Тест проверяет работу магазина от пользователя 'standard_user' с товарами
    'Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie'
    с вводом данных формы - имени, фамилии и почтового индекса.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    login_shop = LoginShopPage(driver)
    login_shop.open()
    login_shop.login("standard_user", "secret_sauce")

    main_shop = MainShopPage(driver)
    main_shop.add_to_cart("sauce-labs-backpack",
                          "sauce-labs-bolt-t-shirt",
                          "sauce-labs-onesie")
    main_shop.open_cart()

    cart = CartPage(driver)
    expected = ["Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"]
    actual = cart.check_cart()
    with (allure.step("Сравнение полученного списка товаров с ожидаемым")):
        assert actual == expected, \
            (f"Ожидаемый результат {expected}, "
             f"фактический результат: {actual}")
    cart.click_checkout()

    order = OrderPage(driver)
    order.fill_form("Ангелина", "Езкина", "129594")
    summary_total_label = order.read_summary()

    with ((allure.step("Сравнение полученной суммы покупки с ожидаемой"))):
        assert "$58.29" in summary_total_label, \
            (f"Итоговая сумма не содержит $58.29, "
             f"фактический результат: {summary_total_label}")
