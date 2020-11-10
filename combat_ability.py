from ability import Ability
import random

class CombatAbility(Ability):
    def __init__(self, name, fatigue, character_damage):
        super(Ability, self).__init__(name, fatigue)
        self.character_damage = character_damage

    def deal_damage(self)
        attack_multiplier = random.randrange(5, 11)
        self.character_damage *= attack_multiplier
