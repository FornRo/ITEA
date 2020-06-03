''' _________________________________________________________________ 72
3)Создать класс автомобиля. Описать общие аттрибуты и методы. Создать
классы легкового автомобиля и грузового. Описать в основном классе базовые
аттрибуты для автомобилей. В классах наследниках описать дополнительные
методы.
'''


class Car:
    def __init__(self, model, engine_type, max_speed, fuel, price):
        self.model = model
        self.engine_type = engine_type
        self.max_speed = max_speed
        self.fuel_consumption = fuel
        self.price = price

    def move(self):
        print(f'The car {self.model} is moving')

    def stop_engine(self):
        print(f'The car {self.model} has been stopped')

    def get_max_speed(self):
        print(f'Max speed is {self.max_speed}')

    def get_flue_consumption(self):
        print(f'Car {self.model} fuel consumption {self.fuel_consumption}')

    def price_car(self):
        print(f'Car {self.model} price: {self.price}')


class Truck(Car):
    def move(self):
        print('Truck is moving')

    def offload(self):
        print('The items are being offloaded')

    def flue_consumption(self):
        print(
            f'Car {self.model} fuel consumption {self.fuel_consumption * 1.25}')

    def increment_speed(self, value):
        self.max_speed += value


car = Car('audi', 'v-6', 240, 5.5, 40000)

car.move()
car.get_max_speed()
car.get_flue_consumption()
car.price_car()

truck_1 = Truck(model='Grat', engine_type='v-4', max_speed=120,
                fuel=10.75, price=80000)


truck_1.move()
truck_1.get_max_speed()
truck_1.get_flue_consumption()
truck_1.price_car()
