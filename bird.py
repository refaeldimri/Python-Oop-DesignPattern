from animal import Animal

class Bird(Animal):
    def __init__(self):
        super().__init__()

    def birdmakesound(self):
        super().makeSound("chif chif")

    def move(self):
        print("bird move")
