from player import Player
from npc_roster import characters
from catalogue import loot, validate_item
from weapon import Weapon
from armor import Armor
from barter_commands import commands

class Barter:
    def __init__(self, player, merchant):
        self.player = player
        self.merchant = merchant
        self.commands = {}
        self.commands['sell'] = self.sell
        self.commands['buy'] = self.buy
        self.commands['examine'] = self.examine
        self.commands['quit'] = self.quit
        self.trading = False
        self.action = None
        self.argument = None

    def notify(self):
        input("Press any key to continue")

    def merchant_insufficient_funds(self, merchant):
        print(f"{merchant}: I'm sorry, I do not have enough gold for that.")
        self.notify()

    def player_insufficient_funds(self, player):
        print(f"{player}: Whoops, I don't have enough gold for that.")

    def sell(self, item, player, merchant):
        if validate_item(item) == True:
            if self.player.check_inventory_for_item(item) == True:
                if self.merchant.gold > loot[item].value:
                    self.finalize_sell(item)
                    loot[item].on_sell()
                else:
                    self.merchant_insufficient_funds(self.merchant.name)
                    self.notify()
            elif item == self.player.weapon or item == self.player.armor:
                self.player.unequip(item)
                self.finalize_sell(item)

    def finalize_sell(self, item):
        self.player.sell(loot[item].name, loot[item].value)
        self.merchant.buy(loot[item].name, loot[item].value)

    def buy(self, item, player, merchant):
        if validate_item(item) == True:
            if self.merchant.check_inventory_for_item(item) == True:
                if self.player.gold >= loot[item].value:
                    self.player.buy(loot[item].name, loot[item].value)
                    self.merchant.sell(loot[item].name, loot[item].value)
                    loot[item].on_buy()
                    self.offer_equip(item)
                else:
                    self.player_insufficient_funds(self.player.name)
                    self.notify()

    def examine(self, item, arg=None, arg2=None):
        if validate_item(item) == True:
            if item in loot:
                loot[item].on_examine(loot[item])

    def quit(self, arg=None, arg2=None, arg3=None):
        self.trading = False

    def show_wares(self):
        print(f"\n\n***\n{self.merchant.name}'s Shop\n***\n\n'")
        self.player.show_inventory()
        self.merchant.show_inventory()

    def return_invalid_command(self):
        print('Invalid command')

    def offer_equip(self, item):
        if isinstance(loot[item], Weapon) or isinstance(loot[item], Armor):
            query = input(f"Equip {item}? [y] [n] ")
            if query == 'y':
                self.player.equip(item)

    def compute_command(self, player_input):
        parsed_cmds = player_input.split(' ')
        arg = parsed_cmds[0]
        argument = ' '.join(parsed_cmds[1:])

        for key, value in commands.items():
            if arg in value:
                self.action = key
                self.argument = argument

    def execute_command(self, player, merchant):
        if self.action in self.commands:
            self.commands[self.action](self.argument, self.player, self.merchant)
        else:
            self.return_invalid_command()
        self.action = None
        self.argument = None

    def trade(self):
        self.trading = True
        print(f"{self.merchant.name}: Welcome, {self.player.name}! How can I help you today? (['buy', 'sell', 'examine', or 'quit'])")
        self.notify()
        while self.trading == True:
            self.show_wares()
            command_input = input('barter> ')
            self.compute_command(command_input)
            self.execute_command(self.player, self.merchant)
