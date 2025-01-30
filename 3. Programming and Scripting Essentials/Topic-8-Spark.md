# Topic 8 - Spark - 30/01/2025

## Data Pipelines Essentials 

### Using SparkSQL in data pipelines

SparkSQL allows you to perform SQL-like queries on large datasets, making it a powerful tool for constructing data pipelines. It integrates seamlessly with Spark’s core, enabling efficient data manipulation and transformation. The code example below demonstrates a simple data pipeline that reads JSON data, transforms it using SQL, and writes the output to a Parquet file. 

*Hive Data is probably new to you at this point. Hive refers to the data stored in Apache Hive, a data warehouse software that facilitates reading, writing, and managing large datasets residing in distributed storage using SQL.
In Spark, a DataFrame can be created from Hive data by connecting to the Hive metastore, allowing users to query and manipulate Hive tables as Spark DataFrames for efficient data processing and analytics.*

**Implementation with SparkSQL**

**Data integration**

- One of the primary strengths of SparkSQL is its ability to seamlessly integrate with various data sources. 

- This feature allowed the HR department to consolidate employee data from multiple systems into a unified view, making it easier to manage and analyse.

- **Feature utilised**: Data Source Integration

- **Why Chosen**: Provides a unified platform for accessing and analysing data from diverse sources, eliminating data silos and improving data consistency.

**Real-time analytics**

- SparkSQL's ability to perform real-time queries enabled the HR department to generate up-to-the-minute reports. 

- This capability was crucial for tasks such as monitoring employee attendance, tracking performance metrics, and identifying trends in workforce demographics.

- **Feature utilised**: Real-Time Querying

- **Why chosen**: Ensures that HR decisions are based on the most current available, enhancing responsiveness and strategic planning

**Scalability and performance**

- Handling large datasets efficiently is a core strength of SparkSQL. 

- The HR department needed a solution that could scale with the organisation's growth, accommodating increasing volumes of employee data without compromising performance.

- **Feature utilised**: Scalability and optimisation
- 
- **Why chosen**: Enables the system to handle large-scale data with high performance, ensuring timely and efficient data processing.

**User-friendly interface**

- By using SparkSQL, the HR staff could write queries in familiar SQL syntax, simplifying the process of data analysis. This user-friendly approach allowed non-technical HR personnel to generate reports and insights without relying on the IT department.
  
- **Feature utilised**: SQL Syntax Support
  
- **Why Chosen**: Makes data querying accessible to users with basic SQL knowledge, empowering HR staff to independently analyse data.

## Spark Streaming

![Spark streaming](https://spark.apache.org/docs/latest/img/streaming-arch.png)

Real-time data processing is essential in several scenarios, such as:

1. Financial fraud detection: Monitoring transactions as they happen to flag suspicious activities.

2. Real-time analytics: Providing up-to-the-minute analytics for websites, mobile apps, or IoT devices.

3. Alerting systems: Generating alerts based on real-time data changes, such as stock price fluctuations or temperature spikes in a sensor network.

```python
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working threads and batch interval of 5 seconds
sc = SparkContext("local[2]", "Minimal Spark Streaming App")
ssc = StreamingContext(sc, 5)  # 5-second batch interval

# Define the data source - a socket stream on localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

# Perform simple processing: Count the words in each RDD
word_counts = lines.flatMap(lambda line: line.split(" ")) \
                    .map(lambda word: (word, 1)) \
                    .reduceByKey(lambda a, b: a + b)

# Print the results to the console
word_counts.pprint()

# Start the streaming context and wait for termination
ssc.start()  
ssc.awaitTermination()
```

**Explanation**:
- **SparkContext**: Core object for Spark functionality.
- **StreamingContext**: Handles streaming data processing.
- **socketTextStream("localhost", 9999)**: Connects to the socket server to read input data.
- **flatMap, map, and reduceByKey**: Standard Spark transformations to process data.
- **pprint()**: Displays the processed results.
- **start() and awaitTermination()**: Control the execution of the streaming job.


### Understanding the flow of time is streaming

In streaming applications, data flows in continuously, and time is a critical factor. Unlike batch processing, which handles data at rest, streaming processes data in motion. Time in streaming can be understood in two contexts:

1. **Event time** - The time at which the event occurred, such as the timestamp on a transaction.

2. **Processing time** - The time at which the event is processed by the system.

*Maintaining the distinction between event time and processing time is crucial for accurate analysis, especially in scenarios like fraud detection where timing can affect the outcome.*

### Definitions of real-time and near-real-time

To understand the flow of time in data streaming a little better let's briefly explore the definitions of real-time and near real-time. What do these terms mean? Here's how a number of well-known companies define these terms:

**Real-time**
- **IBM**: Immediate or almost immediate processing of data upon arrival, within milliseconds.
- **TechTarget**: Continuous input and processing of data, yielding results with negligible latency, typically within milliseconds
- **Microsoft Azure**: Processing and analysing data as soon as it is generated, usually within milliseconds to a few seconds.
- **Informatica**: Processing data as it is received, with minimal delay, usually within milliseconds.

**Near real-time**
- **Microsoft**: Data processing that occurs within a few seconds to minutes.
- **Informatica**: Handling data with minimal delay, typically within seconds to minutes.
- **AWS**: Processing data with a slight delay, usually within seconds to a few minutes.
- **Confluent**: Near-real-time systems aim for processing within seconds to a few minutes, balancing immediacy with processing overhead.

### Batching and microbatching

Spark Streaming primarily uses microbatching to process data streams. Here's how it works:

![spark streaming micro batch](https://meritis.fr/wp-content/uploads/2019/01/1_Spark_streaming_presentation.jpg)

**Batching**

Traditional batch processing involves collecting a large volume of data over a period and then processing it as a single batch. 

This approach is suitable for periodic reports and bulk processing but falls short for real-time applications.

**Microbatching**

Spark Streaming divides incoming data into small batches, called microbatches, which are processed at short, regular intervals (e.g., every second). 

This method provides a balance between real-time processing and the efficiency of batch processing.

**Batching example**

`Data is received continuously from a source (e.g., financial transactions). Every second, the data collected in that second is grouped into a microbatch. Each microbatch is processed and analysed immediately, enabling near real-time insights.`

### Windowing

Windowing is a technique used to aggregate and analyse data over a specified time window, which can be either time-based or count-based. It allows us to handle continuous streams of data more effectively by breaking them into manageable chunks, such as:

1. **Time-based windows** - Group data based on time intervals, such as every 5 minutes or every hour.

2. **Count-based windows** - Group data based on the number of events, such as every 100 transactions.

**Types of windows**

**Turning windows**

Fixed-size, non-overlapping windows. Each event belongs to one window.

**Sliding windows**

Fixed-size, overlapping windows. Events can belong to multiple windows.

**Session windows**

Windows defined by periods of activity separated by inactivity. Useful for session-based analysis.

Here is a simple Spark Streaming example that demonstrates windowing to aggregate transaction data:

```python
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create Spark Context and Streaming Context with 2-second batch interval
sc = SparkContext("local[2]", "Windowed Transaction Aggregation")
ssc = StreamingContext(sc, 2)

# Set a checkpoint directory (necessary for window operations)
ssc.checkpoint("checkpoint")

# Simulated transaction data stream (from localhost socket)
transactions = ssc.socketTextStream("localhost", 9999)

# Parse transactions as (customer_id, transaction_amount)
parsed_transactions = transactions.map(lambda line: line.split(",")) \
                                   .map(lambda parts: (parts[0], float(parts[1])))

# Aggregate the transaction amounts over a 10-second window, sliding every 4 seconds
windowed_sums = parsed_transactions.reduceByKeyAndWindow(
    lambda a, b: a + b,  # Reduce function
    lambda a, b: a - b,  # Inverse reduce function (for performance optimization)
    windowDuration=10,   # Window length
    slideDuration=4      # Slide interval
)

# Print the aggregated transaction amounts
windowed_sums.pprint()

# Start the streaming context and wait for termination
ssc.start()
ssc.awaitTermination()

```

**How It Works**:

1. **Data Stream**:

  The input stream expects data in the format customer_id,transaction_amount (e.g., 101,50.0). This is read through a socket stream on port 9999.

2. **Windowed Aggregation**:

- **Window Duration** (10 seconds): Defines how much historical data is aggregated in each window.

- **Sliding Interval** (4 seconds): How frequently the window slides forward to form the next aggregation.

3. **Reduce Function** (lambda a, b: a + b):

  Combines transaction amounts for each customer within the window.

4. **Inverse Function** (lambda a, b: a - b):
  Efficiently removes old values when the window slides to avoid recomputation.

### Timescales in transformations

When processing streams, various transformations can be applied to the data to derive insights and perform analytics. The timescales involved in these transformations can vary depending on the nature of the analysis, including:

1. **Immediate transformations**: Simple transformations that are applied as soon as the data arrives, such as filtering out transactions over a certain amount.

2. **Short-term aggregations**: Aggregations over short time windows, such as counting the number of transactions in the last 5 minutes.

3. **Long-term trends**: Analysing data over longer periods to identify trends, such as weekly or monthly transaction patterns.

*Each transformation has different latency requirements and processing complexities, and Spark Streaming’s microbatching model accommodates these needs by processing data in near real-time.*

### How Spark Streaming works

Spark Streaming processes data in a continuous, scalable, and fault-tolerant manner. 

Here's a step-by-step overview of its operation:

1. **Data ingestion**: Data is ingested from various sources such as Kafka, HDFS, or sockets.

2. **Microbatching**: The incoming data is divided into small, fixed-duration batches.

3. **Processing**: Each batch is processed using Spark's core APIs, applying transformations and actions.

4. **Output**: The processed data is then written to external systems like databases, dashboards, or file systems for further analysis or immediate action.

*By leveraging Spark's robust processing engine and the microbatching technique, Spark Streaming can handle high-throughput, low-latency data streams efficiently.*

---

## Lecture

### DevOps and CI/CD

**Benefits**
1. Reduced Risk
2. Shorter review time
3. Better code quality
4. Faster bug fixes
5. Measurable progress
6. Faster feedback loops
7. Increased collaboration

### Continuous Integration (CI) - Code creation 

- Merging code frequently 
- Automate processes

**CI best practices**
1. Maintain a code repo
2. automate the build
3. Self-testing
4. Commit daily
5. Build every commit
6. Every bug has a test
7. Builds should be fast
8. Life-like test environments
9. Easy to get deliverables
10. Transparent build results
11. Automate deployment

### Continuous Delivery (CD) - Push and deployment

- Always having a releasable product
- Developing in short cycles
- Always having built and tested software

![CI/CD](https://cms-cdn.katalon.com/banner_5_c080182c13.png)

### Containerisation

Packaging software, so it's all self contained. Like building a virtual machine

It must contain:
- The code
- Libraries
- Runtime environment
- OS kernal

Containers are much more efficient than a lightweight container. It only takes what it needs

*Once you've created a container (image), you can run it anywhere as long as the OS has the platform*

![Container vs Virtual Machine](https://www.netapp.com/media/Screen-Shot-2018-03-20-at-9.24.09-AM_tcm19-56643.png)

### Infrastructure as Code (IaC)

Treating infrastructure in the same way as we would code

We use **Terraform** for this.

- Source controlled
- Can be configured
- Can be automated

**Benefits**
- Speed
- Cost

---

### Docker and Kubernetes

**Docker**

Containerisation tool. Platform as a service

Integrates with python

![Docker](https://docs.docker.com/get-started/images/docker-architecture.webp)

## **Docker for Beginners**

### **What is Docker?**
Docker is a tool that allows you to package your application and its dependencies into containers. Containers are lightweight environments that run the same everywhere.

---

### **Benefits of Docker**
- **Consistency:** Solve the "It works on my machine" problem.
- **Portability:** Run containers on any system with Docker installed.
- **Efficiency:** Faster and lighter than virtual machines.
- **Isolation:** Each container is independent.

---

### **How Docker Works**
- **Docker Image:** Blueprint for a container with all application files and dependencies.
- **Docker Container:** Running instance of a Docker image.
- **Dockerfile:** Instructions for building a Docker image.

---

### **Simple Python Container Example**

#### **Step 1: Create a Python Application**
Create a file named `app.py` with the following content:
```python
print("Hello from Docker!")
```
``` bash
docker build -t hello-docker .

docker run hello-docker
```

**Expected output** "Hello from Docker!"

**Summary**

**Dockerfile**: Describes the container setup.

**docker build**: Creates a Docker image from the Dockerfile.

**docker run**: Runs the application inside the container.

This setup shows how easy it is to containerize a simple Python app.

---

## Kubernetes

![Kubernetes](https://cdn.prod.website-files.com/5ff66329429d880392f6cba2/673f4107a915916cd43fbdf8_646786e5646162c532696293_661.2.jpeg)

### **What is Kubernetes?**
Kubernetes (K8s) is a platform for automating the deployment, scaling, and management of containerized applications. It organizes containers into logical units called **pods** (think of a pod of whales) and ensures they run reliably across different environments.

---

### **Benefits of Kubernetes**
- **Scalability:** Automatically scale applications up or down.
- **Self-healing:** Restart failed containers and maintain desired states.
- **Load balancing:** Efficiently distribute traffic to containers.
- **Portability:** Works across cloud providers and on-premise systems.

---

### **How Kubernetes Works**
- **Pod:** The smallest deployable unit in Kubernetes, often containing one or more containers.
- **Service:** Exposes pods to other services or external traffic.
- **Deployment:** Describes how to deploy and maintain pods.

---

### **Simple Python Kubernetes Example**

#### **Step 1: Create a Simple Python Application**
Create a file named `app.py`:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

#### Step 2: Write a Dockerfile
``` Dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Install dependencies
RUN pip install Flask

# Copy the app code
COPY app.py .

# Expose the container port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
```

### Step 3: Build and Push the Docker Image
``` bash
docker build -t your-docker-username/k8s-example:latest .
docker push your-docker-username/k8s-example:latest
```

#### Step 4: Create Kubernetes Deployment and Service Files
**deployment.yaml**
``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-app
  template:
    metadata:
      labels:
        app: python-app
    spec:
      containers:
      - name: python-app
        image: your-docker-username/k8s-example:latest
        ports:
        - containerPort: 5000
```

**service.yaml**
``` yaml
apiVersion: v1
kind: Service
metadata:
  name: python-app-service
spec:
  type: LoadBalancer
  selector:
    app: python-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
```

#### Step 5: Apply Kubernetes Configurations
``` bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

#### Step 6: Access the application
``` bash
kubectl get services
```

**Summary**

**deployment.yaml**: Defines the application deployment in Kubernetes.

**service.yaml**: Exposes the app to external traffic.

**kubectl apply**: Deploys the application to the Kubernetes cluster.

---

### Practice Notebook L5DE_M3_t9.ipynb in Google Collab

## Reflections

Use Lazy classifier in python for a quick ML model 




