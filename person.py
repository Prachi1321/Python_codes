class Person:
    def __init__(self, name_input, country_input):
        self.name=name_input
        self.country=country_input
    def greet(self):
        if  self.country=="India":
            print("Namaste",self.name)
        else:
            print("Hello",self.name)
p=Person('Prahi','India')
p.greet()
