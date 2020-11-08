from player import Player
from enemy import Enemy
from monster import Monster
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
        self.enemy_timer = None
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
        self.combat_turn(self.player)
        self.combat_turn(self.enemy)
        self.verify_battle()

    def deal_damage(self, character, damage):
        if isinstance(character, Player):
            self.enemy_health -= damage
        elif isinstance(character, Enemy) or isinstance(character, Monster):
            self.player.health -= damage

    def assign_damage(self, character, damage):
        if damage < 0:
            self.combat_turn(character)
        else:
            self.deal_damage(character, damage)

    def use_focus(self, character, attack):
        if isinstance(character, Player):
            self.player.focus -= abilities[attack]['fatigue']
        elif isinstance(character, Enemy) or isinstance(character, Monster):
            self.enemy_focus -= abilities[attack]['fatigue']

    def combat_turn(self, character):
        if isinstance(character, Player):
            character_atk = self.player.atk * random.randrange(10)
        if isinstance(character, Enemy) or isinstance(character, Monster):
            character_atk = self.enemy.atk * random.randrange(5)
        self.assign_damage(character, character_atk)

    def rest(self):
        self.player.health += 100
        self.player.focus += 10
        self.combat_turn(self.enemy)
        self.verify_battle()

    def escape(self):
        attempt = random.randrange(10)
        if attempt > 2:
            self.active = False
        else:
            self.combat_turn(self.enemy)
            self.verify_battle()

    def special_attack(self):
        if len(self.player.special_attacks) > 0:
            print(f"Select attack {self.player.special_attacks}")
            attack = input('sa> ')
            if attack in self.player.special_attacks and self.player.focus > abilities[attack]['fatigue']:
                damage = self.player.atk * random.randrange(9, 10) + abilities[attack]['bonus']
                self.assign_damage(self.player, damage)
                self.use_focus(self.player, attack)
                self.combat_turn(self.enemy)
                self.verify_battle()
            else:
                print(f'Cannot perform {attack}')
                self.notify()
        else:
            print("You have no special attacks")
            self.notify()

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
        self.player.playing = False

    def enemy_special_attack(self):
        if self.counter == 0:
            self.enemy_timer = random.randrange(1, 6)
        if self.counter == self.enemy_timer and len(self.enemy.special_attacks) > 0:
            self.counter = 0
            attack = random.choice(self.enemy.special_attacks)
            if self.enemy_focus > abilities[attack]['fatigue']:
                damage = self.enemy.atk * random.randrange(4, 5) + abilities[attack]['bonus']
                self.assign_damage(self.enemy, damage)
                self.use_focus(self.enemy, attack)
                print(f"{self.enemy.name} used {attack}")
                self.notify() 
                self.verify_battle()

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
        self.enemy.check_inventory_for_weapon()
        self.enemy.check_inventory_for_armor()
        self.active = True

        while self.active == True:
            self.enemy_special_attack()
            self.show_battle_stats()
            self.show_command_list()

            command_input = input('battle> ')
            self.compute_command(command_input)
            self.execute_command()
            self.counter += 1
