import pylab as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

M1=1.989e30
M2=5.98e24
M3=318*M2
dt=3600*24/10
G=6.67e-11

class Three_Body:
	def __init__(self):
		self.pos=[np.array([0.,0.]),np.array([1.5e11,0.]),np.array([778.6e9,0])]
		self.v=[np.array([0.,0.]),np.array([0.,3e4]),np.array([0.,13.1e3])]
		self.M=[M1,M2,M3]
		self.x1=[]
		self.x2=[]
		self.y1=[]
		self.y2=[]
		self.x3=[]
		self.y3=[]
		self.t=0

	def update(self):
		for i in range(3):
			self.F=np.array([0.,0.])
			for j in range(3):
				if (i!=j):
					current_pos=self.pos[i]-self.pos[j]
					#print current_pos
					r=np.sqrt(np.inner(current_pos,current_pos))
					self.F+=-G*current_pos*self.M[i]*self.M[j]/r**3

			self.v[i]+=self.F/self.M[i]*dt
			#print self.F[0]
			self.pos[i]+=self.v[i]*dt
			#print self.v[i]

		self.x1.append(self.pos[0][0])
		self.y1.append(self.pos[0][1])
		self.x2.append(self.pos[1][0])
		self.y2.append(self.pos[1][1])
		self.x3.append(self.pos[2][0])
		self.y3.append(self.pos[2][1])
		self.t+=dt

	def fire(self):
		while (self.t<=120*365*3600*24):
			self.update()

		plt.plot(self.x1,self.y1,color="g",label="Sun")
		#plt.plot(self.x2,self.y2,color='b',label="Earth")
		#plt.plot(self.x3,self.y3,color='k',label="Juipter")
		#print self.x3, self.y3

AA=Three_Body()
AA.fire()
plt.xlim(-2e8,1.9e9)
plt.ylim(-3e9,5e10)
plt.title("Trace Of Sun")
plt.legend(loc="best")
plt.show()
