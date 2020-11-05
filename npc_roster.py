from merchant import Merchant
from enemy import Enemy
from monster import Monster

characters = {
    "Gary": Merchant("Gary", None, 50, 12, 500, 10, 3),
    "Thug": Enemy("Thug", None, 18, 7, 5, 1, 1),
    "Goblin": Monster("Goblin", None, 15, 7, 2, 1, 1),
    "Troll": Monster("Troll", None, 25, 4, 2, 10, 7),
    "Imp": Monster("Imp", None, 7, 5, 2, 1, 1),
    "Hydra": Monster("Hydra", None, 100, 50, 25, 10, 25)
}