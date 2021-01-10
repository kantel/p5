#
# Sine
#
# Smoothly scaling size with the sin() function.

import p5
import math

diameter = None
angle = 0

def setup():
    global diameter

    p5.size(640, 360)
    p5.title("Sinus".encode("utf-8"))

    diameter = height - 10

    p5.no_stroke()
    p5.fill(255, 204, 0)

def draw():
    global angle

    p5.background(100)

    d1 = 10 + (math.sin(angle) * diameter / 2) + diameter / 2;
    d2 = 10 + (math.sin(angle + math.pi / 2) * diameter / 2) + diameter / 2;
    d3 = 10 + (math.sin(angle + math.pi) * diameter / 2) + diameter / 2;

    p5.circle((0, height / 2), d1)
    p5.circle((width / 2, height / 2), d2)
    p5.circle((width, height / 2), d3)

    angle += 0.04

p5.run()