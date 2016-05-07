from pylab import *
x=[0.]
v=[50]
t=[0.]
dt=0.1
a=10
b=1
for i in range(1000):
	t_temp=i*dt
	t.append(t_temp)
	v_temp=v[i]+(a-b*v[i])*dt
	v.append(v_temp)
	print t[i],v[i]
plot(t,v)
show()
