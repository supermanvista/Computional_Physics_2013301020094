from math import *
from pylab import *
g=9.8
dt=0.05
t=1000
a=2.18e-4
b2m=1e-5
def cannon(vx,vy):
	x=[0.]
	y=[0.]
	for i in range(int(t/dt)):
		c=sqrt(vx[i]**2+vy[i]**2)
		p=2.71828**(-(y[i])*0.00001)
		f=b2m*c**2*p*(1-a*y[i])**2.5
		theta_x=vx[i]/c
		theta_y=vy[i]/c
		v_x=vx[i]-f*theta_x*dt
		v_y=vy[i]-g*dt-f*theta_y*dt
		vx.append(v_x)
		vy.append(v_y)
		x_temp=x[i]+vx[i]*dt
		y_temp=y[i]+vy[i]*dt
		print vx[i],vy[i],x[i],y[i]
		if y[i]>=0:
			x.append(x_temp)
			y.append(y_temp)
		else:
			break
	plot(x,y)
for j in [30,35,40,45,50,55,60,70,75]:
	theta=j*3.1415926/180
	vx=[1000*cos(theta)]
	vy=[1000*sin(theta)]
	cannon(vx,vy)
plot()
show()
