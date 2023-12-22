from random import randint
from character import NoUsesLeft

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
    def __init__(self, challenge_rating, skills, undying=True):
        super().__init__("Xhoth", challenge_rating, skills)
        self.undying = undying

    def consume_essence(self, target):
        # Deal damage and steal life force from the target, healing Xhoth.
        damage = randint(2, 4)
        target.temp_gear_score -= damage
        Xhoth.challenge_rating += damage // 2
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
