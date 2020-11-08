from character import Character
from catalogue import loot

class Mage(Character):
    def __init__(self, name, current_room, health, focus, gold, atk, defense, description):
        super(Mage, self).__init__(name, current_room, health, focus, gold, atk, defense, description)
        self.special_attacks = []

    def read(self, book):
        self.special_attacks.append(loot[book].ability)
        loot[book].on_read(loot[book].ability)
