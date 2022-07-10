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
            ob.LINE.put_start_and_end_on([0,0,0], ob.PENDULUM.position)
            ob.bob2.move_to(ob.PENDULUM.position2)
            ob.LINE2.put_start_and_end_on(ob.PENDULUM.position, ob.PENDULUM.position2)
        
        p = PendulumTop(1,1)
        P1=Circle(radius = 0.05, color = YELLOW).set_fill(YELLOW, opacity=1)
        P2=Circle(radius = 0.07, color = RED).set_fill(RED, opacity=1)
        P1.PENDULUM = p
        P1.bob2=P2
        P1.LINE=Line(start=[0,0,0],end=P1.PENDULUM.position,stroke_width=0.7)
        P1.LINE2=Line(start=P1.PENDULUM.position,end=P1.PENDULUM.position2,stroke_width=0.7)
        P1.add_updater(update_position)
        self.add(P1)
        self.add(P1.bob2)
        self.add(P1.LINE)
        self.add(P1.LINE2)
        self.update_self(0)
        self.wait(20)        


class PendulumTop: 
    def __init__(self,length1, length2):
        self.max_amplitude = math.radians(90)
        self.a1, self.a2 =  3, 2
        self.r1, self.r2 = length1, length2
        self.position = np.array([0.0,-self.r1,0.0])
        self.position2 = np.array([0.0,-self.r2,0.0]) 
        self.time = 0
        self.mass1 = 10
        self.mass2 = 10
        self.a1_v = 0
        self.a2_v = 0
        self.a1_acc = 1
        self.a2_acc = 1
        dt=0.5

    def update_object(self,dt):
        self.time += dt
        a1_v=self.a1_v
        a2_v=self.a2_v
        m1, m2 = self.mass1, self.mass2
        r1, r2 = self.r1, self.r2
        a1, a2 = self.a1*dt, self.a2*dt
        
        #update bob1 acc
        num1 = -g * (2 * m1 + m2) * math.sin(a1)
        num2 = -m2 * g * math.sin(a1 - 2 * a2)
        num3 = -2 * math.sin(a1 - a2) * m2
        num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * math.cos(a1 - a2)
        den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
        a1_acc = (num1 + num2 + num3 * num4) / den

        #update bob2 acc
        num1 = 2 * math.sin(a1 - a2)
        num2 = a1_v * a1_v * r1 * (m1 + m2)
        num3 = g * (m1 + m2) * math.cos(a1)
        num4 = a2_v * a2_v * r2 * m2 * math.cos(a1 - a2)
        den = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
        a2_acc = (num1 * (num2 + num3 + num4)) / den
        

        x1 = r1 * math.sin(a1)
        y1 = -r1 * math.cos(a1)
        x2 = x1 + r2 * math.sin(a2)
        y2 = y1 - r2 * math.cos(a2)
        
        self.a1_v += a1_acc*dt
        self.a2_v += a2_acc*dt
        self.a1 += a1_v
        self.a2 += a2_v
        self.position = np.array([x1, y1, 0.0])
        self.position2 = np.array([x2, y2, 0.0])
        