#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt
#we will simply read the csv file and print the output in matlab
from scipy.optimize import curve_fit
import numpy as np


#defining the function that will be used for the curve fitting
def func(x,a,b,c,d,e,f):
	return a + b*x + c*x*x+ d*x**3+ e*x**4+ f*x**5

def func2(x,a,b,c,d,e,f,g):
	return a + b*x + c*x*x+ d*x**3+ e*x**4+ f*x**5+g*x**7



df = pd.read_csv('Va_vs_eta_f_500_200_16:49.csv')
df2 = pd.read_csv('Va_vs_eta_f_100_200_17:00.csv')
df3 = pd.read_csv('Va_vs_eta_f_50_200_17:03.csv')


plt.plot(df.eta,df.Va,"o",label="N=500",color= "green")
#plt.plot(df.eta,df.Va,color = "green")


plt.plot(df2.eta,df2.Va,"o",label="N=100",color = "red")
#plt.plot(df.r,df.Va,color = "red")


plt.plot(df3.eta,df3.Va,"o",label="N=50",color = "blue")
#plt.plot(df3.r,df3.Va,color = "blue")


#Now let us define teh parameters a,b,c to fit the function
popt, pcov = curve_fit(func,df.eta,df.Va,maxfev = 5000)
plt.plot(df.eta,func(df.eta,*popt),color = "green")

popt, pcov = curve_fit(func2,df2.eta,df2.Va,maxfev = 5000)
plt.plot(df2.eta,func2(df2.eta,*popt),color = "red")

popt, pcov = curve_fit(func2,df3.eta,df3.Va,maxfev = 5000)
plt.plot(df3.eta,func2(df3.eta,*popt),color = "blue")



plt.xlabel('Noise Parameter ($\eta$)')
#plt.xlabel('Noise Parameter ('+r'$\eta$'+')')
plt.ylabel('Order Parameter ('+r'$V_a$'+')')
plt.title("Order Parameter($V_a$) vs Noise Parameter($\eta$) for r = 0.1")
plt.legend()
plt.show()































