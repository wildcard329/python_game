from item import Item
from weapon import Weapon
from armor import Armor

loot = {
    "diamond": Item("diamond", "Wow, I'm rich!!!", 1000),
    "ruby": Item("ruby", "This should be worth something...", 200),
    "emerald": Item("emerald", "This should be worth something...", 75),
    "sapphire": Item("sapphire", "This should be worth something...", 50),
    "rusty iron dagger": Weapon("rusty iron dagger", "Really dull blade.", 25, 5, ['stab']),
    "iron dagger": Weapon("iron dagger", "Better than rusty...", 30, 7, ['stab']),
    "steel dagger": Weapon("steel dagger", "Could cause some damage.", 45, 10, ['stab']),
    "rusty iron armor": Armor("rusty iron armor", "Really bad armor.", 50, 10),
    "iron armor": Armor("iron armor", "It might defend fairly well.", 65, 13),
    "steel armor": Armor("steel armor", "Sturdy line of defense.", 75, 17),
    "club": Weapon("club", "Great for blunt force trauma", 50, 15, ['bash']),
    "steel sword": Weapon("steel sword", "Great weapon...I want it!", 200, 55, ['slash', 'thrust'])
}

def validate_item(item):
    if item in loot:
        return True
    else:
        print("Invalid item")

def validate_equipment(item):
    if isinstance(item, Weapon) or isinstance(item, Armor):
        return True
    else:
        print(f"You cannot equip {item}")
        