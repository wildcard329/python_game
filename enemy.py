from character import Character
from npm import NPC

class Enemy(NPC):
    def __init__(self, name, current_room, health, focus, gold, inventory, atk, defense):
        super.__init__(name, current_room, health, focus, gold, inventory, atk, defense)


