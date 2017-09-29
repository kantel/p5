from p5 import *

def setup():
    size(400, 200)
    title("Dein Titel hier …")

def draw():
    background(255, 100, 150)
    center = (width / 2, height / 2)
    fill(0)
    rect_mode("RADIUS")
    square(center, 50)

run()