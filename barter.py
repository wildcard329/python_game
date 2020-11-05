from player import Player
from npc_roster import characters
from catalogue import loot, validate_item

class Barter:
    def __init__(self, player, merchant):
        self.player = player
        self.merchant = merchant
        self.action = {}
        self.action['sell'] = self.sell
        self.action['buy'] = self.buy
        self.action['quit'] = self.quit
        self.trading = False

    def not_in_inventory(self, item, character):
        print(f"{item} is not in {character}'s inventory.")

    def merchant_insufficient_funds(self, merchant):
        print(f"{merchant}: I'm sorry, I do not have enough gold for that.")
        input()

    def player_insufficient_funds(self, player):
        print(f"{player}: Whoops, I don't have enough gold for that.")
        input()

    def sell(self, item):
        if validate_item(item) == True:
            if item in loot:
                if self.merchant.gold > loot[item].value:
                    self.player.sell(loot[item].name, loot[item].value)
                    self.merchant.buy(loot[item].name, loot[item].value)
                    loot[item].on_sell()
                else:
                    self.merchant_insufficient_funds(self.merchant.name)
            else:
                self.not_in_inventory(item, self.player.name)

    def buy(self, item):
        if validate_item(item) == True:
            if item in loot:
                if self.player.gold > loot[item].value:
                    self.player.buy(loot[item].name, loot[item].value)
                    self.merchant.sell(loot[item].name, loot[item].value)
                    loot[item].on_buy()
                else:
                    self.player_insufficient_funds(self.player.name)
            else:
                self.not_in_inventory(item, self.merchant.name)

    def quit(self, arg=None):
        self.trading = False

    def show_wares(self):
        self.player.show_inventory()
        self.player.show_gold()
        self.merchant.show_inventory()
        self.merchant.show_gold()

    def trade(self):
        self.trading = True
        print(f"{self.merchant.name}: Welcome, {self.player.name}! How can I help you today? (['buy', 'sell', or 'quit'])")
        while self.trading == True:
            self.show_wares()
            command_input = input('barter> ')
            parsed_input = command_input.split(' ')
            action = parsed_input[0]
            argument = " ".join(parsed_input[1:])
            self.action[action](argument)
