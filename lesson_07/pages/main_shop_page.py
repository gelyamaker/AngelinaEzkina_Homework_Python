from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    CART_SELECTOR = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, *inventory_items):
        for item in inventory_items:
            self.wait.until(EC.element_to_be_clickable(
                (By.ID, f"add-to-cart-{item}"))).click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(
            self.CART_SELECTOR)).click()
