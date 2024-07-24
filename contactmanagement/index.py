import pprint



def add_contact(contacts):
     name = input("Enter name: ")
     number = input("Enter phone number: ")
     email = input("Enter email: ")
     contacts.append({"name": name, "phone": number, "email": email})
     print("Contact added successfully!")
   

def view_contact(contacts):
    for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    return 
    print("Contact not found")


def search_contact(contacts,name):
    for contact in contacts:
        if contact['name'] == name:
            print(contact)

def delete_contact(contacts,name):
    for contact in contacts:
        if contact['name'] == name:
           contacts.remove(contact)
           print("Successfully removed")
        

def update_contact(contacts,name):
    for contact in contacts:
        # if contact['name'] ==name:
        #     number=input("Enter new number ")
        #     email = input("enter new email")

        #     contact['phone'] = number
        #     contact['email'] = email
        #     print("Updated Sucessfully")
         
        if contact['name'] == name:
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contact['phone'] = new_phone
            contact['email'] = new_email
            print("Contact updated successfully!")


      
     





def main():
    contacts=[]

    while True:
     print("\nWelcome, I am your Personal Contact App")
     print("1. Add contact")
     print("2. View contacts")
     print("3. Search contacts")
     print("4. Delete contacts")
     print("5. Update Contacts")
     print("6. Exit")

     choice = input("Choose an option")
     if choice =='1':
         add_contact(contacts)
     elif choice=='2':
         view_contact(contacts)
     elif choice=='3':
         name = input("Enter the name of the contact to search")
         search_contact(contacts,name)
     elif choice=='4':
         name = input("Enter the name of the contact to delete")
         delete_contact(contacts,name)
     elif choice=='5':
         name=input("Enter the name of the contact to update")
         update_contact(contacts,name)
        
         
     elif  choice=='6':
         break
     else:
         print("Wrong input, try again")
        







if __name__ == '__main__':
    main()