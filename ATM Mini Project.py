balance = 500
def deposit_1():
    global balance
    while True:
        user_input = input("press 1 for deposit or press 2 for menu : ")
        if user_input == "2":
            print(f"Menu Loading.......")
            break

        elif user_input == "1":
            deposit_amount = int(input("Enter amount to deposit : "))
            balance += deposit_amount
            print(f"Successfully Amount Deposited....")

def withdraw_1():
    global balance
    while True:
        user_input_1 = input("press 1 for withdraw or press 2 to exit : ")
        if user_input_1 == "2":
            print(f"Thank you for using ATM.......")
            break

        elif user_input_1 == "1":
            withdrawn = int(input("Enter amount to withdraw : "))
            if withdrawn <= balance:
                balance -= withdrawn
                print("Amount withdrawn success.....")
                break
            else:
                print("Insufficient balance....")

def balance_enquiry():
    print(f"Current Balance = {balance}")
                
            
while True :
    print("\nATM Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Exit")

    choose = input("Enter which option do you want : ")
        

    if choose == "1":
        deposit_1()

    elif choose == "2":
        withdraw_1()

    elif choose == "3":
        balance_enquiry()

    elif choose == "4":
        print("Thank You For Using ATM........")
        break
