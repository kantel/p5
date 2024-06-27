import p5
import os

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample im Editor mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

WIDTH = 450
HEIGHT = 450

class Kitty():
    
    def __init__(self, x, y):
        self.w = x
        self.h = y
        self.tilesize = 90  # Bildgröße: 90x90 Pixel
        self.x = x/2 - self.tilesize/2
        self.y = y/2 - self.tilesize/2
        self.step = self.tilesize/4
    
    def loadPic(self):
        self.img = p5.load_image("images/kitty.png")

    def display(self):
        # Ränder checken:
        if self.x <= 0:
            self.x = 0
        elif self.x >= self.w - self.tilesize:
            self.x = self.w - self.tilesize
        if self.y <= 0:
            self.y = 0
        elif self.y >= self.h - self.tilesize:
            self.y = self.h - self.tilesize
        p5.image(self.img, self.x, self.y)

kitty = Kitty(WIDTH, HEIGHT)

def setup():
    p5.size(WIDTH, HEIGHT)
    p5.title("Klasse, Kitty!")
    kitty.loadPic()

def draw():
    p5.background(235, 215, 182)
    kitty.display()

def key_pressed():
    if key == "UP":
        kitty.y -= kitty.step
    elif key == "DOWN":
        kitty.y += kitty.step
    elif key == "RIGHT":
        kitty.x += kitty.step
    elif key == "LEFT":
        kitty.x -= kitty.step

p5.run(frame_rate = 30)