import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class MainShopPage:
    CART_SELECTOR = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса MainShopPage. Переменная self.wait обозначает явное ожидание.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, *inventory_items: str):
        """
        Добавляет товары в корзину.

        :param inventory_items: tuple[str] — кортеж товаров,
        которые нужно добавить в корзину.
        """
        with allure.step(f"Добавление товаров {inventory_items}"):
            for item in inventory_items:
                with allure.step(f"Добавление товара {item}"):
                    self.wait.until(EC.element_to_be_clickable(
                        (By.ID, f"add-to-cart-{item}"))).click()

    @allure.step("Открытие корзины товаров")
    def open_cart(self):
        """
        Открывает корзину товаров.
        """
        self.wait.until(EC.element_to_be_clickable(
            self.CART_SELECTOR)).click()
