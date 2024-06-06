# exercises
# 1)Create a Dog class that inherits from the Animal class. Give the breed argument
# of Dog.breed a default value of “shepard”.
# Animal class instance variable is name. Method make_voice
# Dog class instance variable is breed. Method make voice
# 2) cat -> color


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def voice(self):
        return f"{self.name} is making sounds"
animal_1 =Animal("Max",3)


class Dog(Animal):
    def __init__(self,name,age,breed="shepard"):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        return f"{self.name} is barking"
dog1 = Dog("Linda",3)
print(dog1.bark())

class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name, age)
        self.color = color
    def meow(self):
        return f"{self.name} is meowing"
cat1 = Cat("Lindi",3,"white")
print(cat1.color)

#
class Cat(Animal):
    def __init__(self,name,age,color = "black"):
        super().__init__(name, age)
        self.color = color
    def meow(self):
        return f"{self.name} is meowing"
cat1 = Cat("Lindi",3)
print(cat1.color)

