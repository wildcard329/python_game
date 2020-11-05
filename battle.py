from player import Player
from enemy import Enemy
from npc_roster import characters
import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.active = False
        self.actions = {}
        self.actions['a'] = self.attack
        self.actions['r'] = self.rest
        self.actions['e'] = self.escape

    def show_battle_stats(self):
        print(f"BATTLE: {self.player.name} vs {self.enemy.name}\n***{self.player.name} health: {self.player.health}\n{self.enemy.name} health: {self.enemy.health}")

    def show_command_list(self):
        print("[a]ttack, [r]est, [e]scape")

    def attack(self):
        player_attack = self.player.atk * random.randrange(10)
        enemy_attack = self.enemy.atk * random.randrange(3)
        self.player.health -= enemy_attack
        self.enemy.health -= player_attack
        self.show_battle_stats()

    def rest(self):
        self.player.health += 10
        enemy_attack = self.enemy.atk * random.randrange(1)
        self.player.health -= enemy_attack
        self.show_battle_stats()

    def escape(self):
        attempt = random.randrange(10)
        if attempt > 2:
            self.active = False
        else:
            enemy_attack = self.enemy.atk * random.randrange(5)
            self.player.health -= enemy_attack
            self.show_battle_stats()

    def end_battle(self):
        self.active = False
        return self.active

    def fight(self):
        self.active = True
        if self.player.health <= 0 or self.enemy.health <= 0:
            self.end_battle()

        while self.active == True:
            self.show_battle_stats()
            self.show_command_list()

            command_input = input('battle> ')
            input(command_input)
            if command_input in self.actions:
                self.actions[command_input]()
            else:
                print('Invalid action')
