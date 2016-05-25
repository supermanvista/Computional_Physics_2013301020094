from pylab import *
import numpy as np
l=9.8
g=9.8
dt=0.01

class pendulum:
	def __init__(self,w,x,t):
		self.w=[w]
		self.x=[x]
		self.t=[t]

	def update(self):
		global g,dt,l
		current_w=self.w[-1]
		current_x=self.x[-1]
		current_t=self.t[-1]
		self.next_w=current_w-g/l*current_x*dt
		self.next_x=current_x+current_w*dt
		self.next_t=current_t+dt
		
	def fire(self):
		while (self.t[-1]<=30):
			self.update()
			self.w.append(self.next_w)
			self.x.append(self.next_x)
			self.t.append(self.next_t)

		plot(self.t,self.x,label='Euler')

class pendulum_2:
	def __init__(self,w,x,t):
		self.w=[w]
		self.x=[x]
		self.t=[t]

	def update(self):
		global g,dt,l
		current_w=self.w[-1]
		current_x=self.x[-1]
		current_t=self.t[-1]
		self.next_w=current_w-g/l*current_x*dt
		self.next_x=current_x+self.next_w*dt
		self.next_t=current_t+dt
		
	def fire2(self):
		while (self.t[-1]<=30):
			self.update()
			self.w.append(self.next_w)
			self.x.append(self.next_x)
			self.t.append(self.next_t)

		plot(self.t,self.x,label='Euler_Cromer')

a=pendulum(0,3,0)
a.fire()
a=pendulum_2(0,3,0)
a.fire2()
legend(loc='best')
show()
