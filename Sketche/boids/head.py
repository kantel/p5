import p5
from pvector import PVector

def setup():
    mover1 = PVector(10.0, 20.0)
    print(mover1.heading())
    print(mover1)
    mover2 = PVector(5, 7)
    print(mover2.heading())
    print(mover2)
    print(mover1 + mover2)
    print(mover1 - mover2)

def draw():
    pass

p5.run()