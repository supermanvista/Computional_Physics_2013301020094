import pylab as plt
import numpy as np 

v1=4*np.pi
v2=-2*np.pi
G=36*np.pi**2
dt=0.0001

class Two_Star:
	def __init__(self,m1,m2):
		self.m1=m1
		self.m2=m2
		self.x1=[2.]
		self.y1=[0]
		self.x2=[-1.]
		self.y2=[0]
		self.vx1=[0.]
		self.vy1=[v1]
		self.vx2=[0.]
		self.vy2=[v2]
		self.t=[0.]

	def update(self):
		current_x1=self.x1[-1]
		current_y1=self.y1[-1]
		current_x2=self.x2[-1]
		current_y2=self.y2[-1]
		current_vx1=self.vx1[-1]
		current_vy1=self.vy1[-1]
		current_vx2=self.vx2[-1]
		current_vy2=self.vy2[-1]
		r=np.sqrt((current_x1-current_x2)**2+(current_y1-current_y2)**2)
		self.next_vx1=current_vx1-G*(current_x1-current_x2)*dt*self.m2/r**3
		self.next_vy1=current_vy1-G*(current_y1-current_y2)*dt*self.m2/r**3
		self.next_vx2=current_vx2-G*(current_x2-current_x1)*dt*self.m1/r**3
		self.next_vy2=current_vy2-G*(current_y2-current_y1)*dt*self.m1/r**3
		self.next_x1=current_x1+self.next_vx1*dt
		self.next_y1=current_y1+self.next_vy1*dt
		self.next_x2=current_x2+self.next_vx2*dt
		self.next_y2=current_y2+self.next_vy2*dt
		self.next_t=self.t[-1]+dt
		

	def fire(self):
		while (self.t[-1]<=15):
			self.update()
			self.vx1.append(self.next_vx1)
			self.vy1.append(self.next_vy1)
			self.vx2.append(self.next_vx2)
			self.vy2.append(self.next_vy2)
			self.x1.append(self.next_x1)
			self.y1.append(self.next_y1)
			self.x2.append(self.next_x2)
			self.y2.append(self.next_y2)
			self.t.append(self.next_t)
			print self.next_vx1, self.next_vy2

		#plt.plot(self.x1,self.y1,color='r')
		#plt.plot(self.x2,self.y2,color='g')


A=Two_Star(1,2)


import visual as vp
A.update()
star1 = vp.sphere(pos = (A.next_x1, A.next_y1), radius = 0.5, color = vp.color.cyan)
star2 = vp.sphere(pos = (A.next_x2, A.next_y2), radius = 0.5, color = vp.color.cyan)
star1.trail = vp.curve(color=star1.color) 
star2.trail = vp.curve(color=star2.color) 
# fire

while (A.t[-1]<=20):
	vp.rate(7500)
	A.update()
	A.vx1.append(A.next_vx1)
	A.vy1.append(A.next_vy1)
	A.vx2.append(A.next_vx2)
	A.vy2.append(A.next_vy2)
	A.x1.append(A.next_x1)
	A.y1.append(A.next_y1)
	A.x2.append(A.next_x2)
	A.y2.append(A.next_y2)
	A.t.append(A.next_t)

	star1.pos = (A.next_x1, A.next_y1)
	star2.pos = (A.next_x2, A.next_y2)
	star1.trail.append(pos = star1.pos)
	star2.trail.append(pos = star2.pos)
