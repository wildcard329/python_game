from character import Character
from catalogue import loot

class Mage(Character):
    def __init__(self, name, current_room, health, focus, gold, atk, defense, description):
        super(Mage, self).__init__(name, current_room, health, focus, gold, atk, defense, description)
        self.special_attacks = []
        self.non_combat_special = []
        self.trapped = []
        self.minions = []

    def read(self, book):
        if loot[book].s_type == 'combat':
            self.special_attacks.append(loot[book].ability)
        elif loot[book].s_type == 'non-combat':
            self.non_combat_special.append(loot[book].ability)
        loot[book].on_read(loot[book].ability)
