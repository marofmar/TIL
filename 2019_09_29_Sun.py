'''
Udaicty Computer Vision Nanodegree
1D Kalmaan filter
Gaussians

Kalman filter: process of measurement and prediction 
Measure: multiplication, Prrediction: addition btw two Gaussianas

'''

from math import *
import matplotlib.pyplot as plt 
import numpy as np 

# gaussian function
def f(mu, sigma2, x):
  coef = 1/sqrt(2.0*pi*sigma2)
  expn = exp(-0.5*(x-mu)**2/sigma2)
  return coef * expn 
  
def update(mean1, var1, mean2, var2):
  new_mean = (mean1*var2 + mean2*var1)/(var1 + var2) 
  new_var = 1/(1/var1 + 1/var2) 
  return [new_mean, new_var] 
  
def predict(mean1, var1, mean2, var2):
  new_mean = mean1 + mean2 
  new_var = var1 + var2 
  return [new_mean, new_var]

##############################################
# measurements for mu and motions, U
me = [5., 6., 7., 9., 10.] # measurement (update) , increase certainty
me_sig = 4.

mo= [1., 1., 2., 1., 1.] # motion (predict) , decrease certainty 
mo_sig = 2.

# initial parameters


mu = 0.
sig = 0.000001
##############################################


for i in range(len(me)):
  mu, sig = update(mu, sig, me[i], me_sig)
  print('update: [{}, {}]'.format(mu, sig))
  mu, sig = predict(mu, sig, mo[i], mo_sig)
  print('predict: [{}, {}]'.format(mu, sig))
