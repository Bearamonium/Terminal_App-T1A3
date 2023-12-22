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

class Weapon(Inventory_Items):
    def __init__(self, name, value, gear_score, quantity=1):
        super().__init__(name, value, quantity)
        self.gear_score = gear_score
        self.type = "weapon"

class Armour(Inventory_Items):
    def __init__(self, name, value,gear_score, quantity=1):
        super().__init__(name, value, quantity)
        self.gear_score = gear_score
        self.type = "armour"

items = {
    'Golden Sphere' : Items("Golden Sphere", 0), 
    'Candle Key' : Items("Candle Key", 0), 
    'Fire Orb' : Items("Fire Orb", 5), 
}

weapons = {
    'Wooden Short Sword' : Weapon("Wooden Sword", 1, 5), 
    'Wooden Short Bow' : Weapon("Wooden Short Bow", 1, 5), 
    'Wooden Staff' : Weapon("Wooden Staff", 3, 5), 
    'Iron Sword' : Weapon("Iron Sword", 1.5, 6), 
    'Elm Short Bow' : Weapon("Elm Short Bow", 1.5, 6), 
    'Elm Staff' : Weapon("Elm Staff", 1.5, 6), 
}

armour = {
    'Chainmail Armour' : Armour("Chainmail Armour", 1, 3),
    'Leather Armour' : Armour("Leather Armour", 1, 3),
    'Student Robes' : Armour("Wizard Robes", 1, 3),
    'Iron Armour' : Armour("Iron Armour", 1.5, 4),
    'Studded Leather Armour' : Armour("Studded Leather Armour", 1.5, 4),
    'Silk Robes' : Armour("Silk Robes", 1.5, 4)
}