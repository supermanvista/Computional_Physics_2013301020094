import numpy as np 
import pylab as plt

g=9.8
l=9.8
dt=0.04
w0=0.
x0=0.2
t0=0.
q=0.5
D=2./3

class pendulum:
	def __init__(self,F):
		self.F=F
		self.w=[w0]
		self.x=[x0]
		self.t=[t0]
		self.delta=[0.]

	def update(self):
		current_w=self.w[-1]
		current_x=self.x[-1]
		current_t=self.t[-1]
		self.next_w=current_w+(-g/l*current_x-q*current_w+self.F*np.sin(D*current_t))*dt
		self.next_x=current_x+self.next_w*dt
		self.next_t=current_t+dt
		self.next_delta=self.next_x-current_x

	def fire(self):
		while (self.t[-1]<=60):
			self.update()
			self.w.append(self.next_w)
			self.x.append(self.next_x)
			self.t.append(self.next_t)
			self.delta.append(self.next_delta)

		plt.plot(self.t,self.delta,label="F="+str(self.F))

#A=pendulum(0)
#A.fire()
A=pendulum(0.5)
A.fire()
#A=pendulum(1.2)
#A.fire()
plt.xlim(0,60)
plt.legend(loc="best")
plt.xlabel("times")
plt.ylabel("theta")
plt.show()
