from player import Player
from catalogue import loot, validate_item, validate_equipment
from npc_roster import characters, validate_barter, validate_battle, is_character
from battle import Battle
from barter import Barter
from equipment import Equipment
from map_commands import commands, commands2
from ability_catalogue import non_combat_abilities, validate_map_spell

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
        self.commands['unequip'] = self.unequip_item
        self.commands['read'] = self.read_book
        self.commands['spell'] = self.spell

    def player_move(self, player, direction):
        player.move(player.current_room, direction)

    def drop_item(self, player, item):
        if validate_item(item) == True:
            if player.check_inventory_for_item(item) == True:
                player.drop(item)
                player.current_room.recieve_item(item)
                loot[item].on_drop()

    def take_item(self, player, item):
        if len(player.current_room.occupants) == 0:
            if item != 'all':
                if validate_item(item) == True:
                    if player.current_room.check_inventory_for_item(item) == True:
                        player.take(item)
                        player.current_room.remove_item(item)
                        loot[item].on_take()
            else:
                print(f"Recieved {player.current_room.inventory}.")
                player.inventory.extend(player.current_room.inventory)
                player.current_room.inventory = []
        else:
            print("Enemies guard this room's contents.")
        if len(player.inventory) > 20:
            player.playing = False

    def search_room(self, player, arg2=None):
        player.explore_room()

    def show_player_inventory(self, player, arg2=None):
        player.show_inventory()

    def show_player_stats(self, player, arg2=None):
        player.show_stats()

    def examine_target(self, player, target):
        if is_character(target) == True or validate_item(target) == True:
            player.examine(target)

    def battle_target(self, player, target):
        if validate_battle(target) is True:
            if player.current_room.check_occupants_for_character(characters[target]) == True:
                battle = Battle(player, characters[target])
                battle.fight()

    def barter_target(self, player, target):
        if validate_barter(target) is True:
            if player.current_room.check_occupants_for_character(characters[target]) == True:
                barter = Barter(player, characters[target])
                barter.trade()

    def equip_item(self, player, target):
        if validate_equipment(loot[target]) == True:
            if player.check_inventory_for_item(target) == True:
                player.equip(target) 

    def unequip_item(self, player, target):
        if loot[target] == player.weapon or loot[target] == player.armor:
            player.unequip_item(loot[target])

    def read_book(self, player, book):
        if validate_item(book) is True and player.check_inventory_for_item(book) is True:
            player.read(book)
            player.drop(book)

    def spell(self, player, arg=None):
        if player.confirm_nc_spells() is True:
            if player.current_room.confirm_defeated() is True or player.show_aquired_trapped() is True:
                player.show_non_combat_spells()
                spell = input('Which spell? ')
                player.current_room.show_defeated()
                player.show_aquired_trapped()
                target = input('Which target? ')
                self.get_spell_targets(spell, target, player)

    def get_spell_targets(self, spell, target, player):
        if validate_map_spell(spell) is True and validate_battle(target) is True:
            list_1 = non_combat_abilities[spell]['target_list_1']
            action_1 = non_combat_abilities[spell]['action_1']
            list_2 = non_combat_abilities[spell]['target_list_2']
            action_2 = non_combat_abilities[spell]['action_2']
            self.execute_spell(list_1, action_1, list_2, action_2, target, player)

    def execute_spell(self, l1, a1, l2, a2, target, player):
        target = characters[target]
        if l1 == 'trapped' and a1 == 'append' and l2 == 'current_room.fallen' and a2 == 'remove':
            player.trapped.append(target)
            player.current_room.fallen.remove(target)
            player.show_aquired_trapped()
        elif l1 == 'minions' and a1 == 'append' and l2 == 'trapped' and a2 == 'remove':
            player.minions.append(target)
            player.trapped.remove(target)
            player.show_aquired_minions()

    def print_help_menu(self, player, arg2=None):
        print("Help: ['h', 'help', 'menu']\nExamine target: ['ex (target)', 'examine (target)']\nBattle Target: ['b (target)', 'battle (target)']\nShop (merchant): ['barter (target)', 'ba (target)', 'shop (target), 's (target)']\nMove: ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']\nCheck Inventory: ['i', 'inventory']\nCheck Stats: ['stats', 'st']\nTake Item: ['t (item)', 'take (item)']\nTake All Items: ['t all']\nDrop Item: ['d (item)', 'drop (item)']\nQuit: ['q', 'quit']")

    def quit(self, player, arg2=None):
        player.quit()

    def return_invalid_command(self):
        print("Invalid command")

    def get_key(self, cmds, s_term):
        for key, value in cmds.items():
            if s_term in value:
                self.action = key

    def compute_command(self, player_input):
        parsed_cmds = player_input.split(' ')
        arg = parsed_cmds[0]
        argument = ' '.join(parsed_cmds[1:])
        self.get_command(parsed_cmds, arg, argument)
        
    def get_command(self, parsed_cmds, arg, argument):
        if len(parsed_cmds) == 1:
            self.get_key(commands, arg)
            self.argument = arg
        else:
            self.get_key(commands2, arg)
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
