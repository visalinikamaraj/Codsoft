contact = {}

def display_contact():
    print("name\t\tcontact")
    for key in contact:
        print("{}\t\t{}.format(key,contact>get(key))")



while True:
    choice= int(input("1.add new contact\n2.search contact\n3.display contact\n4.edit contact\n5.delete contact\n6.exit"))

    if choice == 1:
        name= input("enter the contact name")
        phone= input("enter the mobile number")
        contact[name]=phone

    elif choice == 2:
        search_name= input ("enter the contact name")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("name is not found ")

    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()     

    elif choice == 4:
        edit_contact=input("enter the contact name you want to edit:")
        if edit_contact in contact:
            phone = input("enter the mobile number")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("not fount")

    elif choice == 5:
        delete_contact=input("enter the contact name you want to delete")
        if delete_contact in contact:
            confirm = input("do you want to delete this contact y/n?")
            if confirm =='y' or confirm =='Y':
                contact.pop(delete_contact)

            display_contact()
        else:
            print("name is notb found in contact book")
    else:
        break

print("quit")                     
