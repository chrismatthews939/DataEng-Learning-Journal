# Topic 2 - Data pipeline workflow management 19/06/2025

# Principles of workflow management

**Why workflow management matters**
- Lost revenue
- Operational bottlenecks
- Damaged reputation
- Unexpected costs

### Benefits

- **Dependency tracking**
  - Ensuring tasks run in the correct order.

- **Error handling and retries**
  - Dealing gracefully with failures.

- **Logging and observability**
  - Seeing what’s working and what’s not.

- **Modularity and reusability**
  - Designing workflows that can evolve with your needs.

---

# Five Core Principles of Workflow Management in Data Engineering

1. **Define task boundaries clearly**
Each step should have a clear input and output. This makes your pipeline easier to debug, optimise, and reuse.

2. **Use dependency-driven execution**
Use tools that understand task dependencies, not just time-based triggers. This is where DAG-based systems shine.

3. **Design for failure**
Don’t assume success. Build in retries, alerts, and contingencies to reduce pipeline fragility.

4. **Centralise logging and monitoring**
Without visibility, workflows can silently fail. Use a consistent logging approach to make every step traceable.

5. **Keep it modular**
Complex workflows are easier to manage when broken into smaller, reusable units. This also supports collaboration and testing.

Understanding workflow management is essential for anyone starting in data engineering. Workflows are the series of tasks that move data from source to destination, clean it, transform it, and prepare it for analysis or use in applications. Efficient workflow management ensures that this process is reliable, scalable, and maintainable.

Below are the **five core principles** of workflow management in data engineering, explained in beginner-friendly terms.

---

## 1. **Orchestration**

**What it means:**  
Orchestration is the process of organizing and coordinating all the steps in a data workflow. Think of it like a conductor guiding an orchestra — making sure each instrument (task) plays at the right time.

**Why it's important:**  
Without orchestration, tasks might run in the wrong order, crash into each other, or overload systems.

**Example tools:**  
Apache Airflow, Prefect, Dagster

---

## 2. **Scheduling**

**What it means:**  
Scheduling determines **when** each task or workflow should run — whether it's every hour, once a day, or triggered by some event.

**Why it's important:**  
Running tasks at the right time ensures data is fresh and systems aren’t overloaded.

**Example use case:**  
Running a job every night to update a sales dashboard with the latest numbers.

---

## 3. **Dependency Management**

**What it means:**  
Some tasks rely on others to finish before they start. Dependency management ensures tasks run in the correct order.

**Why it's important:**  
It prevents errors like trying to use data before it’s ready.

**Example:**  
You can’t calculate daily revenue until you've finished importing the day’s sales data.

---

## 4. **Monitoring and Alerting**

**What it means:**  
Monitoring watches workflows to make sure they run correctly. Alerting notifies engineers when something goes wrong.

**Why it's important:**  
You need to know **immediately** if a workflow fails so you can fix it before users or downstream systems are affected.

**Example:**  
An email or Slack message if a critical job fails to run.

---

## 5. **Scalability and Reliability**

**What it means:**  
Workflows should be able to handle increasing amounts of data without breaking (scalability), and they should run successfully every time (reliability).

**Why it's important:**  
As data grows, your systems must keep up — and do so consistently.

**Example:**  
A workflow that handles 1GB of data today should also work for 100GB in the future with little to no changes.

---

## Summary

| Principle              | Purpose                                                  |
|------------------------|----------------------------------------------------------|
| **Orchestration**       | Coordinates all tasks in the workflow                   |
| **Scheduling**          | Sets the timing of task execution                       |
| **Dependency Management** | Ensures tasks run in the correct order               |
| **Monitoring and Alerting** | Keeps workflows healthy and alerts on failure     |
| **Scalability and Reliability** | Ensures workflows can grow and remain stable |

By mastering these five principles, you'll be well-equipped to design and manage robust data workflows as a data engineer.

---

# Introduction to Data Engineering Workflows

Data engineering workflows are structured pipelines that move, transform, and store data. Understanding their core components and patterns is essential for building reliable and scalable data systems. This guide introduces the key **elements** and **workflow patterns** every beginner should know.

---

## 🧱 Key Elements of a Data Engineering Workflow

### 1. **Tasks**
- **Definition:** A task is a single unit of work in the pipeline (e.g., extract data from a source, transform it, load it into a destination).
- **Example:** Downloading a CSV file, running a SQL transformation, or training a machine learning model.

### 2. **Dependencies**
- **Definition:** Dependencies define the order of task execution. Task B might need to wait for Task A to complete first.
- **Purpose:** Ensures data consistency and correctness (e.g., don't load data before transforming it).

### 3. **Triggers**
- **Definition:** A mechanism that starts a workflow or a task.
- **Types:**
  - **Time-based:** Run daily at midnight.
  - **Event-based:** Start when a file lands in a data lake.
  - **Manual:** Triggered by a user.

### 4. **State**
- **Definition:** The status of a workflow or task at a specific moment (e.g., `success`, `failed`, `running`, `skipped`).
- **Use Case:** Helps with recovery, retries, and debugging.

### 5. **Observability**
- **Definition:** Tools and practices for monitoring workflows.
- **Includes:**
  - **Logging:** Record events and errors.
  - **Metrics:** Measure performance and frequency.
  - **Alerts:** Notify teams when failures occur.

---

## 🔁 Common Workflow Patterns

Understanding these patterns will help you recognize and design robust workflows.

### 1. **Linear Chains**
- **Structure:** A → B → C
- **Use Case:** When tasks must run in strict order.
- **Example:** Ingest → Clean → Load

### 2. **Fan-Out**
- **Structure:** A → [B, C, D]
- **Use Case:** One task branches into multiple parallel tasks.
- **Example:** After loading raw data, start parallel enrichment jobs.

### 3. **Fan-In**
- **Structure:** [B, C, D] → E
- **Use Case:** Combine results from parallel tasks into one downstream task.
- **Example:** Wait for three data sources to finish before combining and reporting.

### 4. **Conditional Branching**
- **Structure:** A → (if condition X → B, else → C)
- **Use Case:** Choose task paths based on a condition.
- **Example:** If a file exists, process it; otherwise, skip.

### 5. **Sensor-Driven (Event-Driven)**
- **Structure:** A → wait for event → B
- **Use Case:** Task B starts only when a condition or external event is met.
- **Example:** Start ETL when a file lands in S3 or a table is updated.

---

## ✅ Summary

| Element | Description |
|--------|-------------|
| **Tasks** | Individual units of work |
| **Dependencies** | Execution order and prerequisites |
| **Triggers** | Start mechanisms (time, event, manual) |
| **State** | Tracks task/workflow status |
| **Observability** | Monitoring, logging, alerting |

| Pattern | Description | Example Use Case |
|--------|-------------|------------------|
| **Linear Chain** | Sequential tasks | Basic ETL |
| **Fan-Out** | One-to-many tasks | Parallel enrichments |
| **Fan-In** | Many-to-one tasks | Aggregating results |
| **Conditional Branching** | Tasks based on logic | File check → process or skip |
| **Sensor-Driven** | Wait for event to proceed | File arrives → start |

---

## Basic workflow in Airflow Pseudocode

```python
with DAG("daily_sales_summary", schedule_interval="0 6 * * *") as dag:

    extract = PythonOperator(task_id="extract_data", python_callable=extract_func)
    clean = PythonOperator(task_id="clean_data", python_callable=clean_func)
    summarise = PythonOperator(task_id="calculate_summary", python_callable=summarise_func)
    load = PythonOperator(task_id="load_dashboard", python_callable=load_func)

    extract >> clean >> summarise >> load
```

---

# Workflow Orchestration Tools 

## What Is Workflow Orchestration?

**Workflow orchestration** is the process of managing and automating a sequence of tasks or jobs. Think of it like a **conductor of an orchestra**—it ensures each instrument (task) plays at the right time and in the right order.

In the world of technology, especially in **data engineering**, **DevOps**, and **software development**, there are often many steps that must be executed in sequence or in parallel. Workflow orchestration tools help manage these steps, handle errors, and ensure everything runs smoothly.

---

## Why Do We Need Workflow Orchestration Tools?

- Define workflows using code or configuration (usually Python or YAML).
- Schedule tasks to run at specific times or when triggered by an event.
- Manage dependencies so tasks run only when prerequisites are complete.
- Retry on failure or send alerts if things go wrong.
- Provide visual dashboards for monitoring task status, logs, and history.
- Track state, so workflows resume gracefully if interrupted.

Imagine this scenario:

1. You collect data from a website.
2. You clean the data.
3. You save it to a database.
4. You run reports on the data.
5. You send the results via email.

Instead of running each step manually, a workflow orchestration tool can:

- Automate the entire process
- Retry failed steps automatically
- Notify you if something goes wrong
- Run tasks on a schedule (e.g., daily at 8AM)

---

## Common Features of Orchestration Tools

- **Scheduling:** Run workflows at specific times or intervals.
- **Dependency Management:** Only run step B after step A finishes successfully.
- **Monitoring & Logging:** See what’s running, failed, or completed.
- **Retries:** Automatically try again if something fails.
- **Alerts:** Get notified via email, Slack, etc., if something goes wrong.

---

## Popular Workflow Orchestration Tools

### 1. **Apache Airflow**

- **Best for:** Data pipelines and ETL workflows.
- **How it works:** You write workflows in Python as "DAGs" (Directed Acyclic Graphs).
- **Strengths:** Highly customizable, great for complex dependencies.
- **Downsides:** Requires setup and knowledge of Python.

> Example Use Case: A data engineer runs daily data extraction, transformation, and loading (ETL) jobs using Airflow.

---

### 2. **Prefect**

- **Best for:** Data workflows with more flexibility than Airflow.
- **How it works:** You write workflows in Python, similar to Airflow, but with a focus on simplicity.
- **Strengths:** Easier to use than Airflow, supports dynamic workflows.
- **Downsides:** Still evolving, requires cloud service for some features.

> Example Use Case: Automating both data pipelines and ML model training jobs.

---

### 3. **Luigi**

- **Best for:** Pipelines with strong dependency management needs.
- **How it works:** Also Python-based; focuses heavily on dependency resolution.
- **Strengths:** Simple to start, good for batch workflows.
- **Downsides:** Less feature-rich UI and ecosystem compared to Airflow.

> Example Use Case: Processing a sequence of batch jobs that must be done in order.

---

### 4. **Dagster**

- **Best for:** Data-aware workflows and development-focused environments.
- **How it works:** You define data pipelines with strong typing and testing features.
- **Strengths:** Developer-friendly, built for modern data teams.
- **Downsides:** Newer, smaller community than Airflow or Prefect.

> Example Use Case: Developing well-tested and modular data workflows in a data science team.

---

### 5. **Argo Workflows**

- **Best for:** Kubernetes-native environments.
- **How it works:** You define workflows as YAML files and run them as Kubernetes jobs.
- **Strengths:** Cloud-native, works well in containerized environments.
- **Downsides:** Requires knowledge of Kubernetes and YAML.

> Example Use Case: Running machine learning workflows on Kubernetes using Docker containers.

---

## How to Choose the Right Tool?

| Feature              | Airflow     | Prefect     | Luigi       | Dagster     | Argo        |
|----------------------|-------------|-------------|-------------|-------------|-------------|
| Language             | Python      | Python      | Python      | Python      | YAML        |
| Easy to Learn        | ❌          | ✅           | ✅           | ✅           | ❌          |
| Best for Data Tasks  | ✅           | ✅           | ✅           | ✅           | ✅           |
| Cloud-Native         | ❌          | ✅           | ❌          | ✅           | ✅           |
| UI for Monitoring    | ✅           | ✅           | Limited     | ✅           | ✅           |

---

## Final Thoughts

If you're just starting out:

- Try **Prefect** or **Dagster** for Python workflows—they're easier to learn.
- Use **Airflow** if you're working in a company or team that already uses it.
- Choose **Argo Workflows** if you're working with **Kubernetes**.
- Pick **Luigi** for simple pipelines that need strong task dependencies.

No matter which tool you choose, understanding **how workflows run**, **how tasks depend on each other**, and **how to handle failures** is the most important part.

---

## Next Steps

1. **Pick one tool** to experiment with (start with Prefect or Airflow).
2. **Try a simple project**, like automating a daily report.
3. **Read the docs** of the tool you choose—each has great beginner tutorials.
4. **Practice scheduling, logging, and failure handling.**

---

# Workflow Optimisation: 

Optimising workflows is about making processes faster, more efficient, and cost-effective. Below are three key techniques commonly used in software systems and cloud computing to achieve this, explained in simple terms for beginners.

---

## 1. Parallelism and Concurrency

### What it is:
Parallelism and concurrency are ways to perform multiple tasks at the same time.

- **Concurrency** is about handling multiple tasks that *can* be in progress at the same time, but not necessarily executed *exactly* at the same time. Think of a single waiter managing several tables — switching between tasks quickly.
  
- **Parallelism** is doing multiple tasks *literally* at the same time, like having multiple waiters each handling their own table at once.

### Benefits:
- Speeds up processing time.
- Makes better use of available resources (e.g., CPUs or cloud instances).
- Useful for large data sets or high-volume systems.

### Trade-offs:
- More complex code and system design.
- Requires careful management to avoid bugs like race conditions (where multiple tasks interfere with each other).
- Not all tasks can be parallelised (e.g., steps that depend on each other).

---

## 2. Caching Results

### What it is:
Caching means storing the results of a task so they can be reused later without repeating the work.

For example, if you look up the weather and save the result for 10 minutes, you don’t need to check it again during that time — you use the cached value.

### Benefits:
- Reduces response time dramatically.
- Saves computational resources.
- Improves user experience with faster results.

### Trade-offs:
- Cached data can become outdated (stale), leading to incorrect results if not refreshed carefully.
- Requires strategies to invalidate or refresh the cache at the right time.
- Can take up memory or storage space.

---

## 3. Strategically Scaling Resources

### What it is:
Scaling means adjusting the number of resources (like servers or CPU cores) based on workload.

- **Vertical scaling** means giving a single server more power.
- **Horizontal scaling** means adding more servers to share the load.

Scaling can be **manual** (you decide when and how) or **automatic** (the system adjusts by itself based on rules or demand).

### Benefits:
- Helps manage spikes in demand smoothly.
- Saves money by using only what you need.
- Keeps performance consistent even under heavy load.

### Trade-offs:
- More servers mean more complexity in networking and coordination.
- Auto-scaling can sometimes respond too slowly or overshoot needs.
- There can be a cost trade-off — scaling up may be more expensive if not carefully managed.

---

## Summary Table

| Technique                  | Benefit                          | Trade-Off                           |
|---------------------------|----------------------------------|-------------------------------------|
| Parallelism & Concurrency | Faster processing                | Complex implementation, bugs        |
| Caching                   | Instant results, reduced load    | Risk of outdated data               |
| Scaling Resources         | Handles demand efficiently       | Cost and infrastructure complexity  |

---



