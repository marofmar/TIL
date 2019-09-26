'''
Udacity Computer Vision Nanodegree
Learning Kalman filter now

Topid: Gaussians
Commit msg: CVND_Day1_GaussianCalculations
'''
from math import *
import matplotlib.pyplot as plt 
import numpy as np 

# gaussian function 
def f(mu, sigma2, x):
  return 1/sqrt(2*pi*sigma2) * exp(-0.5*(x-mu)**2/sigma2)
# this function can also be written with two diff parts: coeff * exponential

gauss_1 = f(10,4,8) # 0.12098536225957168

# display a gaussian over a range of x values 
mu = 10 #define parmas
sigma2 = 4 #also a variance 

x_axis = np.arange(0,20,0.1) 

# create a corresponding list of gaussian values 
g = [] 
for x in x_axis:
  g.append(f(mu, sigma2, x))
plt.plot(x_axis, g)
