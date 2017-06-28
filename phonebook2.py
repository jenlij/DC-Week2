#saving the phonebook database via io pickle
import pickle

def menu():
    print "Electronic Phone Book"
    print "====================="
    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Save entries"
    print "6. Load saved entries"
    print "7. Quit"
    user_input = int(raw_input("What do you want to do (1-6)? "))
    return user_input

def look_up(phonebook_dict):
    name = raw_input("Name: ")
    phone_number = phonebook_dict[name]['Phone']
    email = phonebook_dict[name]['Email']
    print "Found entry for %s: %s, %s " %(name, phone_number, email)

def set_entry(phonebook_dict):
    name = raw_input("Name: ")
    phone_number = raw_input("Phone Number: ")
    email = raw_input("Email: ")
    phonebook_dict.update({name : {'Phone': phone_number, 'Email': email}})
    print "Entry stored for %s." %name 
    return phonebook_dict

def delete_entry(phonebook_dict):
    name = raw_input("Name: ")
    del phonebook_dict[name]
    print "Deleted entry for %s." %name
    return phonebook_dict

def list_entries(phonebook_dict):
    print phonebook_dict.items()

def save_entries(phonebook_dict):
    # open the file in write mode (w)
    myfile = open("phonebook.pickle", "w")
    # dump the contents of the phonebook_dict into myfile - the open file
    pickle.dump(phonebook_dict, myfile)
    # close myfile
    myfile.close()
    print "Entries saved to phonebook.pickle"

def load_saved_entries():
    # open the file in read mode (r)
    myfile = open("phonebook.pickle", "r")
    # load the contents from the file and store it in the phonebook_dict variable
    phonebook_dict = pickle.load(myfile)
    print "Restored saved entries."
    return phonebook_dict

def main():
    phonebook_dict = {}
    user_choice = menu()
    while user_choice != 7:
        if user_choice == 1:
            look_up(phonebook_dict)
        elif user_choice== 2:  
            phonebook_dict = set_entry(phonebook_dict)
        elif user_choice == 3:
            phonebook_dict = delete_entry(phonebook_dict)
        elif user_choice == 4:
            list_entries(phonebook_dict)
        elif user_choice == 5:
            save_entries(phonebook_dict)
        elif user_choice == 6:
            phonebook_dict = load_saved_entries()
        print "\n"                 
        user_choice = menu()
    if user_choice == 7:
        print "Exiting program, Goodbye.\n"    
    print phonebook_dict   


main()