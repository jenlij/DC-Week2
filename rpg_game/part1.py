# RPG Game 1
# # Take version 1 of the RPG game and rewrite it using objects.

# Step 1

# Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power of the goblin. Use a hero object in place of the variables hero_health and hero_power and use a goblin object in place of the variables goblin_health and goblin_power all through out the app.

# Step 2

# Take the code for the hero attacking the goblin and extract it into a method (call it attack) of the Hero class. Replace the existing code with a call to the attack method. Hint: attack should take in the goblin (enemy) as a parameter: hero.attack(goblin)

# Step 3

# Similarly, take the code for the goblin attacking the hero and extract it into a method (also call it attack) of the Goblin class. Replace the existing code with a call to the attack method. It should look like goblin.attack(hero).

# Step 4

# Refactor the while condition:

# while goblin.health > 0 and hero.health > 0:
# to

# while goblin.alive() and hero.alive():
# The health checks should be moved to within the alive methods of Hero and Goblin respectively.

# Step 5

# Take the code for printing the health status of the hero and move it into a method called print_status of Hero. Do the same for the goblin.

# Step 6

# Do you see a lot of duplicated or similar code between Hero and Goblin? What if you can share the duplicated code between them? You can by using inheritance! Create a new class called Character and make both Hero and Goblin inherit from it.

# Step 7

# The alive methods on Hero and Goblin should be identical. Move it into Character, and remove them from Hero and Goblin - now they can simply inherit it from Character.

# Step 7: Bonus Challenge

# The methods attack and print_status method in Hero and Goblin look almost identical, but not quite. Is it possible to move them into the Character class as well? Give it a try.

# Step 8: Bonus Challenge 2

# Create a zombie character that cannot die and have it fight the hero instead of the goblin.


class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def attack(self, enemy):
        enemy.health -= self.power
        print "%s does %d damage to the %s." %(self.name, self.power, enemy.name)
        if not enemy.alive():
            print "%s is dead." %enemy.name            
 
    def print_status(self):
        print "%s has %d health and %d power." %(self.name, self.health, self.power)        



class Hero(Character):
    pass  


class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    zombie_health = 0
    zombie_power = 1
    hero = Hero("Hero", hero_health, hero_power)
    goblin = Goblin("Goblin", goblin_health, goblin_power)
    zombie = Zombie("Zombie", zombie_health, zombie_power)
    
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        zombie.print_status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. fight zombie"
        print "3. do nothing"
        print "4. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            hero.attack(goblin)
            if goblin.alive():
                goblin.attack(hero)
        elif input == "2":
            hero.attack(zombie)
            zombie.attack(hero)
        elif input == "3":
            pass
        elif input == "4":
            print "Goodbye"
            break
        else: 
            print "Invalid input %r" % input    
                     
main()      





