from manim import *
import math
import numpy as np
import random
colors = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
g=9.8

class Video(MovingCameraScene):
    def construct(self):
        obs=[]
        
        def update_position(ob,dt):
            ob.PENDULUM.update_object(dt)
            ob.move_to(ob.PENDULUM.position)
            ob.LINE.put_start_and_end_on([0,2,0], ob.PENDULUM.position)
        
        p = PendulumTop(2)
        P1=Circle(radius = 0.05, color = colors[i%6]).set_fill(colors[i%6], opacity=0.7)
        P1.PENDULUM = p
        P1.LINE=Line(start=[0,0,0],end=P1.PENDULUM.position,stroke_width=0.7)
        P1.add_updater(update_position)
        self.add(P1)
        self.add(P1.LINE)
        self.update_self(0)
        self.wait(5)        


class PendulumTop: 
    def __init__(self,length, length2):
        self.max_amplitude = math.radians(90)
        self.max_amplitude2 = math.radians(45)
        self.length1 = length
        self.length2 = length2
        self.mass1 = 1
        self.mass2 = 1
        self.height = 2
        self.position_top = np.array([0.0,0.0,0.0]) 
        self.position_bottom = np.array([self.length2,0.0,0.0])
        self.time = 0
        dt=0.5

    def update_object(self,dt):
        self.time += dt
        m1, m2 = self.mass1, self.mass2
        th1, th2 = self.max_amplitude, self.max_amplitude2
        l1, l2 = self.length, self.length2
        #drag force self.max_amplitude*=math.e**((-0.2/self.mass)*dt)
        theta1 = -g *(2*m1+m2)math.sin(th1) - m2 * g * math.sin(th1-2*th2) - 2* math.sin(th1-th2)*m2*((dt**2)*l2 + (dt**))
        x,y = self.length* math.sin(theta), self.height - (self.length* math.cos(theta))

        self.position = np.array([x,y,0.0])
        