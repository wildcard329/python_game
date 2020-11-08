from item import Item

class Book(Item):
    def __init__(self, name, description, value, ability):
        super(Book, self).__init__(name, description, value)
        self.ability = ability

    def on_read(self, ability):
        print(f"Learned {ability}")
        self.notify()
