from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    # Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    # Авторизуйтесь как пользователь standard_user.
    user_name_input = wait.until(
        EC.element_to_be_clickable((By.ID, "user-name")
                                   ))
    user_name_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button")
                                   ))
    login_button.click()

    # Добавьте в корзину товар: Sauce Labs Backpack.
    backpack_button = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")
                                   ))
    backpack_button.click()

    # Добавьте в корзину товар: Sauce Labs Bolt T-Shirt.
    t_shirt_button = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    t_shirt_button.click()

    # Добавьте в корзину товар: Sauce Labs Onesie.
    onesie_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie_button.click()

    # Перейдите в корзину.
    shopping_cart_link = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")
                                   ))
    shopping_cart_link.click()

    # Нажмите Checkout.
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout")
                                   ))
    checkout_button.click()

    # Заполните форму своими данными: имя,
    first_name_input = wait.until(
        EC.element_to_be_clickable((By.ID, "first-name")
                                   ))
    first_name_input.send_keys("Ангелина")

    # Заполните форму своими данными: фамилия,
    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Езкина")

    # Заполните форму своими данными: почтовый индекс.
    postal_code_input = driver.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("129594")

    # Нажмите кнопку Continue.
    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "continue")
                                   ))
    continue_button.click()

    # Прочитайте со страницы итоговую стоимость (Total).
    summary_total = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        ))
    summary_total_label = summary_total.text

    # Закройте браузер.
    driver.quit()

    # Проверьте, что итоговая сумма равна $58.29.
    assert "$58.29" in summary_total_label, "Итоговая сумма не равна $58.29"
