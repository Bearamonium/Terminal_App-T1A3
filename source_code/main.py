from random import randint
from prettytable import PrettyTable
from textwrap import TextWrapper
from colorama import Fore, Back, Style

class Inventory_Items: 
    def __init__(self, name, value, quantity=1):
        self.name = name
        self.value = value
        self.quantity = quantity

class Items(Inventory_Items):
    def __init__(self, name, value, quantity=1):
        super().__init__(name, value, quantity)
        self.gear_score = None
        self.type = "item"

items = {
    'Golden Sphere' : Items("Golden Sphere", 0), 
    'Candle Key' : Items("Candle Key", 0), 
    'Fire Orb' : Items("Fire Orb", 5), 
}

class Weapon(Inventory_Items):
    def __init__(self, name, value, gear_score, quantity=1):
        super().__init__(name, value, quantity)
        self.gear_score = gear_score
        self.type = "weapon"

weapons = {
    'Wooden Short Sword' : Weapon("Wooden Sword", 1, 3), 
    'Wooden Short Bow' : Weapon("Wooden Short Bow", 1, 3), 
    'Wooden Staff' : Weapon("Wooden Staff", 3, 3), 
    'Iron Sword' : Weapon("Iron Sword", 1.5, 5), 
    'Elm Short Bow' : Weapon("Elm Short Bow", 1.5, 5), 
    'Elm Staff' : Weapon("Elm Staff", 1.5, 5), 
}

class Armour(Inventory_Items):
    def __init__(self, name, value,gear_score, quantity=1):
        super().__init__(name, value, quantity)
        self.gear_score = gear_score
        self.type = "armour"

armour = {
    'Chainmail Armour' : Armour("Chainmail Armour", 1, 3),
    'Leather Armour' : Armour("Leather Armour", 1, 3),
    'Student Robes' : Armour("Wizard Robes", 1, 3),
    'Iron Armour' : Armour("Iron Armour", 1.5, 5),
    'Studded Leather Armour' : Armour("Studded Leather Armour", 1.5, 5),
    'Silk Robes' : Armour("Silk Robes", 1.5, 5)
}

class NoUsesLeft(Exception):
    pass

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
        return sum(item.gear_score for item in self.equipment.values()) + 2

    def reduce_gear_score(self, damage):
        self.temp_gear_score -= damage

    def attack(self, target):
            hit_roll = randint(1, 100)
            if hit_roll <= 50:
                target.challenge_rating -= 1
                print(f"You landed a blow! The monster's challenge rating is now: {target.challenge_rating}")
            else:
                print("Your attack misses.")

class NightWhisperer(Character):
    def __init__(self, lives=1, skills={}, intelligence=10, dexterity=5, strength=2):
        super().__init__("Night Whisperer", lives, skills, intelligence, dexterity, strength)
        self.equipment = {
            "weapon" : weapons["Wooden Staff"], 
            "armour" : armour["Student Robes"]
        }
        self.skills = {
            "Firebolt" : {"damage" : "1d6", "uses" : 6, "description" : "A swirling orb of molten gold, crackling with miniature lightning bursts. The air around it shimmers with heat distortion, exploding on impact."}, 
            "Freezing Wind" : {"damage": "1d8", "uses" : 5, "description" : "Encases the target in a biting frost, slowing their movements and draining their warmth. Brittle ice creeps across their skin."}, 
            "Phantom Feast" : {"damage" : "2d6", "uses" : 3, "description" : "The target is lured by the ghostly feast, their senses drawn to the illusion of forbidden indulgence. They become sluggish and disoriented, their mind entangled in the phantom delights."}, 
            "Moonlight Barrage" : {"damage" : "2d8 + 1d4", "uses" : 1, "description" : "A shower of shimmering blades form, each etched with moonlight and laced with razor-sharp shadows. They tear through the enemy's defenses and leave trails of moonlight wounds."}
            }
    
    def firebolt(self, target):
        damage = randint(1, 6)
        if player.skills["Firebolt"]["uses"] > 0:
            print(f"You draw your hand in a swift arc, concentrating darkness into a blazing sphere and hurl towards the enemy with a whispered curse.")
            print(f"Your sphere explodes against {target.name}, dealing {damage} fire damage.")
            target.challenge_rating -= damage
            player.skills["Firebolt"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def freezing_wind(self, target):
        damage = randint(1, 8)
        if player.skills["Freezing Wind"]["uses"] > 0:
            print("Lips trembling with a whispered frost-spell, a frigid gust rips from your palms. Blades of ice dance toward your enemy within the wind.")
            print(f"Your spell strikes {target.name}, dealing {damage} ice damage.")
            target.challenge_rating -= damage
            player.skills["Freezing Wind"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def phantom_feast(self, target):
        damage = randint(1, 6) + randint(1, 6)
        if player.skills["Phantom Feast"]["uses"] > 0:
            print("You weave the shadows into a spectral feast, a low-pitched, hypnotic chant escaping from your lips as you ensnare the target in your illusion.")
            print(f"{target.name} suffers {damage} illusion damage.")
            target.challenge_rating -= damage
            player.skills["Phantom Feast"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def moonlight_barrage(self, target):
        damage = randint(1, 8) + randint(1, 8) + randint(1, 4)
        if player.skills["Moonlight Barrage"]["uses"] > 0:
            print("You raise your hand, shadows and moonlight swirling around them to create a storm of uncast shadows.")
            print(f"You unleash a volley of spectral blades, piercing {target.name} for {damage} raw magic damage.")
            target.challenge_rating -= damage
            player.skills["Moonlight Barrage"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def gear_score(self):
        return Character.calculate_gear_score(self)

class CrimsonBlade(Character):
    def __init__(self, lives=1, skills={}, intelligence=2, dexterity=5, strength=10):
        super().__init__("Crimson Blade", lives, skills, intelligence, dexterity, strength)
        self.equipment = {
            "weapon" : weapons["Wooden Short Sword"], 
            "armour" : armour["Chainmail Armour"]
        }
        self.skills = {
            "Bloodbath Barrage" : {"damage" : "1d6", "uses" : 8, "description" : "Tear through your enemies with your blade, painting the air with bloody mist."}, 
            "Crimson Cleaver" : {"damage" : "3d6", "uses" : 4, "description" : "Produce a shockwave that cracks the ground, flinging your target/s into the air."}
        }

    def bloodbath_barrage(self, target): 
        damage = randint(1, 6)
        if player.skills["Bloodbath Barrage"]["uses"] > 0:
            print("You swiftly unleash your blade, whirling into a crimson-soaked cyclone as you scream towards your enemy.")
            print(f"{target.name} suffers {damage} physical damage.")
            target.challenge_rating -= damage
            player.skills["Bloodbath Barrage"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def crimson_cleaver(self, target):
        damage = randint(1, 6) + randint(1, 6) + randint(1, 6)
        if player.skills["Crimson Cleaver"]["uses"] > 0:
            print("The ground trembles as you slams their weapon into the earth. A crimson shockwave erupts, cracking the ground and sending tremors that ripple outward.")
            print(f"{target.name} fails to escape your shockwave, dealing {damage} physical damage.")
            target.challenge_rating -=damage
            player.skills["Crimson Cleaver"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def gear_score(self):
        return Character.calculate_gear_score(self)

class SunsHunter(Character):
    def __init__(self, lives=1, skills={}, intelligence=3, dexterity=10, strength=4):
        super().__init__("Sun's Hunter", lives, skills, intelligence, dexterity, strength)
        self.equipment = {
            "weapon" : weapons["Wooden Short Bow"], 
            "armour" : armour["Leather Armour"]
        }
        self.skills = {
            "Hymn of Helios" : {"damage" : "1d6 + 1d4", "uses" : 5, "description" : "Channel the blinding brilliance of the sun, firing a searing arrow leaving smoldering trails in its wake."}, 
            "Sun's Ire" : {"damage": "2d6", "uses" : 4, "description" : "Unleash a scorching arrow imbued with solar fury, exploding on impact and dealing heavy damage to a small area."}, 
            "Hunter's Volley" : {"damage" : "3d8", "uses" : 1, "description" : "Launch a rapid succession of precise arrows, peppering enemies with a hail of feathers and steel."}
            }

    def hymn_of_helios(self, target):
        damage = randint(1, 6) + randint(1, 4)
        if player.skills["Hymn of Helios"]["uses"] > 0:
            print(f"As you draw your bow, light gathers around your arrowhead with the fierceness of the sun as you unleash your arrow, chanting the Sun's blessing.")
            print(f"You strike true, dealing {damage} fire damage to {target.name}.")
            target.challenge_rating -= damage
            player.skills["Hymn of Helios"]["uses"] -= 1
        else: 
            raise NoUsesLeft
    def suns_ire(self, target):
        damage = randint(1, 6) + randint(1, 6)
        if player.skills["Sun's Ire"]["uses"] > 0:
            print("Gritting your teeth and drawing on the Sun's power, you unleashe a devastating solar projectile towards your target.")
            print(f"Finding your mark, {target.name} suffers {damage} fire damage.")
            target.challenge_rating -= damage
            player.skills["Sun's Ire"]["uses"] -= 1
        else: 
            return NoUsesLeft

    def hunters_volley(self, target):
        damage = randint(1, 8) + randint(1, 8) + randint(1, 8)
        if player.skills["Hunter's Volley"]["uses"] != 0:
            print(f"You unleash a storm of sun-kissed arrows, each shot finding their mark without effort.")
            print(f"{target.name} suffers {damage} ranged damage.")
            target.challenge_rating -= damage
            player.skills["Hunter's Volley"]["uses"] -= 1
        else: 
            raise NoUsesLeft

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

    def acidic_spit(self, target, uses=3):
        self.uses = uses
        if uses > 0:
            damage = randint(2, 3)
            print(f"A glob of acidic spit corrodes you for {damage} acid damage!")
            target.temp_gear_score -= damage
            uses -= 1
        elif uses == 0:
            return NoUsesLeft
            
class BoneGnashers(Enemy):
    def __init__(self, challenge_rating, skills, bone_crush_attack=True):
        super().__init__("Bone Gnashers", challenge_rating, skills)
        self.bone_crush_attack = bone_crush_attack

    def bone_club_smash(self, target, uses=3):
        self.uses = uses
        if uses > 0:
            damage = int(2 * randint(1, 2))
            print(f"A bone-tipped club swings down, crushing you for {damage} bludgeoning damage!")
            target.temp_gear_score -= damage
        elif uses == 0:
            return NoUsesLeft

class Whisperers(Enemy):

    def __init__(self, challenge_rating, skills, telepathic_influence=True):
        super().__init__("Whisperers", challenge_rating, skills)
        self.telepathic_influence = telepathic_influence

    def psychic_blast(self, target, uses=3):
        self.uses = uses
        if uses > 0:
            damage = randint(2, 3)
            print(f"The creature's mind explodes with force, striking you for {damage} psychic damage!")
            target.temp_gear_score -= damage
        elif uses == 0:
            return NoUsesLeft

class Gloomweavers(Enemy):
    def __init__(self, challenge_rating, skills, shadow_manipulation=True):
        super().__init__("Gloomweavers", challenge_rating, skills)
        self.shadow_manipulation = shadow_manipulation

    def shadow_lash(self, target, uses=2):
        self.uses = uses
        if uses > 0:
            damage = randint(2, 3)
            print(f"Whipping tendrils of darkness lash out at you, inflicting {damage} shadow damage!")
            target.temp_gear_score -= damage
        elif uses == 0:
            return NoUsesLeft

class Xhoth(Enemy):
    def __init__(self, name="Xhoth", challenge_rating=8, skills=["Consume Essence", "Shadow Tendrils", "Nightmare Visions"]):
        super().__init__(name, challenge_rating, skills)
        self.undying = True

    def consume_essence(self, target):
        # Deal damage and steal life force from the target, healing Xhoth.
        damage = randint(2, 4)
        target.temp_gear_score -= damage
        self.challenge_rating += damage // 2
        print(f"Xhoth drains {damage} life force from {target.name}, growing stronger!")

    def shadow_claws(self, target):
        damage = randint(3, 5)
        target.temp_gear_score -= damage
        print(f" Xhoth's shadow extends, forming claw-like appendages that slash at you from multiple angles, dealing {damage} shadow damage.")

    def night_terror(self, target, uses=1):
        damage = randint(3, 6)
        if uses > 0:
            target.temp_gear_score -= damage
            print(f"Xhoth traps you in a living nightmare, inflicting {damage} shadow damage.")
        else:
            print(f"Xhoth's visions flicker harmlessly in your mind.")
            return NoUsesLeft

def boss_Xhoth():
    pass

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

def explore_room():
    if "additional description" in rooms[current_room]:
        print(rooms[current_room]["additional description"])

    if current_room is rooms["Boss Room"]:
        boss_Xhoth()

    if "enemies" in rooms[current_room]:
        enemy = rooms[current_room]["enemies"][0] # Assuming single enemy for now
        print(f"You have run into {enemy.name}! Prepare yourself!")
        start_combat(enemy)

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
                            player.inventory.append(item)
                            rooms[current_room]["items"].remove(item)
                        break

    else: 
        print("This area seems bare of any treasure or surprises.")

def game_over():
    # TODO: add in choice to restart the adventure or quit the game
    quit()

def attack_list(enemy):

    print("Please select an action.")

    skill_menu = PrettyTable(["Skill", "Damage", "Uses", "Description"])
    for skill, stats in player.skills.items(): 
        skill_menu.add_row([skill, stats["damage"], stats["uses"], stats["description"]])
    skill_menu.add_row(["Basic Attack", 1, "-", "You attack with your current equipped weapon."])
    print(skill_menu)
    while True: 
        attack_choice = input("Make your selection: ").lower()
        match attack_choice:
            case "firebolt":
                if "Firebolt" in player.skills:
                    player.firebolt(enemy)
                    break
            case "freezing wind":
                if "Freezing Wind" in player.skills:
                    player.freezing_wind(enemy)
                    break
            case "phantom feast":
                if "Phantom Feast" in player.skills:
                    player.phantom_feast(enemy)
                    break
            case "moonlight barrage":
                if "Moonlight Barrage" in player.skills:  
                    player.moonlight_barrage(enemy)
                    break
            case "bloodbath barrage":
                if "Bloodbath Barrage" in player.skills:
                    player.bloodbath_barrage(enemy)
                    break
            case "crimson cleaver":
                if "Crimson Cleaver" in player.skills: 
                    player.crimson_cleaver(enemy)
                    break
            case "hymn of helios":
                if "Hymn of Helios" in player.skills:
                    player.hymn_of_helios(enemy)
                    break
            case "sun's ire":
                if "Sun's Ire" in player.skills:
                    player.suns_ire(enemy)
                    break
            case "hunter's volley":
                if "Hunter's Volley" in player.skills:
                    player.hunters_volley(enemy)
                    break
            case "attack":
                player.attack(enemy)
                break
            case _:
                print("Invalid entry. Please try again.")

def use_item():

    usable_items = [item.name for item in player.inventory if isinstance(item, Items)]
    if usable_items:
        print("What item would you like to use?")
        for item_name in usable_items:
            print(item_name)

        while True: 
            item_choice = input("> ").lower()
            match item_choice: 
                case "candle key":
                    if items["Candle Key"] in rooms[current_room]["item use"]:
                        print("Used 'Candle Key'.")
                        print("You place the key gently in the opening on the door, pushing it outwards until a loud click is heard. The ground beneath you trembles as the door cracks in half, illuminating the room in a crude obsidian light. Fear reaches for you, for your soul, as the light grows brighter. But it's not your fear. It's the fear of the fallen beyond this door. The fear of the defeated, the agony of their loss, washes over you in waves. The stench of dread and despair grows stronger as the crack seeping obsidian all but disintigrates the door, leaving a solid stone archway, paving your fate for better or worse.")
                        rooms[current_room]["item use"].remove(items["Candle Key"])
                        rooms[current_room]["exits"] = rooms[current_room]["item used exits"]
                        return
                    else:
                        print("This item cannot be used in this room.")
                        return
                case "fire orb":
                    if items["Fire Orb"] in rooms[current_room]["item use"]:
                        print("Used 'Fire Orb'.")
                        print("A soft click can be heard, along with the scraping sound of stone shifting and sliding against itself.")
                        rooms[current_room]["item use"].remove(items["Fire Orb"])
                        rooms[current_room]["exits"] = rooms[current_room]["item used exits"]
                        return
                    else:
                        print("This item cannot be used in this room.")
                        return
                case "golden sphere":
                    print("This item cannot be used yet.")
                    return
                case _:
                    print("Please select one of the available items to use.")
    else: 
        print("You currently have no items available for use.")

def manage_inventory():
    while True: 
        print("\nInventory:")
        for i, item in enumerate(player.inventory):
            print(f"{i+1}. {item.name} ({item.type})")
        
        print("\nEquipped Items:")
        for slot, item in player.equipment.items():
            print(f"{slot.capitalize()}: {item.name}")

        print("\nChoose an action:")
        print("1. Equip an item.")
        print("2. Unequip an item.")
        print("3. Use an item.")
        print("4. Quit.")

        choice = input("> ")

        if choice == "1": 
            while True:
                try: 
                    item_index = int(input("Enter the number of the item you want to equip: ")) - 1
                    item = player.inventory[item_index]
                    equip_item(item)
                    break
                except (ValueError, IndexError):
                    print("Invalid Choice. Please enter a valid item number.")
        elif choice == "2":
            unequip_item()
        elif choice == "3":
            use_item()
        elif choice == "4":
            break
        else: 
            print("Invalid choice. Please enter a number between 1 and 4.")

def unequip_item(item):
    slot = input("Choose a slot to unequip: ")
    if slot in player.equipment: 
        item = player.equipment[slot]
        player.inventory.append(item)
        del player.equipment[slot]
        print(f"{item.name} unequipped successfully.")
    else: 
        print("Invalid slot.")

def equip_item(item):
    if isinstance(item, Weapon):
        equip_weapon(item)
    elif isinstance(item, Armour):
        equip_armour(item)
    else: 
        print("Invalid item type.")

def equip_weapon(weapon):
    if "weapon" not in player.equipment: 
        player.equipment["weapon"] = weapon
        player.inventory.remove(weapon)
        print("Weapon equipped successfully.")
    else: 
        unequip_choice = input(f"You already have a weapon equipped. Unequip {player.equipment['weapon'].name}? (y/n): ")
        if unequip_choice.lower() == "y":
            unequip_item("weapon")
            equip_weapon(weapon)

def equip_armour(armour):
    if "armour" not in player.equipment: 
        player.equipment["armour"] = armour
        player.inventory.remove(armour)
        print("Armour equipped successfully.")
    else: 
        unequip_choice = input(f"You already have armour equipped. Unequip {player.equipment['armour'].name}? (y/n): ")
        if unequip_choice.lower() == "y":
            unequip_item("armour")
            equip_armour(armour)

def start_combat(enemy):
    global in_combat
    player.temp_gear_score = player.gear_score() # Reset Gear Score for each encounter seeing as healing hasn't been intialised in this game
    in_combat = True

    while in_combat: 

        # Players Turn
        while True: 
            player_action = input("Attack (a) or Flee (f)? ").lower()
            if player_action in ("a", "f"):
                break
            else: 
                print("Invalid response. Please enter 'a' or 'f'.")

        if player_action == "a" or (player_action == "f" and flee_failed(enemy)):
            while True: 
                if player_action == "f" and flee_failed(enemy):
                    print("Oh no! The monster has blocked your escape - you have no choice but to attack!")
                try:
                    attack_list(enemy)
                    if enemy.challenge_rating <= 0:
                        print(f"Victory! You defeated {enemy.name}!")
                        del rooms[current_room]["enemies"]
                        in_combat = False
                    break
                except NoUsesLeft: 
                    print("No more uses left for that skill! Choose another action.")

        else:
            print("You have escaped successfully.")
            in_combat = False

        if in_combat and enemy.challenge_rating > 0:
            if randint(1, 10) <= 8:
                skill_choice = randint(1, len(enemy.skills))
                enemy.skills[skill_choice - 1](player, player)
                print(f"Your gear score is currently {player.temp_gear_score}.")
            else: 
                monster_roll = randint(1, 100)
                if monster_roll <= 70 + enemy.challenge_rating: 
                    player.temp_gear_score -= 2
                    print("The monster strikes back! Your gear score is now:", player.temp_gear_score)
            if player.temp_gear_score <= 0:
                print("Defeat!")
                player.lives -= 1
                if player.lives <= 0:
                    print("Amoria claims another victim to the Abyss...\n\nGAME OVER")
                    in_combat = False
                    game_over()

        if not in_combat: 
            print("Exiting combat.")

def flee_failed(enemy):
    flee_roll = randint(1, 100)
    return flee_roll > 50

rooms = {
    "entrance" : {
        "description" : "Amoria's maw gapes, a silent scream carved in stone. Moss, like venomous veins, crawls across the shattered stone entrance. Silence hangs heavy, broken only by dripping.. something, each drop a chilling knell.",
        "additional description" : "Beyond the entrance, shadows twist and dance as they call upon you to enter the depths of Amoria.",
        "exits" : {"north" : "passage"}
    }, 
    "passage" : {
        "description" : "A single, skeletal bridge spans the chasm, its bones bleached white. With a tentative step, the aged-decayed wood groans in protest under your feet. A quick glance into the abyss below, shadows writhe with unseen eyes glinting like poisoned emeralds.", 
        "additional description" : "As you look around, a sense of unease washes over you in full force. You can see the slight emerald tinge of moss coming creeping out of the opening on the other side of the bridge.",
        "exits" : {"south" : "entrance", "north" : "mossy room"}
    }, 
    "mossy room" : {
        "description" : "The room you enter coils in on itself, walls draped in emerald moss. The eerie silence of your surroundings is only broken by the what seems to be the slight groan of a tree trunk bending to the wind... Wind?.", 
        "additional description" : "The emerald moss begins to whisper under your feet as you bravely fenture further into the room, sunlight bleeding through the slim cracks in the ceiling, casting a dance of shadows around the room. The air, thick with the damp perfume of earth, tickles your nostrils.",
        "exits" : {"south" : "passage", "north" : "candle-lit room", "east" : "misty cavern", "west" : "dark cove"}, 
        "items" : [armour["Studded Leather Armour"]], 
        "enemies" : [
            MossHaggardens(8, [MossHaggardens.acidic_spit], True)
            ]
    }, 
    "candle-lit room" : {
        "description" : "A lone flame pierces the gloom, casting long, skeletal shadows that twist and writhe on the floor. The scent of burning wax bleeds into the metallic tang of anticipation, a bitter cocktail in the quiet before the storm.", 
        "additional description" : "Two doors glean against the flickering light; a little one to your front on the left, and a larger, ornate door carved of wooden and latice to your right. Trying the door on your left, it is stuck steadfast, no amount of force will open it. Walking up to the other door, a shiver runs down your spine. Power glows in the vastness beyond. A small incision opens to the left of the door; a keyhole. Now... where is the key?",
        "exits" : {"south" : "mossy room"}, 
        "items" : [weapons["Iron Sword"]], 
        "enemies" : [
            BoneGnashers(10, [BoneGnashers.bone_club_smash], True)
            ], 
        "item use" : [items["Candle Key"]],
        "item used exits" : {"south" : "mossy room", "north-east" : "Boss Room"}
    }, 
    "misty cavern" : {
        "description" : "Wispy tendrils of mist weave through the cavern, swallowing light and muffling sound. Each step sinks into unseen depths, sending a shiver up your spine. What lurks within this swirling shroud?", 
        "exits" : {"west" : "mossy room", "east" : "dark passageway"}, 
        "enemies" : [
            Gloomweavers(10, [Gloomweavers.shadow_lash], True)
        ]
    }, 
    "dark cove" : {
        "description" : "On first glance, nothing sets the space apart from a regular cave, until you lay eyes on the shrine located in the dead center. The shrine pulses with an unnatural luminescence, emanating from moss-coated runes etched into its obsidian surface. Shadows swirl around it's edges, paired with an unsettling hum resonating through the air that vibrates your bones with each pulse of the shrine's mysterious glow. This is no ordinary cave.",
        "additional description" : "Whispers, thin as frost, slither through the air, twisting your name with malice. You can't discern their source, but they prickle your skin with the promise of unseen danger.",
        "exits" : {"east" : "mossy room"},
        "items" : [weapons["Elm Short Bow"], items["Golden Sphere"]],
        "enemies" : [
            Whisperers(10, [Whisperers.psychic_blast], True)
        ]
    },
    "dark passageway" : {
        "description" : "An unnatural silence hangs in the air, broken only by the soft crunch of your boots on unseen debris. No dripping water, no rustle of unseen creatures, just an oppressive quiet that presses against your ears like a physical weight. You swear you can feel eyes watching from the darkness, unseen and hungry, but see nothing. What lurks within these walls?", 
        "exits" : {"north" : "misty cavern", "south" : "statue room"}, 
        "item use" : [items["Fire Orb"]],
        "item used exits" : {"north" : "misty cavern", "south" : "statue room", "east" : "Xhoth's Rest"}
    }, 
    "Xhoth's Rest" : {
        "description" : "Darkness envelops you as you step inside, only broken by the gleaming visage of a... candle, flickering in the center of the room. Shadows cast appear to move against the sharp dance of the flame, mockingly inviting you to continue stepping foward.", 
        "exits" : {"west" : "dark passageway"},
        "items" : {armour["Silk Robes"], items["Candle Key"]},
        "enemies" : [
            Whisperers(15, [Whisperers.psychic_blast], True)
        ]
    },
    "statue room" : {
        "description" : "The scent of cold stone and ancient dust hangs heavy in the air, a shroud woven from forgotten prayers. Statues, frozen in eternal stillness, line the cavern walls. Marble warriors grip rusted swords, their poses contorted in the throes of battle long past. Regal queens stare with vacant eyes, their gilded crowns mocking the passage of time. Grotesque gargoyles leer from shadowed corners, their stone talons poised to snatch, their silent screams etched in the cracks of weathered wings.", 
        "exits" : {"north" : "dark passageway"}, 
        "items" : [items["Fire Orb"], weapons["Elm Staff"]],
        "enemies" : [
            Gloomweavers(14, [Gloomweavers.shadow_lash], True)
        ]
    },
    "Boss Room" : {
        "description" : "Blind step. Cold stone. Candlelight flickers, painting the darkness with shapes that shift and leer. A throne sits crooked, a bone crown atop its skull-grin back, with Xhoth perched upon it. This, this is Xhoth's pathetic stand. His own bone crown askew, he resembles a spider in a crumbling web. Candlelight dances on his carapace, glinting off obsidian teeth in a grin that chills the air. He's all angles and shadows, a puppet king in a kingdom of dust. Ready? Or will you walk over his ashes and claim the deeper dread?",
        "boss" : [
            Xhoth(20, [Xhoth.consume_essence, Xhoth.night_terror, Xhoth.shadow_claws], True)
        ]
    }
}

current_room = "entrance"

classes = {
    "Crimson Blade": {
        "lives": CrimsonBlade().lives,
        "gear_score": CrimsonBlade().gear_score,
        "skills": ", ".join(CrimsonBlade().skills),
    },
    "Sun's Hunter": {
        "lives": SunsHunter().lives,
        "gear_score": SunsHunter().gear_score,
        "skills": ", ".join(SunsHunter().skills.keys()),
        },
    "Night Whisperer": {
        "lives": NightWhisperer().lives,
        "gear_score": NightWhisperer().gear_score,
        "skills": ", ".join(NightWhisperer().skills),
    },
}

print(Fore.BLACK,Back.WHITE+"Welcome, Foolhardy Soul, to Amoria's Embrace.")

menu_option = input("Would you like to venture forth? (y/n): ")

if menu_option == "y":
    print("The call of Amoria beckons you!")
elif menu_option == "n":
    print("A shame, some other time perhaps? Amoria will be waiting...")
    quit()
else: 
    print("Invalid input! Please select y or n.")

player_name = input(Fore.RED+"What should Amoria know you as, brave adventurer?: ")

class_menu = PrettyTable(["Class", "Lives", "Gear Score", "Skills"])

for class_name, class_data in classes.items():
    class_menu.add_row([class_name, class_data["lives"], class_data["gear_score"](), class_data["skills"]])

print(class_menu)

class_choice = input(f"{player_name}, please choose your starting class (Crimson Blade, Sun's Hunter, Night Whisperer) to begin your descent into Amoria: ").lower()

while class_choice not in ("crimson blade", "sun's hunter", "night whisperer"):
    print("Invalid choice. Please choose one of the three classes.")
    class_choice = input(f"{player_name}, please choose your starting class (Warrior, Rogue, Wizard): ").lower()

# Instantiate player based on the chosen class
if class_choice == "crimson blade":
    player = CrimsonBlade()
elif class_choice == "sun's hunter":
    player = SunsHunter()
elif class_choice == "night whisperer":
    player = NightWhisperer()

print("The ground beneath your feet shivers with a thousand echoing screams. You stand at the precipice of Amoria, where shadows writhe and madness whispers promises in the wind. This is no mere dungeon, adventurer, but a festering wound upon the world, a gateway to horrors beyond mortal comprehension. \n\nHere, hope withers faster than flowers in winter, and courage curdles under the gaze of things best left unseen. Within these obsidian walls, time bends and twists, sanity unravels like silk in a storm, and death is but a prelude to something far worse.\n\nBut you, it seems, possess a curiosity as sharp as a shard of oblivion. Perhaps you seek forbidden knowledge, or treasures worth kingdoms? Or do you walk a different path, one that will find you face to face with T'halth, the crusader of madness that lurks beneath your feet? Whatever reasoning, we welcome you with open arms to Amoria.\n\nMay your steps be swift, and your soul, if you have one left, remain your own until your inevitable, echoing end.")

while True: 
    print(rooms[current_room]["description"])

    while True:
        users_choice = create_menu()

        if users_choice in ["1", "2", "3"]:
            actions = {
                "1" : explore_room, 
                "2" : use_item,
                "3" : manage_inventory
            }
            actions[users_choice]()

            users_choice = ""

        elif users_choice == "4":
            break

        else: 
            print("Invalid choice. Please select a valid option from the menu.")
            users_choice = ""

    exits = list(rooms[current_room]["exits"].keys())
    for exit in exits:
        print(f"- {exit.capitalize()}: {rooms[current_room]['exits'][exit]}")

    action = input("> ").lower()

    if action in exits: 
        current_room = rooms[current_room]["exits"][action]
