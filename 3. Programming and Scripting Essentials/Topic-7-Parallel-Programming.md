# Topic 7 - Parallel Programming - 23/01/2025

## First All Day Hackathon Session

### Big O Notation Practice

L5DE M3T6 Jupyter Notebook in Google Collab for Big O Notation

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

Parallel Programming Jupyter Notebook in Google Collab 



