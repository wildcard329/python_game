from enemy import Enemy
from random import randint

class Monster(Enemy):
    def __init__(self, name, current_room, health, focus, gold, inventory, atk, defense):
        super.__init__(name, current_room, health, focus, gold, inventory, atk, defense)
        self.attacks = ['bite', 'scratch']

    def attack(self):
        damage = randint * self.atk

    def bite(self):
        self.attack()
        self.focus -= 2

    def scratch(self):
        self.attack()
        self.focus -= 1
        