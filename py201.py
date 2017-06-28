# you've used objects!
# here are some objects you've used recently

my_list.index("something")
phonebook_dict.items()
hello_file.readlines()

# I just handwaved over the "." followed by a function name
# those are called methods.

# objects are functions + state
# dictionaries have the .keys() and .values() methods
# lists have .append() and .pop()
# strings have .split() and .upper()
# files have .read(), .readlines(), and .seek()

# Your phonebook app has data and it has functions for manipulating that data.
# What if you wanted multiple phonebooks?
# You could use "classes"

# Classes are "factories for objects"

# So here's a "hello" program

greeting = "Hello"
def greet():
  print greeting

# and here's one that greets whomever
greeting = "Hello %s"
def greet(whom):
  print greeting % whom

# here's another greeter
greeting = "Hello %s, I'm %s"
def greet(to_whom, from_whom):
  print greeting % (to_whom, from_whom)

class Person(object):
  def greet(self):
    print "Hello"

# class - keyword, like def, that starts the definition
# Person - name of class
# object - the thing you're basing this class on
# self - a usable reference to the object itself
# def greet() - a method definition

max = Person()
max.greet()

# This is how you "pre-load" an object with data


class Person(object):
  def __init__(self):
    self.name = "Mr Fancy"

  def greet(self):
    print "Hello, I am " % self.name

# __init__ - is the constructor method, also pronounced "dunder init"
# self.name = an "instance variable"

class Counter(object):
  def __init__(self):
    self.count = 0
  
  def increment(self):
    self.count = self.count + 1
    print self.count

class Person(object):
  def __init__(self, name):
    self.name = name

  def greet(self, whom):
    print "Hello %s, I am " % (whom, self.name)

jethro = Person("jethro")
jethro.greet("oakley")


# parameters vs arguments

# __init__ and greet have 2 "parameters", but you call it with 1 argument

class Contact(object):
  def __init__(self, first_name, last_name, email, phone):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone = phone
  def show(self):
      print "%s, %s - %s (%s)" %(self.last_name, self.first_name, self.email, self.phone) 
me = Contact("chris", "aquino", "chris@digitalcrafts.com", "8675309")
print me.first_name
print me.last_name
print me.email
print me.phone


#keep one class per file
class Phonebook(object):
  def __init__(self):
      self.phonebook = {}
  def add_contact(self, contact):
      self.phonebook[contact.email] = contact
  def delete_contact(self, email):
      del self.phonebook[email]
  def show_all_entries(self):
      print self.phonebook
  def show_entry(self, email):
      print self.phonebook[email] 


#keep this stuff in separate file
from phonebook.phonebook import *
from phonebook.contact import *

def main():
    book = Phonebook()
    choice = -1
    while choice !=5:
        pass


main()        

#touch phonebook/__init__.py