import pylab as plt
import numpy as np 
import random as ra

J=1
K=1
start_temp=5
end_temp=300
step=-start_temp+end_temp+1
class Ising:
	def __init__(self,N):
		self.N=N
		self.s=[[1 for i in range(self.N)] for j in range(self.N)]
		self.t=np.linspace(start_temp,end_temp,step)
		self.final_E=[]
	
	def Cal_Energy(self):
		self.E=0
		for i in range(self.N-1):
			for j in range(self.N-1):
				self.E+=-J*(self.s[i][j]*self.s[i][j-1]+self.s[i][j]*self.s[i][j+1]+self.s[i][j]*self.s[i-1][j]+self.s[i][j]*self.s[i+1][j])

		for i in range(self.N-1):
			self.E+=-J*(self.s[self.N-1][i]*self.s[self.N-1][i-1]+self.s[self.N-1][i]*self.s[self.N-1][i+1]+self.s[self.N-1][i]*self.s[self.N-2][i]+self.s[self.N-1][i]*self.s[0][i])
			self.E+=-J*(self.s[i][self.N-1]*self.s[i+1][self.N-1]+self.s[i][self.N-1]*self.s[i-1][self.N-1]+self.s[i][self.N-1]*self.s[i][self.N-2]+self.s[i][self.N-1]*self.s[i][0])

		self.E+=-J*(self.s[self.N-1][self.N-1]*self.s[self.N-1][self.N-2]+self.s[self.N-1][self.N-1]*self.s[self.N-1][0]+self.s[self.N-1][self.N-1]*self.s[self.N-2][self.N-1]+self.s[self.N-1][self.N-1]*self.s[0][self.N-1])

		return self.E

	def update(self):
		self.E1=self.Cal_Energy()
		chosen_x=ra.randint(0,self.N-1)
		chosen_y=ra.randint(0,self.N-1)
		self.s[chosen_x][chosen_y]=-self.s[chosen_x][chosen_y]
		self.E2=self.Cal_Energy()
		delta_E=self.E2-self.E1
		if delta_E>0:
			p=np.exp(-delta_E/(K*self.T))
			r=ra.uniform(0,1)
			if r>=p:
				self.E3=self.E1
				self.s[chosen_x][chosen_y]=-self.s[chosen_x][chosen_y]
			else:
				self.E3=self.E2
		else:
			self.E3=self.E

	def loop(self):
		self.ave_E=0.
		i=1
		while i<=10000:
			self.update()
			self.ave_E+=self.E3
			i+=1
			#print i

		self.ave_E=self.ave_E/10000
		self.final_E.append(self.ave_E)

	def loop_for_temp(self):
		i=0
		for i in range(step):
			self.T=self.t[i]
			self.loop()
			i+=1

		plt.plot(self.t,self.final_E)

A=Ising(10)
A.loop_for_temp()
plt.xlabel("Tempature")
plt.ylabel("The Energy Of The System")
plt.title("Ising Model Energy Versus Tempature")
plt.show()
