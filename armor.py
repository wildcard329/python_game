from equipment import Equipment

class Armor(Equipment):
    def __init__(self, name, description, value, armor_rating):
        super(Equipment, self).__init__(name, description, value)
        self.armor_rating = armor_rating

    def __str__(self):
        return super(Armor, self).__str__() + f"\nArmor Rating: {self.armor_rating}"
    
    def validate_armor(self, item):
        if isinstance(item, Armor):
            return True
