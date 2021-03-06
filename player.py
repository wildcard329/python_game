from catalogue import loot, validate_item
from npc_roster import characters
from merchant import Merchant
from mage import Mage
from combatant import Combatant
from weapon import Weapon
from armor import Armor

class Player(Merchant, Combatant, Mage):
    def __init__(self, name, current_room, health, focus, gold, atk, defense, description):
        super(Player, self).__init__(name, current_room, health, focus, gold, atk, defense, description)
        self.playing = False
        self.alive = True
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.special_attacks = []
        self.non_combat_special = []
        self.trapped = []
        self.minions = []
        self.level = 1
        self.xp = 0
        self.toNextLevel = self.level * 20

    def __str__(self):
        return f"\n{self.name} is in {self.current_room.name}\n"

    def show_inventory(self):
        print(f"{self.name}\nInventory: {self.inventory}\nGold: {self.gold}\nWeapon: {self.weapon}\nArmor: {self.armor}")   

    def show_aquired_trapped(self):
        if len(self.trapped) > 0:
            print(f"Trapped souls at your disposal: {[char.name for char in self.trapped]}")
            return True
        else:
            print("You have no trapped enemies.")

    def show_aquired_minions(self):
        if len(self.minions) > 0:
            print(f"Minions at your disposal: {[char.name for char in self.minions]}")

    def confirm_nc_spells(self):
        if len(self.non_combat_special) > 0:
            return True
        else:
            print(f"{self} does not have any spells to use outside combat.")

    def show_non_combat_spells(self):
        print(self.non_combat_special)

    def quit(self):
        self.playing = False

    def show_stats(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.atk}\nDefense: {self.defense}\nLevel: {self.level}\nNext: {self.xp}/{self.toNextLevel}\nWeapon: {self.weapon}\nArmor: {self.armor}\nSpecial Attacks: {self.special_attacks}")

    def explore_room(self):
        if self.current_room.entered == False:
            print(self.current_room)
            self.current_room.entered = True
        if len(self.current_room.occupants) > 0:
            self.current_room.get_occupants()
        if len(self.current_room.fallen) > 0:
            self.current_room.show_defeated()
        else:
            self.current_room.get_inventory()

    def return_invalid(self):
        print("Invalid target")

    def examine(self, target):
        if target in loot or target in characters:
            if target in self.inventory or target in self.current_room.inventory:
                print(loot[target])
            elif characters[target] in self.current_room.occupants and target in characters:
                print(characters[target])
            else:
                self.return_invalid()
        else:
            self.return_invalid()

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def levelup(self):
        if self.xp >= self.toNextLevel:
            self.xp -= self.toNextLevel
            self.level += 1
            self.recalculateNextXP()
            print(f"{self.name} leveled up! Now at level {self.level}.")

    def recalculateNextXP(self):
        self.toNextLevel = self.level * 20

    def game_over(self):
        if self.health <= 0:
            print("Oh no, you have taken lethal damage...\n\nGAME OVER")
        elif len(self.inventory) >= 20:
            print("""Congradulations, you have obtained the lost treasure
and defeated the dragon, may word of your deeds spread swiftly
throughout the land, as you claim your new title of dragon slayer.""")
