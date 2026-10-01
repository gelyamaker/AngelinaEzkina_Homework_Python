from selenium import webdriver


def test_session_storage_auth():

    # Откройте страницу https://gitflic.ru/.
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "ODk0OWExYjAtZGQyYy00Yjg0LWFkNTQtYWI3ZDdlYmY0YTFi",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/gelyamaker")

    # Сохраните текущий URL.
    url1 = driver.current_url

    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()

    # Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "Njc4Y2VjNTAtNWUzNS00OWRhLTgzMzAtODBjNGM5Y2RkZmMz",
        "domain": "gitflic.ru"
    })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/angelina_ezkina")

    # Сохраните текущий URL.
    url2 = driver.current_url

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url2 != url1, "URL для пользователя 1 и пользователя 2 совпадают"

    driver.quit()
