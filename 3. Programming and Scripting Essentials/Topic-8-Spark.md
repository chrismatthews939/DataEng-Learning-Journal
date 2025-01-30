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

