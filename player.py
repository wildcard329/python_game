from catalogue import loot, validate_item
from npc_roster import characters
from merchant import Merchant
from weapon import Weapon
from armor import Armor

class Player(Merchant):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        self.name = name
        self.current_room = current_room
        self.health = health
        self.focus = focus
        self.gold = 0
        self.atk = atk
        self.defense = defense
        self.playing = False
        self.inventory = []
        self.weapon = None
        self.armor = None

    def __str__(self):
        return f"\n{self.name} is in {self.current_room.name}\n"

    def quit(self):
        self.playing = False

    def move(self, current_room, direction):
        move = f"{direction}_to"
        if hasattr(current_room, move):
            new_room = getattr(current_room, move)
            self.current_room = new_room
            print(f"{self.name} entered {new_room.name}")
            self.explore_room()
        else:
            print('You cannot move in that direction.')

    def show_inventory(self):
        print(f"{self.name}\nInventory: {self.inventory}")

    def show_gold(self):
        print(f"Gold: {self.gold}")

    def show_stats(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.atk}\nDefense: {self.defense}\nWeapon: {self.weapon}\nArmor: {self.armor}")
        self.show_gold()

    def explore_room(self):
        if self.current_room.entered == False:
            print(self.current_room)
            self.current_room.entered = True
        if len(self.current_room.occupants) > 0:
            self.current_room.get_occupants()
        else:
            self.current_room.get_inventory()

    def check_inventory_for_item(self, item):
        if item in self.inventory:
            return True
        else:
            print(f"{item} is not in inventory.")
    
    def return_invalid(self):
        print("Invalid target")

    def examine(self, target):
        if target in loot:
            if target in self.inventory or target in self.current_room.inventory:
                print(loot[target])
            else:
                self.return_invalid()
        else:
            self.return_invalid()

    def validate_target(self, target):
        if validate_item(target) == True:
            return True
        elif target in characters:
            return True
        else:
            self.return_invalid()

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def equip(self, equipment):
        if isinstance(loot[equipment], Weapon):
            if self.weapon is not None:
                self.unequip(self.weapon)
            self.weapon = equipment
            self.atk += loot[equipment].atk_rating
        if isinstance(loot[equipment], Armor):
            if self.armor is not None:
                self.unequip(self.armor)
            self.armor = equipment
            self.defense += loot[equipment].armor_rating
        self.inventory.remove(equipment)
        loot[equipment].on_equip(equipment)

    def unequip(self, equipment):
        if isinstance(loot[equipment], Weapon):
            self.weapon = None
            self.atk -= loot[equipment].atk_rating
        if isinstance(loot[equipment], Armor):
            self.armor = None
            self.defense -= loot[equipment].armor_rating
        self.inventory.append(equipment)
        loot[equipment].on_unequip(equipment)
