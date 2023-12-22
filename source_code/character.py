from inventory_items import weapons, armour
from random import randint

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
            if hit_roll <= 80:
                target.challenge_rating -= randint(1, 4)
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
            "Firebolt" : {"damage" : "1d8", "uses" : 6, "description" : "A swirling orb of molten gold, crackling with miniature lightning bursts. The air around it shimmers with heat distortion, exploding on impact."}, 
            "Freezing Wind" : {"damage": "1d6 + 1d4", "uses" : 5, "description" : "Encases the target in a biting frost, slowing their movements and draining their warmth. Brittle ice creeps across their skin."}, 
            "Phantom Feast" : {"damage" : "2d6", "uses" : 4, "description" : "The target is lured by the ghostly feast, their senses drawn to the illusion of forbidden indulgence. They become sluggish and disoriented, their mind entangled in the phantom delights."}, 
            "Moonlight Barrage" : {"damage" : "2d8 + 1d4", "uses" : 2, "description" : "A shower of shimmering blades form, each etched with moonlight and laced with razor-sharp shadows. They tear through the enemy's defenses and leave trails of moonlight wounds."}
            }
    
    def firebolt(self, target):
        damage = randint(1, 8)
        if self.skills["Firebolt"]["uses"] > 0:
            print(f"You draw your hand in a swift arc, concentrating darkness into a blazing sphere and hurl towards the enemy with a whispered curse.")
            print(f"Your sphere explodes against {target.name}, dealing {damage} fire damage.")
            target.challenge_rating -= damage
            self.skills["Firebolt"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def freezing_wind(self, target):
        damage = randint(1, 6) + randint(1, 4)
        if self.skills["Freezing Wind"]["uses"] > 0:
            print("Lips trembling with a whispered frost-spell, a frigid gust rips from your palms. Blades of ice dance toward your enemy within the wind.")
            print(f"Your spell strikes {target.name}, dealing {damage} ice damage.")
            target.challenge_rating -= damage
            self.skills["Freezing Wind"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def phantom_feast(self, target):
        damage = randint(1, 6) + randint(1, 6)
        if self.skills["Phantom Feast"]["uses"] > 0:
            print("You weave the shadows into a spectral feast, a low-pitched, hypnotic chant escaping from your lips as you ensnare the target in your illusion.")
            print(f"{target.name} suffers {damage} illusion damage.")
            target.challenge_rating -= damage
            self.skills["Phantom Feast"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def moonlight_barrage(self, target):
        damage = randint(1, 8) + randint(1, 8) + randint(1, 4)
        if self.skills["Moonlight Barrage"]["uses"] > 0:
            print("You raise your hand, shadows and moonlight swirling around them to create a storm of uncast shadows.")
            print(f"You unleash a volley of spectral blades, piercing {target.name} for {damage} raw magic damage.")
            target.challenge_rating -= damage
            self.skills["Moonlight Barrage"]["uses"] -= 1
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
            "Bloodbath Barrage" : {"damage" : "1d8", "uses" : 10, "description" : "Tear through your enemies with your blade, painting the air with bloody mist."}, 
            "Crimson Cleaver" : {"damage" : "3d6", "uses" : 5, "description" : "Produce a shockwave that cracks the ground, flinging your target/s into the air."}
        }

    def bloodbath_barrage(self, target): 
        damage = randint(1, 8)
        if self.skills["Bloodbath Barrage"]["uses"] > 0:
            print("You swiftly unleash your blade, whirling into a crimson-soaked cyclone as you scream towards your enemy.")
            print(f"{target.name} suffers {damage} physical damage.")
            target.challenge_rating -= damage
            self.skills["Bloodbath Barrage"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def crimson_cleaver(self, target):
        damage = randint(1, 6) + randint(1, 6) + randint(1, 6)
        if self.skills["Crimson Cleaver"]["uses"] > 0:
            print("The ground trembles as you slams their weapon into the earth. A crimson shockwave erupts, cracking the ground and sending tremors that ripple outward.")
            print(f"{target.name} fails to escape your shockwave, dealing {damage} physical damage.")
            target.challenge_rating -= damage
            self.skills["Crimson Cleaver"]["uses"] -= 1
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
            "Hymn of Helios" : {"damage" : "1d6 + 1d4", "uses" : 6, "description" : "Channel the blinding brilliance of the sun, firing a searing arrow leaving smoldering trails in its wake."}, 
            "Sun's Ire" : {"damage": "2d6", "uses" : 5, "description" : "Unleash a scorching arrow imbued with solar fury, exploding on impact and dealing heavy damage to a small area."}, 
            "Hunter's Volley" : {"damage" : "3d8", "uses" : 1, "description" : "Launch a rapid succession of precise arrows, peppering enemies with a hail of feathers and steel."}
            }

    def hymn_of_helios(self, target):
        damage = randint(1, 6) + randint(1, 4)
        if self.skills["Hymn of Helios"]["uses"] > 0:
            print(f"As you draw your bow, light gathers around your arrowhead with the fierceness of the sun as you unleash your arrow, chanting the Sun's blessing.")
            print(f"You strike true, dealing {damage} fire damage to {target.name}.")
            target.challenge_rating -= damage
            self.skills["Hymn of Helios"]["uses"] -= 1
        else: 
            raise NoUsesLeft
    def suns_ire(self, target):
        damage = randint(1, 6) + randint(1, 6)
        if self.skills["Sun's Ire"]["uses"] > 0:
            print("Gritting your teeth and drawing on the Sun's power, you unleashe a devastating solar projectile towards your target.")
            print(f"Finding your mark, {target.name} suffers {damage} fire damage.")
            target.challenge_rating -= damage
            self.skills["Sun's Ire"]["uses"] -= 1
        else: 
            return NoUsesLeft

    def hunters_volley(self, target):
        damage = randint(1, 8) + randint(1, 8) + randint(1, 8)
        if self.skills["Hunter's Volley"]["uses"] != 0:
            print(f"You unleash a storm of sun-kissed arrows, each shot finding their mark without effort.")
            print(f"{target.name} suffers {damage} ranged damage.")
            target.challenge_rating -= damage
            self.skills["Hunter's Volley"]["uses"] -= 1
        else: 
            raise NoUsesLeft

    def gear_score(self):
        return Character.calculate_gear_score(self)
