#!/usr/bin/env python3

#This program is to evaluate the order parameter multiple times

import numpy as np
import scipy.spatial as spatial
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


#Number of particles
N=50

#mean velocities of the system
v0 = 1

#setting boundaries for the system
xlim,ylim = 1,1

#radius beyond which we cannot have more particles
r = 0.1

#let us define the time-steps
nn = 200

#time between each time step in second
dt = 0.1


#creating random coordinates for the points
xcoord = [random.random()*xlim for i in range(N)]
ycoord = [random.random()*ylim for i in range(N)]
theta = [random.random()*2*np.pi for i in range(N)]

#Now we want to find the direction array
v0_cos_theta = [v0*np.cos(theta[i]) for i in range(N)]
v0_sin_theta = [v0*np.sin(theta[i]) for i in range(N)]

#creating a dataframe
d = {'X':xcoord,'Y':ycoord,'Vx':v0_cos_theta,'Vy':v0_sin_theta,'theta':theta}
df = pd.DataFrame(d)


#we are writing a function that will return order parameter as result
def vicsek_model(df,r,nn,v0,xlim,ylim,eta,dt):
	for i in range(nn):
		df2 = df.copy(deep=True)
		df2.X = df.X + df.Vx*dt
		df2.Y = df.Y + df.Vy*dt
	    #Applying Periodic Boundary conditions
		df2.X = df2.X%xlim
		df2.Y = df2.Y%ylim

	    #Now let us update the mean value of theta using KDTree
		XY = df[['X','Y']].to_numpy()
	    #let us construct the tree
		XY_tree = spatial.cKDTree(XY)
		for k in range(N):
			a = XY_tree.query_ball_point(XY[k],r)
			theta_ = 0
			for j in range(len(a)):
				theta_ += df.theta[a[j]]
			df2.theta[k]=theta_/len(a) + eta*random.uniform(-np.pi,np.pi)
		df2.Vx = v0*np.cos(df2.theta)
		df2.Vy = v0*np.sin(df2.theta)
		df = df2.copy(deep=True)
	#the order parameter should be given by
	Vx = df.Vx.mean()
	Vy = df.Vy.mean()
	#Va is the order parameter
	Va = np.sqrt(Vx**2+Vy**2)/v0
	return Va

M=20
eta = np.linspace(0,1,M)
Va = [0]*M
for i in range(M):
	Va[i] = vicsek_model(df,r,nn,v0,xlim,ylim,eta[i],dt)
	print(Va[i])
	percent = ((i+1)/M)*100
	percentage = "program completion = "+str(percent)+"%"
	print(percentage)
	
g = {'eta':eta,'Va':Va}
df_ = pd.DataFrame(g)
now = datetime.now()
current_time = now.strftime("%H:%M")

name = "Va_vs_eta_f_"+str(N)+"_"+str(nn)+"_"+current_time+".csv"

df_.to_csv(name)

	
	
	
	
	
	



