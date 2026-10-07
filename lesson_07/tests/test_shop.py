from selenium import webdriver
from pages.login_shop_page import LoginShopPage
from pages.main_shop_page import MainShopPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage


def test_02_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_shop = LoginShopPage(driver)
    login_shop.open()
    login_shop.login("standard_user", "secret_sauce")

    main_shop = MainShopPage(driver)
    main_shop.add_to_cart("sauce-labs-backpack",
                          "sauce-labs-bolt-t-shirt",
                          "sauce-labs-onesie")
    main_shop.open_cart()

    cart = CartPage(driver)
    assert cart.check_cart("Sauce Labs Backpack",
                           "Sauce Labs Bolt T-Shirt",
                           "Sauce Labs Onesie"), \
        "Список товаров не соответствует заявленному"
    cart.click_checkout()

    order = OrderPage(driver)
    order.fill_form("Ангелина", "Езкина", "129594")
    summary_total_label = order.read_summary()

    driver.quit()

    assert "$58.29" in summary_total_label, "Итоговая сумма не равна $58.29"
