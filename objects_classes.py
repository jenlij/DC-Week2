#BASICS Objects 101 6/27
class Person(object):
    def __init__(self, name, email, phone): #, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        #self.friends = friends
        self.greeting_count = 0
        self.people_greeted = []

    def __repr__(self):
        return "%s %s %s" % (self.name, self.email, self.phone)

    def __str__(self):
        return "%s %s" %(self.name, self.email)

    def greet(self, other_person):
        print "Hello %s, I am %s!" % (other_person.name, self.name)
        self.greeting_count += 1
        self.people_greeted.append(other_person)

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" %(self.name, self.email, self.name, self.phone)

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        return len(self.friends)

    def unique_people_greeted(self):
        return len(set(self.people_greeted))

# Write code to

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person('Sonny','sonny@hotmail.com', '483-485-4948') #, [])
sonny.print_contact_info()
print sonny

# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person('Jordan','jordan@aol.com', '495-586-3456') #, [])
#sonny.friends.append(jordan)
#jordan.friends.append(sonny)
#print len(jordan.friends)
jordan.add_friend(sonny)
print "Jordan has", jordan.num_friends(), "friends"


# Have sonny greet jordan using the greet method.
sonny.greet(jordan)

# Have jordan greet sonny using the greet method.
jordan.greet(sonny)
print jordan.greeting_count

# Write a print statement to print the contact info (email and phone) of Sonny.
print "Sonny's email: %s \nSonny's phone: %s" %(sonny.email, sonny.phone)
# Write another print statement to print the contact info of Jordan.        
print "Jordan's email: %s \nJordan's phone: %s " %(jordan.email, jordan.phone)

dee_ann = Person("Dee Ann", "deedee@gmail.com", "not giving you my number")
dee_ann.greet(jordan)
dee_ann.greet(sonny)
dee_ann.greet(sonny)
dee_ann.greet(jordan)
dee_ann.greet(jordan)




print "\n\n\n\n"

#MAKE YOUR OWN CLASS
class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print self.year, self.make, self.model


car = Vehicle('Nissan', 'Leaf', 2015)
print car.make, car.model, car.year        
car.print_info()
