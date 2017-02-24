# Chapter 3
# Visualizing Data

> Although it is easy to create visualizations, it is much harder to produce *good* ones.

There are two primary uses for data visualizations:
* To explore data
* To communicate data

## Matplotlib

The *matplotlib library* might not be adequate to produce elaborate interactive visualizations for the Web, but it would be good choice to make simple bar charts, line charts, and scatterplots.

    matplotlib.pyplot
    from matplotlib import pyplot as plt
    
*matplotlib* is also capable of producing complicated plots within plots, sophisticated formatting, and interactive visualizations. 

## Bar Charts

A bar chart is a good choice when you want to show how some quantity varies among some discrete set of items.

A ar chart can also be a good choice for plotting histograms of bucketed numeric values, in order to visually explore how the values are distributed. 

## Line Charts

A line chart is a good choice to show trends.

## Scatterplots

A scatterplot is the right choice for visualizaing the relationsihp between two paired sets of data. 

If your're scattering comparable variables, you might get a misleading picture if you let matplotlib choose the scale.
>call plt.axis("equal")




# Chapter 4
# Linear Algebra

Linear algebra is the branch of mathematics that deals with *vector space*.
Linear algebra underpins a large number of data science concepts and techniques.

## Vectors

Since Python lists are not vectors, we cannot perform arithmetic on them. 

The dot product of two vectors is the sum of their componentwise products.
The dot product measures how far teh vector v extends in the w direction. 
Another way of saying this is that it's the length of the vector you'd get if you projected v onto w.

> Using lists as vectors is great for exposition but terrible for performance.
> In production code, you would want to use NumPy library, which includes a high-performance array class with all sorts of arithmetic operations included.

## Matrices

A matrix is a two-dimensional collection of numbers, and they are represented as *lists of lists*.

Useful matrices
* Matrices can be used to represent a data set consisting of multiple vectors.
* We can use n*k matrix to represent a linear function that maps k-dimensiona lvectos to n-dimensional vectors.
* Matrices can be used to represent binary relationsihps.

# Chapter %
# Statistics

### Statistics refers to the mathematics and techniques with which we understand data.

## Describin g a SIngle Set of Data

We use statistic sto distill and communicate relevant features of the data.

## Central Tendencies

Mean: the sume of the data dividied by its count
Median: the middle-most value, or the average of the two middle-most values.
Unlike the mean, the median doesn't depend on every value in the data.
Quantile: a generalization of the median.

## Dispersion

Didspersion refers to measures of how spread out the data is.
Range: a very simple lmeasure of the degree of dispersion, which is the difference btw the alrgest and the smallest elements.
Variance: smaple variance is conducted via denominating the nominator by (n-1)
DIfference between the 75th percentile value and the 25th percentile value.

## Correlation

Covariance: the paried analogue of variance. 
> Whereas variance measures how a single variable deviates from its mean, covariance measures how two variables vary in tandem from their means.
> A 'large' positive covariance means that x tends to be large when y is large and small when y is small. A 'large' negative covariance means the opposite. A covariance close to zero means that no such relationship exists.
> Nontheless, this covariance number can be hard to interpret, for a couple of reasons:
* Its units are the product of the inputs' units, which can be hard to make sense of.
* If each user had twice as many friends, the covariance would be twice as large. But in a sense the variables would be just as interrelated. Said differently, it's hard to say what counts as a 'large' covariance.
> For this reason, it's more common to look at the correlation, which divides out the standard deviations of both variables.

Correlation: the *correlation* is unitless and always lies between -1 (perfect anti-correlation) and 1 (perfect correlation).
Sometimes, excluding outliers are in need.

## Simpson's Paradox

Simpson's Pradox: correlations can be misleading when *confounding* variables are igrnored.

> The key issue is that correlation is measuirng the relationship between your two variabels *all else being equal*. If your data classes are assigned at random, as they might be in a well-designed experiment, the assumption might be plausible. 
> But when there is a deeper pattern to class assignments, "all else being equal" can be an awful assumption.
>The only real way to avoid this is by *knowing your data* and by doing what you can to make sure you've checked for possible confounding factors. 

## Some Other Correlational Caveats

## Correlation and Causation

One way to feel more confident about ausality is by conducting randomized trials.







