# Chapter 6
# Probability

> The lwas of probability, so true in general, so fallacious in particular. - Edward Gibbon

* Think of probability as a wasy of quantifuying the uncertinty associated with *events* chosefn form a some *universe* events. 

> One could, were so inclined, get really deep into the philosophy of what probability theory menas. (This is best doen over beers.) We won't be doing that. 

## Dependence and Independence

* Mathematically, we say that two events *E* and *F* are independent if the probability that they both happen is the product of the probabilities that each one happens.


## Conditional Probability

* The probability that *E* happens, given that we know that *F* happens.


## Bayes's Theorem

> One of the data scientist's best friends is Bayes's Theorem, which is a way of "reversing" conditional probabilities. 

> Let's say we need to know the probability of some event *E* conditional on some other event *F* occurring. But we only have information about the probability of *F* conditional on *E* occurring. 


## Random Variables

* A random variable is a variable whose possible values have an associated probability distribution.

* The expected value of a random variable, which is the avearge of its values weighted by their probabilies. 

* Random variable can be conditioned on events just as other events can.

* For the most part, we will be using random variables implicitly in what we do without calling special attention to them.


## Continuous Distribution

> A coin flip corresponds to a *discrete distribution*, one that associates positive probabilikty with discrete outcome. 

> Often we will want to model distributions across a continuum of outcomes. 

> Because there are infinitely many numbers between 0 and 1, this means that the weight it assigns to individual points must necessarily be zero. For this reason, we represent a continuous distribution with a *probability density function (pdf)* such that the probability of seeing a value in a certain interal equals the integral of the densiy function over the interval. 


## The Normal Distribution

> The normal distribution is the king of the distributions.
> It is the classic bell curve-shaped distribution and is completely determined by two parameters: its mean and its standard deviation.
> The mean indicates where the bell is centered, and the standard deviaiton, how "wide" it is.

* When mu is zero and the value of the standard deviation is one, then it's called the *standard normal distribution*. 


## The Central Limit Theorem

> One reason the normal distribution is so useful is the *central limit theorem*, which says (in essence) that a random variable defined as the avearge of a large number of independent and identically distributed random variable sis itself approximately normally distributed. 

* An easy way to illustrate this concept is by looking at *binomal* random variables, which have two parameters *n* and *p*. 

* A Binomial(n,p) random variabel is simply the sum of *n* independent Bernoulli(p) random variables, each of which equals 1 with probabilty *p* and 0 with probability 1-*p*.

* The mean of a Bernoulli(p) variable is *p*, and its standard deviation is sqrt(p*(1-p).

* The central limit theorem says that as n gets larger, a Binomial(n,p) variable is approximately a normal random variable with mean np and deviation of np(1-p). 




# Chapter 7
# Hypythesis and Inference

> It is the mark of truly intelligent person to be moved by statistics. -George Bernard Shaw. 

> The &sicence* part of data science frequently involves forming and testing *hypothesis* about our data and the processes that generate it. 

## Statistical Hypothesis Testing

* In the classical setup, we have a *null hypothesis H0* that represents some default position, and some alternative hypothesis H1 that we would like to compare it with. 

* We use statistics to decie whether we can reject H0 as false or not. 


## Example: Flipping a Coin

> In particular, our test will involve flipping the coin some number *n* times and counting the number of heads X. Each coin flip is a Bernoulli trial, which means that X is a Binomial(n,p) random variable, which we can approximate using the normal distribution.

* We need to make a decision about *significance* - how willing we are to make a *type 1 error* ("false positive"), in which we rejcet H0 even though it's true. 

* This willingness is often set at 5% or 1%. 

* We are often interested in the *power* of a test, which is the probability of not making a *type 2 error*, in which we fail to reject H0 even though it's false. In order to measure this, we have to specify what exactly H0 being false means. 

* p-valuses: Instead of choosing bounds based on some probability cutoff, we compute the probability - assuming H0 is true - that we would see a value at least as extreme as the one we actually observed. 

>P values evaluate how weel the smaple data support the devil's advocate argument (Null Hypothesis) that the null hypothesis is true. It measures how compatible your data are withhe null hypothesis. How likely is the effect observed in your sample data if the null hypothesis is true?

>>High P values: your data are likely with a true null.

>>Low P values: your data are unlikely with a true null.

>A low P value suggests that your sampe provides enough evidence that you can reject the null hypothesis for the entire population.

[Source of the additional explanation](http://blog.minitab.com/blog/adventures-in-statistics-2/how-to-correctly-interpret-p-values)

* Continuity correction <- I don't get this concept well.

* Simulation can be a one way to figure out the estimate is sensible enough.



## Confidence Intervals

* Constructing a confidence interval to test the hypothesis.

* This is a statement about the *interval*, not about *p*. You should understand it as the assertion that if you were to repeat the experiment many times, 95% of the time the "true" parameter (which is the same every time) would lie within the observed confidence interval (which might be different every time).


## P-hacking

* A procedure that erroneously rejects the null hypothesis only 5% of the time will-by definition-5% of the time erroneously reject the null hypothesis.

> If you want to do good *science*, you should determine your hypotheses before looking at the data, you should clean your data without the hypotheses in mind, and you should keep in mind that *p-values* are not substitutes for commone sense. (AN alternative approach is "Bayesian Inference".)


## Example: Runnig an A/B Test

> Experiece optimization, which is a euphemism for trying to get people to click on advertisemnts. LOL.

* T-distribution


## Bayesian Inference

* The procedure we've looked at have involved making probability statements about our *tests: "there's only a 3% chance you'd observe such an extreme statistic if our null hypothesis were true."

* An alternative approach to inference involves treating the unknown parameters themselves as random variables. 

* The analyst (me) starts wit a *prior distribution* for the parameters and then uses the observed data and Bayes's Theorem to get an updated *poterior distribution* for the parameters. 

* Rather than making probability judgeents about the tests, you make probability judgements about the parameers themselves.

> (I don't get this concept..) IT is no coincidence that the posterior distribution was again a Beta distribution. The number of heads is geven by a Binomial distribution, and the Beta is the *conjugate prior* to the BInomial distribution This means that whenever you update a Beta prior using observations from the corresponding binomial, you will get back a Beta posterior.

* If you flipped the coin more and more times, the priror would matter less and less until eventually you'd have (nearly) the same posterior distribution no matter which prior you started with.

> Using Bayesian inference to test hypotheses is considered somewhat controversial - in part because its mathematics can ge somewhat complicated, and in part because of the subjective nature of choosing  a prior. 



# Chapter 8
# Gradient Descent

> Those who boast of their descent, brag on what they owe to others.-Seneca

> Frequently when doing data science, we'll be trying to find the best model for a certian situation. And usually "best" will mean something like "minimizes the error of the model" or "maximizes the likelihood of the data." In other words, it will represent the solution to some sort of optimization problem.

## The Idea Behind Gradient Descent

> If a function has a unique global minimum, this procedure is likely to find it. If a function has multiple (local) minima, this procedure might "find" the wrong one of them, in which case you might re-run the procedure from a variety of starting points. If a function has no minimum, then it's possible the procedure might go on forever.


## Estimating the Gradient

* If 'f' is a funciton of one variable, its derivative at a point x measure how f(x) changes when we make a very small change to x. It is defined as the limit of the idfference quotients.

> (Many a would-be calculus student has been stymied by the mathematical definition of limit. Here we'll cheat and simply saty that it means what you think it means.)

* The derivative is the slope of the tangent line at the point, while the difference quotient is the slope of the not-quite-tanget line that runs through (x+h, f(x+h)). As *h* gets smaller and smaller, the not-quite-tangent line gets closer and closer to the tangent line. 

> A major drawback to this "estimate using difference quotients" approach is that it's computationally expensive. If v has length n, estimate_gradient has to evaluate f on 2n different inputs. If you're repeately estimating gradients, you're doing a whole lot of extra work. 


## Using the Gradient


## Choosing the Right Step Size

* Although the rationale for moving against the gradient is clear, how far to move is not. 

> Indeed, choosing the right step size is more of an art than a science. Popular options include:

>> Using a fixed step size

>> Gradually shrinking the step size over time.

>> At each step, choosing the step size that minimizes the value of the objective fuction.

* The last one sounds optimal but is, in practice, a costly computation. We can approximate it by trying a variety of step sizes and choosing the one that results in the smallest value of the objective function.


## Putting It All Together


## Stochastic Gradient Descent

* As we mentioned before, often we'll be using gradient descent to choose the parameters of a model in a way that minimizes some notion of error.

> Usually these error functions are *additive*, which means that the predictive error on the whole data set is simply the sum of the predictive errors for each data point.

>> When this is the case, we can instead apply  a technique called *stochastic gradient descent*, which computes the gradient (and takes a step) for only one point at a time. It cycles over our data repeatedly until it reaches a stopping point.

* The stochastic version will typically be a lot faster than the batch version. 











