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

# Lecture notes

## Understanding ETL, ELT, and Reverse ETL

If you're new to data engineering or analytics, the terms **ETL**, **ELT**, and **Reverse ETL** can seem a bit confusing. This guide will explain what each one means in simple terms, how they work, and when you'd use them.

---

### 📦 ETL: Extract, Transform, Load

#### What is ETL?

**ETL** stands for **Extract, Transform, Load**. It's a process used to move data from one or more sources into a centralized storage system like a **data warehouse**.

#### How it works:

1. **Extract**: Pull data from different sources (like databases, APIs, CSV files, etc.)
2. **Transform**: Clean, format, and organize the data (e.g., remove duplicates, convert formats, calculate new fields).
3. **Load**: Put the cleaned data into a **data warehouse** (like Snowflake, BigQuery, or Redshift).

#### Example Use Case:

A retail company wants to analyze its sales data. They extract data from their POS systems, clean and format it (e.g., standardize dates, calculate total sales), and then load it into a data warehouse where analysts can run reports.

---

## ⚙️ ELT: Extract, Load, Transform

#### What is ELT?

**ELT** is a newer approach that stands for **Extract, Load, Transform**. It's similar to ETL but the order of operations is different.

#### How it works:

1. **Extract**: Pull data from source systems.
2. **Load**: Load the raw data directly into the data warehouse.
3. **Transform**: Use the processing power of the data warehouse to clean and organize the data.

#### Example Use Case:

A tech company collects user interaction data from its app. Instead of cleaning it first, they load all the raw data into BigQuery and then write SQL scripts to transform it inside the warehouse for different teams to use.

#### Why use ELT?

- Faster to implement for large datasets.
- Modern data warehouses are optimized for fast, scalable transformations.

---

### 🔄 Reverse ETL: Data Out of the Warehouse

#### What is Reverse ETL?

**Reverse ETL** is the process of moving data **from the data warehouse back into operational tools** (like CRMs, marketing platforms, support tools).

#### How it works:

1. Select and format the data in the warehouse.
2. Push that data to external tools (e.g., Salesforce, HubSpot, Zendesk).
3. Teams can use the data in their daily workflows.

#### Example Use Case:

A marketing team wants to run personalized email campaigns. Reverse ETL is used to send customer segments from the data warehouse to their email platform so they can trigger campaigns based on recent activity.

---

### 🧠 Summary Table

| Process       | Order                  | Best For                                      |
|---------------|------------------------|-----------------------------------------------|
| **ETL**       | Extract → Transform → Load | Smaller datasets, legacy systems, strict cleaning before storing |
| **ELT**       | Extract → Load → Transform | Big data, modern warehouses, flexible transformation |
| **Reverse ETL** | Warehouse → Tools       | Operational use of analytics (e.g., sales, marketing) |

---

### Final Thoughts

- **ETL** and **ELT** help you get data **into** your data warehouse.
- **Reverse ETL** helps you get data **out** of your warehouse and into tools people use every day.
- Together, they make data both **centralized** and **actionable**.

---

## Introduction to Data Cataloguing

Data cataloguing is like creating a well-organized library, but instead of books, you're organizing **data**. It's a way to keep track of what data you have, where it lives, what it's about, and how it can be used.

---

### 📘 What is a Data Catalog?

A **data catalog** is a tool or system that helps you:

- **Find data** easily
- **Understand** what the data means
- **Trust** the data by showing where it came from and how it has changed
- **Use** the data more effectively

Think of it like an online store for data. Just like you can search for shoes by brand, size, and price, you can search for data by topic, date, owner, or format.

---

### 🔍 Why is Data Cataloguing Important?

As organizations collect more and more data, it can become overwhelming to manage. Without a data catalog, people often:

- Don't know what data exists
- Waste time looking for it
- Recreate data that already exists
- Use outdated or incorrect data

With a catalog, you:

- Save time
- Improve accuracy
- Increase collaboration
- Make better decisions

---

### 🧩 What Does a Data Catalog Contain?

A good data catalog includes:

- **Metadata**: Data about the data (e.g., title, description, who owns it, when it was created)
- **Data lineage**: Shows where the data came from and how it’s been transformed
- **Data classifications**: Labels to show sensitivity (e.g., confidential, public)
- **Tags and keywords**: Help with searching
- **Usage statistics**: How often it’s used and by whom
- **Comments and ratings**: Feedback from users

---

### 🛠️ How is Data Cataloguing Done?

Here’s a simplified process:

1. **Inventory**: Scan all your systems to find where data lives.
2. **Ingest metadata**: Pull in information about the data automatically.
3. **Enrich**: Add extra info manually (like descriptions or tags).
4. **Organize**: Group and label the data to make it easier to find.
5. **Maintain**: Keep it up to date as data changes.

Some popular tools for data cataloguing are:

- **Alation**
- **Collibra**
- **Google Data Catalog**
- **Microsoft Purview**
- **Apache Atlas**

---

### 📚 Real-World Example

Imagine you're working at a hospital. You might have data on:

- Patients
- Doctors
- Appointments
- Lab results

A data catalog could help you quickly find the "Appointment history for 2024," understand what fields are included, who collected it, and whether you're allowed to use it for research.

---

### ✅ Summary

Data cataloguing helps make data **discoverable**, **understandable**, and **usable**. It’s essential for anyone working with large or complex data environments, and it's the first step toward data-driven decision making.

---

## Introduction to Open Metadata

### What is Open Metadata?

**Open Metadata** is an open-source platform designed to help organizations manage and understand their **data assets** more effectively. Think of it as a central hub that brings together information about all your data — where it's stored, how it's used, who owns it, and more.

This information is known as **metadata**, which simply means "data about data."

For example:
- A table in a database has metadata like the number of rows, column names, types of data, who created it, and how often it gets updated.
- A machine learning model has metadata like the training dataset, the algorithm used, and performance metrics.

Open Metadata helps you collect, organize, and use all this metadata in one place.

---

### How Does Open Metadata Work?

Open Metadata connects to your various **data sources** (like databases, data warehouses, dashboards, data pipelines, etc.) using **connectors**. Once connected, it automatically extracts metadata from these systems.

Here’s a simplified step-by-step overview:

1. **Ingestion**:
   - Open Metadata uses built-in connectors to pull metadata from your tools (like Snowflake, BigQuery, Airflow, Looker, etc.).
   - This includes schemas, table definitions, column data types, usage stats, lineage, etc.

2. **Storage**:
   - The collected metadata is stored in a central **metadata store**.
   - It can be accessed and queried like any regular database.

3. **Visualization & Search**:
   - Open Metadata provides a **user-friendly interface** to search and explore metadata.
   - You can browse datasets, see lineage diagrams, and track how data moves through your system.

4. **Collaboration**:
   - Users can tag, comment, rate, and assign ownership to data assets.
   - Teams can use it to improve communication and understanding of shared data.

5. **Governance**:
   - Open Metadata supports **data quality checks**, **access policies**, and **compliance** monitoring.
   - It helps enforce rules around how data should be used and who can access it.

---

### Key Features

- **Data Discovery**: Find the data you need quickly with search and filtering.
- **Data Lineage**: Visualize how data flows from source to destination.
- **Collaboration**: Add comments, tags, and ownership to promote data sharing.
- **Data Governance**: Enforce rules and policies to keep data secure and accurate.
- **Integration**: Connects with popular data tools (Airflow, dbt, Snowflake, etc.).
- **Open Source**: No vendor lock-in, and you can customize it to fit your needs.

---

### Benefits of Open Metadata

1. **Improved Data Understanding**:
   - Everyone knows what data exists, where it comes from, and how to use it.

2. **Faster Data Access**:
   - Users spend less time searching and more time analyzing.

3. **Better Collaboration**:
   - Teams can share context and knowledge about data assets.

4. **Enhanced Data Quality and Trust**:
   - Track changes, detect issues, and ensure data is reliable.

5. **Stronger Data Governance**:
   - Meet compliance needs and maintain data integrity.

6. **Scalability**:
   - Built to work with large, complex data ecosystems.

---

### Who Uses Open Metadata?

Open Metadata is useful for:
- **Data Engineers**: Manage pipelines and monitor data health.
- **Data Scientists/Analysts**: Find trusted datasets for analysis.
- **Product Managers**: Understand how data supports features.
- **Compliance Officers**: Ensure data use meets legal standards.

---

### Final Thoughts

Open Metadata is like a map and user manual for your organization’s data. It makes your data easier to find, understand, and trust — all while promoting collaboration and compliance.

Because it’s open-source, it also gives you the freedom to adapt and grow your metadata system as your data needs evolve.

---

### Learn More

- Website: [https://open-metadata.org](https://open-metadata.org)
- GitHub: [https://github.com/open-metadata/OpenMetadata
