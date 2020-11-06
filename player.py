from catalogue import loot, validate_item
from npc_roster import characters
from merchant import Merchant
from combatant import Combatant
from weapon import Weapon
from armor import Armor

class Player(Merchant, Combatant):
    def __init__(self, name, current_room, health, focus, gold, atk, defense):
        super(Player, self).__init__(name, current_room, health, focus, gold, atk, defense)
        self.playing = False
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.special_attacks = []

    def __str__(self):
        return f"\n{self.name} is in {self.current_room.name}\n"

    def quit(self):
        self.playing = False

    def show_stats(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.atk}\nDefense: {self.defense}\nWeapon: {self.weapon}\nArmor: {self.armor}\nSpecial Attacks: {self.special_attacks}")

    def explore_room(self):
        if self.current_room.entered == False:
            print(self.current_room)
            self.current_room.entered = True
        if len(self.current_room.occupants) > 0:
            self.current_room.get_occupants()
        else:
            self.current_room.get_inventory()

    def return_invalid(self):
        print("Invalid target")

    def examine(self, target):
        if target in loot:
            if target in self.inventory or target in self.current_room.inventory:
                print(loot[target])
            else:
                self.return_invalid()
        else:
            self.return_invalid()

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)
