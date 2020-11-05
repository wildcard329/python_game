from merchant import Merchant
from enemy import Enemy
from monster import Monster

characters = {
    "Gary": Merchant("Gary", None, 50, 12, 500, 10, 3),
    "Jill": Merchant("Jill", None, 15, 7, 200, 1, 1),
    "Thug": Enemy("Thug", None, 18, 7, 5, 1, 1),
    "Goblin": Monster("Goblin", None, 15, 7, 2, 1, 1),
    "Troll": Monster("Troll", None, 25, 4, 2, 10, 7),
    "Imp": Monster("Imp", None, 7, 5, 2, 1, 1),
    "Hydra": Monster("Hydra", None, 100, 50, 25, 10, 25)
}

characters["Gary"].spawn_inventory("iron dagger")
characters["Gary"].spawn_inventory("steel dagger")
characters["Gary"].spawn_inventory("rusty iron armor")
characters["Gary"].spawn_inventory("iron armor")
characters["Gary"].spawn_inventory("steel armor")

characters["Thug"].spawn_item("iron dagger")
characters["Imp"].spawn_rare_item("sapphire")
characters["Troll"].spawn_item("ruby")
characters["Hydra"].spawn_loot("diamond")