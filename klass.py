#наследование

class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
    def fly(self):
        print(f'{self.name} летает')

    def eat(self):
        print(f'{self.name} кушает')

    def sing(self):
        print(f'{self.name} поет {self.voice}')

    def info(self):
        print(f'{self.name} имя')
        print(f'{self.voice} голос')
        print(f'{self.color} окрас птицы')

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorit_food):
        super().__init__(name, voice, color)
        self.favorit_food = favorit_food

    def wolk(self):
        print(f'{self.name} гуляет')

    def sing(self):
        print(f'{self.name} поет гули гули')

bird1 = Pigeon(name ='Гоша', voice = 'курлык', color = 'серый', favorit_food = 'хлеб')
bird2 = Bird(name = 'Маша', voice = 'чирик', color = 'коричневый')

bird1.sing()
bird1.info()
bird1.wolk()

bird2.sing()