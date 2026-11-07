import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    CHECKOUT_BUTTON_SELECTOR = (By.ID, "checkout")
    INVENTORY_ITEM_NAME_SELECTOR = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса CartPage. Переменная self.wait обозначает явное ожидание.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Получение списка товаров из корзины")
    def check_cart(self) -> list[str]:
        """
        Возвращает содержимое корзины.
        :return: list[str] — список с товарами из корзины.
        """
        inventory_items = self.driver.find_elements(
            *self.INVENTORY_ITEM_NAME_SELECTOR)
        return [item.text for item in inventory_items]

    @allure.step("Нажатие на кнопку 'Checkout'")
    def click_checkout(self):
        """
        Нажимает на кнопку 'Checkout'
        """
        self.wait.until(EC.element_to_be_clickable(
            self.CHECKOUT_BUTTON_SELECTOR)).click()
