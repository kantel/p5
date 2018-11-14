from p5 import *
import os

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

stepsize = 45

def setup():
    global kitty, xpos, ypos
    size(400, 400)
    # Funzt zur Zeit noch nicht, aber das nächste Release soll den Titel wieder anzeigen.
    # title("Dein Titel hier …")
    xpos = width/2 - stepsize
    ypos = height/2 - stepsize
    kitty = load_image("images/kitty.png")

def draw():
    background(235, 215, 182)
    image(kitty, (xpos, ypos))

def key_pressed():
    global xpos, ypos
    if key == "UP":
        ypos -= stepsize
    elif key == "DOWN":
        ypos += stepsize
    elif key == "RIGHT":
        xpos += stepsize
    elif key == "LEFT":
        xpos -= stepsize
    elif key == "ESC":
        exit()

run()