import math
import numpy as np 

class Cannon:
	def __init__(self, vel, force = None, pos = None, spin = None):
		self.vel = np.array(vel, dtype = np.float)
		if force != None:	self.force = force
		else:	self.force = lambda v, p, t: np.zeros(3) 
		if pos != None:		self.pos = np.array(pos, dtype = np.float)
		else:	self.pos = np.zeros(3)
		self.time = 0
		if spin == None:	self.spin = np.zeros(3)
		else:	self.spin = np.array(spin, dtype = np.float)
	def update(self, dt):
		self.pos += self.vel * dt
		self.vel += self.force(self.vel, self.pos, self.time, self.spin) * dt
		self.time += dt
	def get_pos(self):	return self.pos
	def get_vel(self):	return self.vel
	def get_time(self):	return self.time

def F_drag(vel, pos):
	_a = 6.5e-3	
	_alpha = 2.5
	_T_0 = 300.0		
	height = pos[2]
	speed = np.inner(vel, vel) ** 0.5
	_B2_m = 0.0039 + 0.0058 / (1 + math.exp((speed - 35)/5.0) )
	if (1 - _a * height / _T_0) <= 0:	return np.zeros(3)
	return -(1 - _a * height / _T_0)**_alpha * _B2_m * speed * vel
def gravity():	return np.array([0, 0, -9.8])
def F_Magnus(vel, spin):  
	_S0_m = 4.1e-4
	return - _S0_m * np.cross(vel, spin)
def force(vel, pos, time, spin):	return F_drag(vel, pos) + gravity() + F_Magnus(vel, spin)

def fire_trace(saki): 
	t, n, point = 100, 50000, 10000
	dt = 1.0 * t / n
	print dt
	trace = [[], [], []] 
	for p in range(point):
		for i in range(3):
			trace[i].append(saki.get_pos()[i])
		for pp in range( n/point ):
			saki.update(dt) 
			if saki.get_pos()[2] <= 0:  
				for i in range(3):
					trace[i].append(saki.get_pos()[i])
				return trace
	return trace




import matplotlib.pyplot as plt 
for v in [[15,0,12], [12,0,15], [15,0,13]]:
	paodan = Cannon(v, force)
	trace = fire_trace(paodan)
	plt.plot(trace[0], trace[2], label = "v = "+ str(v))
	plt.legend(loc = 'upper right')

plt.show()
