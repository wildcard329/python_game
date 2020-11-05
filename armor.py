from equipment import Equipment

class Armor(Equipment):
    def __init__(self, name, description, value, armor_rating):
        super(Equipment, self).__init__(name, description, value)
        self.armor_rating = armor_rating