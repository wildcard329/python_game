class Parser:
    def __init__(self, command):
        self.command = command
        self.action = None
        self.argument = None
        
    def parse_command(self):
        command = self.command.split(' ')
        self.action = command[0]
        self.argument = ''.join(command[:1])
