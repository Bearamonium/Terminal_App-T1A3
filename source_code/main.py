from random import randint
from prettytable import PrettyTable

class Inventory_Items: 
    def __init__(self, name, value, quantity=1):
        self.name = name
        self.value = value
        self.quantity = quantity

class Items(Inventory_Items):
    def __init__(self, name, value, quantity=1):
        super().__init__(name, value, quantity)
        self.gear_score = None

items = {
    'Golden Sphere' : Items("Golden Sphere", 0), 
    'Candle Key' : Items("Candle Key", 0), 
    'Fire Orb' : Items("Fire Orb", 5), 
}

class Weapon(Inventory_Items):
    def __init__(self, name, value, gear_score, quantity=1):
        super().__init__(name, value, quantity)
        self.gear_score = gear_score

weapons = {
    'Wooden Short Sword' : Weapon("Wooden Sword", 1, 1), 
    'Wooden Short Bow' : Weapon("Wooden Short Bow", 1, 1), 
    'Wooden Staff' : Weapon("Wooden Staff", 3, 3), 
    'Iron Sword' : Weapon("Iron Sword", 1.5, 2), 
    'Elm Short Bow' : Weapon("Elm Short Bow", 1.5, 2), 
    'Elm Staff' : Weapon("Elm Staff", 1.5, 2), 
}

class Armour(Inventory_Items):
    def __init__(self, name, value, gear_score, quantity=1):
        super().__init__(name, value, quantity)
        self.gear_score = gear_score

armour = {
    'Chainmail Armour' : Armour("Chainmail Armour", 1, 1),
    'Leather Armour' : Armour("Leather Armour", 1, 1),
    'Student Robes' : Armour("Wizard Robes", 3, 3),
    'Iron Armour' : Armour("Iron Armour", 1.5, 2),
    'Studded Leather Armour' : Armour("Studded Leather Armour", 1.5, 2),
    'Silk Robes' : Armour("Silk Robes", 1.5, 2)
}

class Character: 
    def __init__(self, class_name, lives, skills, intelligence, dexterity, strength):
        self.class_name = class_name
        self.lives = lives
        self.skills = skills
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.strength = strength
        self.equipment = None
        self.inventory = []
        self.temp_gear_score = 0
    
    def calculate_gear_score(self): 
        return sum(item.gear_score for item in self.equipment)

    def reduce_gear_score(self, damage):
        self.temp_gear_score -= damage



class Wizard(Character):
    def __init__(self, lives=1, skills={"Freezing Wind" : {"damage" : 2, "uses" : 5 }, "Firebolt" : {"damage" : 3, "uses" : 4 }, "Thunderstrike" : {"damage" : 5, "uses" : 2 }, "Water Sense" : {"damage" : 0, "uses" : 5}}, intelligence=10, dexterity=5, strength=2):
        super().__init__("Wizard", lives, skills, intelligence, dexterity, strength)
        self.equipment = [weapons["Wooden Staff"], armour["Student Robes"]]
    
    def Firebolt(self, target):
        damage = int(3)
        if player.skills["Firebolt"]["uses"] > 0:
            print(f"A searing bolt of flame scorches {target.name} for {damage} fire damage!")
            target.challenge_rating -= damage
            player.skills["Firebolt"]["uses"] -= 1
        else:
            print("No more uses left!")

    def Freezing_Wind(self, target, uses=5):
        self.uses = uses
        damage = int(2)
        if player.skills["Freezing Wind"]["uses"] > 0:
            print(f"A frigid gale whips towards {target.name}, dealing {damage} ice damage.")
            target.challenge_rating -= damage
            player.skills["Freezing Wind"]["uses"] -= 1
        else:
            print("No more uses left!")

    def Thunderstrike(self, target, uses=2):
        self.uses = uses
        damage = int(5)
        if player.skills["Thunderstrike"]["uses"] > 0:
            print(f"A bolt of crackling energy surges from your fingertips, striking {target.name} for {damage} lightning damage!")
            target.challenge_rating -= damage
            player.skills["Thunderstrike"]["uses"] -= 1
        elif uses == 0:
            print("No more uses left!")

    def Watersense(self, uses=5):
        self.uses = uses
        if uses > 0:
            print("You feel a deep connection to the surrounding water, unlocking it's secrets to you.")
            uses -= 1
            print(f"Uses left: {uses}")
        elif uses == 0:
            print("No more uses left!")

    def gear_score(self):
        return Character.calculate_gear_score(self)

class Warrior(Character):
    def __init__(self, lives=3, skills=["Upwards Slash", "Ground Smash"], intelligence=2, dexterity=5, strength=10):
        super().__init__("Warrior", lives, skills, intelligence, dexterity, strength)
        self.equipment = [weapons["Wooden Short Sword"], armour["Chainmail Armour"]]

    def Upwards_Slash(self): 
        self.uses = 3
        print(f"{player_name} swiftly unleashes their sword in an upwards arc.")

    def ground_smash(self):
        self.uses = 5
        print(f"{player_name} smashes downwards with the blade, causing the ground to quake.")

    def gear_score(self):
        return Character.calculate_gear_score(self)

class Rogue(Character):
    def __init__(self, lives=2, skills=["Piercing Shot", "Ambush", "Shadow Arrow"], intelligence=3, dexterity=10, strength=4):
        super().__init__("Rogue", lives, skills, intelligence, dexterity, strength)
        self.equipment = [weapons["Wooden Short Bow"], armour["Leather Armour"]]

    def gear_score(self):
        return Character.calculate_gear_score(self)

class Enemy:
    def __init__(self, name, challenge_rating, skills):
        self.name = name
        self.challenge_rating = challenge_rating
        self.skills = skills

class MossHaggardens(Enemy):
    def __init__(self, challenge_rating, skills, swamp_affinity=True):
        super().__init__("Moss Haggardens", challenge_rating, skills)
        self.swamp_affinity = swamp_affinity

    def acidic_spit(self, target, uses=1):
        self.uses = uses
        if uses > 0:
            damage = randint(2, 4)
            print(f"A glob of acidic spit corrodes you for {damage} acid damage!")
            target.temp_gear_score -= damage
            uses -= 1
        elif uses == 0:
            return
            
class BoneGnashers(Enemy):
    def __init__(self, challenge_rating, skills, bone_crush_attack=True):
        super().__init__("Bone Gnashers", challenge_rating, skills)
        self.bone_crush_attack = bone_crush_attack

    def bone_club_smash(self, target, uses=1):
        self.uses = uses
        if uses > 0:
            damage = int(2 * randint(1, 2))
            print(f"A bone-tipped club swings down, crushing you for {damage} bludgeoning damage!")
            target.temp_gear_score -= damage
        elif uses == 0:
            return

class Whisperers(Enemy):

    def __init__(self, challenge_rating, skills, telepathic_influence=True):
        super().__init__("Whisperers", challenge_rating, skills)
        self.telepathic_influence = telepathic_influence

    def psychic_blast(self, target, uses=1):
        self.uses = uses
        if uses > 0:
            damage = int(3)
            print(f"{self.name}'s mind explodes with force, striking you for {damage} psychic damage!")
            target.gear_score -= damage
        elif uses == 0:
            return

class Gloomweavers(Enemy):
    def __init__(self, challenge_rating, skills, shadow_manipulation=True):
        super().__init__("Gloomweavers", challenge_rating, skills)
        self.shadow_manipulation = shadow_manipulation

    def shadow_lash(self, target, uses=2):
        self.uses = uses
        if uses > 0:
            damage = int(3)
            print(f"Whipping tendrils of darkness lash out at you, inflicting {damage} shadow damage!")
            target.temp_gear_score -= damage
        elif uses == 0:
            return

class Xhoth(Enemy):
    def __init__(self, name="Xhoth", challenge_rating=8, skills=["Consume Essence", "Shadow Tendrils", "Nightmare Visions"]):
        super().__init__(name, challenge_rating, skills)
        self.undying = True

    def consume_essence(self, target):
        # Deal damage and steal life force from the target, healing Xhoth.
        damage = randint(4, 6)
        target.gear_score -= damage
        self.challenge_rating += damage // 2
        print(f"Xhoth drains {damage} life force from {target.name}, growing stronger!")

    def shadow_tendrils(self, target):
        # Restrain the target with shadowy appendages, limiting their movement.
        if randint(1, 20) >= 15:
            print(f"Xhoth's shadow tendrils ensnare {target.name}, restricting their movement!")
        else:
            print("Xhoth's tendrils lash out but miss!")

    def nightmare_visions(self, target):
        # Inflict mental anguish on the target, reducing their attack accuracy.
        if randint(1, 20) >= 12:
            print(f"Xhoth plunges {target.name} into a nightmare, shaking their resolve!")
            target.hit_chance -= 10
        else:
            print("Xhoth's visions flicker harmlessly in {target.name}'s mind.")

print("Welcome, Foolhardy Soul, to Amoria's Embrace.")

menu_option = input("Would you like to venture forth? (y/n): ")

if menu_option == "y":
    print("The call of Amoria beckons you!")
elif menu_option == "n":
    print("A shame, some other time perhaps? Amoria will be waiting...")
    quit()
else: 
    print("Invalid input! Please select y or n.")

player_name = input("What should Amoria know you as, brave adventurer?: ")

classes = {
    "Warrior": {
        "lives": Warrior().lives,
        "gear_score": Warrior().gear_score,
        "skills": ", ".join(Warrior().skills),
    },
    "Rogue": {
        "lives": Rogue().lives,
        "gear_score": Rogue().gear_score,
        "skills": ", ".join(Rogue().skills),
    },
    "Wizard": {
        "lives": Wizard().lives,
        "gear_score": Wizard().gear_score,
        "skills": ", ".join(Wizard().skills),
    },
}

class_menu = PrettyTable(["Class", "Lives", "Gear Score", "Skills"])

for class_name, class_data in classes.items():
    class_menu.add_row([class_name, class_data["lives"], class_data["gear_score"](), class_data["skills"]])

print(class_menu)

class_choice = input(f"{player_name}, please choose your starting class (Warrior, Rogue, Wizard) to begin your descent into Amoria: ").lower()

while class_choice not in ("warrior", "rogue", "wizard"):
    print("Invalid choice. Please choose one of the three classes.")
    class_choice = input(f"{player_name}, please choose your starting class (Warrior, Rogue, Wizard): ").lower()

# Instantiate player based on the chosen class
if class_choice == "warrior":
    player = Warrior()
elif class_choice == "rogue":
    player = Rogue()
elif class_choice == "wizard":
    player = Wizard()

print("The ground beneath your feet shivers with a thousand echoing screams. You stand at the precipice of Amoria, where shadows writhe and madness whispers promises in the wind. This is no mere dungeon, adventurer, but a festering wound upon the world, a gateway to horrors beyond mortal comprehension. \n\nHere, hope withers faster than flowers in winter, and courage curdles under the gaze of things best left unseen. Within these obsidian walls, time bends and twists, sanity unravels like silk in a storm, and death is but a prelude to something far worse.\n\nBut you, it seems, possess a curiosity as sharp as a shard of oblivion. Perhaps you seek forbidden knowledge, or treasures worth kingdoms, or simply the thrill of defying the abyss. Whatever your madness, welcome to Amoria.\n\nMay your steps be swift, your blade ever sharp, and your soul, if you have one left, remain your own until the inevitable, echoing end. \n\nNow, enter... if you dare.")

rooms = {
    "entrance" : {
        "description" : "Amoria's maw gapes, a silent scream carved in stone. Moss, like venomous veins, crawls across the shattered stone entrance. Silence hangs heavy, broken only by dripping.. something, each drop a chilling knell. Dare you enter?",
        "additional description" : "A prickle of unease tingles along your neck. Beyond the entrance, shadows twist and dance, obscuring the grisly tableau of broken wood and broken lives",
        "exits" : {"north" : "passage"}
    }, 
    "passage" : {
        "description" : "A single, skeletal bridge spans the chasm, its bones bleached white, each step a tick against eternity. Below, shadows writhe, unseen eyes glint like poisoned emeralds dancing to the beat of your racing heart.", 
        "additional description" : "As you look around, a sense of unease washes over you in full force. You can see the slight emerald tinge of moss coming creeping out of the opening on the other side of the bridge.",
        "exits" : {"south" : "entrance", "north" : "mossy cavern"}
    }, 
    "mossy cavern" : {
        "description" : "A hushed eye of emerald moss, this cave coils on itself, walls draped in velvet silence. Sunlight bleeds through unseen cracks, staining stone with jade and shadow. The air hangs heavy with damp perfume, whispering promises of secrets and slumbering things.", 
        "additional description" : "Your bare skin tingles, chilled by the velvet touch of silence that drapes the cave. Emerald moss whispers underfoot, and sunlight bleeds through unseen veins, casting jade shadows that dance on the cavern walls. The air, thick with damp perfume, tickles your nostrils, urging you to inhale its secrets.",
        "exits" : {"south" : "passage", "north" : "candle-lit room", "east" : "misty cavern", "west" : "dark cove"}, 
        "items" : [weapons["Iron Sword"], armour["Iron Armour"]], 
        "enemies" : [
            MossHaggardens(8, [MossHaggardens.acidic_spit], True)
            ]
    }, 
    "candle-lit room" : {
        "description" : "A lone flame pierces the gloom, casting long, skeletal shadows that twist and writhe on the floor. The scent of burning wax bleeds into the metallic tang of anticipation, a bitter cocktail in the quiet before the storm.", 
        "additional description" : "Two doors glean against the flickering light; a little one to your front on the left, and a larger, ornate door carved of wooden and latice to your right. Trying the door on your left, it is stuck steadfast, no amount of force will open it. Walking up to the other door, a shiver runs down your spine. Power glows in the vastness behind this door. A small incision opens to the left of the door; a keyhole. Now... where is the key?",
        "exits" : {"south" : "mossy cavern", "north-east" : "Boss Room", "north-west": "Secret Room", "east" : "misty cavern", "west" : "dark cove"}, 
        "items" : [weapons["Iron Sword"], armour["Iron Armour"]], 
        "enemies" : [
            BoneGnashers(10, [BoneGnashers.bone_club_smash], True)
            ], 
        "item use" : [items["Candle Key"]]
    }, 
    "misty cavern" : {
        "description" : "Wispy tendrils of mist weave through the cavern, swallowing light and muffling sound. Each step sinks into unseen depths, sending a shiver up your spine. What lurks within this swirling shroud?", 
        "exits" : {"south" : "mossy cavern", "east" : "dark passageway"}, 
        "items" : [weapons["Iron Sword"], armour["Iron Armour"]], 
        "enemies" : [
            Gloomweavers(12, [Gloomweavers.shadow_lash], True)
        ]
    }, 
    "dark passageway" : {
        "description" : "An unnatural silence hangs in the air, broken only by the soft crunch of your boots on unseen debris. No dripping water, no rustle of unseen creatures, just an oppressive quiet that presses against your ears like a physical weight. You swear you can feel eyes watching from the darkness, unseen and hungry.", 
        "exits" : {"south" : "misty cavern", "north" : "statue room"}, 
        "items" : [items["Candle Key"]], 
        "item use" : [items["Fire Orb"]], 
        "item used" : False, 
        "new exits" : {"south" : "misty cavern", "north" : "statue room", "west" : "Xhoth's Rest"}
    }, 
    "Xhoth's Rest" : {

    },
    "statue room" : {
        "description" : "The scent of cold stone and ancient dust hangs heavy in the air, a shroud woven from forgotten prayers. Statues, frozen in eternal stillness, line the cavern walls. Marble warriors grip rusted swords, their poses contorted in the throes of battle long past. Regal queens stare with vacant eyes, their gilded crowns mocking the passage of time. Grotesque gargoyles leer from shadowed corners, their stone talons poised to snatch, their silent screams etched in the cracks of weathered wings.", 
        "exits" : {"south" : "dark passageway"}, 
        "items" : [items["Fire Orb"]]
    }
}

current_room = "entrance"

player_items = []

def hit_chance(gear_score, challenge_rating): 
    return gear_score + challenge_rating 

def create_menu():
    print("What do you want to do?")
    print("[1] Explore the area")
    print("[2] Use an item")
    print("[3] Open Inventory")
    print("[4] Move")
    choice = input("> ")
    return choice

def game_over():
    # TODO: add in choice to restart the adventure or quit the game
    quit()

def attack_list(enemy):
    print("Please select an action.")

    skill_menu = PrettyTable(["Skill", "Damage", "Uses"])
    for skill, stats in player.skills.items(): 
        skill_menu.add_row([skill, stats["damage"], stats["uses"]])
    print(skill_menu)
    print("Attack")
    attack_choice = input("Make your selection: ").lower()
    match attack_choice:
        case "firebolt":
            if "Firebolt" in player.skills:
                player.Firebolt(enemy)
        case "freezing wind":
            if "Freezing Wind" in player.skills:
                player.Freezing_Wind(enemy)
        case "thunderstrike":
            if "Thunderstike" in player.skills:
                player.Thunderstrike(enemy)
        case "water sense":
            if "Water Sense" in player.skills:  
                player.Watersense(enemy)
                print("Through your connection with the water, you are able to see the skills of your opponent:")
                for enemy in rooms[current_room]["enemies"]:
                    print(enemy.skills)
        case "upwards slash":
            if "Upwards Slash" in player.skills:
                pass
        case "ground smash":
            if "Ground Smash" in player.skills: 
                pass
        case "piercing shot":
            if "Piercing Shot" in player.skills:
                pass
        case "ambush":
            if "Ambush" in player.skills:
                pass
        case "shadow arrow":
            if "Shadow Arrow" in player.skills:
                pass
        case "attack":
            hit_roll = randint(1, 100)
            if hit_roll <= 50:
                enemy.challenge_rating -= 1
                print(f"You landed a blow! The monster's challenge rating is now: {enemy.challenge_rating}")
            else:
                print("Your attack misses.")

def use_item():
    print("What item would you like to use?")
    for item in player_items:
        print(f"{item.name}")
    item_choice = input("> ").lower()
    match item_choice: 
        case "candle key":
            if items["Candle Key"] in rooms[current_room]["item use"]:
                print("Used 'Candle Key'")
                rooms[current_room]["item use"].remove(items["Candle Key"])
                rooms[current_room]["item used"] = True
            else:
                print("This item cannot be used in this room.")
                return
        case "fire orb":
            if items["Fire Orb"] in rooms[current_room]["item use"]:
                print("Used 'Fire Orb'")
                rooms[current_room]["item use"].remove(items["Fire Orb"])
                rooms[current_room]["item used"] = True
            else:
                print("This item cannot be used in this room.")
                return

while True: 
    print(rooms[current_room]["description"])
    
    users_choice = ""

    while users_choice != "4":
        users_choice = create_menu()
        if users_choice == "1":

            if "enemies" in rooms[current_room]:
                enemy = rooms[current_room]["enemies"][0] # Assuming single enemy for now
                print(f"You have run into {enemy.name}! Prepare yourself!")
                combat_loop = True
                player.temp_gear_score = player.gear_score() # Reset gear score for each encounter
                print(player.temp_gear_score)

                while combat_loop:
                    player_action = input("Attack (a) or flee (f)? ").lower()
                    
                    match player_action:
                        case "a":
                            attack_list(enemy)
                        case "f":
                            flee_roll = randint(1, 100)
                            if flee_roll <= 50:
                                print("You escape successfully!")
                                combat_loop = False
                            else:
                                print("The monster blocks your escape! You must fight!")
                                player_action = "a" # Force player to attack
                        case _:
                            print("Invalid action - please choose to either attack or flee!")

                    if enemy.challenge_rating > 0 and combat_loop:
                        if randint(1,10) <= 8:
                            skill_choice = randint(1, len(enemy.skills))
                            enemy.skills[skill_choice - 1](player, player)
                            print(f"Your gear score is currently {player.temp_gear_score}")
                        else:
                            monster_roll = randint(1, 100)
                            if monster_roll <= 50 + enemy.challenge_rating:
                                player.temp_gear_score -= 1
                                print("The monster strikes back! Your gear score is now:", player.temp_gear_score)

                    elif player.temp_gear_score <= 0:
                        print("Defeat!")
                        player.lives -= 1
                        if player.lives <= 0:
                            print("Amoria claims another victim to the Abyss...\n\nGAME OVER")
                            combat_loop = False
                            game_over()
                    elif enemy.challenge_rating <= 0:
                        print(f"Victory! You defeated {enemy.name}!")
                        del rooms[current_room]["enemies"]
                        combat_loop = False

                    else: 
                        print("Something went wrong in the combat loop")

            if "items" in rooms[current_room] and len(rooms[current_room]["items"]) > 0:
                while len(rooms[current_room]["items"]) > 0:
                    for item in rooms[current_room]["items"]:
                        print(f"Something shiny catches your eye. You step closer and find yourself looking at a {item.name}!")
                        user_choice = input("Pick up the item? (y/n) ").lower()
                        match user_choice:
                            case "y":
                                if isinstance(item, Weapon):
                                    player.inventory.append(item)
                                    rooms[current_room]["items"].remove(item)
                                elif isinstance(item, Armour):
                                    player.inventory.append(item)
                                    rooms[current_room]["items"].remove(item)
                                else:
                                    player_items.append(item)
                                    rooms[current_room]["items"].remove(item)
                                break

            else: 
                if rooms[current_room]["additional description"]:
                    print(rooms[current_room]["additional description"])
                else:
                    continue
                print("This area seems bare of any treasure or surprises.")
                continue

        elif users_choice == "2":
            if player_items:
                use_item()
            else: 
                print("You have no items in your inventory.")

        elif users_choice == "3":
            if player.inventory:
                inventory_menu = PrettyTable(["Item", "Value", "Gear Score", "Quantity"])
                for item in player.inventory: 
                    inventory_menu.add_row([item.name, item.value, item.gear_score, item.quantity])
                for item in player_items:
                    inventory_menu.add_row([item.name, item.value, item.gear_score, item.quantity])
                print(inventory_menu)

    exits = list(rooms[current_room]["exits"].keys())
    for exit in exits:
        print(f"- {exit.capitalize()}: {rooms[current_room]['exits'][exit]}")

    action = input("> ").lower()

    if action in exits: 
        current_room = rooms[current_room]["exits"][action]
