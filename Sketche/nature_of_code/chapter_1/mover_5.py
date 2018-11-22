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
        self.location = PVector(p5.random_uniform(width), p5.random_uniform(height))
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.topspeed = 4
        self.r = 15
    
    def update(self):
        mouse = PVector(mouse_x, mouse_y)
        dir = mouse - self.location
        dir.normalize()
        dir.mult(0.1)
        self.acceleration = dir
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

numMovers = 20
movers = []

def setup():
    global mover
    p5.size(640, 360)
    for _ in range(numMovers):
        movers.append(Mover())

def draw():
    p5.background(43, 62, 80)
    
    for mover in movers:
        mover.update()
        mover.check_boundaries()
        mover.display()
p5.run()