from enemy import Enemy
from random import randint

class Monster(Enemy):
    def __init__(self, name, current_room, health, focus, gold, atk, defense, special_attacks):
        super(Monster, self).__init__(name, current_room, health, focus, gold, atk, defense)
        self.special_attacks = special_attacks
        self.inventory = []

    def bite(self):
        self.attack()
        self.focus -= 2

    def scratch(self):
        self.attack()
        self.focus -= 1
