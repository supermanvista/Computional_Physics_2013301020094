from pylab import *
import numpy as np
l=9.8
g=9.8
dt=0.04
q=0.5
F=1.2
D=2.0/3.0

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
		self.next_w=current_w-(g/l*np.sin(current_x)+q*current_w-F*sin(D*current_t))*dt
		self.next_x=current_x+self.next_w*dt
		self.next_t=current_t+dt
		
	def fire(self):
		while (self.t[-1]<=5000):
			self.update()
			if self.next_x>np.pi:self.next_x+=-2*np.pi
			else:
				if self.next_x<-np.pi:self.next_x+=2*np.pi
				else:self.next_x=self.next_x
			self.w.append(self.next_w)
			self.x.append(self.next_x)
			self.t.append(self.next_t)

		plot(self.x,self.w,',')

a=pendulum(0,3,0)
a.fire()
show()
