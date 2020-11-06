from player import Player
from catalogue import loot, validate_item, validate_equipment
from npc_roster import characters, validate_barter, validate_battle
from battle import Battle
from barter import Barter
from equipment import Equipment
from map_commands import commands

class Map_Parser:
    def __init__(self):
        self.commands = {}
        self.action = None
        self.argument = None
        self.commands['cardinals'] = self.player_move
        self.commands['menu'] = self.print_help_menu
        self.commands['quit'] = self.quit
        self.commands['drop'] = self.drop_item
        self.commands['take'] = self.take_item
        self.commands['search'] = self.search_room
        self.commands['inventory'] = self.show_player_inventory
        self.commands['stats'] = self.show_player_stats
        self.commands['examine'] = self.examine_target
        self.commands['battle'] = self.battle_target
        self.commands['barter'] = self.barter_target
        self.commands['equip'] = self.equip_item

    def player_move(self, player, direction):
        player.move(player.current_room, direction)

    def drop_item(self, player, item):
        if validate_item(item) == True:
            if player.check_inventory_for_item(item) == True:
                player.drop(item)
                player.current_room.recieve_item(item)
                loot[item].on_drop()

    def take_item(self, player, item):
        if validate_item(item) == True:
            if player.current_room.check_inventory_for_item(item) == True:
                player.take(item)
                player.current_room.remove_item(item)
                loot[item].on_take()

    def search_room(self, player, arg2=None):
        player.explore_room()

    def show_player_inventory(self, player, arg2=None):
        player.show_inventory()

    def show_player_stats(self, player, arg2=None):
        player.show_stats()

    def examine_target(self, player, target):
        if player.validate_target(target) == True:
            player.examine(target)

    def battle_target(self, player, target):
        if validate_battle(characters[target]) is True:
        # if player.validate_target(target) == True:
            if player.current_room.check_occupants_for_character(characters[target]) == True:
                battle = Battle(player, characters[target])
                battle.fight()

    def barter_target(self, player, target):
        # if player.validate_target(target) == True:
        if validate_barter(characters[target]) is True:
            if player.current_room.check_occupants_for_character(characters[target]) == True:
                barter = Barter(player, characters[target])
                barter.trade()

    def equip_item(self, player, target):
        if validate_equipment(loot[target]) == True:
            if player.check_inventory_for_item(target) == True:
                player.equip(target) 

    def print_help_menu(self, player, arg2=None):
        print("Help: ['h', 'help', 'menu']\nExamine target: ['e (target)', 'examine (target)']\nBattle Target: ['b (target)', 'battle (target)']\nShop (merchant): ['barter (target)']\nMove: ['n', 's', 'e', 'w']\nCheck Inventory: ['i', 'inventory']\nCheck Stats: ['stats']\nTake Item: ['t (item)', 'take (item)']\nDrop Item: ['d (item)', 'drop (item)']\nQuit: ['q', 'quit']")

    def quit(self, player, arg2=None):
        player.quit()

    def return_invalid_command(self):
        print("Invalid command")

    def compute_command(self, player_input):
        parsed_cmds = player_input.split(' ')
        arg = parsed_cmds[0]
        argument = ' '.join(parsed_cmds[1:])

        for key, value in commands.items():
            if arg in value:
                self.action = key
                if len(parsed_cmds) == 1:
                    self.argument = arg
                else:
                    self.argument = argument

    def execute_command(self, player):
        if self.action in self.commands:
            self.commands[self.action](player, self.argument)
        else:
            self.return_invalid_command()
        self.action = None
        self.argument = None

    def parse(self, player, cmd):
        self.compute_command(cmd)
        self.execute_command(player)
