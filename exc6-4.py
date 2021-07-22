# методы: go, stop, turn(direction) должны сообщать, что машина поехала, остановилась, повернула (куда)
    # классов: TownCar, SportCar, WorkCar, PoliceCar;
    # в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    # Создайте экземпляры классов, передайте значения атрибутов.
    # Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed} км/час')

# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print(f'Вы превысили скорость')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f'Вы превысили скорость')

class PoliceCar(Car):
    pass

town = TownCar(70, 'красный', 'Kia', False)
print(f'\n1. Марка: {town.name}, Цвет: {town.color}, Скорость: {town.speed}, Полиция: {town.is_police}')
town.go(), town.stop(), town.turn("вправо"), town.show_speed()
sport = SportCar(170, 'черный', 'Ferrari', False)
print(f'\n2. Марка: {sport.name}, Цвет: {sport.color}, Скорость: {sport.speed}, Полиция: {sport.is_police}')
sport.go(), sport.stop(), sport.turn("прямо"), sport.show_speed()
work = WorkCar(50, 'желтый', 'GAZ', False)
print(f'\n3. Марка: {work.name}, Цвет: {work.color}, Скорость: {work.speed}, Полиция: {work.is_police}')
work.go(), work.stop(), work.turn("влево"), work.show_speed()
police = PoliceCar(110, 'Ford', 'белый', True)
print(f'\n4. Марка: {police.name}, Цвет: {police.color}, Скорость: {police.speed}, Полиция: {police.is_police}')
police.go(), police.stop(), police.turn("вправо"), police.show_speed()









