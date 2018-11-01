from p5 import *
import random as r

class Ball(object):

    def __init__(self):
        self.r = r.randint(8, 12)
        self.vel = Vector(1, 1)*r.uniform(2.0, 6.0)
        self.dir = Vector(-1.5, 1.5)
        self.pos = Vector(r.randint(0, width), r.randint(0, height))
        self.red = (r.randint(100, 255))
        self.green = (r.randint(0, 150))
        self.blue = (r.randint(0, 255))

    def update(self):
        self.pos.x += self.vel.x*self.dir.x
        self.pos.y += self.vel.y*self.dir.y

    def display(self):
        fill(self.red, self.green, self.blue)
        no_stroke()
        circle((self.pos.x, self.pos.y), self.r*2)

    def checkEdges(self):
        # rechter Rand
        if (self.pos.x > width - self.r and self.dir.x > 0):
            self.dir.x *= -1
        # linker Rand
        if (self.pos.x < self.r and self.dir.x < 0):
            self.dir.x *= -1
        # top
        if (self.pos.y < self.r and self.dir.y < 0):
            self.dir.y *= -1
        # bottom
        if (self.pos.y > height - self.r and self.dir.y > 0):
            self.dir.y *= -1

balls = []

def setup():
    size(640, 480)
    # title("Bouncing Ball")
    for _ in range(25):
        balls.append(Ball())
def draw():
    background(0, 0, 0)
    for ball in balls:
        ball.display()
        ball.checkEdges()
        ball.update()

run()

