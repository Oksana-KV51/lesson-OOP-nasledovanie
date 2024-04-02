#Дополнительно: Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import json
class Serializable:
    def to_dict(self):
        return self.__dict__

def animal_decoder(obj):
    if "Animal_type" in obj:
        if obj["Animal_type"] == "Bird":
            return Bird(obj['name'], obj['age'])
        elif obj["Animal_type"] == "Mammal":
            return Mammal(obj['name'], obj['age'])
        elif obj["Animal_type"] == "Reptile":
            return Reptile(obj['name'], obj['age'])
    return obj


class Animal(Serializable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} едят")


class Bird(Animal):
    def make_sound(self):
        print(f'{self.name} чирикает')


class Mammal(Animal):
    def make_sound(self):
        print(f'{self.name} рычит')


class Reptile(Animal):
    def make_sound(self):
        print(f'{self.name} шипит')


class Zoo(Serializable):
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        self.save_data()  # Save data whenever you add an animal

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        self.save_data()  # Save data whenever you add a staff member

    # Method to serialize zoo data to a JSON file
    def save_data(self):
        with open('zoo_data.json', 'w', encoding='utf-8') as f:
            data = {
                "animals": [animal.to_dict() for animal in self.animals],
                # Assuming staff can also be serialized in a similar manner
            }
            json.dump(data, f, indent=4)

    # Method to load zoo data from a JSON file
    @classmethod
    def load_data(cls):
        try:
            with open('zoo_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f, object_hook=animal_decoder)
                zoo = cls()
                zoo.animals = data.get("animals", [])
                # Assuming staff can also be loaded in a similar manner
                return zoo
        except FileNotFoundError:
            return cls()


class ZooStaff(Serializable):
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
zoo.add_animal(bird)
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