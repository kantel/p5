import p5

def setup():
    p5.size(400, 400)
    p5.title("Push-Style")

def draw():
    p5.background(235, 215, 182)
    p5.fill(255, 153, 0)
    p5.stroke_weight(2)
    p5.circle(100, 100, 50)
    with p5.push_style():
        p5.fill(255,  51,  51)
        p5.stroke_weight(5)
        p5.circle(200, 200, 50)
    p5.circle(300, 300, 50)
p5.run()