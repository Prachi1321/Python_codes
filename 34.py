class Animal:
    def __init__(self, name, color):
        self.name=name
        self.color = color
class Dog(Animal):
    def bark(self):
        return "Woof!"
d=Dog("Fido", 'brown')
print(d.bark()) # Output: