class Atm:
    def _init_(self):
        self.pin=""
        self.balance=0

        self.menu()
    def menu(self):
        choice=input('''How would you like to move forward?
              1.Enter 1 to create PIN.
              2.Enter 2 to  deposit money.
              3.Enter 3 to withdraw money.
              4. Enter 4 to check balance
                 ''')
        if int(choice)==1:
            self.create_pin()
        elif int(choice)==2:
            self.deposit()
        elif int(choice)==3:
            self.withdraw()
        elif int(choice)==4:
            self.check_balance()
        else:
            print("good bye!")
    def create_pin(self):
        self.pin=input("enter your pin number")
        if len(self.pin)==4:

            print("Pin succesfully set")
        else:
            print("please enter a valid pin of 4 digits")
    def deposit(self):

        temp=input("your pin number")
        if temp==self.pin:
            amount=int(input("enter the amount"))
            self.balance=self.balance+amount
            print("deposit successful")
        else:
            print("invalid pin")
    def withdraw(self):
        temp=input("your pin number")
        if temp==self.pin:
            amount = int(input("how much do you want to withdraw?"))
            if amount<self.balance:
                self.balance=self.balance-amount
            else:
                print("insufficient balance")
        else:
            print("invalid pin")
    def check_balance(self):
        temp=input("your pin number")
        if temp==self.pin:
            print(self.balance)
        else:
            print("invalid PIN")

uco=Atm()
uco.deposit
