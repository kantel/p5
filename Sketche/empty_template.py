from p5 import *
import os

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

def setup():
    size(400, 200)
    # Funzt zur Zeit noch nicht, aber das nächste Release soll den Titel wieder anzeigen.
    # title("Dein Titel hier …")

def draw():
    pass

def key_pressed():
    if key == "ESC":
        exit()

run()