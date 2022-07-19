from manim import *
import numpy as np
import math
import random as rnd
colours = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
G = 0.1
Cd = 0.6
class GravObject:
	def __init__(self, mass, x, y, vel, anchor = False):
		self.mass =  mass
		self.x, self.y =  x, y 
		self.anchor = anchor
		self.pos = np.array([self.x, self.y, 0],dtype='float64')
		self.vel = np.array(vel,dtype='float64')
		self.radius = (self.mass/math.pi)**(1/3) 

	def update(self, other, dt):
		
		if self.anchor: return
		
		if self == other: self.dv = np.array([0,0,0],dtype='float64')
		
		else:
			self.dist = math.sqrt((self.pos[0] - other.pos[0])**2 + (self.pos[1] - other.pos[1])**2)
			self.dv = np.array([0,0,0],dtype='float64')
			if not self.dist:
				self.dv = 0
			else:
				self.F = ((-G *self.mass* other.mass )/self.dist**2) * (self.pos - other.pos)/self.dist
				self.dv = self.F/self.mass
				if self.dist < (self.radius + other.radius + 0.5)*0.3: 
					if other.anchor: self.dv *=0.25
					else: self.dv *=-0.25
		drag_force = 0.5 * (5*(self.dv**2)*Cd * math.pi*(self.radius**2))
		
		self.vel += self.dv*dt
		self.vel -= dt*(drag_force/self.mass)
		if self.pos[1] > 4 or self.pos[1]< -4 or self.pos[0] > 7 or self.pos[0]< -7:
			self.vel *= -1
		
		self.pos += self.vel 

def create_body(mass, x, y, vel, colour, anchor = False):
	grav = GravObject(mass, x,y, vel, anchor=anchor)
	body = Circle(radius = grav.radius*0.3, color = colour).set_fill(colour, opacity=1)
	body.grav_obj = grav
	return body


class Video(MovingCameraScene):
	def construct(self):
		BODIES, N = [], 10
		X = [-6, 6]
		for i in X:
			# BODIES.append(create_body(0.1, rnd.uniform(-2,2), rnd.uniform(-2,2), [0,0,0], colours[i%6]))
			BODIES.append(create_body(0.1, i, 3, [0,0,0], rnd.choice(colours)))

		for i in X:
			# BODIES.append(create_body(0.1, rnd.uniform(-2,2), rnd.uniform(-2,2), [0,0,0], colours[i%6]))
			BODIES.append(create_body(0.1, i, -3, [0,0,0], rnd.choice(colours)))

		BODIES.append(create_body(0.8, 0, 0, [0,0,0], YELLOW, anchor=True))

		def update_position(obj, dt):
			for obj2 in BODIES:
				obj.grav_obj.update(obj2.grav_obj, dt)
			obj.move_to(obj.grav_obj.pos)

		for obj in BODIES:
			obj.add_updater(update_position)
			self.add(obj)

		self.update_self(0)
		self.wait(15)