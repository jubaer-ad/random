from unicodedata import name
from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

# Phone.instantiate_from_csv()
# print(Item.all)
# print(Phone.all[2].count_sellable())

item1 = Item("Lappy", 40, 6)
print(item1)
print(item1.__dict__)
print(item1.send_mail())
print(item1._Item__connect())

item2 = Phone(2, name = "JBPv003",price = 699, quantity = 11)
print(item2)
print(item2.__dict__)
print(item2.send_mail())


