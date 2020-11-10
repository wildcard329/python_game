from spell import Spell

class NonCombatSpell(Spell):
    def __init__(self, name, fatigue, target):
        super(Spell, self).__init__(name, fatigue)
        self.target = target
