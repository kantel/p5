import p5
import os
from pvector import PVector

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

class Mover(object):
    
    def __init__(self):
        self.location = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.topspeed = 10
        self.r = 15
    
    def update(self):
        # self.acceleration = PVector.random2D()
        self.acceleration = PVector(p5.random_uniform(-1, 1), p5.random_uniform(-1, 1))
        self.acceleration.normalize()
        # self.acceleration.mult(0.5)
        self.acceleration.mult(p5.random_uniform(2))
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.location.add(self.velocity)
    
    def display(self):
        p5.stroke(0)
        p5.fill(255, 100, 255)
        p5.circle((self.location.x, self.location.y), 2*self.r)
    
    def check_boundaries(self):
        if (self.location.x > width + self.r):
            self.location.x = -self.r
        elif (self.location.x < -self.r):
            self.location.x = width + self.r
        
        if (self.location.y > height + self.r):
            self.location.y = -self.r
        elif (self.location.y < -self.r):
            self.location.y = height + self.r


def setup():
    global mover
    p5.size(640, 360)
    mover = Mover()

def draw():
    p5.background(43, 62, 80)
    
    mover.update()
    mover.check_boundaries()
    mover.display()

p5.run()