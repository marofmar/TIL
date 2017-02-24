
# 04-4 Logistic Regression

Signoid fucntion, Threshold function, 계단 함수
Logistic Regression belongs to the discriminative category.

Minimize Negative Log Likelihood (Use an optimization algorithm)

Hessian, taking one more derivative function on the gradient function.

## Steepest Descent

* Gradient descent
Size of etha matters to accurately locate the point.
 
*Line search
Determing the right etha by using some numerical optimizations.
 
## Newton's Method
Using both the gradient and the Hessian
Less iteration methos than the Steepests. 

## Regularization

## Multi-Class Logistic Regression


# 05-1 Clustering 

>Representative case of the unsupervised learning 
Used to analyze exploratory data.
Example, anlaying the custoemr group to make some marketing strategies.

## Class vs. Clusters

## K-Means Clustering Algorithm


# 05-2 Mixture Models and Maximum Likelihood Method

## MIxture Modesl

* Latent
* Gaussian mistrue model 

## MaxLik Estimation for GMM(Gaussian Mixture Model)

* Log-likelihood for a latent variable model (LVM)
* Complete data log likelihood
* Observed data log likelihood
** No longer clean solution / Multiple local optima
** Likelihood can be increased indefinitely.

# 05-3 Mixture Models and Expectation-Maximization Algorithm

## Expectation-Maximization
- Since complete data log likelihood is not available, use the *expected complete data log likelihood* (A.k.a auxiliary function)
- Iterate the two steps
** E-step
** M-step

## Evaluating Mixture Model
* The risk of overfitting in Gaussian mixtures
* Determining the number of clusters

# 06-1 Dimensionality Reduction

## Clustering vs. Dimensionality Reduction

## Why Dimensionality Reduction?
### Problems with high dimensional data
Too many features. 
Traditional distance metrics beocme useless.
* Lots of parameters in the model.(**More training data required, more computation, more space**)
* Hard to visualize.

### Two approaches to reducing from dim D to dim L
* Feature selection (eg. Subset selection algorithms)
* Feature extraction (eg. Principle component analysis(PCA))

## Principal Component Analysis(PCA)

Input average- should be located in the original point. (Transformation process is in need to apply PCA)

* Minimize reconstruction error
How to measure the loss of information? (Reconstruction error)
Frobenius squared. (<- don't get this concept at all.)


* The optimal solution, eigenvalues

## PCA

* Minimize reconstruction error = maximize variance of Z





