# multiple inheritance
class Phone:
    def __init__(self, brand,model):
        print("pehle yahan")
        self.brand = brand
        self.model=model
    def buy(self):
        print("Buying a phone")
class Product:
    def review(self):
        print("review the phone")
class Smartphone(Phone, Product):
    pass
s=Smartphone("Apple","iphone15")
s.buy()
s.review()

    
