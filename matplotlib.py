contact = {}

def display_contact() :
    print("Name\t\tConatct Number")
    for key in contact :
        print("{}\t\t{}".format(key,contact.get(key)))
while True :
    choice = int(input(" Type 1 to Add new contact \n Type 2 to Search contact \n Type 3 to View contact \n Type 4 to Edit contact \n Type 5 to Delete contact \n Type 6 to Exit \n Enter your choice"))
    if choice == 1 :
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
    elif choice == 2 :
        search_name = input("Enter the contact name: ")
        if search_name in contact :
            print(search_name,"'s contact number is ",contact[search_name])
        else :
            print("Name is not found in the contact book")
    elif choice == 3 :
        if not contact :
            print("contact book is empty")
        else :
            display_contact()
    elif choice == 4 :
        edit_contact = input("Enter the contact to be edited")
        if  edit_contact in contact :
            phone = input("Enter mobile number")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else :
            print("Name is not found in the contact book")
    elif choice == 5 :
        del_contact =  input("Enter the contact to be deleted")
        if del_contact in contact :
           confirm = input("Do you want to delete this contact y/n ?")
           if confirm == "y" or confirm == "Y":
               contact.pop(del_contact)
           display_contact()
        else :
            print("Name is not found in the contact book")
    else :
        break

