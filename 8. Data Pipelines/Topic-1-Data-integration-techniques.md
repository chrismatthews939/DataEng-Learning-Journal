# Topic 1 - Data integration techniques 12/06/2025

# Limitations of traditional ETL

When designing data pipelines today, it’s important to understand where traditional ETL begins to fall short. ETL - Extract, Transform, Load - was built with a batch mindset. It typically involves scheduled jobs that move data from source systems into a central repository, performing heavy transformations along the way.

## Key limitations of ETL process

1. **Latency**
   - ETL pipelines are often built around scheduled batch jobs - hourly, nightly, or even weekly. This makes them poorly suited to use cases that depend on real - time or near - real - time data, such as fraud detection, recommendation systems, or operational dashboards. Modern data pipelines, especially streaming ones, must support continuous flow - not periodic snapshots.
     
2. **Rigid architecture**
    - Traditional ETL pipelines typically define fixed stages with tightly coupled steps. This makes them hard to adapt to schema changes, new data sources, or changes in business logic. In contrast, data pipelines benefit from modularity and dynamic orchestration - features not easily achieved in classic ETL stacks.
3. **Centralised transformation bottlenecks**
   - In ETL, data is often transformed before being loaded, which can cause performance bottlenecks and reduce reusability of raw data. Modern pipelines often favour an ELT or stream-first model - where data is ingested quickly and transformations are applied later or incrementally, supporting parallel processing and on - demand transformation.
4. **Poor Support for Unstructured and Semi - Structured Data**
   - ETL tools were designed for structured relational data. But data pipelines today must handle JSON, logs, images, clickstreams, and other complex formats. ETL often struggles with flexibility, whereas modern pipelines can be built to accommodate varied and unpredictable data structures.
5. **Difficult to Scale and Monitor**
   - Traditional ETL tools may not be built for horizontal scalability or distributed processing. They often lack native support for fault tolerance, retry logic, or observability - all essential characteristics of modern, production - grade data pipelines.

---

# Modern data integration

When you build a pipeline today, you're not just stitching together systems - you're building bridges across constantly shifting ground. APIs evolve. Data formats change. Teams demand answers faster. The traditional ETL model says: “Move everything, transform it, then report on it.”Modern pipelines ask instead: “What’s the lightest, fastest way to get the right data where it needs to be?” Let’s explore four answers to that question.

### Data Federation: Access Without Movement

Imagine you could reach into three different systems - without ever copying their data - and query them as one. That’s the essence of data federation: it enables your pipeline to query multiple backends as though they were one source.


- **Great for:** real-time reporting, operational dashboards
- **Watch out for:** performance bottlenecks if sources are slow or unavailable

### Data virtualisation: Creating a unified view

**Data virtualisation** provides a consistent schema over disparate systems. It's not just about access - it's about **abstraction**. This is your pipeline’s way of saying: “No matter how messy the sources are, I’ll present clean columns downstream.” Often used in tandem with semantic layers or governed data platforms, virtualisation supports reusability across teams without replicating storage.

### Data blending: Lightweight, purpose-built integration

Where virtualisation offers abstraction, blending focuses on **fast combinations**. This is the integration approach you use when your pipeline is pulling together data for a specific purpose - say, a marketing report or an ad spend dashboard - and you don’t need a perfect schema match.

### ELT: Ingest Now, Transform Later

Sometimes the best pipeline strategy is speed. ELT - Extract, Load, Transform -  flips the traditional model: it gets the data into your platform first, then applies transformations once it's safely there. It’s fast, cost-effective, and cloud-native. Here's why it matters for pipelines:

- Reduces latency between collection and storage
- Allows transformations to be versioned and decoupled from ingestion
- Scales well with columnar stores like Snowflake, BigQuery, Redshift

# Real-time and streaming data integration

As data becomes more dynamic and time-sensitive, the way we process it must evolve. Traditional batch processing—once the backbone of data workflows—is no longer fast or flexible enough for many modern use cases. Today, organisations are shifting towards streaming and micro-batching models that enable real-time insights and responsive systems. This section explores how and why that shift is happening, and what it means for designing modern data pipelines.

### Batch

Data is collected over time, then processed in bulk.

**Pro:** Good for historical analysis, low-latency use cases.

**Con:** Poor for real-time insights or immediate action.

### Streaming

Data flows continuously, event-by-event, through the pipeline.

**Pro:** Enables low-latency decision-making, live dashboards, and responsive automation.

**Con:** Requires careful design: state man

### Micro Batching

A hybrid: mini-batches processed rapidly in intervals (e.g., every few seconds)

Lower complexity than pure streaming.

Supported by tools like Spark Structured Streaming.

## What does a streaming pipeline look like?

A typical streaming data pipeline includes:

- **Event Sources:** Where the data originates (e.g., Kafka, Kinesis, IoT devices)
- **Stream Processor:** Where logic is applied in-flight (e.g., filtering, joining, enriching via Flink, Spark Streaming)
- **Sink:** Where the data lands (e.g., data lake, real-time dashboard, alert system)

![Streaming pipeline](https://hpe-developer-portal.s3.amazonaws.com/uploads/media/2020/12/example-streamline-processing-pipeline-1610604239860.png)

Real-time pipelines are crucial when:

- **Speed equals value:** e.g., fraud detection, stock trading, alert systems
- **Continuous data sources are involved:** e.g., sensors, logs, clickstreams
- **Event-driven actions are needed:** e.g., triggering notifications or workflows based on incoming data

### Streaming Challenges

- **State management:** Holding context across events (e.g., running totals, session tracking)
- **Ordering and replay:** Ensuring events arrive and are processed correctly, even with delays or retries
- **Monitoring:** Streaming pipelines need tight observability, since they run 24/7

# Architectural approaches to integration

## Option 1: Point-to-point integration

**Headline: Fast but fragile**

### Advantages

- Simple to set up

### Disadvantages

- Becomes unmanageable as systems grow.
- High risk of duplication and inconsistency.

## Option 2: Hub-and-spoke or bus architecture

**Headline: Centralised and controlled**

### Advantages

- Better control over transformation logic, monitoring, and governance.

### Disadvantages

- Can become a bottleneck or single point of failure
- Easier to track lineage and enforce schema contracts.

## Option 3: Distributed or decentralised integration

**Headline: Scalable by design**

Here, the pipeline is designed as a network of independent, loosely coupled components with the following advantages:

1. Services publish and subscribe to events (e.g., Kafka topics).
2. Data lakes and lakehouses decouple storage and compute.
3. Transformation can be pushed downstream, on-demand.

**This is the architecture of data mesh, event-driven pipelines, and cloud-native platforms.**

It’s less like a central station and more like a city-wide tram network. Each stop serves a purpose, but the system doesn’t collapse if one line pauses.

This design supports:

- Schema evolution
- Independent scaling
- Greater fault tolerance

## Design considerations for pipeline architects

As you explore integration architecture, encourage learners to think about:

- **Metadata propagation:** Can lineage, quality, and schema tags follow the data?
- **Schema management:** How does the pipeline adapt to changes in upstream format?
- **Transformation placement:** Do we transform at the source, in transit, or downstream?
- **Modularity:** Can pipeline components be swapped, updated, or scaled independently?

--

# Tooling ecosystem overview

## Data extraction and ingestion

## Apache NiFi

### What is Apache NiFi?

Apache NiFi is an open-source **data integration and workflow automation tool**. It is designed to automate the **movement and transformation of data** between systems in real-time. NiFi helps build **data pipelines** that are easy to manage and monitor through an intuitive **drag-and-drop web interface**.

At its core, NiFi provides a **visual programming model** for designing data flows. It enables users to move, route, filter, transform, and process data across different systems **without writing much code**.

---

### Key Concepts

- **FlowFile**: A FlowFile is the basic data record in NiFi. It includes the actual data (content) and a set of attributes (metadata).
- **Processor**: A component that performs a specific task such as reading a file, transforming data, or sending it to another system.
- **Connection**: A queue that connects processors and stores FlowFiles between steps in the pipeline.
- **Flow Controller**: Manages how processors and other components execute.
- **Process Group**: A container for grouping related processors to organize complex data flows.

---

### Role of NiFi in Data Pipelines

Apache NiFi is ideal for **data ingestion and flow orchestration**. It acts as a **data logistics layer**, ensuring data gets from one system to another **safely, reliably, and in the right format**.

In a typical data pipeline, NiFi sits at the **start** or **middle**:

- At the **start**, it collects data from various sources: files, APIs, databases, or message queues.
- In the **middle**, it transforms, enriches, filters, and routes data to the right destinations.
- It can also **trigger other systems** or pass data to downstream tools like Apache Kafka, databases, or cloud services.

---

### Strengths of Apache NiFi

1. **Visual Flow Design**: No coding needed to build pipelines. Use drag-and-drop components in a web UI.
2. **Real-Time and Batch Support**: Handle streaming data and batch data processing.
3. **Data Provenance**: Full visibility into where data came from, how it changed, and where it went.
4. **Extensibility**: 300+ built-in processors; custom processors can be written in Java.
5. **Built-in Security**: Supports SSL, encrypted content, user authentication, and access control.
6. **Scalability**: Can run on a single node or scale out in a cluster.
7. **Back Pressure & Prioritization**: Controls data flow when systems are overloaded.

---

### Where Apache NiFi Fits in the Pipeline

| Stage            | NiFi's Role                                  |
|------------------|----------------------------------------------|
| Data Ingestion   | Collects data from various systems           |
| Transformation   | Cleans, formats, and enriches data           |
| Routing          | Sends data to different systems based on rules|
| Monitoring       | Tracks data lineage and flow performance     |
| Delivery         | Forwards data to databases, APIs, or queues  |

---

### Common Use Cases

1. **ETL (Extract, Transform, Load)**:
   - Extract data from databases or APIs
   - Transform it using built-in processors
   - Load into data warehouses or Hadoop

2. **Real-Time Stream Processing**:
   - Ingest logs or IoT data
   - Route to Apache Kafka or Elasticsearch

3. **Cloud Migration**:
   - Move data from on-premise systems to AWS, Azure, or GCP

4. **Data Lake Ingestion**:
   - Continuously feed data lakes like Hadoop HDFS or Amazon S3

5. **API Integration**:
   - Poll REST APIs or serve data via NiFi as a REST API

6. **Log Aggregation**:
   - Collect logs from various servers and centralize them

7. **IoT and Sensor Data Collection**:
   - Ingest and process data from thousands of devices in real-time

---

### Summary

Apache NiFi is a powerful and flexible tool for **building and managing data pipelines**. Its strengths lie in ease of use, real-time capabilities, extensibility, and end-to-end data visibility. Whether you're handling **small-scale integrations** or **enterprise-wide data movement**, NiFi can be a key component in your data infrastructure.

### Other Tools

**Fivetran**, **Stitch** – Managed ELT platforms; quick setup for pulling from SaaS sources like Salesforce, Shopify

**Debezium** – Change Data Capture (CDC) from databases for real-time ingestion

---

## Streaming services

## Apache Kafka

### What Is Apache Kafka?

Apache Kafka is a **distributed event streaming platform** used to build real-time data pipelines and streaming applications. It’s designed to handle **high-throughput**, **low-latency**, and **fault-tolerant** data communication between systems.

Think of Kafka as a **central hub** where different systems can send and receive messages (called "events") in real time.

---

### Key Concepts

- **Producer**: A program that sends (produces) messages to Kafka.
- **Consumer**: A program that reads (consumes) messages from Kafka.
- **Topic**: A category or feed name to which messages are published. Think of it like a channel.
- **Broker**: A Kafka server that stores data and serves client requests.
- **Partition**: Topics are split into partitions to allow for scalability and parallel processing.
- **Offset**: A unique ID for each message within a partition, used by consumers to keep track of what they've read.

---

### Kafka’s Role in a Data Pipeline

Kafka acts as a **buffer** or **middle layer** in data pipelines, decoupling data producers from data consumers. This enables:

- Asynchronous communication (systems don’t need to wait on each other)
- Scalability (each part of the system can grow independently)
- Resilience (data is stored durably and can be replayed if needed)

**Basic pipeline flow:**

1. Data is **produced** from sources like apps, logs, or IoT devices.
2. Kafka **streams** this data to one or more topics.
3. **Consumers** (like databases, analytics engines, or dashboards) read from the topics.

---

### Strengths of Kafka

- 🔄 **Durability**: Messages are stored on disk and replicated across servers.
- ⚡ **High throughput**: Kafka can handle millions of messages per second.
- 📈 **Scalability**: Easily scales horizontally by adding more brokers and partitions.
- 🧵 **Real-time streaming**: Ideal for low-latency use cases.
- 🔌 **Decoupling**: Producers and consumers don’t need to know about each other.
- 📂 **Replayability**: Consumers can re-read data from any point in time.

---

### Where Kafka Fits in a Data Pipeline

Kafka often sits between:

- **Data Producers**: Web apps, databases, sensors, logs, APIs
- **Kafka Topics**: Where the data is temporarily held
- **Data Consumers**: Data warehouses, stream processors, machine learning models, dashboards

---

## Transformation

## Talend

### What is Talend?

Talend is a powerful **open-source data integration platform** used to connect, transform, and manage data across various sources and destinations. It helps businesses collect data from different systems, clean it, transform it, and load it into target systems like databases, data warehouses, or cloud platforms.

Talend is part of the broader category of **ETL tools** (Extract, Transform, Load) and supports a wide range of data integration, data quality, and data governance tasks.

---

### Why Use Talend?

Talend simplifies and automates the movement and transformation of data. Here are some key **reasons** to use Talend:

- **Open-source availability**: Talend offers a free version (Talend Open Studio) for basic data integration needs.
- **Wide connector support**: It can connect to hundreds of data sources — databases, flat files, cloud storage, APIs, and more.
- **Graphical UI**: Users can design ETL workflows using a drag-and-drop interface, with minimal coding.
- **Scalability**: From small batch jobs to large real-time pipelines, Talend supports growing data needs.
- **Integrated tools**: Talend includes modules for data quality, master data management (MDM), and data governance.

---

### Talend’s Role in a Data Pipeline

Talend is typically used in the **data engineering** part of the pipeline, especially for:

1. **Extracting data** from various sources — databases, APIs, files, cloud apps, etc.
2. **Transforming data** — cleaning, filtering, aggregating, converting formats, joining tables, etc.
3. **Loading data** into a target — databases, data warehouses (like Snowflake, BigQuery), or cloud data lakes.

In a **modern data pipeline**, Talend can be used as the core ETL or ELT tool, helping to prepare data for analytics, reporting, machine learning, or compliance.

---

### Key Strengths of Talend

| Strength                     | Description |
|-----------------------------|-------------|
| **Ease of Use**             | Drag-and-drop UI for designing data flows, reducing the need for heavy coding. |
| **Extensive Connectivity**  | Supports a wide variety of data sources and destinations, including legacy systems, cloud services, and APIs. |
| **Open Source Option**      | Talend Open Studio is free and widely adopted. |
| **Built-in Data Quality**   | Tools to identify, clean, and validate data. |
| **Real-time & Batch**       | Can process data in both batch and real-time modes. |
| **Cloud Integration**       | Easily integrates with AWS, Azure, GCP, and SaaS platforms. |

---

### Typical Use Cases

Talend is suitable for many scenarios where data integration and transformation are needed. Some common use cases include:

- **Data Warehousing**: Moving and preparing data for storage in a central data warehouse (e.g., Redshift, Snowflake).
- **Data Migration**: Transferring data between systems during upgrades or cloud adoption.
- **Data Synchronization**: Keeping data consistent between systems (e.g., CRM ↔ ERP).
- **Data Cleaning & Standardization**: Detecting duplicates, fixing formatting issues, and enriching data.
- **API Integration**: Combining and transforming data from APIs (e.g., marketing tools, payment processors).
- **Real-time Analytics**: Ingesting and transforming data on the fly for dashboards and live reports.

---

### Getting Started

To begin using Talend:

1. **Download Talend Open Studio** from the official website (https://www.talend.com).
2. **Install and launch the application.**
3. **Create a new project** and start building your first ETL job using the graphical UI.
4. **Explore built-in connectors and components** to create pipelines tailored to your data needs.

---

### Summary

Talend is a versatile, beginner-friendly tool that plays a vital role in building modern data pipelines. With both open-source and enterprise versions, it offers scalability, flexibility, and strong integration capabilities for a wide range of data tasks.

Whether you're migrating data, building a warehouse, cleaning datasets, or integrating APIs, Talend can help streamline your workflow with minimal coding effort.

### Other Tools

**dbt** – SQL-based transformation tool often used with ELT workflows

**Apache Beam**, Spark Structured Streaming – Unified batch and stream processing

---

## Orchestration and Workflow Management

Even the best-designed pipelines need orchestration. This is where **Apache Airflow** and **Prefect** come in. They help coordinate which tasks happen when, in what order, and under what conditions. With Airflow, you define workflows as Python code using DAGs (Directed Acyclic Graphs), making it highly customisable. Prefect builds on these ideas with better handling of retries, observability, and dynamic workflows - making it especially appealing for modern, distributed workloads.

### Monitoring and Observability

Supporting all of this is a final layer: monitoring and observability. Pipelines must not only function - they must be visible. Tools like **Prometheus** and **Grafana** offer dashboards and alerts based on system metrics. Meanwhile, platforms like Great Expectations or OpenLineage let you track data quality and metadata over time, helping ensure that what flows through your pipeline is both correct and well-documented.

---

# Data quality and governance in integration
