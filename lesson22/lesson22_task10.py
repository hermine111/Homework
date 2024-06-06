# 10. Class Exercise:
# Create a Python class representing a car with methods for accelerating and braking.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        if self.speed >= decrement:
            self.speed -= decrement
        else:
            self.speed = 0

    def get_speed(self):
        return self.speed


my_car = Car("Ford", "Mustang", "2022")
my_car.accelerate(70)
my_car.brake(30)
print(my_car.get_speed())
