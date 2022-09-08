class Item:
    def __init__(self, size):
        self.size = size

item001 = Item("y")
item001.name = "Table"
print(item001.name)
print(item001.size)
item001.size = 4
print(item001.size)
