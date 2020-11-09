from room import Room
from npc_roster import characters

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'chamber':  Room("Hidden Chamber", """Here dwells the weapons master of legend!
Face him if you dare!"""),

    'dragon':   Room("Dragon's Lair", """Ah, here's all the treasure...wait, nobody
said anything about a dragon!!!""")

}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['chamber'].e_to = room['overlook']
room['overlook'].w_to = room['chamber']
room['dragon'].w_to = room['narrow']
room['narrow'].e_to = room['dragon']

room["foyer"].spawn_item("emerald")
room["foyer"].spawn_item("rusty iron dagger")
room["overlook"].spawn_item("ruby")
room["narrow"].spawn_item("rusty iron dagger")
room["narrow"].spawn_item("emerald")
room["treasure"].spawn_item("ruby")
room['chamber'].spawn_loot("ruby")
room["chamber"].spawn_loot("sapphire")
room["dragon"].mass_spawn_loot("ruby")
room["dragon"].mass_spawn_loot("emerald")
room["dragon"].mass_spawn_loot("emerald")
room["dragon"].mass_spawn_loot("sapphire")
room["dragon"].mass_spawn_loot("sapphire")
room["dragon"].mass_spawn_loot("sapphire")

room["outside"].spawn_merchant(characters["Rebecca"])
room["outside"].spawn_merchant(characters["Gary"])
room["foyer"].spawn_enemy(characters["Goblin"])
room["foyer"].spawn_enemy(characters["Goblin"])
room["foyer"].spawn_enemy(characters["Goblin"])
room["foyer"].spawn_enemy(characters["Goblin"])
room["foyer"].spawn_enemy(characters["Goblin"])
room["foyer"].spawn_enemy(characters["Thug"])
room["overlook"].spawn_req_fight(characters["Troll"])
room["narrow"].spawn_enemy(characters["Imp"])
room["narrow"].spawn_enemy(characters["Imp"])
room["narrow"].spawn_enemy(characters["Thug"])
room["narrow"].spawn_enemy(characters["Thug"])
room["narrow"].spawn_enemy(characters["Goblin"])
room["treasure"].spawn_req_fight(characters["Hydra"])
room["chamber"].spawn_req_fight(characters["Weapons Master"])
room["dragon"].spawn_req_fight(characters["Dragon"])

def notify():
    input('Press [enter] to continue.')

def map1_intro():
    print("""Greetings, adventurer. You have been carefully selected 
for the quest of finding the lost treasure of the forgotten
mine. Although you are going in empty-handed, you will find
enemies that on occasion drop loot which will either have
monetary value or boost your battle performance. Best of luck
on your adventure!!!""")
    notify()
