from manim import *
import math
import numpy as np
import random
colors = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
g=9.8
vibgyor = ['#9400D3', '#4B0082', '#0000FF', '#00FF00', '#FFFF00', '#FF7F00', '#FF0000']
def random_colour():
    hexadecimal = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    return hexadecimal

class Video(Scene):
    def construct(self):
        obs=[]
        
        def update_position(ob,dt):
            ob.BOB1.update_object(dt)
            ob.move_to(ob.BOB1.position)
            ob.LINE.put_start_and_end_on([0,0,0], ob.BOB1.position)
            ob.BOB2.move_to(ob.BOB1.position2)
            ob.LINE2.put_start_and_end_on(ob.BOB1.position, ob.BOB1.position2)
            # dot = Dot(point = ob.BOB1.position2, color = WHITE, radius = 0.1)
            # self.add(dot)
            # self.play(Create(dot, run_time=0.0001))
        
        for i in range(1,101):
            p = DubPendulum(1,1,(i),(i+1))
            colour1 = random.choice(vibgyor)
            #colour2 = random.choice(vibgyor)
            bob1=Circle(radius = 0.05, color = colour1).set_fill(colour1, opacity=1)
            bob2=Circle(radius = 0.07, color = colour1).set_fill(colour1, opacity=1)
            bob1.BOB1 = p
            bob1.BOB2=bob2
            bob1.LINE=Line(start=[0,0,0],end=bob1.BOB1.position,stroke_width=0.7)
            bob1.LINE2=Line(start=bob1.BOB1.position,end=bob1.BOB1.position2,stroke_width=0.7)
            bob1.add_updater(update_position)
            obs.append(bob1)
        for obj in obs:   
            self.add(obj)
            self.add(obj.BOB2)
            self.add(obj.LINE)
            self.add(obj.LINE2)
        self.update_self(0)
        self.wait(15)        


class DubPendulum: 
    def __init__(self,length1, length2, A1, A2):
        self.max_amplitude = math.radians(90)
        self.a1, self.a2 =  A1, A2
        self.r1, self.r2 = length1, length2
        self.position = np.array([0.0,-self.r1,0.0])
        self.position2 = np.array([0.0,-self.r2,0.0]) 
        self.time = 0
        self.mass1 = 10
        self.mass2 = 10
        self.a1_v = 0
        self.a2_v = 0
        self.a1_acc = 0
        self.a2_acc = 0
        self.dt=0.02

    def update_object(self,dt):
        self.time += dt
        a1_v=self.a1_v
        a2_v=self.a2_v
        m1, m2 = self.mass1, self.mass2
        r1, r2 = self.r1, self.r2
        a1, a2 = self.a1*self.dt, self.a2*self.dt
        
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
        
        self.a1_v += a1_acc*self.dt
        self.a2_v += a2_acc*self.dt
        self.a1 += a1_v
        self.a2 += a2_v
        self.position = np.array([x1, y1, 0.0])
        self.position2 = np.array([x2, y2, 0.0])
        