from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import random
A_a=range(61)
A_a.remove(15)
A_a.remove(45)
class Fields:
	def __init__(self):
		self.v=[]
		self.old_v=[]
		for i in range(61):
			self.v.append([])
			self.old_v.append([])

		for i in range(61):
			for j in range(61):
				self.v[i].append(random.uniform(-1,1))

		#print self.v

	def update(self):
		for i in range(61):
			self.v[i][0]=0
			self.v[i][60]=0

		for i in range(15,45):
			self.v[i][15]=-1
			self.v[i][45]=1

		for j in range(61):
			self.v[0][j]=0
			self.v[60][j]=0


		for i in range(61):
			for j in range(61):
				self.old_v[i].append(self.v[i][j])
		
		self.Delta_v=0.

		for i in range(1,60):
			for j in range(1,60):
				if ((j==15 and (i in range(15,45))) or (j==45 and (i in range(15,45)))):
					self.v[i][j]=self.v[i][j]
				else:
					self.v[i][j]=(self.v[i-1][j]+self.v[i+1][j]+self.v[i][j-1]+self.v[i][j+1])/4.
			
			self.Delta_v+=abs(self.old_v[i][j]-self.v[i][j])

			print self.Delta_v

		
		     

	def fire(self):
		for i in range(1000):
			self.update()
			i+=1
			print i

		return self.v

AA=Fields()
Super=AA.fire()
fig = plt.figure()
ax = fig.gca(projection='3d')
x=range(61)
y=range(61)
x, y = np.meshgrid(x, y)
surf = ax.plot_surface(x, y, Super, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.xlabel("X")
plt.ylabel("Y")

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
