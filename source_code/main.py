
inventory = []
equipment = []

# Define Item class for all inventory items 
class Item():
    def __init__(self, name, value, quantity = 1):
        self.name = name
        self.value = value
        self.quantity = quantity

    def itemadd(self):
        inventory.append(Item)

# Define Weapons sub-class of Items for all weapons available in the game
class Weapon(Item):
    def __init__(self, name, value, gear_score, quantity = 1):
        super().__init__(name, value, quantity)

        self.gear_score = gear_score 
        
    def weaponadd(self):
        weapons.append(Weapon)

# Define Armour sub-class of Items for all armour available in the game
class Armour(Item):
    def __init__(self, name, value, gear_score, quantity = 1):
        super().__init__(name, value, quantity)

        self.gear_score = gear_score 

# Define starting classes

class Classes():
    def __init__(self, health, gear_score, skills, name):
        self.health = health
        self.gear_score = gear_score
        self.skills = skills
        self.name = name

    def getHealth(self):
        return self.health
    def getGear_Score(self):
        return self.gear_score

class Warrior(Classes): 
    def __init__(self, health, gear_score, skills, name):
        super().__init__(health, gear_score, skills, name)

    def set_starting_inventory():
        global inventory
        inventory = [weapons['Wooden Short Sword'], armour['Chainmail Armour']]
    
class Rogue: 
    def __init__(self, health, gear_score, skills, name):
        super().__init__(health, gear_score, skills, name)

    def set_starting_inventory():
        global inventory
        inventory = [weapons['Wooden Short Bow'], armour['Leather Armour']]

class Wizard: 
    def __init__(self, health, gear_score, skills, name):
        super().__init__(health, gear_score, skills, name)

    def set_starting_inventory():
        global inventory
        inventory = [weapons['Wooden Staff'], armour['Student Robes']]


# Create Enemy classes for within Amoria
class Enemies: 
    pass

class Moss_Haggardens(Enemies): 
    pass

class Bone_Gnashers(Enemies):
    pass

class Gloomweavers(Enemies):
    pass

class Whisperers(Enemies):
    pass

class Xhoth(Enemies):
    pass

class Shrill_Chorus(Enemies):
    pass
        
# Define Weapons dictionary for all weapons available in the game
weapons = {
    'Wooden Short Sword' : Weapon("Wooden Sword", 1, 1), 
    'Wooden Short Bow' : Weapon("Wooden Short Bow", 1, 1), 
    'Wooden Staff' : Weapon("Wooden Staff", 1, 1), 
    'Iron Sword' : Weapon("Iron Sword", 1.5, 2), 
    'Elm Short Bow' : Weapon("Elm Short Bow", 1.5, 2), 
    'Elm Staff' : Weapon("Elm Staff", 1.5, 2), 
}

# Define Armour dictionary for all armour available in the game
armour = {
    'Chainmail Armour' : Armour("Chainmail Armour", 1, 1),
    'Leather Armour' : Armour("Leather Armour", 1, 1),
    'Student Robes' : Armour("Wizard Robes", 1, 1),
    'Iron Armour' : Armour("Iron Armour", 1.5, 2),
    'Studded Leather Armour' : Armour("Studded Leather Armour", 1.5, 2),
    'Silk Robes' : Armour("Silk Robes", 1.5, 2)
}

# Initialise rooms within a dictionary to call upon during the game loop for descriptions and pathway layouts
rooms = {
    "entrance" : {
        "description" : "Amoria's maw gapes, a silent scream carved in stone. Moss, like venomous veins, crawls across the shattered stone entrance. Silence hangs heavy, broken only by dripping.. something, each drop a chilling knell. Dare you enter?", 
        "exits" : {"north" : "passage"}
    }, 
    "passage" : {
        "description" : "A single, skeletal bridge spans the chasm, its bones bleached white, each step a tick against eternity. Below, shadows writhe, unseen eyes glint like poisoned emeralds. Dare you cross, adventurer, to dance with the nightmares within?", 
        "exits" : {"south" : "entrance", "north" : "mossy cavern"}
    }
}

for item in inventory: 
    print(item.name, item.value, item.gear_score)

print("Welcome, Foolhardy Soul, to Amoria's Embrace.\n\nThe ground beneath your feet shivers, not with earthquake, but with a thousand echoing screams. You stand at the precipice of Amoria, where shadows writhe and madness whispers promises in the wind. This is no mere dungeon, adventurer, but a festering wound upon the world, a gateway to horrors beyond mortal comprehension. \n\nHere, hope withers faster than flowers in winter, and courage curdles under the gaze of things best left unseen. Within these obsidian walls, time bends and twists, sanity unravels like silk in a storm, and death is but a prelude to something far worse.\n\nBut you, it seems, possess a curiosity as sharp as a shard of oblivion. Perhaps you seek forbidden knowledge, or treasures worth kingdoms, or simply the thrill of defying the abyss. Whatever your madness, welcome to Amoria.\n\nMay your steps be swift, your blade ever sharp, and your soul, if you have one left, remain your own until the inevitable, echoing end. \n\nNow, enter... if you dare.")