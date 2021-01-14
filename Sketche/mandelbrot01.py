from p5 import *


left   = -2.25
right  = 0.75
bottom = -1.5
top    = 1.5
maxlimit = 2.0
maxiter = 20


def setup():
    size(400, 400)
    # Funzt zur Zeit noch nicht, aber es gibt einen Workaround.
    title("Mandelbrötchen".encode("utf-8"))
    

def draw():
    background(235, 215, 182)
    color_mode("HSB", 255)
    print("Start Mandelbrötchen")
    mandelbrot()
    print("I did it Babe!")
    no_stroke()
    no_loop()

def mandelbrot():
    for x in range(width):
        cr = left + x*(right - left)/width
        for y in range(height):
            ci = bottom + y*(top - bottom)/height
            c = complex(cr, ci)
            z = complex(0.0, 0.0)
            i = 0
            for i in range(maxiter):
                if abs(z) > maxlimit:
                    break
                z = (z**2) + c
                if i == (maxiter - 1):
                    fill(Color(0, 0, 0))
                    point(x, y)
                else:
                    fill(Color((i*48)%255, 255, 255))
                    point(x, y)

run()