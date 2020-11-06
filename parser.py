# This file currently does not do anything, but I hope to eventually make it a parent class for the map parser, battle parser, and barter parser
# The reason it did not work was because I don't initialize parser with anything, so I can't pass attributes down which get reused between the three classes

# commands = {}

# class Parser:
#     def __init__(self):
#         self.commands = {}
#         self.action = None
#         self.argument = None

#     def return_invalid_command(self):
#         print('Invalid command')

#     def compute_command(self, player_input):
#         parsed_cmds = player_input.split(' ')
#         arg = parsed_cmds[0]
#         argument = ' '.join(parsed_cmds[1:])

#         for key, value in commands.items():
#             if arg in value:
#                 self.action = key
#                 if len(parsed_cmds) == 1:
#                     self.argument = arg
#                 else:
#                     self.argument = argument

#     def execute_command(self, player):
#         if self.action in self.commands:
#             self.commands[self.action](player, self.argument)
#         else:
#             self.return_invalid_command()
#         self.action = None
#         self.argument = None

#     def parse(self, player, cmd):
#         self.compute_command(cmd)
#         self.execute_command(player)
