import p5
import random as r

class Ball(object):

    def __init__(self):
        self.r = r.randint(8, 12)
        self.vel = p5.Vector(1, 1)*r.uniform(2.0, 6.0)
        self.dir = p5.Vector(-1.5, 1.5)
        self.pos = p5.Vector(r.randint(0, width), r.randint(0, height))
        self.red = (r.randint(100, 255))
        self.green = (r.randint(0, 150))
        self.blue = (r.randint(0, 255))

    def update(self):
        self.pos.x += self.vel.x*self.dir.x
        self.pos.y += self.vel.y*self.dir.y

    def display(self):
        p5.fill(self.red, self.green, self.blue)
        p5.no_stroke()
        p5.circle((self.pos.x, self.pos.y), self.r*2)

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
num_balls = 30

def setup():
    p5.size(400, 400)
    p5.title("Bouncing Ball")
    for _ in range(num_balls):
        balls.append(Ball())
def draw():
    p5.background(43, 62, 80)
    for ball in balls:
        ball.display()
        ball.checkEdges()
        ball.update()

p5.run()