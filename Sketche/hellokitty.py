import p5
import os

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

stepsize = 45

def setup():
    global kitty, xpos, ypos
    p5.size(400, 400)
    # Funzt zur Zeit noch nicht, aber das nächste Release soll den Titel wieder anzeigen.
    # p5.title("Dein Titel hier …")
    xpos = width/2 - stepsize
    ypos = height/2 - stepsize
    kitty = p5.load_image("images/kitty.png")

def draw():
    p5.background(235, 215, 182)
    p5.image(kitty, (xpos, ypos))

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

p5.run(frame_rate = 30)