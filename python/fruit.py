class Fruit:
    def __init__(self, taste, color):
        self.taste = taste
        self.color = color

class Apple(Fruit):
    def printStat(self):
        print("Apple:" + self.taste + ":" + self.color)
class Banana(Fruit):
    def printStat(self):
        print("Banana:" + self.taste + ":" + self.color)

banana001 = Banana("taste001", "color001")
print(banana001.taste)
banana001.printStat()
apple001 = Apple("taste002", "color002")
apple001.printStat()