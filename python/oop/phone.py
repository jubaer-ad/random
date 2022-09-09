from item import Item
import csv

class Phone(Item):
    def __init__(self, broken = 0, **kwargs):
        assert broken >= 0, f"Broken ({broken}) can not be less than 0!"
        super().__init__(
            name = kwargs["name"],
            price = kwargs["price"],
            quantity = kwargs["quantity"]
        )
        self.broken = broken
    
    def count_sellable(self):
        return self.quantity - self.broken
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("oop/phones.csv", "r") as f:
            reader = csv.DictReader(f)
            phones = list(reader)
        for phone in phones:
            Phone(
                broken = int(phone["broken"]),
                name = phone["name"],
                price = float(phone["price"]),
                quantity = int(phone["quantity"])
            )
    
    def __repr__(self) -> str:
        if Phone.is_integer(self.price):
            return f"{self.__class__.__name__}({self.broken}, \"{self.name}\", {int(self.price)}, {self.quantity})"
        return f"{self.__class__.__name__}({self.broken}, \"{self.name}\", {self.price}, {self.quantity})"
