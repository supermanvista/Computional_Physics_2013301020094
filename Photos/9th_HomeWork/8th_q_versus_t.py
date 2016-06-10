import numpy as np 
import pylab as plt

g=9.8
l=1.0
dt=0.01
w0=0.
x0=3.
t0=0.

class pendulum:
	def __init__(self,q):
		self.q=q
		self.w=[w0]
		self.x=[x0]
		self.t=[t0]

	def update(self):
		current_w=self.w[-1]
		current_x=self.x[-1]
		current_t=self.t[-1]
		self.next_w=current_w+(-g/l*current_x-self.q*current_w)*dt
		self.next_x=current_x+self.next_w*dt
		self.next_t=current_t+dt

	def fire(self):
		while (self.t[-1]<=20):
			self.update()
			self.w.append(self.next_w)
			self.x.append(self.next_x)
			self.t.append(self.next_t)

		plt.plot(self.t,self.x,label="q="+str(self.q))

A=pendulum(1.0)
A.fire()
A=pendulum(5)
A.fire()
A=pendulum(10)
A.fire()
plt.xlim(0,20)
plt.legend(loc="best")
plt.xlabel("times")
plt.ylabel("theta")
plt.show()
