from room import Room
from player import Player
from item import Item
from parser import Parser
from map1 import room

playing = True
while playing == True:
    name = input('Enter a player name ')
    player = Player(name, room['outside'])
    player.playing = True
    while player.playing == True:
        p_cmd = input('> ')
        parse_cmd = Parser()
        parse_cmd.parse(player, p_cmd)
    if player.playing == False:
        playing = False