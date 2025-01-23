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

### Understanding `map` vs `flatMap` in Apache Spark

Both `map` and `flatMap` are transformation operations in Apache Spark that apply a function to each element of an RDD (Resilient Distributed Dataset). While they seem similar, they behave differently in terms of the output structure.

### `map`
The `map` transformation applies a function to each element of an RDD and returns a new RDD where **each input element corresponds to exactly one output element**.

#### Example:
If you have a list of numbers `[1, 2, 3]` and apply `map` to multiply each number by 2, you get `[2, 4, 6]`.

```python
data = [1, 2, 3]
rdd = spark.sparkContext.parallelize(data)
mapped_rdd = rdd.map(lambda x: x * 2)  # Output: [2, 4, 6]
```

## Spark Broadcast Variables

### What Are They?
Broadcast variables in Apache Spark are a way to share data with all the worker nodes in your cluster without sending it repeatedly. Imagine you have a small list, like a table of country codes and their names, that every task needs to use. Instead of sending this list every time a task runs, Spark can send it once and store it on each worker node. This makes your program faster and more efficient.

*Bascially like caching*

### Why Use Broadcast Variables?
1. **Efficiency**: Avoids sending the same data multiple times with each task, reducing network overhead.
2. **Speed**: Accessing broadcast data is faster since it is stored locally on the worker nodes.

### Limitations
- Broadcast variables are **read-only**, meaning you cannot modify their value once they are broadcast.
- The size of the data that can be broadcast depends on the cluster's memory; broadcasting very large data can lead to memory issues.

### Common Use Cases
1. Distributing small to medium-sized lookup tables to worker nodes for joins or filtering.
2. Sharing configuration data or constants across all tasks.
3. Improving performance when the same data is used repeatedly in transformations.

## Spark SQL: A Beginner's Guide

*MySQL needs a database and schema. Spark is more flexible*

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


![Sparksql vs Mysql](https://i.sstatic.net/NkrUy.png)


**Link for SQL in Spark training notebook**
https://eur02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1fa2G3YuXx3Isqyby5kFETqmWotFwtqlH&data=05%7C02%7Cchristopher.matthews%40ee.co.uk%7C632bf4016f524ff94c1408dd3bc694bd%7Ca7f356889c004d5eba4129f146377ab0%7C0%7C0%7C638732446255387705%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=UuRltfSGKrE9G9oxF%2BNYAvDmLEifKSEw%2BJOrfU5rz%2FM%3D&reserved=0

## E-Learning

## Paralell Programming

The asyncio library allows for concurrent code execution using the async/await syntax. It handles asynchronous operations, enabling programs to perform multiple tasks simultaneously without waiting for each to complete sequentially. This is particularly useful for I/O-bound and network code. 

## Performance and deployment considerations
