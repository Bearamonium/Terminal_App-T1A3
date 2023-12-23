from random import randint
from prettytable import PrettyTable
import textwrap
from colorama import Fore, Style, Back
from inventory_items import Items, Weapon, Armour, items, weapons, armour
from character import CrimsonBlade, NightWhisperer, SunsHunter, NoUsesLeft
from enemies import MossHaggardens, Whisperers, Gloomweavers, BoneGnashers, Xhoth

def initialise_game():
    player = None
    player_name = None

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
            "enemies" : [
                Xhoth(20, [Xhoth.consume_essence, Xhoth.night_terror, Xhoth.shadow_claws], True)
            ]
        }
    }
    
    current_room = "entrance"
    return player, player_name, rooms, current_room

player_name, player, rooms, current_room = initialise_game()

class GameOverException(Exception):
    pass

def start_game():
    global player

    print(Style.BRIGHT + "Welcome, Foolhardy Soul, to Amoria's Embrace.")

    menu_option = input("Would you like to venture forth? (y/n): ")

    if menu_option == "y":
        print("The call of Amoria beckons you!")
    elif menu_option == "n":
        print("A shame, some other time perhaps? Amoria will be waiting...")
        quit()
    else: 
        print("Invalid input! Please select y or n.")

    player = class_menu(player)

    print(Fore.BLACK + text_wrapper.fill("""
        The ground beneath your feet shivers with a thousand echoing screams. You stand at the precipice of Amoria, where shadows writhe and madness whispers promises in the wind. This is no mere dungeon, adventurer, but a festering wound upon the world, a gateway to horrors beyond mortal comprehension.
    """))
    print(text_wrapper.fill("""Here, hope withers faster than flowers in winter, and courage curdles under the gaze of things best left unseen. Within these obsidian walls, time bends and twists, sanity unravels like silk in a storm, and death is but a prelude to something far worse.
    """))
    print(text_wrapper.fill("""But it seems that you possess a curiosity as sharp as a shard of oblivion. Perhaps you seek forbidden knowledge, or treasures worth kingdoms? Or do you walk a different path, one that will find you face to face with T'halth, the crusader of madness that lurks beneath your feet?
    """))
    print(text_wrapper.fill("""Whatever reasoning, we welcome you with open arms to Amoria. May your steps be swift, and your soul, if you have one left, remain your own until your inevitable, echoing end.
    """))

    while True: 
        global current_room
        try:      
            print(Fore.GREEN + text_wrapper.fill(rooms[current_room]["description"]))

            if current_room == "Boss Room":
                boss_Xhoth()

            while True:
                users_choice = create_menu()

                if users_choice in ["1", "2"]:
                    actions = {
                        "1" : explore_room, 
                        "2" : manage_inventory
                    }
                    actions[users_choice]()

                    users_choice = ""

                elif users_choice == "3":
                    break

                else: 
                    print("Invalid choice. Please select a valid option from the menu.")
                    users_choice = ""

            while True:
                exits = list(rooms[current_room]["exits"].keys())
                for exit in exits:
                    print(f"- {exit.capitalize()}: {rooms[current_room]['exits'][exit]}")

                action = input("> ").lower()

                if action in exits: 
                    current_room = rooms[current_room]["exits"][action]
                    break
                elif action not in exits: 
                    print("Invalid response. Please enter one of the available exits to continue.")

        except GameOverException:
            game_over()

        except Exception as e:
            print("An unexpected error occured:", e)
            choice = input("Would you like to try restarting? (y/n): ")
            if choice.lower() == "y":
                restart_game()
            else: 
                raise

def class_menu(player):

    player_name = input(Fore.GREEN + "What should Amoria know you as, brave adventurer?: ")

    class_menu = PrettyTable(["Class", "Lives", "Gear Score", "Skills"])

    for class_name, class_data in classes.items():
        class_menu.add_row([
            Fore.WHITE + class_name, 
            Fore.YELLOW + str(class_data["lives"]), 
            Fore.CYAN + str(class_data["gear_score"]()), 
            Fore.WHITE + class_data["skills"]])

    print(class_menu, Fore.RESET)

    class_choice = input(f"{player_name}, please choose your starting class (Crimson Blade, Sun's Hunter, Night Whisperer) to begin your descent into Amoria: ").lower()

    while class_choice not in ("crimson blade", "sun's hunter", "night whisperer"):
        print("Invalid choice. Please choose one of the three classes.")
        class_choice = input(f"{player_name}, please choose your starting class (Crimson Blade, Sun's Hunter, Night Whisperer): ").lower()

    if class_choice == "crimson blade":
        player = CrimsonBlade()
    elif class_choice == "sun's hunter":
        player = SunsHunter()
    elif class_choice == "night whisperer":
        player = NightWhisperer()
    return player

def create_menu():
    print(Fore.BLUE)
    print("What do you want to do?")
    print("[1] Explore the area")
    print("[2] Open Inventory")
    print("[3] Move")
    print(Fore.RESET)
    choice = input("> ")
    return choice

def hit_chance(gear_score, challenge_rating): 
    return gear_score + challenge_rating 

def attack_list(enemy):

    print("Please select an action.")

    skill_menu = PrettyTable(["Skill", "Damage", "Uses", "Description"])
    for skill, stats in player.skills.items(): 
        skill_menu.add_row([skill, stats["damage"], stats["uses"], stats["description"]])
    skill_menu.add_row(["Attack", "1d4", "-", "You attack with your current equipped weapon."])
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

def explore_room():
    if "additional description" in rooms[current_room]:
        print(Fore.YELLOW + text_wrapper.fill(rooms[current_room]["additional description"]))

    if "enemies" in rooms[current_room]:
        enemy = rooms[current_room]["enemies"][0] # Assuming single enemy for now
        print(Fore.LIGHTRED_EX + f"You have run into {enemy.name}! Prepare yourself!" + Fore.RESET)
        start_combat(enemy)

    if "items" in rooms[current_room] and len(rooms[current_room]["items"]) > 0:
        while len(rooms[current_room]["items"]) > 0:
            for item in rooms[current_room]["items"]:
                print(Fore.LIGHTCYAN_EX + f"Something shiny catches your eye. You step closer and find yourself looking at a {item.name}!" + Fore.RESET)
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

def boss_Xhoth():
    print(f"XHOTH: {player_name}, welcome to your final resting place.")
    enemy = rooms[current_room]["boss"][0]
    start_combat(enemy)
    print("Silence. A single ray of light pierces the gloom, illuminating the dust motes dancing in its path. Victory, but at what cost? The weight of the journey settles, a bittersweet blend of triumph and loss. But, Xhoth was just the first step on your hellish journey, and Amoria can't be kept waiting...")
    print("You have successfully cleared the first floor of Amoria! Thank you for playing and we hope you will be eager to return and continue your players journey on the second floor of Amoria, for the real danger has only just begun.")
    game_over()

def game_over():
    choice = input("Would you like to restart the adventure or quit the game? (r/q): ")
    if choice.lower() == "r":
        restart_game()
    else:
        quit()

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
                        break
                    else:
                        print("This item cannot be used in this room.")
                        break
                case "fire orb":
                    if items["Fire Orb"] in rooms[current_room]["item use"]:
                        print("Used 'Fire Orb'.")
                        print("A soft click can be heard, along with the scraping sound of stone shifting and sliding against itself.")
                        rooms[current_room]["item use"].remove(items["Fire Orb"])
                        rooms[current_room]["exits"] = rooms[current_room]["item used exits"]
                        break
                    else:
                        print("This item cannot be used in this room.")
                        break
                case "golden sphere":
                    print("This item cannot be used yet.")
                    break
                case _:
                    print("Please select one of the available items to use.")
    else: 
        print("You currently have no items available for use.")

def manage_inventory():
    while True: 
        print("\nInventory:")
        for i, item in enumerate(player.inventory):
            print(Fore.BLUE + text_wrapper.fill(f"{i+1}. {item.name} ({item.type})"))
        
        print("\nEquipped Items:")
        for slot, item in player.equipment.items():
            print(Fore.RED + text_wrapper.fill(f"{slot.capitalize()}: {item.name}"))

        print(Fore.BLUE + "\nChoose an action:")
        print("1. Equip an item.")
        print("2. Unequip an item.")
        print("3. Use an item.")
        print("4. Quit." + Fore.RESET)

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
    player.temp_gear_score = player.gear_score() # Reset Gear Score for each encounter 
    in_combat = True

    while in_combat: 

        # Players Turn
        while True: 
            player_action = input("Attack (a) or Flee (f)? ").lower()
            if player_action in ("a", "f"):
                break
            else: 
                print("Invalid response. Please enter 'a' or 'f'.")

        if player_action == "a":
            try:
                attack_list(enemy)
                if enemy.challenge_rating <= 0:
                    print(f"Victory! You defeated {enemy.name}!")
                    del rooms[current_room]["enemies"]
                    in_combat = False
                    break
            except NoUsesLeft:
                print("No more uses left for that skill! Choose another action.")
                # Player's turn continues
        elif player_action == "f":
            if flee_failed():
                print("Oh no! The monster has blocked your escape - you must attack!")
                while True: 
                    try:
                        attack_list(enemy)
                        if enemy.challenge_rating <= 0:
                            print(f"Victory! You defeated {enemy.name}!")
                            del rooms[current_room]["enemies"]
                            in_combat = False
                            break
                        break
                    except NoUsesLeft:
                        print("No more uses left for that skill! Choose another action.")                        
            else:
                print("You have escaped successfully.")
                in_combat = False
                break

        if in_combat and enemy.challenge_rating > 0:
            if randint(1, 10) <= 8:
                skill_choice = randint(1, len(enemy.skills))
                enemy.skills[skill_choice - 1](player, player)
                print(f"Your gear score is currently {player.temp_gear_score}.")
            else: 
                monster_roll = randint(1, 100)
                if monster_roll <= 70 + enemy.challenge_rating: 
                    player.temp_gear_score -= randint(1, 2)
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

def flee_failed():
    flee_roll = randint(1, 100)
    return flee_roll > 25

def restart_game():
    print("Restarting the game...")
    global player_name, player, rooms, current_room
    player_name, player, rooms, current_room = initialise_game()
    start_game()

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

text_wrapper = textwrap.TextWrapper(width=95,
                                    initial_indent="    ",
                                    subsequent_indent="    ",
                                    drop_whitespace=False,
                                    replace_whitespace=False
                                    )

start_game()