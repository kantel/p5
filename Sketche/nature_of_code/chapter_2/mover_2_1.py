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
        self.location = PVector(width/2, height/2) # Ort
        self.velocity = PVector(1, 0.5) # Geschwindigkeit
        self.acceleration = PVector(0, 0) # Beschleunigung
        self.r = 15 # Radius
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
    
    def display(self):
        p5.stroke(0)
        p5.fill(255, 100, 255)
        p5.circle((self.location.x, self.location.y), 2*self.r)
    
    def check_edges(self):
        if (self.location.x > width - self.r):
            self.location.x = width - self.r
            self.velocity.x *= -1
        elif (self.location.x < self.r):
            self.location.x = self.r
            self.velocity.x *= -1
        
        if (self.location.y > height - self.r):
            self.location.y = height - self.r
            self.velocity.y *= -1
        elif (self.location.y < self.r):
            self.location.y = self.r
            self.velocity.y *= -1


def setup():
    global mover
    p5.size(640, 360)
    mover = Mover()

def draw():
    p5.background(43, 62, 80)
    
    mover.update()
    mover.check_edges()
    mover.display()

p5.run()