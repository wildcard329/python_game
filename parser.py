class Parser:
    def __init__(self, command):
        self.command = command
        self.action = None
        self.argument = None
        
    def parse_command(self):
        self.action = self.command[0]
        self.argument = self.command[:1]
