class Phone:
    def __init__(self, price, brand, camera):
        print("inside contructor code")
        self.price=price
        self.__brand=brand
        self.camera=camera
    def get_brand(self):
        return self.__brand
class smartphone(Phone):
    pass
s=smartphone("70000","apple","32")
print(s.get_brand())
#it means that  the attribute is private and can't be accessed directly from outside of the class