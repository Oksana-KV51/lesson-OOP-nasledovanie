#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).

#2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня
# доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = 'user'
    def get_user_id(self):
        return self._user_id
    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'admin'
    def add_user(self, usser_list, user):
        usser_list.append(user)
        print(f'пользователь успешно добавлен')
        print(usser_list)
    def remove_user(self, usser_list, user):
        usser_list.remove(user)
        print(usser_list)

#применение
users = []
admin = Admin('a1', 'Петя')
user1 = User('a2', 'Вася')

print(user1.get_name())
admin.add_user(users, user1)
