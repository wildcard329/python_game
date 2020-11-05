import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.entered = False
        self.inventory = []
        self.occupants = []

    def __str__(self):
        return f"\n{self.name}\n***\n{self.description}\n"

    def get_inventory(self):
        if len(self.inventory) > 0:
            print(self.inventory)
        else:
            print("You see nothing of interest in this room.")

    def get_occupants(self):
        if len(self.occupants) > 0:
            print([occupant.name for occupant in self.occupants])

    def spawn_item(self, item):
        spawn = random.randrange(4)
        if spawn == 3:
            self.inventory.append(item)

    def spawn_enemy(self, enemy):
        spawn = random.randrange(4)
        if spawn > 1:
            self.occupants.append(enemy)

    def spawn_req_fight(self, enemy):
        self.occupants.append(enemy)

    def spawn_merchant(self, merchant):
        self.occupants.append(merchant)

    def not_in_room(self, arg):
        print(f"{arg} is not in this room.")

    def check_inventory_for_item(self, item):
        if item in self.inventory:
            return True
        else:
            self.not_in_room(item)

    def check_occupants_for_character(self, char):
        if char in self.occupants:
            return True
        else:
            self.not_in_room(char.name)

    def recieve_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)