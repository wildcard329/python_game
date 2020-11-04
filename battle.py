from player import Player
from enemy import Enemy
from random import randint

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.active = True

    def show_battle_stats(self):
        print(f"BATTLE: {self.player.name} vs {self.enemy.name}\n***{self.player.name} health: {self.player.health}\n{self.enemy.name} health: {self.enemy.health}")

    def show_command_list(self):
        print("[a]ttack, [r]est, [e]scape")

    while self.active == True:
        player_health = self.player.health
        enemy_health = self.enemy.health
        self.show_battle_stats()

        command_input = input('> ')