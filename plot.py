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



df = pd.read_csv('Va_vs_r_100_200_17:58.csv')
df2 = pd.read_csv('Va_vs_r_f_50_200_15:12.csv')
df3 = pd.read_csv('Va_vs_r_f_500_200_15:37.csv')


plt.plot(df2.r,df2.Va,"o",label="N=50",color= "green")
#plt.plot(df2.r,df2.Va,color = "green")


plt.plot(df.r,df.Va,"o",label="N=100",color = "red")
#plt.plot(df.r,df.Va,color = "red")


plt.plot(df3.r,df3.Va,"o",label="N=500",color = "blue")
plt.plot(df3.r,df3.Va,color = "blue")


#Now let us define teh parameters a,b,c to fit the function
popt, pcov = curve_fit(func,df2.r,df2.Va,maxfev = 5000)
plt.plot(df2.r,func(df2.r,*popt),color = "green")

popt, pcov = curve_fit(func2,df.r,df.Va,maxfev = 5000)
plt.plot(df.r,func2(df.r,*popt),color = "red")




plt.xlabel('Radius of Interaction (r)')
#plt.xlabel('Noise Parameter ('+r'$\eta$'+')')
plt.ylabel('Order Parameter ('+r'$V_a$'+')')
plt.title("Order Parameter($V_a$) vs Radius of Interaction(r) for $\eta$ = 0.2")
plt.legend()
plt.show()































