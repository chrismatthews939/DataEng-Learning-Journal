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

### Understanding algorithm design

Algorithms are step-by-step instructions for solving specific tasks. Just like an architect considers materials, load-bearing structures, and aesthetics, we consider factors like time complexity, space efficiency, and correctness.

**Algorithm design**

1. Time complexity
2. Space efficiency
3. Optimising resource usage

### Problem-solving strategies

**Divide and conquer**

Imagine breaking a big problem into smaller, manageable pieces. Divide and conquer algorithms recursively solve subproblems and combine their solutions. Examples include Merge Sort, Quick Sort, and binary search.

**Dynamic programming**

Imagine a painter covering a canvas with intricate patterns. Dynamic programming breaks complex problems into overlapping subproblems. We store solutions to subproblems and build up to the final solution. Examples include the Fibonacci sequence and solving shortest path problems.

**Greedy Algorithms**

Imagine a squirrel collecting nuts for winter. Greedy algorithms make locally optimal choices at each step. They don’t always guarantee the best global solution but work well for certain problems. An example is Dijkstra’s algorithm for finding the shortest path.

### Real-world application of problem-solving strategies

**Routing Algorithms (GPS Navigation):**

- GPS devices find the shortest route from point A to point B.
- They use graph algorithms (like Dijkstra’s) to optimise travel time.

**Data Compression (ZIP Files):**

- Compression algorithms reduce file size while preserving data.
- ZIP files use techniques like Huffman coding.

**Network Routing (Internet Traffic):**

- Imagine directing traffic on a busy highway
- Routing algorithms manage data packets efficiently across networks
- BGP (Border Gateway Protocol) is an example

## Advanced Algorithmic Techniques

### An introduction to graph algorithms

Graphs are powerful tools used to model complex systems. They are like interconnected cities on a map. In this section, we will delve into advanced graph algorithms that help us navigate these ‘cities’ efficiently. 

### Shortest path algorithms

These algorithms help us find the most efficient path between two nodes in a graph. 

They are like GPS systems guiding a traveller to their destination. 

![shortest path algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Shortest_path_with_direct_weights.svg/1200px-Shortest_path_with_direct_weights.svg.png)
```
In graph theory, the shortest path problem is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimised. 

Algorithms like Dijkstra’s and Bellman-Ford help you discover the most efficient path.

Dijkstra’s algorithm explores neighbouring cities in order of increasing distance, ensuring you reach your destination with minimal travel time.

Bellman-Ford handles negative edge weights and detects negative cycles.
```

### Cycle detection algorithms

These algorithms help us identify cycles in a graph, preventing us from going in circles. 

In computer science, cycle detection or cycle finding is the algorithmic problem of finding a cycle in a sequence of iterated function values.

![cycle detection algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Functional_graph.svg/330px-Functional_graph.svg.png)

```
In the graph above, so-called cycles may appear, for example around {4}, or between {1}, {6} and {3}. 

Detecting cycles may be helpful as a way of discovering infinite loops in certain types of computer programs. 

For example, in Excel, circular references could cause problems in your workbooks. Excel uses cycle detection to manage this.
```

### Network flow algorithms

These algorithms help us optimise the flow in a network while respecting capacity constraints. 

They are like traffic control systems optimising the flow of vehicles on the road. 

![Network flow algorithms](https://media.geeksforgeeks.org/wp-content/cdn-uploads/ford_fulkerson2.png)


### String algorithms

Strings are sequences of characters that can be likened to musical notes in a song. In this section, we will explore advanced string algorithms that help us find patterns and harmonies within these ‘notes’.

**Pattern matching algorithms**

These algorithms help us locate patterns within a longer text. 

- Algorithms like **Knuth-Morris-Pratt (KMP)** and **Boyer-Moore** efficiently locate patterns within a longer text
- KMP avoids unnecessary character comparisons by using a prefix function
- Boyer-Moore skips ahead based on mismatched characters

*They are like a reader searching for a specific word in a book.*

**Substring search algorithms**

These algorithms help us quickly identify matching substrings. 

- Algorithms like Rabin-Karp use hashing to quickly identify matching substrings.
- Rabin-Karp slides a window over the text, hashing each substring and comparing it to the target hash

*They are like a music enthusiast searching for a specific phrase in a song’s lyrics.*

**Substring compression algorithms**

These algorithms help us reduce the space needed to store strings while preserving data (like DNA sequences or text documents).

- Compression algorithms reduce the space needed while preserving data
- Techniques like Run-Length Encoding (RLE) replace repeated characters with a count.

*They are like a librarian archiving books in a compact yet accessible manner.*

```
Modern software applications typically use pre-existing libraries for pattern matching algorithms like Knuth-Morris-Pratt (KMP) and Boyer-Moore, avoiding the need to reinvent the wheel. These algorithms are integral to various tools and systems for efficient text searching.
Examples of software packages that use string searching and pattern matching algorithms include: Text Editors and IDEs, Databases, Search Engines, Bioinformatics software (e.g. for DNA sequence analysis).
File Search Utilities: Unix tools like grep, Compilers, Text Processing Libraries: Regular expression libraries in Python and Java.
Version Control Systems: Tools like Git, Security Systems: Intrusion detection and antivirus software, NLP Libraries like SpaCy and NLTK.
String searching and pattern matching algorithms are embedded in lots of widely used libraries, ensuring efficient text searching and pattern matching across various applications.
```

### Advanced Data Structures

Data structures are foundational elements in computer science, much like Lego blocks in a construction set. In this section, we will explore more complex structures that provide efficient ways to organise and manipulate data.  These are as follows:

**Heaps (Priority queues)**

Heaps help us maintain a partially ordered structure, are useful for tasks like scheduling. 

- **Min-heaps** ensure the smallest element is at the top, useful for scheduling tasks
- **Max-heaps** prioritise the largest element, helpful for finding top-k elements.

These are a fairly abstract concept, but you can think of them as a 'black box' where you can add elements and trust that they will come back to you in the right order.

**Tries (Prefix trees)**

Tries help us store words in a tree-like structure for efficient word lookup. 

- Each level represents a character, allowing fast word lookup
- Tries power autocomplete features and spell-checkers

They are like a dictionary organised in a way that allows fast word search. 

**Segment Trees (Interval trees)**

Segment trees help us handle range queries efficiently. 

- Segment trees handle range queries efficiently
- They divide data into segments, allowing quick calculations (e.g., finding maximum or sum) within specific intervals
- Segment trees are essential for handling dynamic data

They are like a timeline tracking events such as temperature changes over time.

### Real-life applications

Understanding these advanced algorithmic techniques is not just an academic exercise. They have real-world applications that impact our daily lives:

- **Social networks (Graph algorithms):** Social networking platforms like Facebook and LinkedIn use graph algorithms to suggest friends and recommend job opportunities based on mutual connections.

- **Search engines (String algorithms):** Search engines like Google use string algorithms to find relevant web pages based on search queries. Efficient indexing and searching of web content rely heavily on these algorithms.

- **Database indexing (Advanced data structures):** Database systems use advanced data structures for efficient indexing. This allows quick retrieval of data, enhancing the performance of database operations.






## Lecture notes

## Topic 6 Reflections


