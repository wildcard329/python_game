from room import Room
from player import Player
from item import Item
from map_parser import Map_Parser
from map1 import room

playing = True
while playing == True:
    name = input('Enter a player name ')
    player = Player(name, room['outside'], 50, 18, 0, 2, 1)
    player.explore_room()
    player.playing = True
    while player.playing == True:
        p_cmd = input('> ')
        parse_cmd = Map_Parser()
        parse_cmd.parse(player, p_cmd)
    if player.playing == False:
        playing = False
