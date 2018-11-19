import p5
import os
# import math
import random as r
# import numpy as np

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Fenstergröße, wenn diese verändert wird, muß auch das
# Hintergrundbild angepaßt werden
WIDTH = 600 
HEIGHT = 600
# Anzahl der Boids
N = 10   

class Boid():
    
    def __init__(self, _x, _y):
        self.x = _x + 10*r.randint(-20, 20)
        self.y = _y + 10*r.randint(-20, 20)
        self.speed = 3
    
    def move(self):
        self.x += self.speed
        if self.x >= WIDTH + 10:
            self.x = -10
            self.y = self.y + 10*r.randint(-20, 20)
    
    def show(self):
        p5.fill(0, 0, 0)
        p5.triangle((self.x-5, self.y-5), (self.x+10, self.y), (self.x-5, self.y+5))
        

boids = []

def setup():
    global bg
    p5.size(WIDTH, HEIGHT)
    # Funzt zur Zeit noch nicht, aber das nächste Release soll den Titel wieder anzeigen.
    # p5.title("Dein Titel hier …")
    bg = p5.load_image("images/sunset.jpg")
    for _ in range(N):
        boids.append(Boid(WIDTH/2, HEIGHT/2))

def draw():
    p5.background(bg)
    for boid in boids:
        boid.move()
        boid.show()

def key_pressed():
    pass

p5.run()