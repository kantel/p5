import p5


left   = -2.25
right  = 0.75
bottom = -1.5
top    = 1.5
maxlimit = 2.0
maxiter = 20


def setup():
    p5.size(100, 100)
    # Funzt zur Zeit noch nicht, aber das nächste Release soll den Titel wieder anzeigen.
    # p5.title("Dein Titel hier …")
    # p5.color_mode("HSB", 255, 100, 100)
    

def draw():
    p5.background(235, 215, 182)
    print("vor mandelbrot")
    p5.no_stroke()
    mandelbrot()
    print("nach mandelbrot")
    p5.no_loop()

def mandelbrot():
    # p5.background(0, 0, 0)
    for x in range(width):
        cr = left + x*(right - left)/width
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            c = complex(cr, ci)
            z = 0.0
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    p5.fill(0, 0, 255)
                    p5.line((x, y), (x, y))
                else:
                    p5.fill(255, 0, 0)
                    # p5.fill((i*48)%255, 100, 100)
                    p5.line((x, y), (x, y))

p5.run()