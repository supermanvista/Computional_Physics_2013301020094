import numpy as np
import pylab as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

g=[0,0,-9.8]
a=2e-3
dt=0.1
w=2000/60

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

class Cannon:
	def __init__(self,v):
		self.v=np.array(v,dtype=float)
		self.g=np.array(g)
		self.w=np.array([0,0,w],dtype=float)
		self.F_Magus=np.array([0,0,0],dtype=float)
		self.pos=np.array([0,0,0],dtype=float)
		self.x=[]
		self.y=[]
		self.z=[]
		self.w=np.array([0,0,w])


	def update(self):
		self.F_Magus=-np.cross(self.v,self.w)*4.1e-4
		self.f=self.g #+np.sqrt(self.v**2)#+self.F_Magus
		self.v+=self.f*dt
		self.pos+=self.v*dt


	def fire(self):
		while (self.pos[2]>=0):
			self.update()
			self.x.append(self.pos[0])
			self.y.append(self.pos[1])
			self.z.append(self.pos[2])
			if (self.pos[2]<0):
				break

		plt.plot(self.x,self.y,self.z,label="Without Air Drag")


class free_Cannon:
	def __init__(self,v):
		self.v=np.array(v,dtype=float)
		self.g=np.array(g)
		self.w=np.array([0,0,w],dtype=float)
		self.F_Magus=np.array([0,0,0],dtype=float)
		self.pos=np.array([0,0,0],dtype=float)
		self.x=[]
		self.y=[]
		self.z=[]
		self.w=np.array([0,0,w])


	def update(self):		
		self.f=self.g +self.v**2*a/np.sqrt(self.v**2)
		self.v+=self.f*dt
		self.pos+=self.v*dt
		#print self.F_Magus


	def fire(self):
		while (self.pos[2]>=0):
			self.update()
			self.x.append(self.pos[0])
			self.y.append(self.pos[1])
			self.z.append(self.pos[2])
			if (self.pos[2]<0):
				break

		plt.plot(self.x,self.y,self.z,label="Without air Drag")

class free_Cannon_2:
	def __init__(self,v):
		self.v=np.array(v,dtype=float)
		self.g=np.array(g)
		self.w=np.array([0,0,w],dtype=float)
		self.F_Magus=np.array([0,0,0],dtype=float)
		self.pos=np.array([0,0,0],dtype=float)
		self.x=[]
		self.y=[]
		self.z=[]
		self.w=np.array([0,0,w])
		

	def update(self):		
		self.f=self.g +self.v**2*a/np.sqrt(self.v**2)*(1-2.18e-4*self.pos[2])
		self.v+=self.f*dt
		self.pos+=self.v*dt
		


	def fire(self):
		while (self.pos[2]>=0):
			self.update()
			self.x.append(self.pos[0])
			self.y.append(self.pos[1])
			self.z.append(self.pos[2])
			if (self.pos[2]<0):
				break

		plt.plot(self.x,self.y,self.z,label="Air Drag With Altitude Changes")

O=Cannon([100,200,300])
O.fire()
CD=free_Cannon([100,200,300])
CD.fire()
CD=free_Cannon_2([100,200,300])
CD.fire()
plt.legend(loc="upper right")
plt.show()
