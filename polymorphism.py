#using super function to execute the parent class
class Phone:
    def __init__(self, brand, model):
        print("inside phone constructor")
        self.brand = brand
        self.model=model
class Smartphone(Phone):
    def __init__(self,brand,model,price,camera):
        print("pehle yaha")
        super().__init__(brand,model)
        self.price = price
        self.camera=camera
        print("inside smartphone constructor")
s=Smartphone("Apple","15pro","1000000","64")
print(s.brand)
