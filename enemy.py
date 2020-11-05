from character import Character
from npc import NPC
from random import randint

class Enemy(NPC):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        super(Enemy, self).__init__(name, current_room, health, focus, gold, atk, defense)
        self.inventory = []

    def attack(self):
        damage = self.atk * randint

    def spawn_loot(self, item):
        self.inventory.append(item)