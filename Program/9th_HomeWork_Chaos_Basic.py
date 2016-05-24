from pylab import *
from math import *
x=[3.]
t=[0.]
w=[0.]
dt=0.04
endt=2000
g=9.8
l=9.8
q=0.5
F=1.2
D=2.0/3.0
for i in range(int(endt/dt)):
	w_temp=w[i]-( (g/l)*sin(x[i])+q*w[i]-F*sin(D*t[i]) )*dt
	x_temp=x[i]+w_temp*dt
	t_temp=t[i]+dt
	if x_temp>pi:x_temp=x_temp-2*pi
	else:
		if x_temp<-pi:x_temp=x_temp+2*pi
		else:x_temp=x_temp
	w.append(w_temp)
	x.append(x_temp)
	t.append(t_temp)
 

plot(w,x,',')
show()
