from spell import Spell
from combat_ability import CombatAbility

class CombatSpell(Spell, CombatAbility):
    def __init__(self, name, fatigue, character_damage)
        super(Spell, CombatAbility, self).__init__(name, fatigue, character_damage)
        