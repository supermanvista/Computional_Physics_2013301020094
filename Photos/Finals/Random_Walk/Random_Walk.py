import random as ra 
import pylab as plt
import numpy as np 

N=100
class rand:
	def __init__(self):
		self.x=np.linspace(0,0,N)
		self.t=[]
		self.x2=[]

	def update(self):
		t_temp=0
		x=0.
		for i in range(N):
			r=ra.uniform(0,1)
			if (r<0.5):
				self.x[i]=self.x[i-1]+1
			else:
				self.x[i]=self.x[i-1]-1
			t_temp+=1
			self.t.append(t_temp)
			x+=self.x[i]**2
			if (i!=0):
				avex=float(x)/i
			else:
				avex=x
			self.x2.append(avex)
	def draw(self):
		plt.subplot(1,2,1)
		plt.plot(self.t,self.x,'-')
		plt.title("Random walk in one dimension")
		plt.xlabel("step number")
		plt.ylabel("X")
		plt.subplot(1,2,2)
		plt.plot(self.t,self.x2,'-')
		plt.title("Random walk in one dimension")
		plt.xlabel("step number")
		plt.ylabel("<x^2>")

A=rand()
A.update()
A.draw()
B=rand()
B.update()
B.draw()
plt.show()
