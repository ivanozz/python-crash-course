from car import Car
from electric_car import ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_new_car.read_omometer()

# прямое изменение атрибута
my_new_car.odometer_reading(23)
my_new_car.read_omometer()

# обновление через сеттер
my_new_car.update_odometer(23)
my_new_car.read_omometer()

