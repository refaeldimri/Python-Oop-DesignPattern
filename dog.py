from animal import Animal

class Dog(Animal):

    def __init__(self, km):
        super().__init__()
        self.km = km

    def run(self):
        print("dog run", self.km)

    def dogmakesound(self):
        super().makeSound("hav hav")

   # def move(self):
    #    print("dog move")

