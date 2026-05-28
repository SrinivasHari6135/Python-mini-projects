customer_name = input("Enter your name :").title()

# list of items
items_list = '''
Rice               Rs 30/kg
Sugar              Rs 15/kg
Milk               Rs 55/lit
Drinks             Rs 39/lit
Bansi rava         Rs 66/kg
Coffee Powder      Rs 65/packet
Red chilli         Rs 59/packet
Oil                Rs 165/lit
'''

# declarations
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

items = {'rice':30,'sugar':15,'milk':55,'drinks':39,'bansirava':66,'coffeepowder':65,'redchilli':59,'oil':165}


while True:
    choose = input("press 1 to get list or press 2 to exit :")
    if choose == "2":
        print("Thanks for visting store.....")
        break
    elif choose == "1":
        print(items_list)

        while True:
            input_1 = input("To press 1 for buy or press 2 to exit :")
            if input_1 == "2":
                print("Thanks for visting store...... ")
                break
            elif input_1 == "1":
                item = input("Choose your items :").lower()
                while True:
                    quantity_input = input("Enter the quantity : ")
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                        break
                    else:
                        print("Please Enter the vaild quantity.....")

                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item,quantity,items[item],price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item Not available , Sorry for the inconvenience......")
             
            #billing 
        if totalprice > 0:
            tax = (totalprice * 2)/100
            finalamount = totalprice + tax
            discount = (10/100)*totalprice
            finalamount -= discount


            print(f"{"="*40} Fills Supermarket {"="*40}")
            print(f"\t\t\t\t\t     Mandapeta")
            print(f"Name : {customer_name}\t\t\t\t\t\t\t              15-05-2026")
            print(f"{"-"*100}")
            print(f"sno{" "*10} items {" "*8} quantity {" "*5} price")
            for i in range(len(pricelist)):
                print(i+1,13*" ", ilist[i], 8*" ", qlist[i], 8*" ", plist[i])
            print("-"*100)
            print(f"{" "*60} Total amount : {totalprice:.2f}")
            print(f"Tax amount {" "*50} {tax:.2f}")
            print(f"Discount {" "*55}{discount:.2f}")

            print("-"*100)
            print(f"{" "*60} Final amount : {finalamount:.2f}")
            print("-"*100)
            print(f"{" "*35}Thank you & Visit again")
            print("-"*100)