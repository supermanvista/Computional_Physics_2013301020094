from pylab import *
v=0
t=0
dt=0.1
t2=10
for i in range(int(t2/dt)):
   v=v+(10-v)*dt
   t=(i+1)*dt
   plot(v, color='green', linewidth = 2.0,linestyle='-')
   print v
show()