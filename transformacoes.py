import glfw
from OpenGL.GL import *
import math

vertices = (
    (-0.2, -0.2),
    (0.2, -0.2),
    (0.0, 0.2)
)

def init():
    glClearColor(0,0,0,1)
    
def translacao(v, tx, ty):
    novo = []
    for x, y in v:
        novo.append([x+tx, y+ty])
    return novo

def rotacao(v, a):
    r = math.radians(a)
    novo = []
    for x, y in v:
        novo.append([x*math.cos(r) - y*math.sin(r), x*math.sin(r) + y*math.cos(r)])
    return novo

def escala(v, s):
    novo = []
    for x, y in v:
        novo.append([x*s, y*s])
    return novo

def render(v):
    glBegin(GL_TRIANGLES)
    for x, y in v:
        glVertex2f(x, y)
    glEnd()

def main(): 
    glfw.init()
    window = glfw.create_window(800, 600, "Matrizes de Tranformação", None, None)
    glfw.make_context_current(window)
    init()
    tr = translacao(vertices, -0.1, 0.5)    #vermelho
    ro = rotacao(vertices, 180)              #verde     
    es = escala(vertices, 2)              #azul
    glClear(GL_COLOR_BUFFER_BIT)
    while not glfw.window_should_close(window):     
        glfw.poll_events()
        glColor3f(1, 0, 0)
        render(tr)
        glColor3f(0, 0, 1)
        render(es)
        glColor3f(0, 1, 0)
        render(ro)
        glColor3f(1, 1, 1)
        render(vertices)
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main()