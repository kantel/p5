import p5
import os

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample im Editor mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

def setup():
    p5.size(400, 400)
    p5.title("Dein Titel hier …")

def draw():
    p5.background(43, 62, 80)

def key_pressed():
    pass

p5.run()