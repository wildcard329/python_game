from equipment import Equipment

class Weapon(Equipment):
    def __init__(self, name, description, value, atk_rating, special_attacks):
        super(Equipment, self).__init__(name, description, value)
        self.atk_rating = atk_rating
        self.special_attacks = special_attacks

    def __str__(self):
        return super(Weapon, self).__str__() + f"\nAttack Rating: {self.atk_rating}"

    def validate_weapon(self, item):
        if isinstance(item, Weapon):
            return True
