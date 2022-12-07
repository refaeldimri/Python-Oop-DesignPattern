from abc import abstractclassmethod, ABC

class Animal(ABC):
    # members:
    
    def __init__(self):
        self.time = 0

    def sleep(self, time = 10):
        self.time = time
        print("sleep in hours: " + str(self.time))

    def makeSound(self, sound):
        self.sound = sound
        print(self.sound)

    @abstractclassmethod
    def move(self):
        pass
    





