class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"


class Room(Item):
    def __init__(self, name, description, items):
        self.items = items
        super().__init__(name, description)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.item}"
