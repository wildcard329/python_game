class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.description}\nValue: {self.value} Gold"

    def on_take(self):
        print(f"Aquired {self.name}")

    def on_drop(self):
        print(f"Drooped {self.name}")

    def on_sell(self):
        print(f"Sold {self.name}")

    def on_buy(self):
        print(f"Bought {self.name}")
