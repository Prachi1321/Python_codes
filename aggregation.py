class Customer:
    def __init__(self,name, gender,Address):
        self.name=name
        self.gender=gender
        self.Address=Address
    def edit_profile(self,newname,newCity,new_pin,newState):
        self.name=newname
        self.Address.change_address(newCity,new_pin,newState)

class address:

    def __init__(self, city,pin,state):
        self.city=city
        self.pin=pin
        self.state=state
    def change_address(self, newCity, newPin, newState):
        self.city = newCity
        self.pin=newPin
        self.state=newState
add=address("haldwani","263139",'uk')
cust=Customer("bebu","female",add)
cust.edit_profile("Prachi","gurgaon","122011","haryana")
print(cust.Address.pin)