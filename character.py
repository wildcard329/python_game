class Character:
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        self.name = name
        self.current_room = current_room
        self.health = health
        self.focus = focus
        self.gold = gold
        self.inventory = []
        self.atk = atk
        self.defense = defense

    def explore_room(self):
        if self.current_room.entered == False:
            print(self.current_room)
            self.current_room.entered = True

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

    def show_gold(self):
        print(f"Gold: {self.gold}")

    def check_inventory_for_item(self, item):
        if item in self.inventory:
            return True
        else:
            print(f"{item} is not in inventory.")
            