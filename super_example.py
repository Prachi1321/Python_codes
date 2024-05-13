class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class child(Parent):
    def __init__(self,num,val):
        super().__init__(num)
        self.__val=val
    def get_val(self):
        return self.__val
    
s=child(100,200)
print(s.get_num())
print(s.get_val())