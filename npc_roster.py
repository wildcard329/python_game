from merchant import Merchant
from enemy import Enemy
from monster import Monster

characters = {
    "Gary": Merchant("Gary", None, 50, 12, 15000, 10, 3),
    "Jill": Merchant("Jill", None, 15, 7, 200, 1, 1),
    "Thug": Enemy("Thug", None, 180, 7, 5, 1, 1),
    "Goblin": Monster("Goblin", None, 150, 7, 2, 1, 1, ['bite', 'scratch']),
    "Troll": Monster("Troll", None, 250, 4, 2, 10, 7, ['clobber']),
    "Imp": Monster("Imp", None, 70, 5, 2, 1, 1, ['bite', 'scratch']),
    "Hydra": Monster("Hydra", None, 2500, 50, 25, 10, 25, ['strike', 'wrap']),
    "Weapons Master": Enemy("Weapons Master", None, 2000, 75, 52, 100, 91),
    "Dragon": Monster("Dragon", None, 5000, 100, 2000, 150, 75, ['fire breath', 'stomp', 'strike', 'chomp'])
}

characters["Gary"].spawn_inventory("iron dagger")
characters["Gary"].spawn_inventory("steel dagger")
characters["Gary"].spawn_inventory("rusty iron armor")
characters["Gary"].spawn_inventory("iron armor")
characters["Gary"].spawn_inventory("steel armor")
characters["Gary"].spawn_inventory("plasma cutter")

characters["Thug"].spawn_item("iron dagger")
characters["Thug"].spawn_rare_item("steel dagger")
characters["Imp"].spawn_rare_item("sapphire")
characters["Troll"].spawn_item("ruby")
characters["Troll"].spawn_loot("club")
characters["Weapons Master"].spawn_loot("steel sword")
characters["Weapons Master"].spawn_loot("steel armor")
characters["Hydra"].spawn_loot("diamond")

def return_invalid():
    print("Invalid target")

def is_character(target):
    if target in characters:
        return True
    else:
        return_invalid()

def validate_barter(target):
    if is_character(target) == True:
        if isinstance(characters[target], Merchant):
            return True
        else:
            return_invalid()

def validate_battle(target):
    if is_character(target) == True:
        if isinstance(characters[target], Enemy) or isinstance(target, Monster):
            return True
        else:
            return_invalid()
        