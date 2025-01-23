# Topic 7 - Parallel Programming - 23/01/2025

## First All Day Hackathon Session

### Big O Notation Practice

'L5DE M3T6' Jupyter Notebook in Google Collab for Big O Notation

### Parallel Programming

*Decreasing the time it takes to run things by running things at the same time*

**Concurrency vs Parrallelism**

*One will be quicker than the other depending on the problem*

![Concurrency vs Parrallelism](https://techdifferences.com/wp-content/uploads/2017/12/Untitled.jpg)

**Multiprocessing vs Multithreading**

*Multiprocessing is like having multiple chefs in a kitchen, each with their own stove, cooking different dishes at the same time. They work independently, so even if one chef is slow, the others keep going.*

*Multithreading, on the other hand, is like one chef multitasking—stirring a pot, chopping veggies, and baking all at once. The chef (the CPU) switches between tasks quickly, giving the impression that everything is happening simultaneously, even though it's sharing the same workspace.*

In short, multiprocessing uses multiple CPUs, while multithreading shares one CPU across tasks.

![Multiprocessing vs Multithreading](https://miro.medium.com/v2/resize:fit:763/1*QiaqQ0HLT4Iy0N608A5mVA.png)

**Multiprocessing**: This involves using multiple CPUs or cores to run processes in parallel. Each process runs independently and has its own memory space. Think of it as multiple chefs working in separate kitchens on different dishes.

**Multithreading**: This involves using multiple threads within the same process to perform tasks. Threads share the same memory space but can execute parts of a program simultaneously. Imagine one chef multitasking between chopping veggies, boiling water, and seasoning a dish in one kitchen.

**How a thread works**
A thread is like a single line of instructions that a program follows to complete a specific task. Imagine a program as a recipe book, and each thread is a chef working on one recipe at a time.

Start: A thread begins at a specific point in the program and starts executing instructions one by one.
Sharing Resources: Threads within the same program share the same memory and resources, like variables or files, which makes communication between them easy.
Switching: If a thread is waiting for something (like input from a user or a file to load), the CPU can temporarily pause it and switch to another thread, keeping things efficient.
Finish: Once the thread completes its task, it stops, freeing up resources for other threads.
Threads are lightweight because they rely on the main program's memory space rather than creating their own, but this shared memory also makes them prone to issues like conflicts if multiple threads try to change the same data at once.

**Multiprocessing**

**Pros**:
- True parallelism on multi-core processors.
- Crashes in one process won’t affect others.
- Better for CPU-bound tasks (e.g., heavy computations).

**Cons**:
- Higher memory usage (each process has its own memory space).
- More overhead when creating and managing processes.
- Multithreading

**Multithreading**

**Pros**:
- Lower memory usage (threads share memory).
- Faster to create and switch between threads.
- Great for I/O-bound tasks (e.g., reading files, network calls).

**Cons**:
- Threads can interfere with each other (e.g., race conditions).
- Limited by the Global Interpreter Lock (GIL) in Python for CPU-bound tasks.
- A crash in one thread can affect the whole process.

### Fork Join Model

![Forkl Join Model](https://www.student.chemia.uj.edu.pl/~mrozek/USl/OpenMP/OpenMP_pliki/fork_join1.gif)

### Parallel Programming Practice

'Parallel Programming' Jupyter Notebook in Google Collab 

### Distributed computing 

Uses multiple processors possibly at different locations

![Distributed computing](https://www.techtarget.com/rms/onlineimages/the_distributed_computing_process-f_mobile.png)

### Spark Programming Practice

'Spark' Programming Jupyter Notebook in Google Collab 

## Apache Spark: A Beginner's Guide

Apache Spark is an open-source distributed computing system designed for big data processing and analytics. It uses in-memory computation to speed up data processing tasks and supports multiple languages like Python, Java, Scala, and SQL, making it highly versatile.

### Why Use Apache Spark?
- **Speed**: Processes data up to 100x faster than traditional systems like Hadoop due to in-memory computation.
- **Ease of Use**: Offers APIs for developers in popular programming languages.
- **Scalability**: Efficiently handles large-scale data across clusters of machines.
- **Versatility**: Supports batch processing, real-time streaming, machine learning, and graph processing.

### Limitations
- **Resource Intensive**: Requires substantial memory and compute resources.
- **Complexity**: Learning curve for beginners due to its distributed nature and ecosystem.
- **Cost**: Running Spark at scale on large clusters can be expensive.

### Common Use Cases
- **Data Analytics**: Processing and analyzing massive datasets for business intelligence.
- **Real-Time Streaming**: Handling live data streams for tasks like fraud detection or real-time dashboards.
- **Machine Learning**: Building scalable machine learning models with its MLlib library.
- **ETL Pipelines**: Extracting, transforming, and loading (ETL) data for data warehouses.

## Spark SQL: A Beginner's Guide

Spark SQL is a module of Apache Spark that allows users to query structured data using SQL (Structured Query Language). It integrates seamlessly with Spark's other modules and can process data from various sources like JSON, Parquet, Hive, and JDBC databases.

### Why Use Spark SQL?
- **Unified API**: Combines SQL queries with Spark's other APIs for advanced analytics.
- **Performance**: Uses Spark's distributed engine for faster query execution on large datasets.
- **Compatibility**: Works with existing BI tools and supports standard SQL syntax.
- **Data Source Flexibility**: Reads and writes data from diverse sources, including cloud storage, databases, and distributed file systems.

### When to Use Spark SQL Over MySQL
- **Large-Scale Data**: Spark SQL is better suited for analyzing terabytes or petabytes of data, whereas MySQL struggles with such volumes.
- **Distributed Processing**: If the workload requires parallel processing across multiple nodes, Spark SQL is the ideal choice.
- **Complex Workflows**: When combining SQL with advanced data processing tasks like machine learning, Spark SQL offers seamless integration.
- **Batch and Streaming Data**: Use Spark SQL for scenarios involving both static and real-time data.

### Limitations
- **Resource Heavy**: Requires significant hardware resources compared to MySQL.
- **Higher Setup Complexity**: Setting up and maintaining a Spark cluster can be challenging.
- **Not Ideal for Small Data**: For small datasets and simple queries, MySQL or similar databases are more efficient.

### Common Use Cases
- **Big Data Analytics**: Querying massive datasets stored in distributed systems like Hadoop or cloud storage.
- **Data Lakes**: Providing SQL capabilities on top of semi-structured and unstructured data.
- **ETL Pipelines**: Transforming and querying large-scale data before moving it into data warehouses.
- **Real-Time Analytics**: Running SQL queries on streaming data for real-time insights.

