import csv

class Item:
    discount: float = 0.8
    all = []
    assert discount >= 0 and discount <= 1, "Discount must be between 0 and 1!"
    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0, "Price ({price}) can not be negative!".format(price = price)
        assert quantity >= 0, "Quantity ({quantity}) can not be negative!".format(quantity = quantity)
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)
    
    #getter for private attribute name
    @property
    def name(self):
        return self.__name
    
    #setter for private attribute name
    @name.setter
    def name(self, value):
        if len(value) > 20:
            raise Exception("The length of Name is must be under 20!")
        else:
            self.name = value
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value: float):
        if isinstance(value, float) or isinstance(value, int):
            assert value >= 0, "Price ({value}) can not be negative!".format(value = value)
            self.__price = value
        else:
            raise Exception("Invalid price value!")

    
    def calculate_total_price(self):
        return self.__price * self.quantity
        
    def calculate_discounted_price(self):
        return self.calculate_total_price() * self.discount
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __connect(self):
        return "In connect!"
    
    def __message_body(self):
        pass
    
    def __send(self):
        pass
    
    def send_mail(self):
        self.__connect()
        self.__message_body()
        self.__send()
        return "Mail sent!"
    
    def __repr__(self) -> str:
        if Item.is_integer(self.__price):
            return f"{self.__class__.__name__}(\"{self.name}\", {int(self.__price)}, {self.quantity})"
        return f"{self.__class__.__name__}(\"{self.name}\", {self.__price}, {self.quantity})"
    
