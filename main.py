from dog import Dog
from bird import Bird
from factory import Factor

from person import Person


if __name__ == "__main__":
    # a = Dog(10)
    # a.dogmakesound()

    # b = Bird()
    # b.birdmakesound()

    # a.move()

    r = Factor(15)
    x = r.getObject()
    x.drink()

    p = Person()
    
    