import p5

a_angle = 0
a_velocity = 0
a_accleration = 0.001


def setup():
    p5.size(400, 400)
    # Funzt zur Zeit noch nicht, aber das nächste Release soll den Titel wieder anzeigen.
    # p5.title("Dein Titel hier …")

def draw():
    global a_angle, a_velocity, a_accleration
    p5.background(235, 215, 182)
    
    p5.fill(175)
    p5.stroke(0)
    p5.rect_mode("CENTER")
    p5.translate(width/2, height/2)
    p5.rotate(a_angle)
    p5.line((-100, 0), (100, 0))
    p5.fill(255, 0, 0)
    p5.ellipse((100, 0), 30, 20)
    p5.ellipse((-100, 0), 30, 20)
    
    a_velocity += a_accleration
    a_angle += a_velocity
    if a_velocity >= 0.4:
        a_velocity = 0

p5.run()