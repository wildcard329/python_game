from enemy import Enemy
from random import randint

class Monster(Enemy):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        super(Monster, self).__init__(name, current_room, health, focus, gold, atk, defense)
        self.attacks = ['bite', 'scratch']
        self.inventory = []

    def bite(self):
        self.attack()
        self.focus -= 2

    def scratch(self):
        self.attack()
        self.focus -= 1
