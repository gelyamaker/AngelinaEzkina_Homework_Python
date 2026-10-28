from sqlalchemy import create_engine, text
import random


class StudentTable:
    __scripts = {
        "select": text("select * from student"),
        "delete_by_id": text("delete from student "
                             "where \"user_id\" = :id_to_delete"),
        "insert_new": text("insert into student(\"user_id\", \"level\", "
                           "\"education_form\", \"subject_id\") "
                           "values (:new_user_id, :new_level, :new_form, "
                           ":new_subject_id)"),
        "update_by_id": text("update student set \"subject_id\" = :subj "
                             "where \"user_id\" = :id_to_update"),
        "select_by_id": text("select * from student "
                             "where \"user_id\" = :select_id"),
        "get_max_id": text("select max(\"user_id\") from users"),
        "users_not_students": text("select u.user_id, u.subject_id "
                                   "from users as u "
                                   "left join student as s "
                                   "on u.user_id = s.user_id "
                                   "where s.user_id is null"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_students(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    """
    Получает случайный id и предмет пользователя, не являющегося студентом.
    Если все пользователи - студенты, id - 'макс. id + 1', предмет случайный.
    Если пользователей нет, то id равен 1, предмет - случайный.
    """
    def get_random_user_not_student(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["users_not_students"])
        rows = result.mappings().all()
        conn.close()
        users = []
        for user in rows:
            users.append((user["user_id"], user["subject_id"]))

        if users:
            user = random.choice(users)
            return user[0], user[1]
        else:
            conn = self.__db.connect()
            result = conn.execute(self.__scripts["get_max_id"])
            max_id = result.scalar()
            conn.close()
            if max_id is not None:
                return max_id + 1, random.randint(1, 15)
            else:
                return 1, random.randint(1, 15)

    def delete(self, delete_id):
        conn = self.__db.connect()

        conn.execute(self.__scripts["delete_by_id"],
                     {"id_to_delete": delete_id})

        conn.commit()
        conn.close()

    def create(self, user_id=None, level=None, education_form=None,
               subject_id=None):
        conn = self.__db.connect()

        conn.execute(self.__scripts["insert_new"],
                     {
                         "new_user_id": user_id,
                         "new_level": level,
                         "new_form": education_form,
                         "new_subject_id": subject_id
                         })

        conn.commit()
        conn.close()

    def update_subject(self, user_id, subject_id):
        conn = self.__db.connect()

        conn.execute(self.__scripts["update_by_id"],
                     {"id_to_update": user_id, "subj": subject_id})

        conn.commit()
        conn.close()

    def get_student_by_id(self, update_id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_by_id"],
                              {"select_id": update_id})
        rows = result.mappings().all()
        conn.close()
        return rows
