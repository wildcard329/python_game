class Character:
    def __init__(self, name, current_room, health, focus, gold, atk, defense, description):
        self.name = name
        self.current_room = current_room
        self.health = health
        self.focus = focus
        self.gold = gold
        self.inventory = []
        self.atk = atk
        self.defense = defense
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\nClass: {type(self).__name__}\nDescription: {self.description}"

    def explore_room(self):
        if self.current_room.entered == False:
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
        print(f"{self.name}\nInventory: {self.inventory}\nGold: {self.gold}")

    def check_inventory_for_item(self, item):
        if item in self.inventory:
            return True
        else:
            print(f"{item} is not in inventory.")

