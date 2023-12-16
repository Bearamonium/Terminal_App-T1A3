from random import randint
inventory = []
equipment = []
player_gear_score = 0
base_hit_chance = 50
gear_modifer_per_point = 5
challenge_modifier_per_point = -10

def attack_modifier(gear_score): 
    return gear_score // 3

def defence_modifier(gear_score): 
    return gear_score // 2

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

        def equip_starting_gear(self, starting_weapons, starting_armour):
            self.inventory = [starting_weapons, starting_armour]

class Warrior(Classes): 
    def __init__(self, health, gear_score, skills, name):
        super().__init__(health, gear_score, skills, name)
        self.equip_starting_gear(weapons["Wooden Short Sword"], armour["Chainmail Armour"])
    
class Rogue: 
    def __init__(self, health, gear_score, skills, name):
        super().__init__(health, gear_score, skills, name)
        self.equip_starting_gear(weapons['Wooden Short Bow'], armour['Leather Armour'])

class Wizard: 
    def __init__(self, health, gear_score, skills, name):
        super().__init__(health, gear_score, skills, name)
        self.equip_starting_gear(weapons['Wooden Staff'], armour['Student Robes'])

# Create Enemy classes for within Amoria
class Enemy:
    def __init__(self, name, challenge_rating, skills):
        self.name = name
        self.challenge_rating = challenge_rating
        self.skills = skills

class MossHaggardens(Enemy):
    def __init__(self, challenge_rating, skills, swamp_affinity=True):
        super().__init__("Moss Haggardens", challenge_rating, skills)
        self.swamp_affinity = swamp_affinity

class BoneGnashers(Enemy):
    def __init__(self, challenge_rating, skills, bone_crush_attack=True):
        super().__init__("Bone Gnashers", challenge_rating, skills)
        self.bone_crush_attack = bone_crush_attack

# class Gloomweavers(Enemies):
#     def __init__(self, gear_score, skills, shadow_manipulation=True):
#         super().__init__(gear_score, skills)
#         self.shadow_manipulation = shadow_manipulation

# class Whisperers(Enemies):
#     def __init__(self, gear_score, skills, shadow_manipulation=True):
#         super().__init__(gear_score, skills)
#         self.shadow_manipulation = shadow_manipulation

# class Xhoth(Enemies):
#     def __init__(self, gear_score, skills, shadow_manipulation=True):
#         super().__init__(gear_score, skills)
#         self.shadow_manipulation = shadow_manipulation

# class Shrill_Chorus(Enemies):
#     def __init__(self, gear_score, skills, shadow_manipulation=True):
#         super().__init__(gear_score, skills)
#         self.shadow_manipulation = shadow_manipulation

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
        "enemies" : [
            MossHaggardens(5, ["swamp_magic", "toxic_touch"], True)
            ]
    }, 
    "candle-lit room" : {
        "description" : "A lone flame pierces the gloom, casting long, skeletal shadows that twist and writhe on the floor. The scent of burning wax bleeds into the metallic tang of anticipation, a bitter cocktail in the quiet before the storm.", 
        "exits" : {"south" : "mossy cavern", "north-east" : "Boss Room", "north-west": "Secret Room", "east" : "misty cavern", "west" : "dark cove"}, 
        "items" : [weapons["Iron Sword"], armour["Iron Armour"]], 
    }, 
    "misty cavern" : {
        "description" : "Wispy tendrils of mist weave through the cavern, swallowing light and muffling sound. Each step sinks into unseen depths, sending a shiver up your spine. What lurks within this swirling shroud?", 
        "exits" : {"south" : "mossy cavern", "east" : "dark passageway"}, 
        "items" : [weapons["Iron Sword"], armour["Iron Armour"]], 
        # "enemies" : bone_gnashers
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
        # "enemies" : gloomweavers
    }
}

current_room = "entrance"

def hit_chance(gear_score, challenge_rating): 
    return base_hit_chance + gear_score * gear_modifer_per_point + challenge_rating * challenge_modifier_per_point

print("Welcome, Foolhardy Soul, to Amoria's Embrace.\n\nThe ground beneath your feet shivers, not with earthquake, but with a thousand echoing screams. You stand at the precipice of Amoria, where shadows writhe and madness whispers promises in the wind. This is no mere dungeon, adventurer, but a festering wound upon the world, a gateway to horrors beyond mortal comprehension. \n\nHere, hope withers faster than flowers in winter, and courage curdles under the gaze of things best left unseen. Within these obsidian walls, time bends and twists, sanity unravels like silk in a storm, and death is but a prelude to something far worse.\n\nBut you, it seems, possess a curiosity as sharp as a shard of oblivion. Perhaps you seek forbidden knowledge, or treasures worth kingdoms, or simply the thrill of defying the abyss. Whatever your madness, welcome to Amoria.\n\nMay your steps be swift, your blade ever sharp, and your soul, if you have one left, remain your own until the inevitable, echoing end. \n\nNow, enter... if you dare.")

combat_loop = False

while True: 
    print(rooms[current_room]["description"])
    
    if "enemies" in rooms[current_room]:
        # Generate Monster Descriptions
        for enemy in rooms[current_room]["enemies"]:
            print(f"You see a {enemy.name} lurking in the shadows!")

    print("What do you want to do?")
    print("[1] Attack the enemies")
    print("[2] Explore further")
    print("[3] Use an item")
    print("[4] Open Inventory")

    choice = input("> ")

    if choice == "1":
        combat_loop = True
        while combat_loop:
            player_action = input("Attack (a) or flee (f)? ").lower()
            temp_gear_score = player_gear_score

            if player_action == "a":
                hit_roll = randint(1, 100)
                if hit_roll <= hit_chance(player_gear_score, enemy.challenge_rating in rooms[current_room]["enemies"]):
                    enemy.challenge_rating -= 1
                    print("You land a blow! The monster's challenge rating is now:", enemy.challenge_rating)
                    if enemy.challenge_rating <= 0: 
                        print(f"Victory! You defeated {enemy.name}!")
                        combat_loop = False
                else: 
                    print("Your attack misses.")

            elif player_action == "f": 
                flee_roll = randint(1, 100)
                if flee_roll <= 50: 
                    print("You escap successfully!")
                    combat_loop = False
                else: 
                    print("The monster blocks your escape! You must fight!")
                    player_action == "a"
            else: 
                print("Invalid action - please choose either attack or flee!")

            if enemy.challenge_rating > 0: 
                monster_roll = randint(1, 100)
                if monster_roll <= 50 + enemy.challenge_rating * challenge_modifier_per_point:
                    temp_gear_score -= 1
                    print("The monster strickes back! Your grear score is now:", temp_gear_score)
                if temp_gear_score <= 0: 
                    print("Defeat! Amoria claims another victim to the Abyss...")
                    combat_loop = False
                    game_over = True

        if not combat_loop: 
            print("Press Enter to continue your adventure.")
            input()

    exits = list(rooms[current_room]["exits"].keys())
    for exit in exits:
        print(f"- {exit.capitalize()}: {rooms[current_room]['exits'][exit]}")

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
            del rooms[current_room][item]
        else: 
            print("There's nothing left here for you to take.")
    elif action == "inventory": 
        if inventory: 
            print("You are carrying:")
            for item in inventory: 
                print(f"- {item.name}")
    