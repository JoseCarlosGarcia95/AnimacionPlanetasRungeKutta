# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:30:18 2015

@author: jose
"""


from __future__ import division
import numpy as np

"""
    Esta clase se utiliza para determinar el estado de un elemeto dado en el espacio.
    @State.t: Representa el tiempo por el cual la partícula está pasando.
    @State.x: Representa la posición respecto al eje x.
    @State.y: Representa la posición respecto al eje y.
    @State.vx: Representa la velocidad respecto al eje x.
    @State.vy: Representa la velocidad respecto al eje y.
"""
class State:
    def __init__(self, t, x, y, vx, vy):
        self.t = t
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
"""
    Esta clase resuelve por el método de Runge Kutta un sistema donde f y g, definen las ecuaciones diferenciales a resolver.
"""
class RKSolver:
    def __init__(self, f, g):
        self.f = f
        self.g = g
        
    """
        Resuelve un sistema dado utilizando las funciones "f" y "g", dado unos valores iniciales, una magnitud y el tiempo final.
    """
    def solve(self, tf, e, h):        
        x = e.x
        y = e.y
        vx = e.vx
        vy = e.vy
        t0 = e.t
        
        times = np.linspace(t0, tf, (tf-t0)/h)
        
        for t in times:
            k1 = h*vx
            l1 = h*self.f(x, y, vx, vy, t)
            q1 = h*vy
            m1 = h*self.g(x, y, vx, vy, t)
            
            k2 = h*(vx+l1/2)
            l2 = h*self.f(x+k1/2, y+q1/2, vx+l1/2, vy+m1/2, t+h/2)
            q2 = h*(vy+m1/2)
            m2 = h*self.g(x+k1/2, y+q1/2, vx+l1/2, vy+m1/2, t+h/2)
            
            k3 = h*(vx+l2/2)
            l3 = h*self.f(x+k2/2, y+q2/2, vx+l2/2, vy+m2/2, t+h/2)
            q3 = h*(vy+m2/2)
            m3 = h*self.g(x+k2/2, y+q2/2, vx+l2/2, vy+m2/2, t+h/2)
            
            k4 = h*(vx+l3)
            l4 = h*self.f(x+k3, y+q3, vx+l3, vy+m3, t+h)
            q4 = h*(vy+m3)
            m4 = h*self.g(x+k3, y+q3, vx+l3, vy+m3, t+h)
            
            x = x+(k1+2*k2+2*k3+k4)/6
            vx = vx+(l1+2*l2+2*l3+l4)/6
            y = y+(q1+2*q2+2*q3+q4)/6
            vy = vy + (m1+2*m2+2*m3+m4)/6
        
        e.x = x
        e.vx = vx
        
        e.y = y
        e.vy = vy
        e.t = tf
        return True