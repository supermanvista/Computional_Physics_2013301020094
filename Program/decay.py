from pylab import *
nA=[500]
nB=[0]
t=[0.]
dt=0.1
endt=5
tau=1
for i in range(int(endt/dt)):
	temp_nA=nA[i]+(nB[i]-nA[i])*dt
	temp_nB=nB[i]+(nA[i]-nB[i])*dt
	nA.append(temp_nA)
	nB.append(temp_nB)
	t.append(dt*(i+1))

plot(t,nA,color='g',label="N_A")
plot(t,nB,color='b',label="N_B")
legend(loc="upper right")
show()
