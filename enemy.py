from character import Character
from npc import NPC
from combatant import Combatant
from random import randint
from weapon import Weapon
from armor import Armor
from catalogue import loot, validate_equipment

class Enemy(NPC, Combatant):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        super(Enemy, self).__init__(name, current_room, health, focus, gold, atk, defense)
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.special_attacks = []

    def attack(self):
        damage = self.atk * randint

    def spawn_loot(self, item):
        self.inventory.append(item)

    def enemy_equip(self, equipment):
        print(f"{self.name} is about to equip {equipment}")
        self.equip(equipment)

    def equip_gear(self):
        for item in self.inventory:
            if validate_equipment(loot[item]) == True:
                self.enemy_equip(item)
                