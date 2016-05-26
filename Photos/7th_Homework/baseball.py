from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

g=9.8
dt=0.01
frac=1e-5
b2m=4.1e-4
w=2000./60

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

class free_baseball:
	def __init__(self,vx,vy,vz):
		self.vx=[vx]
		self.vy=[vy]
		self.vz=[vz]
		self.x=[0.]
		self.y=[0.]
		self.z=[0.]

	def update2(self):
		global g,dt
		current_vx=self.vx[-1]
		current_vy=self.vy[-1]
		current_vz=self.vz[-1]
		self.next_vx=current_vx
		self.next_vy=current_vy
		self.next_vz=current_vz-g*dt
		current_x=self.x[-1]
		current_y=self.y[-1]
		current_z=self.z[-1]
		self.next_x=current_x+current_vx*dt
		self.next_y=current_y+current_vy*dt
		self.next_z=current_z+current_vz*dt
		

	def fire(self):
		while (self.z[-1]>=0):
			self.update2()
			self.x.append(self.next_x)
			self.y.append(self.next_y)
			self.z.append(self.next_z)
			self.vx.append(self.next_vx)
			self.vy.append(self.next_vy)
			self.vz.append(self.next_vz)

		ax.plot(self.x, self.y, self.z,color='g',label="No AirDrag or Spin")
		
		


class real_baseball:
	def __init__(self,vx,vy,vz):
		self.vx=[vx]
		self.vy=[vy]
		self.vz=[vz]
		self.x=[0.]
		self.y=[0.]
		self.z=[0.]

	def update(self):
		global g,dt,b2m
		current_vx=self.vx[-1]
		current_vy=self.vy[-1]
		current_vz=self.vz[-1]
		vel=np.sqrt(current_vx**2+current_vy**2+current_vz**2)
		force=frac*(vel**2)
		theta_x=current_vx/vel
		theta_y=current_vy/vel
		theta_z=current_vz/vel
		self.next_vx=current_vx-force*theta_x
		self.next_vy=current_vy-force*theta_y
		self.next_vz=current_vz-g*dt-force*theta_z
		current_x=self.x[-1]
		current_y=self.y[-1]
		current_z=self.z[-1]
		self.next_x=current_x+current_vx*dt
		self.next_y=current_y+current_vy*dt
		self.next_z=current_z+current_vz*dt
		

	def fire(self):
		while (self.z[-1]>=0):
			self.update()
			self.x.append(self.next_x)
			self.y.append(self.next_y)
			self.z.append(self.next_z)
			self.vx.append(self.next_vx)
			self.vy.append(self.next_vy)
			self.vz.append(self.next_vz)
			print self.z[-1]

		ax.plot(self.x, self.y, self.z,color='r',label='With Air Drag')
		#ax.legend()

class real_baseball_2:
	def __init__(self,vx,vy,vz):
		self.vx=[vx]
		self.vy=[vy]
		self.vz=[vz]
		self.x=[0.]
		self.y=[0.]
		self.z=[0.]

	def update(self):
		global g,dt,b2m
		current_vx=self.vx[-1]
		current_vy=self.vy[-1]
		current_vz=self.vz[-1]
		vel=np.sqrt(current_vx**2+current_vy**2+current_vz**2)
		force=frac*(vel**2)
		f_x=-b2m*vel*current_vx
		f_y=-b2m*w*current_vx
		theta_x=current_vx/vel
		theta_y=current_vy/vel
		theta_z=current_vz/vel
		self.next_vx=current_vx-force*theta_x+f_x*dt
		self.next_vy=current_vy-force*theta_y+f_y*dt
		self.next_vz=current_vz-g*dt-force*theta_z
		current_x=self.x[-1]
		current_y=self.y[-1]
		current_z=self.z[-1]
		self.next_x=current_x+current_vx*dt
		self.next_y=current_y+current_vy*dt
		self.next_z=current_z+current_vz*dt
		

	def fire(self):
		while (self.z[-1]>=0):
			self.update()
			self.x.append(self.next_x)
			self.y.append(self.next_y)
			self.z.append(self.next_z)
			self.vx.append(self.next_vx)
			self.vy.append(self.next_vy)
			self.vz.append(self.next_vz)
			print self.z[-1]

		ax.plot(self.x, self.y, self.z,color='b',label='With Air Drag And Spin')
		#ax.legend()

a=free_baseball(20,20,30)
a.fire()
b=real_baseball(20,20,30)
b.fire()
c=real_baseball_2(20,20,30)
c.fire()
ax.legend()
plt.show()
