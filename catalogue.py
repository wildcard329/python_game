from item import Item
from weapon import Weapon
from armor import Armor
from book import Book

loot = {
    "diamond": Item("diamond", "Wow, I'm rich!!!", 4000),
    "ruby": Item("ruby", "This should be worth something...", 2000),
    "emerald": Item("emerald", "This should be worth something...", 750),
    "sapphire": Item("sapphire", "This should be worth something...", 500),
    "rusty iron dagger": Weapon("rusty iron dagger", "Really dull blade.", 25, 5, ['stab']),
    "iron dagger": Weapon("iron dagger", "Better than rusty...", 30, 7, ['stab']),
    "steel dagger": Weapon("steel dagger", "Could cause some damage.", 45, 10, ['stab']),
    "rusty iron armor": Armor("rusty iron armor", "Really bad armor.", 50, 10),
    "iron armor": Armor("iron armor", "It might defend fairly well.", 65, 13),
    "steel armor": Armor("steel armor", "Sturdy line of defense.", 75, 17),
    "club": Weapon("club", "Great for blunt force trauma", 50, 15, ['bash']),
    "steel sword": Weapon("steel sword", "Great weapon...I want it!", 200, 55, ['slash', 'thrust']),
    "plasma cutter": Weapon("plasma cutter", "Cuts through everything like butter.", 5000, 2000, ['slice and dice', 'skewer']),
    "book: zap": Book("book: zap", "Teaches reader how to shoot sparks from fingertips", 200, "zap"),
    "book: burn": Book("book: burn", "Teaches reader how to evoke flames", 200, "burn"),
    "book: chill": Book("book: chill", "Teaches reader how to use ice attacks", 200, "chill"),
    "book: ensnare": Book("book: ensnare", "Teaches reader how to trap enemy in a pocket dimension", 1000, "ensnare"),
    "book: summon": Book("book: summon", "Teaches reader how to summon ensnared enemies", 1000, "summon")
}

def validate_item(item):
    print(item)
    print(item in loot)
    if item in loot:
        return True
    else:
        print("Invalid item")

def validate_equipment(item):
    if isinstance(item, Weapon) or isinstance(item, Armor):
        return True
    else:
        print(f"You cannot equip {item.name}")
