---
id: hdpobsfzkt6t2si7wrce5ov
title: Python
desc: ''
updated: 1652091803157
created: 1650540938888
---
Python was released in 1991. Using Python, we can create client-server applications, connect to databases, perform operations, solve big mathematical problems, and prototype or create production-level software systems. Python is a high-level programming language because it is abstracted from assembly language, and because it provides instructions to CPU

These are the differences between the two versions of Python:

- Unicode is a specification designed to list every character used by human languages and give each character a unique code. Python 2 has less Unicode support compared to Python 3. Python 3 treats strings as Unicode by default. In Python 2, we need to mark the string with 'u’ if we want to store it as Unicode.

- Python 2 treats print as a statement rather than a function, meaning it is not necessary to wrap the text around parentheses in Python 2 print statements. Python 3 treats print as a function. Users must wrap the text around parentheses.

- Python 2 treats numbers without decimal as an integer by default. That means the result of 5/2 is 2. This is not the case in Python 3. It will give the result of 5/2 as 2.5.

- In Python 2, list comprehension–a variable that is used inside comprehension–impacts global, or outside, variables. This can be understood as a bug. The was resolved in Python 3.

**Memory management in Python**
Python also has a private heap that manages objects and other data structures. Python has a built-in memory manager that manages memory requirements. This memory manager takes care of object sharing and the segmentation and allocation of objects. Python gives no control to the user regarding memory management. Python also has a garbage collector. When objects are not needed, Python reclaims the memory from them automatically.

Is Python compiled or interpreted?

Compiled languages use a special program that is called a compiler. It takes the code written and converts that code to machine code. This machine code executes directly on the processor. So, the translation of the complete code happens before the start of the execution.

Interpreted languages do not do perform any translation prior to run time. During the run time of the code, they start translating the code line by line in a machine-understandable format.

‘Compiled’ or ‘interpreted’ is not the property of a language. It is the property of implementation. Python is neither a purely compiled language nor a purely interpreted language. Python programs can run directly from source code, so the official Python is interpreted. We also have other implementations of Python available that first convert the Python code to machine code.

We do not need to put any data type before the variable, as is required in some other programming languages (C, Java, etc.). In other words, Python is not statically typed. That means we do not need to declare the variables or their type before using them. Every variable in Python is an object.

We cannot combine different types of variables.. however change the type and then do what you want to do.

In Python, we use variables locally or globally. If a variable is declared inside a function, its scope is limited, and it is called the local variable. If a variable is declared outside a function, its scope is global, and it can be used outside of the function.

If we use the same name for global and local variables, the local variable would be preferred inside its parent function

**Decision making using if elif else statements**
Definite and indefinite iterations
Iteration can be definite or indefinite. Definite iterations are repeated a specific number of times, while indefinite iterations are repeated until a condition is met.

While loop
A while loop iterates a block until the condition remains True.

The while loop operates using the following logic:

When the program reaches a while loop, the condition is checked. If the underlying condition is True, the code under the while block will be executed. After the execution of the complete block, the condition is checked again. If is True, the statement is executed again. Otherwise, the controls go to the code after the loop block.

We need to be careful with loops. We may end up writing an infinite loop.

- Sometimes infinite loops are needed. For example, in an operating system process queue, the OS checks the queue indefinitely.

**Loop control statement** -> Using a loop control statement, we can come out of the loop. We have two keywords in Python: break and continue.

*break:* if execution reaches a break statement, control is transferred out of the loop.

*continue:* when control reaches the continue statement, it moves the control to the next condition check and skips the remaining block of code.

**Functions are used to create reusable code.**
In Python, we can create a function using the def keyword. The body of the function will be indented. It contains an optional return statement that returns the control from the function to the calling program.

Function parameters: Parameters are information that can be passed in the function. We can give any number of parameters to the function. These should be separated by commas. Functions are called by reference. All the changes made inside the function will also reflect the original variable.

Sometimes we don’t know the number of arguments that we are going to use inside a function. Python supports variable-length arguments. We can define the *variable to denote a variable-length argument.

-> If a function does not have a return statement, what will be the default return value ? -> None

-> What is the name of the technique in which a function calls itself inside the body? -> Recurison

- Lists are containers that are used to store multiple data elements. Lists have an order of elements and have a count of elements. These ordered elements can be accessed by the index. The index order starts from 0 and goes the length of the list. Lists in Python are mutable objects.

- A tuple is also a collection of objects as a list. The difference between the list and tuples is mutability. Lists are mutable which means that elements of the list can change but tuples are immutable which means elements of the tuple are ordered and cannot be changed. We can’t add or delete elements of a tuple. Furthermore, it isn’t possible to append another tuple to an existing tuple.

- The dictionary is a set of key-value pairs. The keys of the dictionary are unique and unordered, meaning that the key storage does not have any order.

Like other programming languages, Python is an object-oriented programming language. Classes can be created using the class keyword.

The class can be created using a class keyword. Let’s create a simple class with no functionality.

```python

class Car:
  pass
porsche = Car()
print(porsche)

# What would the best definition s1 = Student() be?
# s1 is a reference to the Student object

# Classes contain attributes which can be used with objects.
class Car:
  speed_limit = 240

porsche = Car()
print(porsche.speed_limit)

#We can also define functions inside the class; these are called class methods.

class Car:
  speed_limit = 240
  def car_speed_breakdown(self):
    return self.speed_limit - 50

porsche = Car()
print(porsche.car_speed_breakdown())

# Methods inside the class can also be accessed by the object of the class, the same as the variable

# To initialize different attributes, we can put an __init __ () method inside the class definition. 
# This method will be called once at the time of object creation. We can think of similar behavior in other programming languages (e.g. Java) as the constructor

class Car:
  speed_limit = 240
  def __init__(self,speed_limit=None):
    self.speed_limit = 150
  def car_speed_breakdown(self):
    return self.speed_limit - 50

porsche = Car()
print(porsche.car_speed_breakdown())

# First, the __init__() method is called when the object is created

# Which method works as a constructor in the class?  -> __init()__
```

## NUMPY

Arrays in NumPy are used heavily for general-purpose tasks.
The array consists of elements of the same type.
The number of dimensions of the array is called the rank of the array. Elements of the NumPy array are accessed with square brackets.

What is the difference between a Python list and a NumPy array?

- The key difference between these two is in performance. NumPy arrays are smaller in size, and better in performance, and functionality.

- Size – For n elements, the size of a NumPy array is less than that of a Python list.

- In a Python list, each list object points to another object, meaning an additional eight bytes are needed for reference. These are not needed in the NumPy array.
- Functionality - NumPy arrays are loaded with many scientific and numeric computation functions.
- Speed – NumPy arrays are faster than Python lists.
- The scipy.special package contains various mathematical functions. These special functions include cubic root, exponential, permutation, combination, kelvin, and relative error exponential.

How can we handle missing values in the Pandas Data Frame?
Sol: We can either drop the rows that are missing values using the dropna() function, or replace the missing values using the fillna() function.

You have a Data Frame that contains one column called 'length'. How can you select records that have length > 10?
Sol : We can use the Pandas row subset operation. The subset of the records can be selected with: data[data.length > 10]

How can we randomly select rows in Pandas?
Sol: We can apply a sample() function over the dataset. The function can be applied in two ways:
we can get the specific number of rows with parameter n, or we can get a fraction of rows with parameter frac.

What is the difference between loc and iloc in Pandas?
Sol: Both are used to subset the data frame.

- loc gets columns or rows with particular labels from the index. (need named indices)
- iloc gets columns or rows with a particular position in the index. (need integer indices)

How can we extract a data summary from a Pandas Data Frame?
Sol: Some data statistics can be generated using describe(), value_counts(), nunique(), min(), max(), mean(), median(), std(), etc

Why use data Visualization?
Sol: When we place data into a visual context patterns, trends, and correlations that might have otherwise gone undetected rise to the surface.
In the middle stages of a project, we can use visualizations to gain more insights and generalize model results.
Towards the end of a project, it’s very important to be able to present our results in a clear, concise, and compelling manner so that our audience (which is often made up of non-technical people) can understand the results.

- Efficient deep learning and reinforcement learning requires GPU level computing. Sklearn does not support them by design.

sklearn supports DecisionTreeClassifier and ExtraTreeClassifier

Name a few ensemble-based regression models supported by sklearn.
Sol: Sklearn supports AdaBoostRegressor, BaggingRegressor, GradientBoostingRegressor, VotingRegressor, RandomForestRegressor, etc

Which sklearn classes are used in training a Neural Network?
Sol: MLPClassifier and MLPRegressor

Tensorflow is an end-to-end machine learning platform for creating and deploying industry-standard machine learning models. It was created by the Google Brain team. TensorFlow can train and run neural networks of different types. It supports a large number of architectures, which makes creating robust models.
TensorFlow is a popular library, comparable to PyTorch, CNTK (by Microsoft), and Apache MXNet.

How does it work?
TensorFlow allow users to create data flow graphs, which describe how the data moves with nodes in the graph. Each node in the graph represents a mathematical operation, and each is a tensor or multidimensional array. TensorFlow applications can run on CPUs and GPUs. The power of TensorFlow is that it can enable GPUs for faster training and prediction.

What are Tensors in TensorFlow?
Sol: Tensors are the generalizations of metrics and vectors to higher dimensions. TensorFlow represents these tensors as ndarrays of base datatypes.

What is TensorBoard?
Sol: Tensorboard is a visualization tool that provides a dashboard for the plot metrics of training models

KNIME:
Nodes are able to perform doing some tasks and produce their results. Nodes have different states. Initially, nodes are in the 'not configured state'. After configuration, nodes moved to the idle state. If the execution is successful, nodes move to the executed state. If the execution is failed due to some error, nodes move to the error state

Workflows are a combination of nodes. Users can create a flow in which the data moves, and all processing is performed node by node.

We can use various tools offline to build ML models. Sometimes, we don’t have enough computing power to create models. Also, we may want our model to be deployed in an environment which will always be available.

To work within these constraints, we can use cloud machine learning solution providers. In the past, people have used high-end machines and installed Python or R based libraries on their servers. Now, cloud service providers give specialized services for building machine learning and deep learning models that are fast and have an easy to understand GUI.

After building a model, the user can deploy the solution using APIs provided by the system.
