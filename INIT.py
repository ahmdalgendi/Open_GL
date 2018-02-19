from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

from numpy import *
import math

COLORS = {'white': (1, 1, 1),
          'green': (0., 1., 0.),
          'red': (1., 0., 0.),
          'blue': (0.0, 0.4, 0.8),
          'black': (0., 0., 0.) , 'grey' : (108.0,123,139)
          ,'back' : (139/255,90/255 , 43/255)
          }

pi = math.acos(-1)
def add_circle(x, y, r, color='green'):
    glBegin(GL_POLYGON)
    glColor(COLORS[color])
    res = 100
    for i in range(res):
        x_ = x + r * math.cos((i / res) * (math.pi * 2))
        y_ = y + r * math.sin((i / res) * (math.pi * 2))
        glVertex2d(x_, y_)
    glEnd()


def add_rectangle(x, y, w, h, color='green'):
    glColor(COLORS[color])
    glBegin(GL_POLYGON)
    glVertex2d(x, y)
    glVertex2d(x+w, y)
    glVertex2d(x+w, y+h)
    glVertex2d(x, y+h)
    glEnd()

def add_triangle(x1,y1,x2,y2,x3,y3,color):
    glColor(COLORS[color])
    glBegin(GL_POLYGON)
    glVertex2d(x1, y1)
    glVertex2d(x2, y2)
    glVertex2d(x3, y3)
    glEnd()

