

# ML lec 01 
# Basic terminologies

## Machine Learning
* Limitations of explicit programming
* Machine learning: "Field of study that gives computers the ability to learn without being explicitly programmed" Arthur Samuel (1959)

## Supervised/ Unsupervised Learning
* Supervised: Learvning with labeled examples - training set.
* Unsupervised learning: Un-labeled data - ex. Google news grouping, Word clustering

## Supervised learning
* Image labeling, Email spam filter, predicting exam score.
* Analyze with labeled data(training data) (and maybe test later with test data)

## Training data set
* Train with training data set and test with the Test data set.

## Alpha Go

## Types of supervised learning
* Predicting final exam score based on time spent - regression
> Predicting within certain range from 0 to 100

* Pass/ Non-pass based on time spent - binary classification
> Choosing one from the two, which is called the Classification, especially the selctions is limited in the two, then, called the binary.

* Letter grade (A, B, C) basd on time spent - multi-label calssification
> With more than two labels, then called multi-label



# ML lec 02
# Linear Regression

## Predicting exam score: regression
* Predict within a certain scope - utilize regression to predict certain value.

## (Linear) Hypothesis
* There are many data set that can be expalined with linear models.
* If we set up a linear hypothesis, then we need to decide a certain line, and to find the right line is the goal of this model.

## Which hypothesis is better?
* Figure out the distance between the hypothetical line and the each single point.

## Cost function
* How fit the line to our (training) data
* Calculating the distance between the hypothetical and the real data.
* The distance can be both positive or negative, therfore, we squre the value to figure out the value. -> and denominate with the number of the data, to get the average number.
* Cost function can also be called as 'Loss function'
* The parameter of the cost function is (w,b)
> Let us find the right parameters of the W and b to minimize the cost function.
> Goal: Minimize cost 



# ML lec 03
# Explainig the cost minimization algorithm

## How to minimize cost
* Hypothesis H(x) = Wx+b
* Cost(W,b)

## Simplified hypothesis
* Remove the b from the H(x)

## What cost(W) looks like?

## Gradient descent algorithm
* To find the minimum value of the cost
* Used to various minimization problems

## How it works?
* The starting point can be anywhere
* Keep changing the W and b a little bit to reduce cost function value.
* Repeat


## Formal definition of cost function to gest the derivative of the  cost function easily
* Derivatives

## Gradient descent algorithm

## Convex function
* In convex function, starting point does not matter to find the minimized value of the function.
* Therefore, we need to figure out that the function be categorized into the convex function. 
* If not, the gradient fucntion algorithm would lead to some local minimized points, which can be quite different from the right value that we are looking for.


# ML lec 04
# Multi-variable linear regression

## Recap
* Hypothesis
* Cost function
* Gradient descent algorithm

## Predicting exam score
* Setting a model with a single feature would be not sufficient to explaint the result adequately.
* If the feature is equal or more than 2, then we call them multi-variable.
* Multi-variable = multi-feature
* Getting more variable does not affect significantly, though.
* Enable to set up more weight to each parameter

## Matrix
* To show the model with neat and simple forms. 
* The long-long equation can be presented with simple two boxes of matrices.

## Matrix multiplication
* Dot product

## Hypothesis without b
* The bias 'b' term, which is quite annoying can also be included in the matrix multipliation form.
* In matrix representing the weight of each parameter, include b, and in the parameter matrix include 1, to present the 1 * b.


## W vs X
* The matrix of weight, presented with big capital W, and the other X.
* People want the both matrix to be shown in the same format.
* To enable the multiplication of the same formatted matrix, which is W and X, here comes the *Transpose*.


## Transpose

## Hypothesis using Transpose


# ML lec 5-1
# Logistic Classification

## Regression
* Hypothesis
* Cost function: measuring the distance is calculating the cost.
> Finding out the weight to minimize the cost.
* Gradient descent
> The step size is represented with the alpha value, which is also called as *learning weight*

## Classification
* The regression has been used to predic certain value. 
* However, this classificaiton let to choose between the two; Binary.
* Ex. Spam Detection (Spam or Ham), Facebook feed (Show or Hide), Credit Card Fradulent Transaction detection (Legitimate or Fraud)

## 0,1 encoding
* Spam(1), or Ham(0)
* Facebook, show(1), hide(0)
* Credit card, legitimate(0), fraud(1)
* Raiology or Finance filed also actively use this method.

## Pass(1)/ Fail(0) based on stury hours

## Linear regression
* The hypothesis value may generate certain value located far from the range [0:1].
* Hypothesis can give values larger than 1 or less than 0.

## Logistic Hypothesis
* There comes a need to pressure down the value range of the Hypothesis.
* Replacing the H(x) to z, and found the very inteteresting function, *Sigmoid*.

## Sigmoid
* The horizontal line is represented with the value of z
* The vertical line is represented with the g(z)
* Some large value of z can be very close to the value of 1, and the very small value of z will provide the g(z), which located very close to the value of 0.
* The former Wx can be replaced witht the *z*, and the H(x) can be represented with g(z) in this logistics format.


# ML lec 5-2
# Logistic (regression) classification: cost function & gradient descent

## Cost function
* The function has been transformed to generate only between 0 and 1
* The former cost function that we learnt in the linear part has been very smooth. However, the transformed one now be drawn with uneven line.
* Sine the sigmoid term is not anymore linear. -> uneven shape
* Therefore, in this uneven line, the starting point would matter a lot to land in the minimum points which would possibly one of the local minimum points.

## New Cost Function for logistic
* We need to change the form of function since our hypothesis has been changed.

## Understanding the cost function
* We utilize the *log* to fix the uneven feature of the hypothesis function.
* Since the exponential is the opposit to the log.
* If our prediction get close to the real one, then our cost becomes small.
* Eg. if the real value of y is 1, and our prediction equlas with that, then the cost(1) becoems 0, since the real label equals with the prediction.
* If our prediction gets wrong, then the cost reaches almost infinite value, which punishes our model system.
* Eg2. if the real value of label y is zero, and we predict orrectly, then the cost is zero. 
* If our system make mistakes predicting the value to 1, then the cost reaches to the infinite. 
* If we combine the two different part, then the combined one becomes smoooth and convex function.

## Cost function
* We define the function based on the different y value: y=0, and y=1.
* And the last form of function comes out, to optimally combine the two different parts.
* C(H((x),y) = -ylog(H(x))-(1-y)log(1-H(x)) -> Easily programm-able

## Minimize cost - Gradient descent algorithm
* Derivative comes out to get the value of the slope.




# ML lec 6-1
# Softmax classification: Multinomial classification

## Logistic regression
* The linear model H(x) = Wx, sometimes become too large or too small.
* Therefore, we replace the H(x) to some other variable z, and make another function g(z), generating the value between the range(0:1), limiting the max and minimum value
* The function that performs in that way is called the sigmoid. 
* If we frame the process,
> X goes into the box named *W*, and after that the value goes into the sigmoid function and finally the Y-bar comes out.
* The Box W distinguishes the value by drawing hyperplane, geometrically.

## Multinomial classification
* Multinomial means there exist many classes.
* Adopting only the binary classification can also be effective to work in the multinomial classification.
* B or not / A or not/ C or not
* Forming the multinomial classification into the matrix format, which generate the whole values at once,

## Where is sigmoid?
* How to make it simple and neat?



# ML lec 6-2
# Cost funciton of the Softmax classfier

## Where is sigmoid?

## Sigmoid?
* We want the each y-bar value to be located in the range(0:1), using the sigmoid.
* Softmax works to generate the value in the right format of the range (0:1)
* The alst value is between 0:1 and the sum of the whole becoems 1, just like a probability.
* One-Hot Encoding

## Cost function
* Corss-Entropy
* The softmax function value S(y) which also can be called as y-bar.
* And the hot encoded value L
* D(S,L) = - SUM(L*log(S))


## Cross-entropy cost function
* L multiplies with the negative log(y-bar)
* The y-bar is always between 0 to 1, since the value has been through the softmax.
* Summing up the each element of the matrix.
> Wow, imporessive. 
* Element-wise

## Logistic cost VS Cross entropy
* Both functions are actually identical.

## Cost function
* Summing up the all value, and figure out the average number.

## Gradient descent



# ML lec 07-1
# Application & Tips: Learning rate, data preprocessing, overfitting

## Gradient descent
* Learning rate *alpha*

## Large learning rate: overshooting
* If the alpha value is too large, which means the gradient step is too big, then the larning owuld not be processed properly. 
* This phenomenon is called *overshooting*.
* The cost not being decreased, but flips away- suspect the overshooting.

## Small learning rate: takes too long, stops at local minimum

## Try seeral learning rates
* To define the rate depends heavily on each different circumstance.
* Observe the cost function

## Data (X) preprocessing for gradient descent
* Sometimes, we need to *preprocess* the data.
> Normalize
* Zero-centered data
* Normalized data

## Standardization
* The difference between the value and the mean, denominated with the standard deviation.

## Overfitting
* Too dependent and too much fitted to the train data only, and not works with the test dataset or in real use.

## Solutions for overfitting
* More training data
* Reduce the number of features (Remove the redundancy, etc.)
* *Regularization*

## Regularization
* Let's not have too big numbers in the weight
* Adding another term to the cost function: lambda * SUM of the squred value of each element of Matrix W
* The labda is called, the regularization strength.
* We can manage the regularization strength value.

## Summary
* Learning rate
* Data preprocessing
* Overfitting - More training data / Regularization


# ML lec 07-2
# Application & Tips: Learning and test data sets

## Performance evaluation: is this good?

## Evaluation using training set?
* Very bad testing, it's like a way of cheating.

## Training and test sets
* Cut the data to two different sets: Training, and Test
* Never use the test set, work and make a model based on the training sets, and check the validity of the model using the hidden test dataset.

## Training, validation and tst sets
* Break the training set once again: Training and Validation set.
* Validation dataset for more delicate fine tuning, before tseting the model with the real testing dataset.

## Online learning
* If there are too much data, then there another method called, online learning.
* If there are a million data, then cut the data grouping with 100 thousand.
* Time efficient, and memory efficient. 

## MINIST Dataset

## Accuracy
* How many of your predictions are correct?
* 95% ~ 99%?



# ML lec 08-1
# Deep Nerla Nets for Everyone

## Ultimate dream: thinking machine

## Activation Functions

## Logistic regression units

## HArdware implementations
* Frank Rosenblatt, Widrow and Hoff

## False Promises
* Dr Frank, " *itself* be conscious of its existence..."

## (Simple) AND/OR problem: Linealry separable?

## (Simple) XOR problem: Linearly separable?
* Different values generate 1 , and identical values generate zero.

## Perceptrons (1969) by Marvin Minsky, founder of the MIT AI Lab
* We need to use MLP, multilayer perceptions ( multilayer neural nets)
* No one on earth had found a viable way to tarin MLPs good enough to learn wuch simple functions.

## "No one on earth had found a viable way to train" by Marvin Minsky 1969

## Backpropagation (1974, 1982 by Paul Werbos, 1986 by Hilton)
* A newly invented algorithm, deliver the data in backward.

## Convolutional Neural Networks
* Using a cat.
* Cut data, and make them learn each by each.

## A BIG problem
* Backpropagation just did not work well for normal neural nets with many layers.
> THe input value gets considered weaker and weaker as the process goes into the higher layer.Weaker performance.
* Other rising machine learning algorithms: SVM, Random Forest, etc.
* 1995 "Comparison of Learning Algorithms For Handwritten Digit Recognition" by LeCun et al. found that this new approach worked better.
> The neural network system entered the second regression period.



# ML lec 08-2 
# The emergence of the 'DEEP'

## A BIG problem

## CIFAR* Canadian Institute for Advanced Research (CIFAR)
* CIFAR encourages basic research withoujt direc application, was what motivated Hinton to move to Canada in 1987,and funded his work afterward.

## "Everyone else was doing sth different"
* "Worst possible time"
* "making that gamble"
* "huge impact in forming a community"

## Braeakthrough in 2006 and 2007 by Hinton and Bengio
* REbranding to *Deppt Nets, Deep Learning*

## IMAGENET

## ImageNet Classification
* The error gets smaller and smaller

## Neural networks that can explain photos

## Deep API Learning

## Speech recognition errors

## Geoffrey Hinton's summary of findings up to today
* Our labeled datasets were thousands of times too small.
* Our computers were millions of times too slow.
* We initialized the weights in a stupid way.
* We used the wrong type of non-linearity.

## Why should I care?
* The subtitle of the youtube is not typed and inputted by each human being. Those were presented with the recognition of the sound, and they are really accurate. (OMG)


## Why NOW?
* Students/ Researchers
> Not too late to e a world expert
> Not too complicated (mathematically)
* Practitioner
> Accurate enough to be used in practice
> Many ready-to-use tols such as TensorFlow
> Many easy/simple programming languages such as Python
* After all, it is fun!




# ML lec 09-1
# Necral Nets(NN) for XOR

## One logistic regression unit cannot separate XOR
* It has been proved that a single simple process do not work well to solve the XOR.

## XOR using NN
* Could not find the difinite line to distinguish the area.

## Neural Net
* Calculate with the weight matrix and add the bias term.
* Get the value, and put it again in the sigmoid, which will generate 0 or 1.
* Calculate four times with (0,0) (1,0) (0,1), (1,1)

## Forward propagation
* Can you find another W and b for the XOR?

## NN
* Multinomial classification
* How can we learn W1, W2, b1, b2 from training data?


# ML lec 9-x
# Special lecture on Derivative

## Basic derivative

## Partial derivative: consider other variables as constants
* Chain Rule: multiply each value of the derivative to get that of the complex one.


# ML lec 9-2
# Backpropagation

## Neural Network (NN)
* How can we learn W1, W2, b1, b2 from training data?
* Derivation is needed to get the right value.

## Derivation
* Complex

## Backpropagation (Chain rule)
* Only understanding the simple method of getting the derivative value enables to solve the complex problems of the dataset.
* 


