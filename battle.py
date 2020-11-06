from player import Player
from enemy import Enemy
from npc_roster import characters
from battle_commands import commands
from ability_catalogue import abilities
import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.enemy_health = self.enemy.health
        self.enemy_focus = self.enemy.focus
        self.active = False
        self.action = None
        self.counter = 0
        self.actions = {}
        self.actions['attack'] = self.attack
        self.actions['rest'] = self.rest
        self.actions['escape'] = self.escape
        self.actions['help'] = self.help
        self.actions['special attack'] = self.special_attack

    def notify(self):
        input('Press [enter] to continue')

    def show_battle_stats(self):
        print(f"BATTLE: {self.player.name} vs {self.enemy.name}\n***\n{self.player.name} health: {self.player.health} focus: {self.player.focus}\n{self.enemy.name} health: {self.enemy_health} focus: {self.enemy_focus}")

    def show_command_list(self):
        print("[a]ttack, [r]est, [e]scape, [sa] (special attack)")

    def help(self):
        print("Attack: ['a', 'attack']\nRest: ['r', 'rest']\nEscape: ['e', 'escape']\nSpecial Attack: ['s', 'special', 'sa', 'special attack']\nHelp: ['h', 'help']")

    def attack(self):
        player_attack = self.player.atk * random.randrange(10)
        enemy_attack = self.enemy.atk * random.randrange(3)
        self.player.health -= enemy_attack -self.player.defense
        self.enemy_health -= player_attack - self.enemy.defense
        self.show_battle_stats()
        self.verify_battle()

    def rest(self):
        self.player.health += 10
        self.player.focus += 1
        enemy_attack = self.enemy.atk * random.randrange(1)
        self.player.health -= enemy_attack -self.player.defense        
        self.show_battle_stats()
        self.verify_battle()

    def escape(self):
        attempt = random.randrange(10)
        if attempt > 2:
            self.active = False
        else:
            enemy_attack = self.enemy.atk * random.randrange(5)
            self.player.health -= enemy_attack -self.player.defense
            self.show_battle_stats()
        self.verify_battle()

    def special_attack(self):
        if len(self.player.special_attacks) > 0:
            print(f"Select attack {self.player.special_attacks}")
            attack = input('sa> ')
            if attack in self.player.special_attacks and self.player.focus > abilities[attack]['fatigue']:
                self.enemy_health -= self.player.atk * random.randrange(9, 10) + abilities[attack]['bonus']
                self.player.focus -= abilities[attack]['fatigue']
                self.player.health -= self.enemy.atk * random.randrange(5)
                self.show_battle_stats()
            else:
                print(f'Cannot perform {attack}')
                self.notify()
        else:
            print("You have no special attacks")
            self.notify()
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

    def enemy_special_attack(self):
        if self.counter == 5 and len(self.enemy.special_attacks) > 0:
            self.counter = 0
            attack = random.choice(self.enemy.special_attacks)
            if self.enemy_focus > abilities[attack]['fatigue']:
                self.player.health -= self.enemy.atk * random.randrange(4, 5) + abilities[attack]['bonus']
                self.enemy_focus -= abilities[attack]['fatigue']
                print(f"{self.enemy.name} used {attack}")
                self.notify() 

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
        print(self.enemy.special_attacks)
        self.active = True

        while self.active == True:
            self.enemy_special_attack()
            self.show_battle_stats()
            self.show_command_list()

            command_input = input('battle> ')
            self.compute_command(command_input)
            self.execute_command()
            self.counter += 1
