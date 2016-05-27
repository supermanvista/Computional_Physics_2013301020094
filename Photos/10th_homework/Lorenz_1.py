from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np



#mpl.rcParams['legend.fontsize'] = 10
#fig = plt.figure()
#ax = fig.gca(projection='3d')

sigma=10
b=8.0/3.0
dt=0.0001

class Lorenz:
	def __init__(self,x,y,z,r):
		self.x=[x]
		self.y=[y]
		self.z=[z]
		self.r=r
		self.t=[0.]

	def update(self):
		current_x=self.x[-1]
		current_y=self.y[-1]
		current_z=self.z[-1]
		#print current_x,current_y,current_z
		a_x=sigma*(current_y-current_x)
		a_y=-current_x*current_z+self.r*current_x-current_y
		a_z=current_x*current_y-b*current_z
		self.next_x=current_x+a_x*dt
		self.next_y=current_y+a_y*dt
		self.next_z=current_z+a_z*dt
		self.next_t=self.t[-1]+dt

	def fire(self):
		while (self.t[-1]<=50):
			self.update()
			self.x.append(self.next_x)
			self.y.append(self.next_y)
			self.z.append(self.next_z)
			self.t.append(self.next_t)
			#print self.z[-1]

		#plt.plot(self.t,self.z,label='r='+str(self.r))
		plt.plot(self.x,self.z)

A=Lorenz(1,0,0,25)
A.fire()
#A=Lorenz(1,0,0,10)
#A.fire()
#A=Lorenz(1,0,0,5)
#A.fire()
#plt.legend(loc='upper right')
plt.show()
