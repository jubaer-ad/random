car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.keys()
print(x) #before the change

car["color"] = "white"

y = car.keys()

print(x) #after the change
