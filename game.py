from room import Room
from player import Player
from item import Item
from map_parser import Map_Parser
from map1 import room, map1_intro

playing = True
while playing == True:
    map1_intro()
    name = input('Enter a player name ')
    player = Player(name, room['outside'], 1500, 180, 20000, 10, 8, "Star of the show.")
    player.explore_room()
    player.playing = True
    while player.playing == True:
        p_cmd = input('> ')
        parse_cmd = Map_Parser()
        parse_cmd.parse(player, p_cmd)
    if player.playing == False:
        player.game_over()
        playing = False
