# Topic 4 - Data Structures and OOP - 19/12/2024

## Getting started with Python

**IDEs**
**Visual Studio Code (VSCode)**
Microsofts Product. Good all rounder

**PyCharm**
PyCharm is a Python-focused IDE with a rich feature set for professional development, including debugging and version control. It's heavier on system resources compared to VSCode but provides a more out-of-the-box, Python-optimised experience.

Difference from VSCode: PyCharm offers an all-in-one solution tailored specifically for Python development, requiring less configuration and extension installation compared to the more general-purpose VSCode.

**Spyder**
Spyder is an IDE primarily geared towards scientists and data analysts, featuring built-in support for scientific Python libraries. It has an interactive console and variable explorer ideal for data manipulation and analysis. It’s typically packaged with Anaconda. 

While VSCode is extensible and supports multiple languages, Spyder is specifically optimised for scientific computing in Python, offering features like a variable explorer that are less common in general-purpose editors like VSCode.

**Jupyter Notebook**
Web application. Gives more of a front end to see the code running or display graphs etc.

![IDE comparison](IDE_Comparison.png)

### Exploration of Anaconda

Instead or even alongside your IDE, you can use one of the most popular data science distributions, Anaconda. But what is Anaconda?

Well, Anaconda is a popular distribution for Python and R that simplifies package management and deployment. It comes pre-loaded with numerous libraries and includes Conda, a tool for easy package and environment management. Anaconda helps data scientists work more efficiently across tasks such as data manipulation, visualisation, and machine learning. 

**Jupyter Notebooks** (packaged with Anaconda) are excellent for data science and interactive computing because they allow for real-time code execution, visualisation, and data analysis in a single, easily shareable document, facilitating iterative development and enabling clear documentation of methodologies and insights.

## Introduction to Data Structures

In Python, data structures help us store and manage multiple pieces of information in an organised manner. Imagine you need to store a list of names. You could use individual variables for each, like name1, name2, etc., but that's impractical and error-prone. A better approach is using data structures like lists to hold all names collectively. 

### Fundamental Data Types

**Integers**
These are whole numbers that can be positive, negative, or zero. They do not have a decimal point. Examples include -2, -1, 0, 1, 2, and so on

**Floats**
These are numbers that have a decimal point. They can represent real numbers, which include both whole numbers and fractions. Examples include -2.5, -1.0, 0.0, 0.5, 1.0, 2.2, and so on. Floats can represent a wider range of values than integers, with greater precision

**Strings**
Store sequences of characters and are wrapped in quotes: 'Hello'

**Booleans**
Booleans (bool) store either True or False.

### Non-Fundamental Data Types

**Lists**
Lists are ordered, changeable collections that can store different types of items. [1,2,3,4]

**Tuples**
Tuples are like lists but are immutable, meaning their elements cannot be changed. (1,"apple", 3.5

Tuples are like lists but are immutable, meaning their elements cannot be changed. There is a silly benefit and an important benefit to tuple’s immutability. 

The silly benefit is that code that uses tuples is slightly faster than code that uses lists. (Python is able to make some optimisations knowing that the values in a tuple will never change.) But having your code run a few nanoseconds faster is not important.

The important benefit to using tuples is similar to the benefit of using constant variables: it’s a sign that the value in the tuple will never change, so anyone reading the code later will be able to say, "I can expect that this tuple will always be the same. Otherwise the programmer would have used a list." 

This also lets a future programmer reading your code say, "If I see a list value, I know that it could be modified at some point in this program. Otherwise, the programmer who wrote this code would have used a tuple."

**Dictionaries**
Dictionaries hold key-value pairs and are incredibly versatile. Here is an example: {'name#: 'Johnm', 'age': 30}

*A note on Identifiers*

Identifiers are the names we give to variables (and also to collections, functions, classes, etc.). There are rules for naming identifiers:

- Must start with a letter or an underscore (_).
- Cannot start with a number.
- Can only contain alphanumeric characters and underscores.

For example, **my_number** is a valid identifier, but **1my_number** is not.

## Lists and Dictionaries

### Lists
A list in Python is an ordered collection of items that can contain elements of mixed types.

Unlike basic data types, lists allow us to hold multiple items in a single structure, making it easier to perform operations on them as a group. 

The features of lists include:

- Ordered - The items have a specific, consistent order
- Mutable - Lists can be altered even after their creation

### When and when to use lists

Use lists when:

**Order matters**
- Lists keep your elements in the order you added them.

**Duplicates allowed**
Lists allow duplicate items.

**Dynamic changes**
You need a collection that you can modify (add, remove, change items).

### Why and when to use Dictionaries

A dictionary in Python is an unordered collection of key-value pairs.

Imagine you are building a contact book where you want to store multiple details for each person—like their phone number, email, and address. 

Using a list would be cumbersome. This is where dictionaries come in handy, as they allow us to store key-value pairs.

The features of dictionaries include:

- Key-Value Pair: Items are stored as 'key' and 'value' combinations
- Fast Lookups: Excellent for retrieving data quickly

Use dictionaries when:

**Key-Value Pairs**
- You have a set of unique keys that map to specific values.

**Lookup Table**
Quick data retrieval is essential.

**Dynamic changes**
You want the flexibility to add or remove key-value pairs.

### Collections vs Data Structures

**Collections** in Python are containers that are used to store multiple elements, such as lists, sets, dictionaries, and tuples. **Data Structures**, on the other hand, are a broader concept that includes collections but also encompasses other ways of organising and storing data, such as arrays, linked lists, trees, and graphs.

**Advanced Python collections**

Python, as a versatile and powerful programming language, offers a variety of advanced collections that provide robust functionality and flexibility for handling data. This section delves into these advanced collections, exploring their definitions, examples of their usage.

### Sets
**Definition:** A set is an unordered collection of unique elements.

**Use Cases:** Sets are useful for membership testing, eliminating duplicate entries, and performing mathematical set operations like union, intersection, and difference.

**Example:** unique_numbers = {1,2,3,4}

### Frozen Sets
**Definition:** A frozenset is an immutable version of a set, meaning its elements cannot be changed after creation.

**Use Cases:** Frozensets are used in situations where a set's immutability is required, such as keys in dictionaries.

**Example:** frozen_unique_numbers = frozenset([1,2,3,4])

### Named Tuples
**Definition:** Named tuples are an extension of the regular tuple that allows you to name the elements, improving code readability.

**Use Cases:** Named tuples are ideal for cases where you need tuples but also want to access elements by name rather than index.

**Example:** from collections import namedtuple Point = namedtuple('Point', ['x','y']) p = Point(1,2)

### OrderedDict
**Definition:** An OrderedDict is a dictionary that maintains the order of items based on insertion order.

**Use Cases:** OrderedDicts are beneficial when the order of items is important, such as in LRU (Least Recently Used) caches.

**Example:** from collections import namedtuple Point = namedtuple('Point', ['x','y']) p = Point(1,2)

from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4










## Lecture Notes


## Topic 4 Reflections

