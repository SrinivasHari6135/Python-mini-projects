dictionary_1 = {}

while True:
    print("\nDictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display all Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        word = input("Enter the Word : ").lower()
        meaning = input("Enter the Meaning : ")
        dictionary_1[word] = meaning
        print("Word added successfully.......")

    elif choice == "2":
        word = input("Enter the word to search : ").lower()
        if word in dictionary_1:
            print("Meaning :",dictionary_1[word])

        else:
            print(f"{word} Not found in the Dictionary.....")


    elif choice == "3":
        if dictionary_1:
            print ("words and their meanings :")
            for word, meaning in dictionary_1.items():
                print(f"{word}: {meaning}")

        else:
            print("Dictionary is Empty...")

    elif choice == "4":
        word = input("Enter the word to update the meaning : ").lower()
        if word in dictionary_1:
            new_meaning = input("Enter the new meaning : ")
            dictionary_1[word] = new_meaning
            print(f" new meaning updated successfully completed.....")
            print("Updated Meaning :",dictionary_1[word])

        else:
            print("Word not found in dictionary......")

    elif choice == "5":
        word = input("Enter the Word to delete : ").lower()
        if word in dictionary_1:
            del dictionary_1[word]
            print("Word deleted successfully....")
        else:
            print("Word not found in the Dictionary.....")

    elif choice == "6":
        print("Exiting......")
        break
    else:
        print("Invaild choice!, Please Enter a vaild option...")
        
        
