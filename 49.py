#multilevel inheritance
#base class
class Person:
    def display(self):
        print("this is class person")
#deived classs
class employee(Person):
    def printing(self):
        print("this is derived class")
class programmer(employee):
    def show(self):
        print("this is derived class 2")
p1=programmer()
p1.display()
p1.printing()
p1.show()