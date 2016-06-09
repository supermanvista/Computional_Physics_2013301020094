import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

c=1
l=1
dt=1e-2
dx=1e-2
x0=0.3
x1=l-x0
r=c*dt/dx
k=1000
t=30
N=int(t/dt)
n=int(l/dx)+1

class wave(object):
	"""docstring for wave"""
	def __init__(self):
		self.x=np.linspace(0,1,n)
		self.y0=np.exp(-k*(self.x-x0)**2)+np.exp(-k*(self.x-x1)**2)
		self.y=[self.y0]
		self.temp_y=np.linspace(0,0,n)
		for j in range(n-2):
			self.temp_y[j+1]=2*(1-r**2)*self.y0[j+1]-self.y0[j+1]+r**2*(self.y0[j+2]+self.y0[j])
		
		self.y.append(self.temp_y)
		#print self.y0

	def update(self):
		self.new_y=np.linspace(0,0,n)
		for j in range(n-2):
			self.new_y[j+1]=2*(1-r**2)*self.y[-1][j+1]-self.y[-2][j+1]+r**2*(self.y[-1][j+2]+self.y[-1][j])

	def fire(self):
		while (len(self.y)<=(N+1)):
			self.update()
			self.y.append(self.new_y)
			

Har=wave()
Har.fire()
print Har.y[1]
fig = plt.figure(figsize=(6,6))
ax = plt.axes(xlim=(0, l), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=2)

def init():  
    line.set_data([], [])  
    return line,

def animate(i):
    x = Har.x
    y = Har.y[i]
    line.set_data(list(x), list(y))	  
    return line,

anim=animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=25)
plt.show()
