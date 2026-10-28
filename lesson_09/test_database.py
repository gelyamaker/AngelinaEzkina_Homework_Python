from student_table import StudentTable
import config

db = StudentTable(config.DB)


def helper_create_student():
    user_id, subject_id = db.get_random_user_not_student()
    level = 'Elementary'
    education_form = 'personal'

    # создать нового студента
    db.create(user_id, level, education_form, subject_id)

    # Получить студента
    row = db.get_student_by_id(user_id)[0]

    return row


def test_insert_student():
    # Получить количество компаний до создания
    body = db.get_students()
    len_before = len(body)

    new_student = helper_create_student()

    # Получить количество студентов после создания
    body = db.get_students()
    len_after = len(body)

    db.delete(new_student["user_id"])

    # Проверить, что +1
    assert len_after - len_before == 1

    found = False
    for student in body:
        if student["user_id"] == new_student["user_id"]:
            found = True
            # Проверить поля студента
            assert student["level"] == new_student["level"]
            assert student["education_form"] == new_student["education_form"]
            assert student["subject_id"] == new_student["subject_id"]
            break
    assert found


def test_update_student():
    new_student = helper_create_student()
    user_id = new_student["user_id"]

    new_subject = 12
    db.update_subject(user_id, new_subject)

    # Получить студента
    row = db.get_student_by_id(user_id)[0]

    db.delete(user_id)

    # Проверить измененное поле студента
    assert row["subject_id"] == new_subject
    assert new_subject != new_student["subject_id"]


def test_delete_student():
    new_student = helper_create_student()
    user_id = new_student["user_id"]

    db.delete(user_id)

    # Проверка того, что студента с таким ID нет
    row = db.get_student_by_id(user_id)
    assert len(row) == 0
