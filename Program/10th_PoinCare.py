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
		self.chosen_w=[]
		self.chosen_x=[]
		self.chosen_t=[]

	def update(self):
		global g,dt,l
		current_w=self.w[-1]
		current_x=self.x[-1]
		current_t=self.t[-1]
		self.next_w=current_w-(g/l*np.sin(current_x)+q*current_w-F*sin(D*current_t))*dt
		self.next_x=current_x+self.next_w*dt
		self.next_t=current_t+dt
		
	def fire(self):
		while (self.t[-1]<=50000):
			self.update()
			if self.next_x>np.pi:self.next_x+=-2*np.pi
			else:
				if self.next_x<-np.pi:self.next_x+=2*np.pi
				else:self.next_x=self.next_x
			self.w.append(self.next_w)
			self.x.append(self.next_x)
			self.t.append(self.next_t)
			test=((self.t[-1]*D)%np.pi)/np.pi
			test2=self.t[-1]-int(self.t[-1]/np.pi)*np.pi
			#print test
			if (test<=0.01):
				if (test2<=1):
					self.chosen_x.append(self.next_x)
					self.chosen_w.append(self.next_w)
					self.chosen_t.append(self.next_t)
				else:
					pass
			else:
				pass


		plot(self.chosen_x,self.chosen_w,',')



		#plot(self.x,self.w,',',label='Chaos')
		#plot(self.chosen_x,self.chosen_w)

a=pendulum(0,3,0)
a.fire()

#legend(loc='best')
show()
