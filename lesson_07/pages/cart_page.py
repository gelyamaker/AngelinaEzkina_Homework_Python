from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CHECKOUT_BUTTON_SELECTOR = (By.ID, "checkout")
    INVENTORY_ITEM_NAME_SELECTOR = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_cart(self):
        inventory_items = self.driver.find_elements(
            *self.INVENTORY_ITEM_NAME_SELECTOR)
        return [item.text for item in inventory_items]

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(
            self.CHECKOUT_BUTTON_SELECTOR)).click()
