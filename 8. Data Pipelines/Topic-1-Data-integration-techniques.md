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

