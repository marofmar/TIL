'''
Logistic Regression without sklearn library
Soley depending on Numpy
Credits to Codebasics
'''
# Load dependent libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import random

# Generate dataset 
df = pd.DataFrame({"age": [22,25,47,52, 46,56,55,60,62,61,18,28,27,29,49,55,25,58,19,18,21,26,40,45,50,54,23], "bought_insurance":[0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0]})

# Pull out random 7 units for testing
test = df.sample(7)

# and training data is the rest
train = df[~df.isin(test)]
train.dropna(inplace = True)

# sigmoid for activation function
def sigmoid(x):
  return 1/(1+np.exp(-x)) 
  
# square loss function 
def square_loss(y_pred, target):
  return np.mean(pow((y_pred - target),2))
  
# train, test [age-X, bouth_insurance-y]

X_tr, y_tr = train.age, train['bought_insurance']
X_te, y_te = test.age, test['bought_insurance']

########## training part
# X_tr, y_tr = train.age, train['bought_insurance'].reshape(-1,1)
# X_te, y_te = test.age, test['bought_insurance'].reshape(-1,1)

#def model(n=100, X,  lr = 0.01):
lr = 0.01
W = np.random.uniform(0,1) # colom 1
b = 0.1
for i in range(10000):
  z = np.dot(X_tr, W) + b 
  y_pred = sigmoid(z)
  l = square_loss(y_pred, y_tr)
  gradient_W = np.dot((y_pred-y_tr).T, X_tr)/X_tr.shape[0] 
  gradient_b = np.mean(y_pred-y_tr) 
  W = W - lr * gradient_W 
  b = b - lr* gradient_b 
########## training part


# let's test

for i in range(len(X_te)):
  r = sigmoid(np.dot(X_te, W) + b)

# changed array into list for convenience
out = []
for i in r:
  out.append(i)

########## testing
pred =[]
for i in out:
  if i>0.5:
    pred.append(1)
  else:
  

# result
print(pred) #[1, 1, 1, 0, 0, 1, 1]
print(y_te) #[1 1 0 0 0 1 1]
    pred.append(0)
