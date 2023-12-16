from random import randint
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

items = {
    'Golden Sphere' : Item("Golden Sphere", 0), 
    'Candle Key' : Item("Candle Key", 0), 
    'Fire Orb' : Item("Fire Orb", 5), 
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
    }, 
    "mossy cavern" : {
        "description" : "A hushed eye of emerald moss, this cave coils on itself, walls draped in velvet silence. Sunlight bleeds through unseen cracks, staining stone with jade and shadow. The air hangs heavy with damp perfume, whispering promises of secrets and slumbering things.", 
        "exits" : {"south" : "passage", "north" : "candle-lit room", "east" : "misty cavern", "west" : "dark cove"}, 
        "items" : [weapons["Iron Sword"], armour["Iron Armour"]], 
        "enemies" : Moss_Haggardens()
    }, 
    "candle-lit room" : {
        "description" : "A lone flame pierces the gloom, casting long, skeletal shadows that twist and writhe on the floor. The scent of burning wax bleeds into the metallic tang of anticipation, a bitter cocktail in the quiet before the storm.", 
        "exits" : {"south" : "mossy cavern", "north-east" : "Boss Room", "north-west": "Secret Room", "east" : "misty cavern", "west" : "dark cove"}, 
        "items" : [weapons["Iron Sword"], armour["Iron Armour"]], 
        "enemies" : Whisperers()
    }, 
    "misty cavern" : {
        "description" : "Wispy tendrils of mist weave through the cavern, swallowing light and muffling sound. Each step sinks into unseen depths, sending a shiver up your spine. What lurks within this swirling shroud?", 
        "exits" : {"south" : "mossy cavern", "east" : "dark passageway"}, 
        "items" : [weapons["Iron Sword"], armour["Iron Armour"]], 
        "enemies" : Bone_Gnashers()
    }, 
    "dark passageway" : {
        "description" : "An unnatural silence hangs in the air, broken only by the soft crunch of your boots on unseen debris. No dripping water, no rustle of unseen creatures, just an oppressive quiet that presses against your ears like a physical weight. You swear you can feel eyes watching from the darkness, unseen and hungry.", 
        "exits" : {"south" : "misty cavern", "north" : "statue room"}, 
        "items" : [items["Candle Key"]]
    }, 
    "statue room" : {
        "description" : "The scent of cold stone and ancient dust hangs heavy in the air, a shroud woven from forgotten prayers. Statues, frozen in eternal stillness, line the cavern walls. Marble warriors grip rusted swords, their poses contorted in the throes of battle long past. Regal queens stare with vacant eyes, their gilded crowns mocking the passage of time. Grotesque gargoyles leer from shadowed corners, their stone talons poised to snatch, their silent screams etched in the cracks of weathered wings.", 
        "exits" : {"south" : "dark passageway"}, 
        "items" : [items["Fire Orb"]], 
        "enemies" : Gloomweavers()
    }
}

for item in inventory: 
    print(item.name, item.value, item.gear_score)

player_gear_score = 0
enemy_gear_score = 0

def attack_modifier(gear_score): 
    return gear_score // 3

def defence_modifier(gear_score): 
    return gear_score // 2

current_room = "entrance"

print("Welcome, Foolhardy Soul, to Amoria's Embrace.\n\nThe ground beneath your feet shivers, not with earthquake, but with a thousand echoing screams. You stand at the precipice of Amoria, where shadows writhe and madness whispers promises in the wind. This is no mere dungeon, adventurer, but a festering wound upon the world, a gateway to horrors beyond mortal comprehension. \n\nHere, hope withers faster than flowers in winter, and courage curdles under the gaze of things best left unseen. Within these obsidian walls, time bends and twists, sanity unravels like silk in a storm, and death is but a prelude to something far worse.\n\nBut you, it seems, possess a curiosity as sharp as a shard of oblivion. Perhaps you seek forbidden knowledge, or treasures worth kingdoms, or simply the thrill of defying the abyss. Whatever your madness, welcome to Amoria.\n\nMay your steps be swift, your blade ever sharp, and your soul, if you have one left, remain your own until the inevitable, echoing end. \n\nNow, enter... if you dare.")

combat_loop = False

while True: 
    print(rooms[current_room]["description"])

    exits = list(rooms[current_room]["exits"].keys())
    print("Exits: ", ", ".join(exits))

    while "enemies" in rooms[current_room]:
        combat_loop = True
        while combat_loop: 
            for enemy in rooms[current_room]["enemies"]: 
                print(f"You have encountered {enemy.name}!")
            atk_def = input("Attack (a) or Defend (d)? ").lower()
            if action == "a":
                player_roll = randint(1, 20)
                enemy_defence = randint(1, 20) + defence_modifier(enemy_gear_score)
                if player_roll + attack_modifier(player_gear_score) > enemy_defence: 
                    print(f"You struck the {enemy.name} with a powerful blow!")
                    # TODO: Implement damage calculations based on the difference between the attack of player and defence of enemy
                    enemy_gear_score -= 1
                else: 
                    print(f"Oh no! The {enemy.name} countered your attack!")
            elif action == "d":
                print("You ready yourself for an attack.")
            else: 
                print("Invalid action! Please choose to either attack or defend.")
            
            if enemy_gear_score > 0: 
                enemy_roll = randint(1, 20)
                player_defence = randint(1, 20) + defence_modifier(player_gear_score)
                if enemy_roll + attack_modifier(enemy_gear_score) > player_defence: 
                    print(f"The {enemy.name} has landed a blow against you.")
                    # TODO: Implement damage calculations based on the difference between the attack of player and defence of enemy
                    player_gear_score -= 1
                else: 
                    print(f"You successfully avoid the attack from {enemy.name}")
            else: 
                print("You win!")
                combat_loop = False

            if player_gear_score <= 0: 
                print("You have sucumbed to the abyss of Amoria. GAME OVER...")
                combat_loop = False


    action = input("> ").lower()


    if action in exits: 
        current_room = rooms[current_room]["exits"][action]
    elif action == "look":
        if "items" in rooms[current_room]:
            for item in rooms[current_room]["items"]:
                print(f"You see a {item.name}.")
        else: 
            print("You see nothing of interest.")
    elif action == "take": 
        if "items" in rooms[current_room]:
            item = rooms[current_room]["items"][0]
            inventory.append(item)
            print(f"You take the {item}.")
            del rooms[current_room]["items"]
        else: 
            print("There's nothing left here for you to take.")
    elif action == "inventory": 
        if inventory: 
            print("You are carrying:")
            for item in inventory: 
                print(f"- {item.name}")
    