
inventory = []
equipment = []


class Item():
    def __init__(self, name, value, quantity = 1):
        self.name = name
        self.value = value
        self.quantity = quantity

        def itemadd(self):
            inventory.append(Item)


class Weapon(Item):
    def __init__(self, name, value, gear_score, quantity = 1):
        super().__init__(name, value, quantity)

        self.gear_score = gear_score 

    def weaponadd(self):
        weapons.append(Weapon)


class Armour(Item):
    def __init__(self, name, value, gear_score, quantity = 1):
        super().__init__(name, value, quantity)

        self.gear_score = gear_score 

class Warrior: 
    def __init__(self, health, gear_score, skills, name):
        self.health = health
        self.gear_score = gear_score
        self.skills = skills
        self.name = name


    def set_starting_inventory():
        global inventory
        inventory = [weapons['Wooden Short Sword'], armour['Chainmail Armour']]
        
    def getHealth(self):
        return self.health
    def getGear_Score(self):
        return self.gear_score
    
class Rogue: 
    def __init__(self, health, gear_score, skills, name):
        self.health = health
        self.gear_score = gear_score
        self.skills = skills
        self.name = name


    def set_starting_inventory():
        global inventory
        inventory = [weapons['Wooden Short Bow'], armour['Leather Armour']]
        
    def getHealth(self):
        return self.health
    def getGear_Score(self):
        return self.gear_score
    
class Wizard: 
    def __init__(self, health, gear_score, skills, name):
        self.health = health
        self.gear_score = gear_score
        self.skills = skills
        self.name = name


    def set_starting_inventory():
        global inventory
        inventory = [weapons['Wooden Staff'], armour['Student Robes']]
        
    def getHealth(self):
        return self.health
    def getGear_Score(self):
        return self.gear_score

weapons = {
    'Wooden Short Sword' : Weapon("Wooden Sword", 1, 1), 
    'Wooden Short Bow' : Weapon("Wooden Short Bow", 1, 1), 
    'Wooden Staff' : Weapon("Wooden Staff", 1, 1), 
    'Iron Sword' : Weapon("Iron Sword", 1.5, 2), 
    'Elm Short Bow' : Weapon("Elm Short Bow", 1.5, 2), 
    'Elm Staff' : Weapon("Elm Staff", 1.5, 2), 
}

armour = {
    'Chainmail Armour' : Armour("Chainmail Armour", 1, 1),
    'Leather Armour' : Armour("Leather Armour", 1, 1),
    'Student Robes' : Armour("Wizard Robes", 1, 1),
    'Iron Armour' : Armour("Iron Armour", 1.5, 2),
    'Studded Leather Armour' : Armour("Studded Leather Armour", 1.5, 2),
    'Silk Robes' : Armour("Silk Robes", 1.5, 2)
}

Warrior.set_starting_inventory()

print(inventory)
