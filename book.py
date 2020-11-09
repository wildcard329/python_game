from item import Item

class Book(Item):
    def __init__(self, name, description, value, ability, s_type):
        super(Book, self).__init__(name, description, value)
        self.ability = ability
        self.s_type = s_type

    def on_read(self, ability):
        print(f"Learned {ability}")
        self.notify()
