from player import Player
from catalogue import loot, validate_item

class Parser:
    def __init__(self):
        self.cardinals = ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']
        self.help = ['h', 'help', 'menu']
        self.quit = ['q', 'quit']
        self.drop = ['d', 'drop']
        self.take = ['t', 'take']
        self.search = ['search']
        self.inventory = ['i', 'inventory']
        self.examine = ['e', 'examine']

    def print_help_menu(self):
        print("Help: ['h', 'help', 'menu']\nExamine target: ['e (target)', 'examine (target)']\nMove: ['n', 's', 'e', 'w']\nCheck Inventory: ['i', 'inventory']\nTake Item: ['t (item)', 'take (item)']\nDrop Item: ['d (item)', 'drop (item)']\nQuit: ['q', 'quit']")

    def return_invalid_command(self):
        print("Invalid command")

    def parse(self, player, cmd):
        parsed_cmds = cmd.split(' ')
        action = parsed_cmds[0]
        if len(parsed_cmds) == 1:
            if action in self.cardinals:
                player.move(player.current_room, action)
            elif action in self.help:
                self.print_help_menu()
            elif action in self.quit:
                player.quit()
            elif action in self.search:
                player.explore_room()
                player.current_room.get_inventory()
            elif action in self.inventory:
                player.show_inventory()
            else:
                self.return_invalid_command()
        else:
            argument = " ".join(parsed_cmds[1:])
            if action in self.drop:
                if validate_item(argument) == True:
                    if player.check_inventory_for_item(argument) == True:
                        player.drop(argument)
                        player.current_room.recieve_item(argument)
                        loot[argument].on_drop()
            elif action in self.take:
                if validate_item(argument) == True:
                    if player.current_room.check_inventory_for_item(argument) == True:
                        player.current_room.remove_item(argument)
                        player.take(argument)
                        loot[argument].on_take()
            elif action in self.examine:
                if player.validate_target(argument) == True:
                    player.examine(argument)
            else:
                self.return_invalid_command()
            