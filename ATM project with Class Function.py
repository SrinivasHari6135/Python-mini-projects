class atm():
    def __init__(self,bank,branch,location,pin=1234,balance=500):
        self.bank = bank
        self.branch = branch
        self.location = location
        self.__pin = pin
        self._balance = balance
    def Deposit(self):
        while True:
            user_input = input("press 1 for deposit or press 2 for menu : ")
            if user_input == "2":
                print(f"Menu Loading.......")
                break

            elif user_input == "1":
                deposit_amount = float(input("Enter amount to deposit : "))
                self._balance += deposit_amount
                print(f"Successfully Amount Deposited....")

    def Withdraw(self):
        while True:
            user_input_1 = input("press 1 for withdraw or press 2 to exit : ")
            if user_input_1 == "2":
                print(f"Thank you for using ATM.......")
                break

            elif user_input_1 == "1":
                withdrawn = int(input("Enter amount to withdraw : "))
                if withdrawn <= self._balance:
                    self._balance -= withdrawn
                    print("Amount withdrawn success.....")
                    break
                else:
                    print("Insufficient balance....")

    def Balance_Enquiry(self):
        print(f"Current Balance = {self._balance:.2f}")

    def pin_change(self):
        user_input_3 = int(input("Enter your old pin : "))
        if user_input_3 == self.__pin:
            new_pin = int(input("Enter the new pin : "))
            self.__pin = new_pin
            print(f"Pin changed Successfully......")
        else:
            print(f"Enter the correct pin......")

SBI = atm("SBI","Mandapeta","Near karachi sweet shop")

while True :
    print("\nATM Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Pin change")
    print("5. Exit")

    choose = input("Enter which option do you want : ")
        

    if choose == "1":
        SBI.Deposit()

    elif choose == "2":
        SBI.Withdraw()

    elif choose == "3":
        SBI.Balance_Enquiry()

    elif choose == "4":
        SBI.pin_change()  
    elif choose == "5":
        print("Thank You For visiting SBI ATM........")
        break   