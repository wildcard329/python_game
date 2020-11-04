from character import Character
from catalogue import loot
import random

class NPC(Character):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        super.__init__(name, current_room, health, focus, gold, atk, defense)
        self.inventory = []

    def spawn_item(self, item):
        generate_loot = random.randrange(3)
        if generate_loot == 2:
            self.inventory.append(item)

    def spawn_rare_item(self, item):
        generate_loot = random.randrange(10)
        if generate_loot == 5:
            self.inventory.append(item)