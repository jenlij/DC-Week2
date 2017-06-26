def menu():
    print "Electronic Phone Book"
    print "====================="
    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Quit"
    user_input = int(raw_input("What do you want to do (1-5)? "))
    return user_input

def look_up(phonebook_dict):
    name = raw_input("Name: ")
    phone_number = phonebook_dict[name]
    print "Found entry for %s: %s " %(name, phone_number)

def set_entry(phonebook_dict):
    name = raw_input("Name: ")
    phone_number = raw_input("Phone Number: ")
    phonebook_dict.update({name: phone_number})
    print "Entry stored for %s." %name 
    return phonebook_dict

def delete_entry(phonebook_dict):
    name = raw_input("Name: ")
    del phonebook_dict[name]
    print "Deleted entry for %s." %name
    return phonebook_dict

def list_entries(phonebook_dict):
    print phonebook_dict.items()
    
def main():
    phonebook_dict = {'Jen': '1234'}
    user_choice = menu()
    while user_choice != 5:
        if user_choice == 1:
            look_up(phonebook_dict)
        elif user_choice== 2:  
            phonebook_dict = set_entry(phonebook_dict)
        elif user_choice == 3:
            phonebook_dict = delete_entry(phonebook_dict)
        elif user_choice == 4:
            list_entries(phonebook_dict)
        print "\n"                 
        user_choice = menu()
    if user_choice == 5:
        print "Exiting program, Goodbye.\n"    
    print phonebook_dict    
main()
