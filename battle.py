from player import Player
from enemy import Enemy
from npc_roster import characters
import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.enemy_health = self.enemy.health
        self.active = False
        self.actions = {}
        self.actions['a'] = self.attack
        self.actions['r'] = self.rest
        self.actions['e'] = self.escape

    def show_battle_stats(self):
        print(f"BATTLE: {self.player.name} vs {self.enemy.name}\n***{self.player.name} health: {self.player.health}\n{self.enemy.name} health: {self.enemy_health}")

    def show_command_list(self):
        print("[a]ttack, [r]est, [e]scape")

    def attack(self):
        player_attack = self.player.atk * random.randrange(10)
        enemy_attack = self.enemy.atk * random.randrange(3)
        self.player.health -= enemy_attack
        self.enemy_health -= player_attack
        self.show_battle_stats()
        self.verify_battle()

    def rest(self):
        self.player.health += 10
        enemy_attack = self.enemy.atk * random.randrange(1)
        self.player.health -= enemy_attack
        self.show_battle_stats()
        self.verify_battle()

    def escape(self):
        attempt = random.randrange(10)
        if attempt > 2:
            self.active = False
        else:
            enemy_attack = self.enemy.atk * random.randrange(5)
            self.player.health -= enemy_attack
            self.show_battle_stats()
        self.verify_battle()

    def verify_battle(self):
        if self.enemy_health <= 0:
            self.victory()
            self.active = False
        if self.player.health <= 0:
            self.defeat()
            self.active = False

    def get_reward(self):
        reward = self.enemy.inventory
        gold = self.enemy.gold
        self.player.gold += gold
        if len(reward) > 0:
            self.player.inventory.extend(reward)
            print(f"Recieved {reward}, {gold} Gold")
        else:
            print(f"Recieved {self.enemy.gold} Gold")

    def victory(self):
        self.get_reward()
        self.player.current_room.occupants.remove(self.enemy)
        print(f"Congratulations!!! You have defeated {self.enemy.name}!")

    def defeat(self):
        print(f"{self.player.name} has fallend in battle...")
        self.player.playing = False

    def fight(self):
        self.active = True

        while self.active == True:
            self.show_battle_stats()
            self.show_command_list()

            command_input = input('battle> ')
            if command_input in self.actions:
                self.actions[command_input]()
            else:
                print('Invalid action')
