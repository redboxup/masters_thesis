#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
#we will simply read the csv file and print the output in matlab
from scipy.optimize import curve_fit
import numpy as np


#defining the function that will be used for the curve fitting
def func(x,a,b,d):
	return a + b*np.exp(d*x)

def func2(x,a,b,c,d,f):
	return a + b*x + c*x*x+ d*x**3+ f*x**5



df = pd.read_csv('Va_vs_l_f_500_200_23:36.csv')
#df2 = pd.read_csv('Va_vs_eta_f_100_200_17:00.csv')
#df3 = pd.read_csv('Va_vs_eta_f_50_200_17:03.csv')

l = df['l'].to_numpy()
vol = l*l
rho = 500/vol


fig, ax = plt.subplots()

ax.plot(rho,df.Va,"o",color= "green")
#ax.invert_xaxis()
#plt.plot(df.eta,df.Va,color = "green")


#plt.plot(df2.eta,df2.Va,"o",label="N=100",color = "red")
#plt.plot(df.r,df.Va,color = "red")


#plt.plot(df3.eta,df3.Va,"o",label="N=50",color = "blue")
#plt.plot(df3.r,df3.Va,color = "blue")


#Now let us define teh parameters a,b,c to fit the function
popt, pcov = curve_fit(func2,rho,df.Va,maxfev = 5000)
plt.plot(rho,func2(rho,*popt),color = "green")

#popt, pcov = curve_fit(func2,df2.eta,df2.Va,maxfev = 5000)
#plt.plot(df2.eta,func2(df2.eta,*popt),color = "red")

#popt, pcov = curve_fit(func2,df3.eta,df3.Va,maxfev = 5000)
#plt.plot(df3.eta,func2(df3.eta,*popt),color = "blue")


d = 'Density of particles '+r'$\rho$'
plt.xlabel(d)
#plt.xlabel('Noise Parameter ('+r'$\eta$'+')')
plt.ylabel('Order Parameter ('+r'$V_a$'+')')
plt.title("Order Parameter($V_a$) vs Density("+r"$\rho$) for r = 0.1 and $\eta$ = 0.2")
#plt.legend()
plt.show()































