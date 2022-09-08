class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound}! I am {name}! {sound}".format(name = self.name, sound = self.sound))


class Pig(Animal):
    sound = "Oink!"

piggy = Pig("Piggy")
piggy.speak()

class Cow(Animal):
    sound = "Moo!"

milky = Cow("Aussi Brown")
milky.speak()

# pig = Animal("piggy")
# pig.speak() 