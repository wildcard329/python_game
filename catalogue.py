from item import Item
from weapon import Weapon
from armor import Armor
from room import Room
from map1 import room

loot = {
    "diamond": Item("diamond", "This should be worth something...", 1000),
    "ruby": Item("ruby", "This should be worth something...", 200),
    "emerald": Item("emerald", "This should be worth something...", 75),
    "sapphire": Item("sapphire", "This should be worth something...", 50),
    "rusty iron dagger": Weapon("rusty iron dagger", "Really dull blade.", 25, 5),
    "iron dagger": Weapon("iron dagger", "Better than rusty...", 30, 7),
    "steel dagger": Weapon("steel dagger", "Could cause some damage.", 45, 10),
    "rusty iron armor": Armor("rusty iron armor", "Really bad armor.", 50, 10),
    "iron armor": Armor("iron armor", "It might defend fairly well.", 65, 13),
    "steel armor": Armor("steel armor", "Sturdy line of defense.", 75, 17)
}

def validate_item(item):
    if item in loot:
        return True
    else:
        print("Invalid item")
