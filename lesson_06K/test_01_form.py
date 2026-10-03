from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    # Откройте страницу в браузере Edge.
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Заполните форму значением: First name Иван
    first_name_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "first-name")
                                   ))
    first_name_input.send_keys("Иван")

    # Заполните форму значением: Last name Петров
    last_name_input = driver.find_element(By.NAME, "last-name")
    last_name_input.send_keys("Петров")

    # Заполните форму значением: Address Ленина, 55-3
    address_input = driver.find_element(By.NAME, "address")
    address_input.send_keys("Ленина, 55-3")

    # Заполните форму значением: Email test@skypro.com
    email_input = driver.find_element(By.NAME, "e-mail")
    email_input.send_keys("test@skypro.com")

    # Заполните форму значением: Phone number +7985899998787
    phone_input = driver.find_element(By.NAME, "phone")
    phone_input.send_keys("+7985899998787")

    # Заполните форму значением: City Москва
    city_input = driver.find_element(By.NAME, "city")
    city_input.send_keys("Москва")

    # Заполните форму значением: Country Россия
    country_input = driver.find_element(By.NAME, "country")
    country_input.send_keys("Россия")

    # Заполните форму значением: Job position QA
    job_input = driver.find_element(By.NAME, "job-position")
    job_input.send_keys("QA")

    # Заполните форму значением: Company SkyPro
    company_input = driver.find_element(By.NAME, "company")
    company_input.send_keys("QA")

    # Нажмите кнопку Submit.
    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='submit']")
                                   ))
    submit_button.click()

    # Проверьте (assert), что поле Zip code подсвечено красным.
    zip_alert = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "alert-danger" in zip_alert, "Поле Zip code не подсвечено красным"

    # Проверьте (assert), что остальные поля подсвечены зеленым.
    fields = [
        {
            "id": "first-name",
            "name": "First Name",
        },
        {
            "id": "last-name",
            "name": "Last Name",
        },
        {
            "id": "address",
            "name": "Address",
        },
        {
            "id": "e-mail",
            "name": "Email",
        },
        {
            "id": "phone",
            "name": "Phone number",
        },
        {
            "id": "city",
            "name": "City",
        },
        {
            "id": "country",
            "name": "Country",
        },
        {
            "id": "job-position",
            "name": "Job position",
        },
        {
            "id": "company",
            "name": "Company",
        }
    ]

    for field in fields:
        element = driver.find_element(By.ID, field["id"])
        class_element = element.get_attribute("class")
        assert "alert-success" in class_element, \
            f"Поле {field["name"]} не подсвечено зеленым"

    driver.quit()
