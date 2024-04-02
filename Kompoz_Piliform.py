#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и
# методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает
# метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например,
# `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

#Дополнительно: Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        print(f"{self.name} едят")

class Bird(Animal):#птицы
    def make_sound(self):
        print(f'{self.name} чирикает')


class Mammal(Animal): #млекопетающие
    def make_sound(self):
        print(f'{self.name} рычит')


class Reptile(Animal): #рептилии
    def make_sound(self):
        print(f'{self.name} шипит')

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

class ZooStaff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(ZooStaff):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(ZooStaff):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

class Cleaner(ZooStaff):
    def clean_animal(self, animal):
        print(f"{self.name} убирает в клетке {animal.name}.")

# Пример использования
bird = Bird("Попугай", 3)
mammal = Mammal("Лев", 5)
reptile = Reptile("Змея", 2)

animals = [bird, mammal, reptile]
for animal in animals:
    animal.make_sound()

zoo = Zoo()
zoo.add_animal(Bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

keeper = ZooKeeper("Иванов")
vet = Veterinarian("Петров")
cleaner = Cleaner("Сидоров")

zoo.add_staff(keeper)
zoo.add_staff(vet)
zoo.add_staff(cleaner)

keeper.feed_animal(bird)
vet.heal_animal(mammal)
cleaner.clean_animal(reptile)
