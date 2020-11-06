from character import Character
from catalogue import loot, validate_item
from weapon import Weapon
from armor import Armor

class Combatant(Character):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        super(Combatant, self).__init__(name, current_room, health, focus, gold, atk, defense)
        self.weapon = None
        self.armor = None
        self.inventory = []

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
