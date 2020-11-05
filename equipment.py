from item import Item

class Equipment(Item):
    def __init__(self, name, description, value):
        super(Equipment, self).__init__(name, description, value)

    def on_equip(self, equipment):
        print(f"Equiped {equipment}")
        input()

    def on_unequip(self, equipment):
        print(f"Unequipped {equipment}")
        input()