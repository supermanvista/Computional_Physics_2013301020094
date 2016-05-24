from pylab import *
x=[3.]
y=[3.]
t=[0.]
t2=[0.]
w=[0.]
w2=[0.]
dt=0.05
endt=10
g=9.8
l=1
for i in range(int(endt/dt)):
	w_temp=w[i]-g/l*x[i]*dt
	w2_temp=w2[i]-g/l*y[i]*dt
	x_temp=x[i]+w_temp*dt
	y_temp=y[i]+w2[i]*dt
	t_temp=t[i]+dt
	t2_temp=t2[i]+dt
	w.append(w_temp)
	x.append(x_temp)
	t.append(t_temp)
	w2.append(w2_temp)
	y.append(y_temp)
	t2.append(t2_temp)

plot(t,x,label='Euler-Cromer')
plot(t,y,label='Euler')
legend(loc="best")
show()
