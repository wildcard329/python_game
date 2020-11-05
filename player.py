from catalogue import loot
from merchant import Merchant

class Player(Merchant):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        self.name = name
        self.current_room = current_room
        self.playing = False
        self.inventory = []

    def __str__(self):
        return f"\n{self.name} is in {self.current_room.name}\n"

    def quit(self):
        self.playing = False

    def move(self, current_room, direction):
        move = f"{direction}_to"
        if hasattr(current_room, move):
            new_room = getattr(current_room, move)
            self.current_room = new_room
            print(f"{self.name} entered {new_room.name}")
            self.explore_room()
        else:
            print('You cannot move in that direction.')

    def show_inventory(self):
        print(f"{self.name}\nInventory: {self.inventory}")

    def explore_room(self):
        if self.current_room.entered == False:
            print(self.current_room)
            self.current_room.entered = True
        if len(self.current_room.occupants) > 0:
            self.current_room.get_occupants()
        else:
            self.current_room.get_inventory()

    def check_inventory_for_item(self, item):
        if item in self.inventory:
            return True
        else:
            print(f"{item} is not in your inventory.")
    
    def return_invalid(self):
        print("Invalid target")

    def examine(self, target):
        if target in loot:
            if target in self.inventory or target in self.current_room.inventory:
                print(loot[target])
            else:
                self.return_invalid()
        else:
            self.return_invalid()

    def validate_target(self, target):
        if target in loot:
            return True
        else:
            self.return_invalid()

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)