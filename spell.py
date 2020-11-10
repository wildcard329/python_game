from ability import Ability

class Spell(Ability):
    def __init__(self, name, fatigue):
        super(Spell, self).__init__(name, fatigue)
        