# RPG Game

# You will base your game on step 5 of the game and make mods to the game.

# Characters

# make the hero generate double damage points during an attack with a probabilty of 20%
# make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a probability of 20%
# make a character called Shadow who has only 1 starting health but will only take damage about once out of every ten times he is attacked.
# make a Zombie character that doesn't die even if his health is below zero
# come up with at least two other characters with their individual characteristics, and implement them.
# Give each enemy a bounty. For example, the prize for defeating the Goblin is 5 coins, for the Wizard it is 6 coins.
# Items

# make a SuperTonic item to the store, it will restore the hero back to 10 health points.
# add an Armor item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
# add an Evade item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
# come up with at least two other items with their unique characteristics and implement them. You can add more attributes to the hero or the characters.
# Bonus

# allow items to be used on the battle field. The hero can carry the items with him, and you have the option of choosing to use a tonic at any turn in a battle.
# make a Swap item, which when used on a battle field, will swap the power values of the two characters for one turn.
# there is a bug in the store that allows the hero to buy items even if he has no coins. Fix this bug.


"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
import sys
class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

    def attack(self, enemy):
        damage_increase = random.random() > 0.8
        if damage_increase:
            print "%s increases power by 20 percent during attack" % self.name
            self.power = self.power * 1.2
        super(Hero, self).attack(enemy)
        if damage_increase:
            self.power = self.power / 1.2   
    
    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 1

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 5

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 2
        self.bounty = 2

    def receive_damage(self, points):
        super(Medic, self).receive_damage(points)
        heal = random.random() > 0.8 
        if heal:
            print "%s has healed 2 points after attack" % self.name
            self.health += 2

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 1
        self.defence_count = 0
        self.bounty = 3

    def receive_damage(self, points):
        self.defence_count += 1
        if self.defence_count % 10 == 0:
            super(Shadow, self).receive_damage(points)

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 0
        self.power = 1
        self.bounty = 100

    def alive(self):
        return True

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                sys.exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            hero.coins += enemy.bounty
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard(), Medic(), Shadow(), Zombie()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        sys.exit(0)

    shopping_engine.do_shopping(hero)

print "YOU WIN!"
