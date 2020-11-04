import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.entered = False
        self.inventory = []

    def __str__(self):
        return f"\n{self.name}\n***\n{self.description}\n"

    def get_inventory(self):
        if len(self.inventory) > 0:
            print(self.inventory)
        else:
            print("You see nothing of interest in this room.")

    def spawn_item(self, item):
        spawn = random.randrange(4)
        if spawn == 3:
            self.inventory.append(item)

    def check_inventory_for_item(self, item):
        if item in self.inventory:
            return True
        else:
            print(f"{item} is not in this room.")

    def recieve_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)