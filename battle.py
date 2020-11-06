from player import Player
from enemy import Enemy
from npc_roster import characters
from battle_commands import commands
import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.enemy_health = self.enemy.health
        self.enemy_focus = self.enemy.focus
        self.active = False
        self.action = None
        self.actions = {}
        self.actions['attack'] = self.attack
        self.actions['rest'] = self.rest
        self.actions['escape'] = self.escape
        self.actions['help'] = self.help
        self.actions['special attack'] = self.special_attack

    def show_battle_stats(self):
        print(f"BATTLE: {self.player.name} vs {self.enemy.name}\n***{self.player.name} health: {self.player.health} focus: {self.player.focus}\n{self.enemy.name} health: {self.enemy_health} focus: {self.enemy_focus}")

    def show_command_list(self):
        print("[a]ttack, [r]est, [e]scape")

    def help(self):
        print("Attack: ['a', 'attack']\nRest: ['r', 'rest']\nEscape: ['e', 'escape']\nSpecial Attack: ['s', 'special', 'sa', 'special attack']\nHelp: ['h', 'help']")

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

    def special_attack(self):
        pass

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
        if self.enemy.weapon is not None:
            self.enemy.unequip(self.enemy.weapon)
        if self.enemy.armor is not None:
            self.enemy.unequip(self.enemy.armor)
        self.get_reward()
        self.player.current_room.occupants.remove(self.enemy)
        print(f"Congratulations!!! You have defeated {self.enemy.name}!")

    def defeat(self):
        print(f"{self.player.name} has fallen in battle...")
        self.player.playing = False

    def compute_command(self, player_input):
        for key, value in commands.items():
            if player_input in value:
                self.action = key

    def execute_command(self):
        if self.action in self.actions:
            self.actions[self.action]()
        else:
            print("Invalid action")
        self.action = None

    def fight(self):
        self.active = True

        while self.active == True:
            self.show_battle_stats()
            self.show_command_list()

            command_input = input('battle> ')
            self.compute_command(command_input)
            self.actions[self.action]()
            self.action = None
