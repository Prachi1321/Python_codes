class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
def greet(customer):
    if customer.gender=="male":
        print("Hello",customer.name,"sir")
    else:
        print("Hello",customer.name,"ma'am")
    cust2= Customer("kovid","male")
    return cust2
    
cust=Customer("prachi","female")
new_cust=greet(cust)
print(new_cust.name, new_cust.gender)