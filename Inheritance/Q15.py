class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(self.name, "makes a sound")

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

class Cat(Animal):
    def sound(self):
        print(self.name, "meows")

class Cow(Animal):
    def sound(self):
        print(self.name, "moos")

d = Dog("Tiger")
c = Cat("Kitty")
cow = Cow("Tulsi")
d.sound()
c.sound()
cow.sound()