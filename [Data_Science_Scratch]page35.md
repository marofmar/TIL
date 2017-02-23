#Data Science from Scratch 
#2017-02-22

##<Preface>##

Data scientist has been called, 'the sexiest job of the 21st century.'
**What is data scientist?**
According to a Venn diagram, data science lies at the intersection of:
Hacking skills/ Math and statistics knowledge/ Substantive expertise

, and this book focuses on the first two traits.

>Playing with data is fun! (Especially compared to some of the alternatives, like tax preparation or coal mining.)

>All she needs is an inquisitiv emind, a willingness to work hard, and this book. Hence this book.


##1. Introduction##

**The Ascendence of Data**

Let's find some answers that no one's ever thought to ask, under the enormous data world.

**What Is Data Science?**

>We'll say that a data scientist is someone who extracts insights from messy data. Today's world is full of people trying to turn data into insight.

>But it certainly won't hurt your career if you like figuring out the best way to get people to click on advertisements.

**Motivating Hypothetical: DataSciencester**

>Welcome aboard, and good luck! (You're allowed to wear jeans on Friday, and the bathroom is down the hall on the right.)

**Finding Key Connectors**

>In particular, he wnats you to identify who the "key connectors" are among data scientists.
>(which, in one of the great cosmic coincidentces, rhymes with the user's id)

**Salaries and Experience**

**Paid Account**

**Topics of Interest**




##2. A Crah Course in Python##

**Whitespace Fromatting**

**Modules**
Certain features of Python are not loaded in first hand, which requres additional work, so called, 'import'. 

-simpoly import 
-when there were need a number of typing, add 'as sth'
-when in need of a few specific values form a module, import explicitly by 'from A import B'

**Arithmatic**

**Functions**

-A function is a rule for taking zero or more inputs and returning a corresponding output.
-Star with 'def' and never forget to add the ':', mostly ends with 'return'
-Python functions are *first-class*, which means that we can assign them to variables and pass them into functions just like any other arguemnts: *I don't get this*
-Both indicate same functional performance.     
     \'another_double = lambda x: 2*x\'
     \'def another_double(x): return 2*x\'

**Strings**

-Strings can be delimited by single or doulbe quotation marks, but the quotes have to match)

**Exceptions**

-Handle the exceptions, raised by Python since there were something wrong in the code, using 'try' and 'except'

**Lists**

-A likst is simply an ordered collection. (It's similar to 'arrays' of some other languages with some added functionality.)
-Python has an 'in' operator to check for list memebership:
      \'1 in [1,2,3] *#True*\'
      \'0 in [1,2,3] *#False*\'

**Tuples**

-Lists go with this big parenthesis [], and tuples go with this small ones () or sometimes without parenthesis at all.
-Tuples are a convenient way to return multiple values from functions.
-Tuples (and lists) can also be used for multiple assignment.

**Dictionaries**

-A dictionary associates values with keys and allows the users to quickly retrieve the value corresponding to a given key.
-Dictionaries go with this parenthesis, {}
-A user can look up the value for a key using a square brackets, like \'grade["Joel"]\'
-A user can check for the existence of a key using \'in\'
-Dictionary keys must be immutable; in particular, you cannot use lists as keys. If you need  amultipart key, you should use a tuple or figure out a way to turn the key into a string.
-DefaultDict / Counter

**Sets**

-Set is a collection of distinct element
-By using 'sets', the speed of the process gets faster.

**Control Flow*

-Using 'if' enables users to perform an action conditionally.

**Truthiness**

-Booleans in Python should have capitalized first letter to perform adequately.
-Python uses the value 'None' to indicate a nonexistent value. It is similar to other language's null.
-Python lets you uses any value where it expects a Boolean. And pretty much anything else gets treated as True. 

**Sorting**

-If you don't want to mess up your list, you can use the 'sorted' function, which returns a new list.
-    \'y = sorted(x) or x.sort()\'
-By default, the sorting is conducted to a list from smallest to largest based on naively comparing the elements to one another.
-If you want elements sorted from largest to smallest, you can specify a \'reverse=True\' parameter. 


**List Comprehensions**

-To transform a list into another list

**Generators and Iterators**

-A generator is sth that you can iterate over (for us, usually using for) but whose values are produced only as needed (lazily).

>The flip side of laziness is that you can only iterate through a generator once. IF you need to iterate through something multiple times, you will need to either recreate the generator each time ro use a list.


-A second way to create generators: using 'for' comprehensions wrapped in parenthesis.


**Randomness**

-TO generate random numbers with random moudle: import random

-The random module actually produces pseudorandom (that is, deterministic) numbers based on an internal state that you can set with random.seed if you want to get reproducible results.

-random.randrange

-random.shuffle

-random.choice

-ramdom.sample


**Regular Expression**

-Regular expressions provide a way of searching text.

     \'import re\'

**Object-Oriented Programming**

>Like many languages, Python allows you to define classes that encapsulate data and the functions that operate on them. We will use them sometimes to make our code cleaner and simpler. 


**Functional Tools**

-When passing functions around, sometimes we will want to partilally apply (or carry) functions to create new functions. 

**Enumerate**

-Not infrequently, you'll want to iterate over a list and use both its elements and their indexes

**zip and Arguments Unpacking**

-zip transforms multiple lists into a single of tupels of corresponding elements.

-'Unzip', using the asterisk's performance.

**args and kwargs**

-




>>>> Hm,,,,,,,,,,,,,, seems like reading once is not enough. need to practice the exmaples of this book. 








