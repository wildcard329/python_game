abilities = {
    'slash':    {'bonus': 150, 'fatigue': 10},
    'thrust':   {'bonus': 200, 'fatigue': 15},
    'bash':     {'bonus': 50, 'fatigue': 7},
    'stab':     {'bonus': 35, 'fatigue': 4},
    'bite':     {'bonus': 5, 'fatigue': 2},
    'scratch':  {'bonus': 3, 'fatigue': 1},
    'clobber':  {'bonus': 7, 'fatigue': 8},
    'strike':   {'bonus': 11, 'fatigue': 6},
    'wrap':     {'bonus': 8, 'fatigue': 4},
    'fire breath': {'bonus': 15, 'fatigue': 10},
    'stomp':     {'bonus': 9, 'fatigue': 5},
    'chomp':     {'bonus': 11, 'fatigue': 3},
    'slice and dice':   {'bonus': 2000, 'fatigue': 100},
    'skewer':   {'bonus': 1500, 'fatigue': 80},
    'zap':      {'bonus': 500, 'fatigue': 20},
    'burn':     {'bonus': 500, 'fatigue': 20},
    'chill':    {'bonus': 500, 'fatigue': 20}
}

non_combat_abilities = {
    'ensnare':  {'target_list_1': 'trapped', 'action_1': 'append', 'target_list_2': 'current_room.fallen', 'action_2': 'remove'},
    'summon':   {'target_list_1': 'minions', 'action_1': 'append', 'target_list_2': 'trapped', 'action_2': 'remove'}
}

def validate_map_spell(spell):
    if spell in non_combat_abilities:
        return True
    else:
        print(f"{spell} is not a spell")
