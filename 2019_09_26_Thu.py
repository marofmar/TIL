'''
Udacity Computer Vision Nanodegree
Learning Kalman filter now

Topid: Gaussians and Updating the values after obtaining new information
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



# the update function
'''
Kalman Filter is about the iterative process btw measurement and motion. 
From Gaussians perspective, it is iterative process between measurement updates and prediction.

Let's consider a new Gaussian distribution has been introduced to the exsiting Gaussian distribution.
Then our uncertainty would be mediated, since we have got a piece of new information.
In this case, let's see what mean and variance value that the updated Gaussians would have.

'''
def update(mean1, var1, mean2, var2):
    ''' This function takes in two means and two squared variance terms,
        and returns updated gaussian parameters.'''
    ## TODO: Calculate the new parameters
    new_mean = (var1*mean2 + var2*mean1)/(var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    
    return [new_mean, new_var]

new_params = update(10, 4, 12, 4)
print(new_params) # [11.0, 2.0]



# display a gaussian over a range of x values 
mu = 10 #define parmas
sigma2 = 4 #also a variance 

x_axis = np.arange(0,20,0.1) 

# create a corresponding list of gaussian values 
g = [] 
for x in x_axis:
  g.append(f(mu, sigma2, x))
plt.plot(x_axis, g)
