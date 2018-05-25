# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:01:27 2015

@author: jose
"""

import pygame
import RK
import numpy as np
import gtk

window = gtk.Window()
screen = window.get_screen()


background_colour = (0,0,0)
(width, height) = (screen.get_width(), screen.get_height())

def f(x, y, vx, vy, t):
    r = np.sqrt(x*x+y*y)
    return -x/(r*r*r)

def g(x, y, vx, vy, t):
    r = np.sqrt(x*x+y*y)
    return (-y/(r*r*r))
    
class Particle:
    def __init__(self, (x, y), size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.thickness = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)


def drawSun():
    sun = Particle((width/2, height/2), 30, ( 253, 184, 19))
    sun.display()
        
particleArray = []
def generateStarts():
      for i in range(width*height/2000):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        particleArray.append(Particle((x, y), 2, (202, 216, 255)))

def drawStart():
    for i in range(len(particleArray)):
        particleArray[i].display()
            
#h = 0.00005
h = 0.01
x0 = 1.0
vy0 = 1.2
solver = RK.RKSolver(f, g)
generateStarts()
orbitArray = []
def drawPlanet(st):    
    solver.solve(st.t+0.05, st, h)
    #orbitArray.append(Particle(((int)(100*st.x+width/2), (int)(100*st.y+height/2)), 1, (255, 0, 0)))
    planet = Particle(((int)(100*st.x+width/2), (int)(100*st.y+height/2)), 5, (153, 217, 250))
    planet.display()

def drawOrbit():
    for i in range(len(orbitArray)):
        orbitArray[i].display()
        
st = RK.State(0.0, x0, 0.0, 0.0, vy0)
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('Orbita de los planetas')
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    screen.fill(background_colour)
    drawStart()
    drawSun()
    drawPlanet(st)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == 5:
            running = False
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()