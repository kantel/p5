import p5

def setup():
    p5.size(400, 200)
    p5.title("Dein Titel hier …")

def draw():
    # p5.background(255, 100, 150)
    center = (width / 2, height / 2)
    p5.fill(0)
    p5.rect_mode("RADIUS")
    p5.square(center, 50)
    # print("After square()")

p5.run()