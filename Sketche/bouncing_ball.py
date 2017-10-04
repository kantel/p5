from p5 import *

class Ball(object):

    def __init__(self):
        self.r = 10
        self.vel = Vector(1, 1)*4
        self.dir = Vector(1, 1)
        self.pos = Vector(width/2, height/2)

    def update(self):
        self.pos.x += self.vel.x*self.dir.x
        self.pos.y += self.vel.y*self.dir.y

    def display(self):
        fill(255, 255, 255)
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

def setup():
    global ball
    size(400, 400)
    title("Bouncing Ball")
    ball = Ball()

def draw():
    global ball
    background(0, 0, 0)
    ball.display()
    ball.checkEdges()
    ball.update()

run()

