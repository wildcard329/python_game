from character import Character

class Merchant(Character):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        super(Merchant, self).__init__(name, current_room, health, focus, gold, atk, defense)
        self.inventory = []

    def spawn_inventory(self, item):
        self.inventory.append(item)

    def sell(self, item, value):
        self.inventory.remove(item)
        self.gold += value

    def buy(self, item, value):
        self.inventory.append(item)
        self.gold -= value

    