# Topic 2 - Heterogenous data ingestion patterns 24/04/2025

## Defining your data ingestion architecture

Defining your ingestion architecture should happen before proceeding with ingestion, as any changes in design may mean changes to tooling and timelines, which translates to costs. Additionally, your architectural design requires communication with stakeholders to help define and fulfil your business and technical requirements. There are two main types of data ingestion:

1.	Batch Processing
2.	Real-Time (or Stream) Processing

| Characteristic    | Batch                |Real-time             |
|-------------|----------------------------------|----------------------------------|
| Timing  | Data is collected in large 'batches' at scheduled intervals - hourly, daily, weekly, etc., depending on the system's requirements.  |Data is ingested and processed continuously in real-time or near real-time.  |
| Suitability  | Ideal for scenarios where its not necessary to have real-time data insights and where processing large volumes of data at once is more efficient.     |Best for scenarios where immediate data processing and quick decision-making are crucial. |
| Characteristics   |Often simpler and less resource-intensive compared to real-time processing. The downside is latency in data availability and potential relevancy.|More complex and resource-intensive due to the need for constant data processing and immediate response. It often requires more sophisticated technology, like stream processing engines. |
| Use cases   |Common in situations where the data doesn't change rapidly, like processing sales records at the end of the day or generating daily reports.|Typical in scenarios like fraud detection, monitoring of financial transactions, real-time analytics in IoT devices, and live data feeds. |

### Data velocity

Data velocity refers to the speed with which data enters your system and how long it takes for processing to occur.

Data velocity can affect network latency and user traffic.

Your design must account for questions like:

- How fast does data flow happen?
- Will this velocity compete with my business traffic?
- Can my network bandwidth handle the data flow?
- Will it increase latency for my users?

### Data volume

All data ingestion tools are built in diverse ways and have workload limits, some to the petabyte or terabyte scale.

Therefore, in deciding what ingestion tools to implement, you must ask questions like:

- What is the volume of data ingested frequently?
- How many rows/columns are present?
- Are there plans to scale in the future?
- Will your solution scale to accommodate the growing/changing business demand?
- Fulfilling this requirement is essential because if your data workload exceeds your ingestion system, it may result in downtimes for your business.

### Data frequency

Your ingestion framework should note your business goal, timeliness of responses, and budget to select the best ingestion design.

- How often does ingestion from sources occur?
- What is the response time needed on the data to create value? Some data contains a time window and lose value for longer response times.
- Will batched or real-time streaming work?
- Can you implement micro-batching to ensure near real-time updates?

### Data format

Your ingestion design must consider data schema and format in your workflow.

- In what format does the data arrive?
- Is it unstructured, like video or text, or structured, like JSON and CSV?
- Does this tool validate and enforce schema?
- Can you afford the engineering time needed to configure and validate the schema if not?

### Data security and governance

Ensuring data security and governance is crucial to your ingestion design and may involve asking questions like:

- Who has access to this data?
- Will data be consumed internally or externally?
- Are sensitive data like Personally Identifiable Information (PII) present in the data?
- What are some security measures to implement to ensure no leaks or breaches?

### Monitoring and tracking

Most organisations will have numerous data sources and must prioritise the sources to include in their ingestion pipeline to avoid having bad and unnecessary data.

Additionally, your tooling infrastructure must employ ingestion best practices like validating data at strategic points in the pipeline, auditing, log-viewing, and visualisations to observe and track the ingestion workflow.

## Heterogeneous data ingestion use cases

**What is a heterogeneous data ingestion pattern?**

A heterogeneous data ingestion pattern involves managing data that comes in various formats and structures, such as a mix of structured, semi-structured, and unstructured data. It also involves those scenarios in which data undergoes transformations during its ingestion into the destination storage system. These transformations range from basic adjustments like altering the data type or format to adhere to the requirements of the destination, to more intricate processes such as employing machine learning algorithms to generate new data attributes. This approach typically occupies most of the time for data engineers and ETL developers, who work on cleansing, standardising, formatting, and structuring the data according to business and technological specifications.

### Use cases for a heterogenous data pattern

**Healthcare Data Management**

Hospitals and healthcare providers manage a myriad of data types: electronic health records are structured data, doctors’ handwritten notes are unstructured data, and diagnostic imaging files are semi-structured data.

**Relational data ingestion**

Relational data ingestion between different data engines – Online businesses that have been migrating legacy MySQL databases to Elasticsearch to adapt to search query patterns from their users. Also, between same data engines (for example, Microsoft SQL Server to Amazon RDS for SQL Server or SQL Server on Amazon EC2, or Oracle to Amazon RDS for Oracle) – this use case can apply to migrating your peripheral workload into the cloud or for scaling your workload to expand on new requirements like reporting.

**Ingesting large objects**

Ingesting large objects (BLOB, photos, videos) ingestion into cloud bucket object storage - this is common for social media and businesses that let their users upload rich media files.

**Data files ingestion**

Data files ingestion from on-premises storage to a cloud data lake (for example, ingesting parquet files from Apache Hadoop to Amazon Simple Storage Service (Amazon S3) or ingesting CSV files from a file share to Amazon S3) - this use case may be one time to migrate your big data solutions or may apply to building a new data lake capability in the cloud.

**Streaming from internet of things**

Industries that employ multiple sensors and log files to a central data lake. For example, energy plants that build digital twins of their turbines, so that a ML algorithm can spot when the weakest link of the turbine is going to fail within the next 24 hours.

**E-Commerce platforms**
An online retailer deals with structured data like product specifications, semi-structured data such as customer reviews, and unstructured data, including product images and videos.

## Advanced data ingestion patterns

By understanding and leveraging different data ingestion patterns, organisations can effectively extract, transform, and load data from diverse sources into their storage systems, thereby unlocking its full potential. Choosing the right data ingestion method requires careful consideration of several factors, including:

- Where is your data originating from?
- What's the intended storage destination?
- How is the data currently structured within that system?

### An introduction to advanced ingestion patterns

Some more advanced ingestion patterns beyond streaming and batching include:

1.	Change Data Capture (CDC)
2.	Lambda Architecture
3.	Kappa Architecture

## Change Data Capture

**Change Data Capture (CDC)** is a design pattern that captures incremental changes made to a database and applies them to a target data store in near real-time. CDC uses transaction logs or triggers to identify and capture changes. A key feature of CDC is it applies directly to database events (not system events, application events, log events etc).

#### CDC is ideal for the following:
- Synchronising data between transactional and analytical systems.
- Enabling real-time analytics on operational data.
- Feeding real-time dashboards and applications with up-to-date data.
- Replicating data for disaster recovery and high availability.

#### A CDC pipeline typically includes the following components:
- Source database with CDC enabled (e.g., MySQL Postgres, Oracle GoldenGate).
- CDC tool to capture and transmit changes.
- Feeding real-time dashboards and applications with up-to-date data.
- Target data store to apply changes (data warehouse, data lake, NoSQL database).

#### Tools for CDC

Tools for CDC include AWS Database Migration Service (DMS), Azure Data Factory, Google Cloud Datastream.

#### Pros
- Enables near real-time data synchronisation.
- Minimises impact on source systems (no expensive queries).
- Supports heterogeneous source and target systems.
- Integrates well with existing data pipelines and architectures.

#### Cons
- Requires enabling CDC on source databases (may need DBA involvement).
- Can be complex to set up and manage, especially for multiple sources.
- May increase load on source systems and networks.
- Some CDC tools can be expensive for high-volume workloads.

### Lambda Architecture

The Lambda Architecture is a design pattern that combines batch and real-time processing to enable comprehensive and accurate data analysis. It consists of three layers: batch, speed, and serving.

#### The Lambda Architecture is ideal for:
- Use cases that require both real-time and historical data analysis.
- Handling complex data transformations and aggregations.
- Ensuring data consistency and accuracy across batch and real-time views.
- Supporting ad-hoc queries and data exploration.

#### A Lambda Architecture includes the following components:
- Batch layer: ingests and processes historical data (Hadoop, Spark).
- Speed layer: ingests and processes real-time data (Spark Streaming, Flink).
- Serving layer: combines batch and real-time views and serves data to applications (Cassandra, HBase).

#### Tools for Lambda Architecture include the following:
- Open-source: Apache Hadoop, Apache Spark, Apache Cassandra.
- Cloud-specific: AWS EMR, Azure HDInsight, Google Cloud Dataproc.
- Cloud-agnostic: Databricks.

#### Pros
- Provides a comprehensive view of data (batch + real-time).
- Supports complex data processing and analytics.
- Ensures data consistency and accuracy.
- Enables ad-hoc querying and data exploration.

#### Cons
- Requires maintaining two separate processing pipelines (batch and speed).
- Can be complex to set up and manage.
- May introduce latency due to batch processing.
- Requires more infrastructure and resources than simpler architectures.

### Kappa Architecture

The Kappa Architecture is a simplification of the Lambda Architecture that uses a single, real-time processing pipeline for both real-time and historical data. It leverages stream processing and retains an immutable log of all data.

#### The Kappa Architecture is ideal for:
- Use cases that primarily require real-time data processing.
- Simplifying data architecture by eliminating batch processing.
- Leveraging the power and flexibility of stream processing frameworks.
- Enabling faster data processing and analysis.

#### A Kappa Architecture includes the following components:
- Message queue or log to capture all data (Kafka, Kinesis).
- Stream processing engine to process and serve data (Spark Streaming, Flink).
- Serving layer to store and expose processed data (Cassandra, HBase).

#### Tools for Kappa Architecture include the following:
- Open-source: Apache Kafka, Apache Flink, Apache Druid.
- Cloud-agnostic: Confluent Platform, Materialise.

#### Pros
- Simpler architecture than Lambda (no separate batch and speed layers).
- Enables faster data processing and analysis.
- Leverages the power and flexibility of stream processing.
- Supports time-travel and reprocessing of historical data.

#### Cons
- Requires more upfront planning and design.
- May be more resource-intensive than batch processing for large historical datasets.
- Relies heavily on the performance and reliability of the message queue and stream processing engine.
- May require specialised skills and tools for stream processing.

### A comparison summary

Here is a summary of the key differences between Lambda and Kappa architecture:

| Criteria    | Lambda            |Kappa           |
|-------------|----------------------------------|----------------------------------|
| Processing paradigm  | Batch & Streaming  |Streaming  |
| Re-processing paradigm  | Every Batch Cycle  |Only when code changes |
| Resource consumption  | Function = Query (All data)  |Incremental algorithms, running on deltas  |
| Reliability | Batch is reliable, Streaming is approximate  |Streaming with consistency (exactly once)|

---

| Pattern   | Real-Time    |High Volume   | Complex Transfer | CDC   | Ad-Hoc Queries  | Ease of Use |
|-----------|--------------|--------------|------------------|-------|-----------------|-------------|
| Batch  | No    |Yes    | Yes  | No   |Yes  | Easy |
| Real-Time  | Yes    |Yes    | No | No    | No  | Medium |
| CDC  | Yes     |No   | No | Yes   | No  | Hard |
| Lambda   | Yes     |Yes   |Yes  | No    | Yes  | Hard |
| Kappa  | Yes    |Yes  | Yes  | No    | Yes  | Yes |


## Introduction to AWS Glue, Azure Data Explorer, and Azure Data Factory

This guide provides a beginner-friendly overview of three powerful cloud-based data services: **AWS Glue**, **Azure Data Explorer**, and **Azure Data Factory**. These tools are essential for modern data processing, analytics, and integration across cloud platforms.

---

### 🧪 AWS Glue

**What is AWS Glue?**

AWS Glue is a fully managed **extract, transform, and load (ETL)** service provided by Amazon Web Services (AWS). It helps users **prepare and transform data** for analytics, machine learning, and application development.

**Use Cases:**
- Moving data between data stores (e.g., from S3 to Redshift).
- Cleaning and transforming raw data.
- Cataloging data for search and discovery.

**Benefits:**
- **Serverless**: No need to manage infrastructure.
- **Automated schema discovery**: Uses crawlers to detect data structure.
- **Integration**: Works well with AWS services like Athena, Redshift, and S3.

**Alternative Cloud Equivalents:**
- Azure Data Factory (Microsoft Azure)
- Google Cloud Dataflow (Google Cloud Platform)

---

### 🔎 Azure Data Explorer (ADX)

**What is Azure Data Explorer?**

Azure Data Explorer is a fast, highly scalable **data analytics service** optimized for **exploring large volumes of data** in near real-time. It's ideal for telemetry, log data, and time-series analytics.

**Use Cases:**
- Analyzing large-scale log and telemetry data.
- Real-time dashboarding and monitoring.
- Exploratory data analysis using Kusto Query Language (KQL).

**Benefits:**
- **Fast query performance** for large datasets.
- **Highly scalable and managed**.
- **Built-in ingestion tools** for seamless data flow.

**Alternative Cloud Equivalents:**
- Amazon OpenSearch (formerly Elasticsearch Service)
- Google BigQuery (for analytics workloads)

---

### 🛠️ Azure Data Factory (ADF)

**What is Azure Data Factory?**

Azure Data Factory is a **cloud-based data integration service** from Microsoft. It allows users to create **data-driven workflows (pipelines)** to move and transform data across various data stores.

**Use Cases:**
- ETL/ELT processes across on-premise and cloud data.
- Orchestrating and scheduling data pipelines.
- Integrating data from multiple sources for BI and analytics.

**Benefits:**
- **Code-free UI** for building pipelines.
- **Connects to 90+ data sources** (on-prem and cloud).
- **Integration with Azure Synapse, Databricks, etc.**

**Alternative Cloud Equivalents:**
- AWS Glue (Amazon Web Services)
- Google Cloud Dataflow / Cloud Composer

---

### Summary Table

| Service               | Purpose                      | Key Feature                        | Cloud Provider | Alternatives                    |
|-----------------------|------------------------------|------------------------------------|----------------|----------------------------------|
| **AWS Glue**          | ETL and data cataloging       | Serverless ETL & schema discovery  | AWS            | Azure Data Factory, GCP Dataflow |
| **Azure Data Explorer** | Big data analytics (logs, telemetry) | Real-time analytics with KQL     | Azure          | Amazon OpenSearch, BigQuery      |
| **Azure Data Factory** | Data integration & pipelines  | Code-free data workflows           | Azure          | AWS Glue, GCP Dataflow           |

---

### Final Thoughts

These services each play a critical role in building modern data solutions. Here's a quick analogy to help you remember:

- **AWS Glue**: Like a data janitor — it cleans, transforms, and moves data.
- **Azure Data Explorer**: Like a detective — it helps you quickly search through huge piles of data to find insights.
- **Azure Data Factory**: Like a delivery manager — it organizes, schedules, and delivers your data wherever it needs to go.

Understanding these tools is essential for anyone working with cloud-based data solutions.

