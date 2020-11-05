from equipment import Equipment

class Weapon(Equipment):
    def __init__(self, name, description, value, atk_rating):
        super(Equipment, self).__init__(name, description, value)
        self.atk_rating = atk_rating
