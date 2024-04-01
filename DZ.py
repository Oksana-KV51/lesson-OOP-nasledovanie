#Разработай систему управления учетными записями пользователей для небольшой компании. Компания
# разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный
# идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют
# дополнительный уровень доступа и могут добавлять или удалять пользователя из системы. Требования:

#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).

#2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня
# доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).


class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.__users_list = []

    def add_user(self, user):
        if user not in self.__users_list:
            self.__users_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен успешно")
        else:
            print("User already exists.")

    def remove_user(self, user):
        if user in self.__users_list:
            self.__users_list.remove(user)
            print(f"Пользователь {user.get_name()} переименован успешно.")
        else:
            print("Пользователь не найден")

    def list_users(self):
        for user in self.__users_list:
            print(user)


# Пример использования
admin = Admin('001', 'Иванов')

user1 = User('002', 'Вера')
user2 = User('003', 'Вася')

admin.add_user(user1)
admin.add_user(user2)

admin.list_users()

admin.remove_user(user1)
admin.list_users()

