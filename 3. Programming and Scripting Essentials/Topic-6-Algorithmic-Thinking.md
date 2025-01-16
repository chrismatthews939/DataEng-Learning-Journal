# Topic 6 - Algorithmic Thinking - 16/01/2025

## An introduction to algorithmic thinking

*In essence, algorithmic thinking is a systematic approach to solving problems. It involves breaking down problems, designing efficient algorithms, and implementing these algorithms in code.*

Imagine a toolbox filled with powerful tools, each designed to solve specific problems efficiently. 

Algorithms are like those tools—they are step-by-step instructions for solving computational tasks. 

**Search engines (Google, Bing)**

- Ranking web pages: Algorithms analyse pages, considering keywords, links, and user behaviour. The famous PageRank algorithm, courtesy of Google’s founders, ranks pages based on authority and relevance
- Efficient retrieval: Imagine searching for 'best pizza places.' Algorithms zip through billions of web pages, fetching the most relevant results in a flash

**Personalised shopping: algorithms tailored just for you**

- Browsing history insights: Algorithms analyse your virtual trail—what you have clicked, searched for, and lingered on. Based on this, they suggest products customised to your taste.
- Collaborative filtering: Ever noticed those 'Customers who bought this also bought…' recommendations? That’s collaborative filtering. It groups users with similar tastes and suggests items based on what others like you enjoyed.
- Content-based filtering: Algorithms examine product features. If you’re a sci-fi fan, they will recommend more sci-fi books. It’s like having a personal shopping assistant who knows your preferences.
- Matrix factorisation: Behind the scenes, algorithms break down your preferences into mathematical matrices. These matrices predict what you might like next.

**Social networks (Facebook, LinkedIn etc)**

- Friend suggestions: Ever received a 'People You May Know' notification? Algorithms analyse your network, uncovering hidden links. They suggest potential friends based on mutual connections and shared interests
- Graph algorithms: Think of social circles as interconnected nodes. Graph algorithms—like breadth-first search and shortest path—reveal fascinating patterns in how you’re linked to others

### Sorting Algorithms

**Bubble sort**

Imagine you have a toolbox filled with wrenches of different sizes all jumbled up. You want to arrange them in ascending order of their size. 
You start from one end of the toolbox, comparing each wrench with its neighbour. 
If a wrench is larger than its neighbour, you swap their places. 
You repeat this process until you’ve moved through the entire toolbox and all the wrenches are in order.

**Quick sort**

Consider the same toolbox with jumbled wrenches. This time, you pick a wrench at random (let’s call it the pivot) and divide the rest into two groups - one with wrenches smaller than the pivot and the other with wrenches larger. 
You then sort each group separately in the same manner, picking a pivot and dividing. You continue this process until all the wrenches are sorted and then put them back into the toolbox.

**Merge Sort**

Again, think of the toolbox with the mixed-up wrenches. You split the entire set of wrenches into two halves. You sort each half separately, perhaps by using one of the methods above. 
Once you have two sorted halves, you merge them together in a sorted manner, comparing the smallest unplaced wrench in each half and placing the smaller one next. You continue this until all the wrenches are sorted and back in the toolbox.

### So, how do you apply algorithmic thinking?

Algorithmic thinking is a critical skill in problem-solving. It involves the following steps: 

**1. Breaking down problems**
   
  - Break the problem into smaller, manageable pieces. This involves identifying the key components of the problem, similar to recognising nodes (locations) and edges (connections) in a map.

**2. Designing efficient algorithms**

  - Design algorithms, such as Dijkstra’s algorithm, to find optimal solutions. These algorithms help solve the problem with minimal effort, akin to finding the most efficient path to a destination.

**3. Implementing algorithms in code**
   
  - Test rigorously and ensure correctness.

### Tips and tricks for efficient algorithmic thinking

1. Define the requirements clearly in terms of inputs and outputs. The more time you spend on clarifying the user's requirements for your algorithm, the better your solution will be. Think in terms of inputs and outputs. What (different examples of) data does your algorithm need to look at? What (different types of) outputs does it need to produce?

2. Break the problem down into small, simple parts and define the solution for each part of the problem. This will help you stay focused and prevent you from becoming overwhelmed.

3. First implement the basic solution... Later you can make it efficient (eventually). Do not strive for perfection. It is better to get a slow algorithm to work, and then make it faster, rather than having no algorithm at all.

## Software development tools and techniques

In the digital age, software development has become an integral part of our lives, shaping the way we work, play, and interact. From the apps on our phones to the systems that run our cities, software is the invisible thread that connects and enhances our world. To create these complex systems, developers use a variety of tools and techniques. This section aims to delve into these tools and techniques, shedding light on how they contribute to the software that powers our digital world. 

### Collaborative software

**How they are useful...**

Data engineering often involves collaboration among multiple engineers. Version control systems enable seamless collaboration, allowing each engineer to work on different parts of the system without interfering with others’ work.

**Real-world application...**

For instance, one engineer might be working on improving the recommendation algorithm, while another might be optimising the database structure. Debugging tools help fix any issues that arise during this process, ensuring the final system works as intended.

### Software development tools

**How they are useful...**

In data engineering, software development tools are like a craftsman’s workshop. They enable efficient project management and collaboration, helping data engineers track progress, automate processes, and enhance productivity throughout the development lifecycle. 

**Real-world application...**

For example, Apache Hadoop is a popular tool for processing large datasets, while Apache Airflow is used for scheduling and monitoring workflows.

### Version Control

**How they are useful...**

Version control systems are essential in data engineering. They allow teams to manage changes to source code, enabling collaboration, history tracking, and seamless merging of code changes. 

**Real-world application...**

For instance, when developing a new feature for a data processing pipeline, a data engineer can create a separate branch in Git, make changes, and then merge those changes back into the main codebase without disrupting the work of others.

### Debugging techniques

**How they are useful...**

Debugging is a critical aspect of data engineering. 

It involves identifying and fixing issues in code. 

**Real-world application...**

Common bugs include syntax errors (like typos), logic errors (where code produces incorrect results), and null pointer exceptions.

Tools like IDEs and debuggers help data engineers locate and resolve these issues efficiently.

### Testing

**How they are useful...**

Testing is another crucial aspect of software development in data engineering. 

It ensures that software components work as intended. 

**Real-world application...**

For instance, a data engineer might write **unit tests** for individual functions or modules in their code, ensuring that each part works correctly in isolation. 

**Integration testing** then checks that these parts work together correctly. In **test-driven development (TDD)**, data engineers write tests before writing the code itself, ensuring that the code meets its requirements from the outset.

### Documentation in software development

In the realm of software development, documentation serves as the backbone of understanding and maintaining the codebase. Just as a well-written user manual is crucial for assembling furniture, comprehensive documentation is indispensable for scaling software projects. It provides a clear roadmap to developers, enabling them to comprehend the intricacies of the codebase, troubleshoot issues, and contribute effectively. 

**Importance of documentation**

Documentation in software development is akin to a blueprint in architecture. It provides a detailed overview of the software, including its design, functionalities, and operation.

This is particularly crucial when the software is complex or when multiple developers are working on the same project. 

Without proper documentation, developers may find it challenging to understand the codebase, leading to inefficiencies and errors.

**Tools for documentation**

**Markdown**

A lightweight markup language with plain-text-formatting syntax. It is often used for formatting readme files, or for writing messages in online discussion forums, and in text editors for the quick creation of rich text documents

**Sphinx**

A tool that makes it easy to create intelligent and beautiful documentation. It was originally created for the Python documentation

**Javadoc**

The Javadoc tool parses the declarations and documentation comments in a set of Java source files and produces a set of HTML pages describing the classes, interfaces, constructors, methods, and fields

**Benefits of documentation**

Documentation plays a pivotal role in software development. It helps other developers understand the codebase, troubleshoot issues, and contribute effectively. 

It serves as a guide for new team members to understand the project quickly and contributes to the maintainability of the software.

Moreover, it aids in the efficient tracking of bugs and facilitates smoother updates and upgrades.

## Constructing efficient algorithms





## Lecture notes

## Topic 6 Reflections


