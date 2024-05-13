#single level inheritance
class Phone:
    def __init__(self,brand,model,price):
        print("inside phone constructor")
        self.brand=brand
        self.model=model
        self.price=price
    def buy(self):
        print("Buying a Phone")
    def return_phone(self):
        print("Returning the Phone")
class Smartphone(Phone):
    pass
s=Smartphone("Apple","15pro",100000).return_phone()
    