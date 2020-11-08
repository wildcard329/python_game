from character import Character
from npc import NPC
from combatant import Combatant
from random import randint
from weapon import Weapon
from armor import Armor
from catalogue import loot

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

    def check_inventory_for_weapon(self):
        for item in self.inventory:
            if isinstance(loot[item], Weapon):
                self.enemy_equip(item)

    def check_inventory_for_armor(self):
        for item in self.inventory:
            if isinstance(loot[item], Armor):
                self.enemy_equip(item)
