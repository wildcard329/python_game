from item import Item
from room import Room
from map1 import room

loot = {
    "diamond": Item("diamond", "This should be worth something...", 1000),
    "ruby": Item("ruby", "This should be worth something...", 200),
    "emerald": Item("emerald", "This should be worth something...", 75),
    "sapphire": Item("sapphire", "This should be worth something...", 50),
    "rusty iron dagger": Item("rusty iron dagger", "Really dull blade.", 25),
    "iron dagger": Item("iron dagger", "Better than rusty...", 30),
    "steel dagger": Item("steel dagger", "Could cause some damage.", 45),
    "rusty iron armor": Item("rusty iron armor", "Really bad armor.", 50),
    "iron armor": Item("iron armor", "It might defend fairly well.", 65),
    "steel armor": Item("steel armor", "Sturdy line of defense.", 75)
}

def validate_item(item):
    if item in loot:
        return True
    else:
        print("Invalid item")
