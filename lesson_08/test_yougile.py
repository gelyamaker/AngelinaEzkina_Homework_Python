from yougile_project import YougileProject


base_url = 'https://ru.yougile.com/'

project = YougileProject(base_url)


# Функция хелпер создание проекта (используется во всех тестах, кроме 2)
def helper_create_project(title):
    resp = project.create_project(title)
    project_id = resp.json()["id"]

    # Проверка статус-кода 201
    assert resp.status_code == 201
    # Проверка наличия проекта (id не пустой)
    assert len(project_id) > 0

    return project_id


# Функция хелпер удаление проекта (используется во всех тестах, кроме 2 и 6)
def helper_delete_project(project_id, title):
    # Изменить значение ключа "deleted" на true
    resp = project.update_project(project_id, title, True)

    # Проверка статус-кода 200
    assert resp.status_code == 200

    # Получить проект по ID
    resp = project.get_project_by_id(project_id)
    body = resp.json()

    # Проверка удаления проекта
    assert body["deleted"] is True


# 1. Создание проекта без опциональных полей
def test_create_project():

    # Создать проект с заголовком "Создать проект"
    title = "Создать проект"
    project_id = helper_create_project(title)

    # Получить проект по ID
    resp = project.get_project_by_id(project_id)
    body = resp.json()

    # Проверка ID и заголовка проекта
    assert body["id"] == project_id
    assert body["title"] == title

    helper_delete_project(project_id, title)


# 2. Создание проекта с пустым заголовком
def test_create_project_with_empty_title():

    # Создать проект с заголовком 123
    title = 123
    resp = project.create_project(title)

    # Проверка статус-кода 400
    assert resp.status_code == 400
    # Проверка текста ошибки
    assert "title must be a string" in resp.text


# 3. Изменение заголовка проекта
def test_update_title_project():
    # Создать проект с заголовком "Удалить проект"
    title = "Измени меня"
    project_id = helper_create_project(title)

    # Изменить заголовок проекта
    new_title = "Проект изменен"
    resp = project.update_project(project_id, new_title)

    # Проверка статус-кода 200
    assert resp.status_code == 200

    # Получить проект по ID
    resp = project.get_project_by_id(project_id)
    body = resp.json()

    # Проверка изменения заголовка проекта
    assert body["title"] == new_title
    assert new_title != title

    helper_delete_project(project_id, new_title)


# 4. Изменение заголовка проекта на пустой
def test_update_empty_title():
    # Создать проект с заголовком "Изменить проект"
    title = "Изменить проект"
    project_id = helper_create_project(title)

    new_title = ''
    resp = project.update_project(project_id, new_title, None)

    # Проверка статус-кода 400
    assert resp.status_code == 400
    # Проверка текста ошибки
    assert "title should not be empty" in resp.text

    helper_delete_project(project_id, title)


# 5. Получение проекта по ID проекта
def test_get_project_by_id():
    # Создать проект с заголовком "Получить проект"
    title = "Получить проект"
    project_id = helper_create_project(title)

    # Получить проект по ID
    resp = project.get_project_by_id(project_id)
    body = resp.json()

    # Проверка статус-кода 200
    assert resp.status_code == 200
    # Проверка ID и заголовка проекта
    assert body["id"] == project_id
    assert body["title"] == title
    # Проверка наличия обязательного поля timestamp
    assert "timestamp" in body

    helper_delete_project(project_id, title)


# 6. Получение проекта с id запроса из пробела
def test_get_project_with_space_id():
    project_id = ' '

    # Получить проект по ID
    resp = project.get_project_by_id(project_id)

    # Проверка статус-кода 404
    assert resp.status_code == 404
    # Проверка текста ошибки
    assert "Проект не найден" in resp.text
