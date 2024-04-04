class Engin():
    def start(self):
        print('двигатель завелся')
    def stop(self):
        print('двигатель выключен')

class Car():
    def __init__(self):
        self.engin = Engin()
    def start(self):
        self.engin.start()
    def stop(self):
        self.engin.stop()

my_car = Car()
my_car.start()
my_car.stop()


