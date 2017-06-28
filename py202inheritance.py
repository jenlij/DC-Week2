# Yesterday, you learned about making your own custom
# objects in python so that you could move beyond
# tuples, lists, and dictionaries for working
# with data.

# When trying to figure out the pieces of your app,
# you'll want to make things that are more
# specific versions of the same thing.

# So today, you'll learn how to make entire categories of things

# Let's say you go to a restaurant and look at the menu.
# In the section labeled "salads" you might see:
# Superfood salad
# Garden salad
# Caesar (cipher) salad

# What might you assume about all of these?
# - they've all got lettuce
# - there's going to be some kind of dressing
# - it's supposedly healthy

# And, because of that, you don't *really*
# have to mention that they all have lettuce.
# But you might need to specify the particular
# dressing for each salad.

# What you care about is that you can start with the
# general blueprint of a salad and then make
# customizations.

# (cats)

# Inheritance

class Animal(object):
  def sleep(self):
    print "zzzz"

# A cat is-a kinda of Animal
# In python, we express this as follows:
class Cat(Animal):
  def meow(self):
    print "rowr!"

# We say that a Cat is a subclass of Animal.

# And, we can make more subclasses.
class Dog(Animal):
  def bark(self):
    print "woof!"


# Animal is referred to as the superclass
# of Cat and Dog


# Cat objects have a meow method
# and Dog objects have a bark method
# but *both* of them inherit the Animal's nap method

oakley = Cat()
oakley.meow()

leon = Dog()
leon.bark()

oakley.sleep()
leon.sleep()


## Method lookup

# When you ask a Cat object to run its
# sleep method, it first looks to see if
# Cats have that method.
# If it doesn't find it, it looks to its superclass.

# And, you can keep going, inheriting from
# a subclass of Animal:

class Siamese(Cat):
  def teleport(self):
    print "*poof*"

jethro = Siamese()
jethro.teleport()
jethro.meow()
jethro.sleep()

# Overriding methods

# What's the first place python looks for a method?
# It looks at that object's class.
# Let's say that the Siamese makes a different
# meow sound:


class Siamese(Cat):
  def teleport(self):
    print "*poof*"

  def meow(self):
    print "purr purr rowr"

jethro = Siamese()
jethro.meow()


# You could also override the superclass's superclass
# methods:

class Siamese(Cat):
  def teleport(self):
    print "*poof*"

  def meow(self):
    print "purr purr rowr"

  def sleep(self):
    print "purr purr zzz"


jethro = Siamese()
jethro.teleport()
jethro.meow()
jethro.sleep()

# Python is simply doing the least amount of
# work necessary to find what it needs.


# Super
# Python gives you a way to refer to 
# the superclass in case you need to 
# access its version of a method.

class Developer(object):
  def __init__(self, name, platform):
    self.name = name
    self.platforms = [platform]
    self.experience = {}

    # Could we rewrite this to combine 
    # platforms and experience?

    print "Hello! My name is %s" % self.name
  
  def learn(self, platform):
    print "Learning %s" % (platform, )
    self.platforms.append(platform)

  def work_on(self, platform):
    if platform not in self.platforms:
      self.learn(platform)
    print "Working on %s" % (platform)
    self.level_up(platform)
  
  def level_up(self, platform):
    if platform not in self.experience:
      self.experience[platform] = 0
    self.experience[platform] = self.experience[platform] + 1
    print "Just got more experience in %s" % platform

class WebDeveloper(Developer):
  def build_web_app(self):
    self.work_on('JavaScript')
    self.work_on('CSS')
    self.work_on('HTML')

class VeryHardWorkingDeveloper(Developer):
  def __init__(self, name, platform, intensity):
    super(VeryHardWorkingDeveloper, self).__init__(name, platform)
    self.intensity = intensity

  def level_up(self, platform):
    for i in range(self.intensity):
      super(VeryHardWorkingDeveloper, self).level_up(platform)


# A VeryHardWorkingDeveloper object has a 
# level_up method that invokes the superclass
# version multiple times.
# Notice that it can't just call its own version
# of level_up *inside* of its definition of
# level_up. Why not?
# Python would crash or give you an error.