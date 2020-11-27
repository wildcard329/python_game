from merchant import Merchant
from enemy import Enemy
from monster import Monster

characters = {
    "Gary": Merchant("Gary", None, 50, 12, 15000, 10, 3, "Here to buy and sell goods."),
    "Rebecca": Merchant("Rebecca", None, 15, 7, 200, 1, 1, "Here to buy and sell goods"),
    "Thug": Enemy("Thug", None, 180, 7, 5, 1, 1, "Looks kind of menacing.", 10),
    "Goblin": Monster("Goblin", None, 150, 7, 2, 1, 1, "Just a filthy, green goblin", ['bite', 'scratch'], 5),
    "Troll": Monster("Troll", None, 250, 4, 2, 10, 7, "Yikes, a troll...",  ['clobber'], 50),
    "Imp": Monster("Imp", None, 70, 5, 2, 1, 1, "Full of mischeif", ['bite', 'scratch'], 5),
    "Hydra": Monster("Hydra", None, 2500, 50, 25, 10, 25, "If the legends are true, I don't want to fight this.", ['strike', 'wrap'], 100),
    "Weapons Master": Enemy("Weapons Master", None, 2000, 75, 52, 100, 91, "The renowned weapons expert. I'd hate to be in a dual with him.", 2500),
    "Dragon": Monster("Dragon", None, 5000, 100, 2000, 150, 75, "Well, there's the treasure...and unfortunately the dragon.", ['fire breath', 'stomp', 'strike', 'chomp'], 5000)
}

characters["Gary"].spawn_inventory("iron dagger")
characters["Gary"].spawn_inventory("steel dagger")
characters["Gary"].spawn_inventory("rusty iron armor")
characters["Gary"].spawn_inventory("iron armor")
characters["Gary"].spawn_inventory("steel armor")
characters["Gary"].spawn_inventory("plasma cutter")

characters["Rebecca"].spawn_inventory("book: zap")
characters["Rebecca"].spawn_inventory("book: burn")
characters["Rebecca"].spawn_inventory("book: chill")
characters["Rebecca"].spawn_inventory("book: ensnare")
characters["Rebecca"].spawn_inventory("book: summon")

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
        