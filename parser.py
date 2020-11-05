from player import Player
from catalogue import loot, validate_item, validate_equipment
from npc_roster import characters
from battle import Battle
from barter import Barter
from equipment import Equipment
from commands import commands

class Parser:
    def __init__(self):
        self.cardinals = ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']
        self.help = 'help'
        self.h = 'h'
        self.menu = 'menu'
        self.quit = 'quit'
        self.q = 'q'
        self.drop = 'drop'
        self.d = 'd'
        self.take = 'take'
        self.t = 't'
        self.search = 'search'
        self.inventory = 'inventory'
        self.i = 'i'
        self.examine = 'examine'
        self.e = 'e'
        self.battle = 'battle'
        self.b = 'b'
        self.barter = 'barter'
        self.equip = 'equip'
        self.stats = 'stats'
        self.commands = {}
        self.commands[self.n] = self.player_move
        self.commands[self.s] = self.player_move
        self.commands[self.e] = self.player_move
        self.commands[self.w] = self.player_move
        self.commands[self.north] = self.player_move
        self.commands[self.south] = self.player_move
        self.commands[self.east] = self.player_move
        self.commands[self.west] = self.player_move
        self.commands[self.help] = self.print_help_menu
        self.commands[self.quit] = self.quit
        self.commands[self.drop] = self.drop_item
        self.commands[self.take] = self.take_item
        self.commands[self.search] = self.search_room
        self.commands[self.inventory] = self.show_player_inventory
        self.commands[self.stats] = self.show_player_stats
        self.commands[self.examine] = self.examine_target
        self.commands[self.battle] = self.battle_target
        self.commands[self.barter] = self.barter_target
        self.commands[self.equip] = self.equip_item

    def player_move(self, player, direction):
        player.move(direction)

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
        if player.validate_target(target) == True:
            if player.current_room.check_occupants_for_character(characters[target]) == True:
                battle = Battle(player, characters[target])
                battle.fight()

    def barter_target(self, player, target):
        if player.validate_target(target) == True:
            if player.current_room.check_occupants_for_character(characters[target]) == True:
                barter = Barter(player, characters[target])
                barter.trade()

    def equip_item(self, player, target):
        if player.validate_equipment(loot[target]) == True:
            player.equip(target) 

    def print_help_menu(self, player, arg2=None):
        print("Help: ['h', 'help', 'menu']\nExamine target: ['e (target)', 'examine (target)']\nMove: ['n', 's', 'e', 'w']\nCheck Inventory: ['i', 'inventory']\nTake Item: ['t (item)', 'take (item)']\nDrop Item: ['d (item)', 'drop (item)']\nQuit: ['q', 'quit']")

    def return_invalid_command(self):
        print("Invalid command")

    def parse(self, player, cmd):
        parsed_cmds = cmd.split(' ')
        zr = parsed_cmds[0]
        action = commands[zr]
        argument = parsed_cmds[1:]

        if self.commands[action]:
            self.commands[action](player, argument)
        # if len(parsed_cmds) == 1:
        #     if action in self.cardinals:
        #         player.move(player.current_room, action)
        #     elif action in self.help:
        #         self.print_help_menu()
        #     elif action in self.quit:
        #         player.quit()
        #     elif action in self.search:
        #         player.explore_room()
        #     elif action in self.inventory:
        #         player.show_inventory()
        #     elif action in self.stats:
        #         player.show_stats()
        #     else:
        #         self.return_invalid_command()
        # else:
        #     argument = " ".join(parsed_cmds[1:])
        #     if action in self.drop:
        #         if validate_item(argument) == True:
        #             if player.check_inventory_for_item(argument) == True:
        #                 player.drop(argument)
        #                 player.current_room.recieve_item(argument)
        #                 loot[argument].on_drop()
        #     elif action in self.take:
        #         if validate_item(argument) == True:
        #             if player.current_room.check_inventory_for_item(argument) == True:
        #                 player.current_room.remove_item(argument)
        #                 player.take(argument)
        #                 loot[argument].on_take()
        #     elif action in self.examine:
        #         if player.validate_target(argument) == True:
        #             player.examine(argument)
        #     elif action in self.battle:
        #         if player.validate_target(argument) == True:
        #             if player.current_room.check_occupants_for_character(characters[argument]) == True:
        #                 battle = Battle(player, characters[argument])
        #                 battle.fight()
        #     elif action in self.barter:
        #         if player.validate_target(argument) == True:
        #             if player.current_room.check_occupants_for_character(characters[argument]) == True:
        #                 barter = Barter(player, characters[argument])
        #                 barter.trade()
        #     elif action in self.equip:
        #         if validate_equipment(loot[argument]) == True:
        #             player.equip(argument)
        #     else:
        #         self.return_invalid_command()
            