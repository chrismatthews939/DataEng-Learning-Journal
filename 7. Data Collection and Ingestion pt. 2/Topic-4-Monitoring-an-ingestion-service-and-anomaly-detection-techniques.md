# Topic 4 - Monitoring an ingestion service and anomaly detection techniques 02/06/2025

## The importance of monitoring in data engineering

In modern data-driven organisations, data ingestion pipelines are critical components that must operate reliably and efficiently. Monitoring these pipelines is essential to:

-	**Ensure data integrity:** Detect and prevent data loss or corruption.
-	**Maintain performance:** Identify bottlenecks and optimise resource utilisation.
-	**Enhance reliability:** Quickly detect and respond to system failures or anomalies.
-	**Support compliance:** Meet regulatory requirements for data handling and reporting.

**Logs** are records of events
**Metrics** are used to measure performance
**Alerts** notifications of issues
**Dashboards** visualise performance

## Industry-standard monitoring tools

## Introduction to Prometheus 

**Prometheus** is an **open-source monitoring and alerting toolkit** originally developed at SoundCloud. It's now part of the Cloud Native Computing Foundation (CNCF), just like Kubernetes.

Prometheus is designed for **recording real-time metrics** in a time series database, with **powerful queries and alerts**. It’s widely used to monitor servers, containers, databases, applications, and even custom systems.

---

## Key Concepts

Here are some essential concepts to understand Prometheus:

### 1. **Metrics and Time Series**
- A **metric** is a numeric value about a system (e.g., CPU usage, memory used).
- A **time series** is a sequence of metric values, recorded over time.

Example:
```
http_requests_total{method="GET", handler="/api"} 12345
```

- This says: the metric `http_requests_total` counted 12,345 GET requests to `/api`.

### 2. **Pull-Based Model**
- Prometheus **pulls data** from targets at regular intervals (instead of targets pushing data).
- These targets expose an HTTP endpoint (usually `/metrics`) that Prometheus scrapes.

### 3. **Prometheus Server**
- The core of the system. It collects metrics, stores them, and allows querying.

### 4. **Exporters**
- Exporters are small programs that **expose metrics in a Prometheus-friendly format**.
- Example: `node_exporter` exposes OS-level metrics like CPU, memory, and disk usage.

### 5. **PromQL**
- Prometheus Query Language (PromQL) is used to **query and filter metrics**.
- Example: To get the rate of HTTP requests:
```
rate(http_requests_total[5m])
```

### 6. **Alerting**
- Prometheus supports **alerts based on metrics**.
- Alerts are sent to an **Alertmanager**, which can notify you via email, Slack, PagerDuty, etc.

---

## How Prometheus Works

Here’s a simplified flow:

1. Prometheus server is configured with a list of **targets** to monitor.
2. It **scrapes metrics** from the targets periodically (every 15 seconds by default).
3. The metrics are **stored locally** in a time-series database.
4. You can **query the data** using PromQL through:
   - The **Prometheus UI**
   - **Grafana dashboards** (for beautiful visualization)
5. Alerts are evaluated and sent to **Alertmanager** if necessary.

---

## Example Use Case

Let's say you want to monitor a web server:

- You install an **exporter** (like `node_exporter`) on the server.
- Prometheus scrapes metrics from it every 15s.
- You view a **dashboard in Grafana** showing CPU usage, memory, and HTTP requests.
- You set up an **alert** if CPU usage goes above 90% for 5 minutes.

---

## Why Use Prometheus?

- 🆓 **Free and open-source**
- 🧩 **Works well with Kubernetes**
- 🧠 **Powerful query language (PromQL)**
- 📦 **Many ready-to-use exporters**
- 📊 **Integrates easily with Grafana**
- 📣 **Built-in alerting system**

---

## Getting Started (High-Level Steps)

1. **Install Prometheus**: Download or use Docker.
2. **Configure targets** in the `prometheus.yml` file.
3. **Run Prometheus** and access the web UI at `http://localhost:9090`.
4. **Install an exporter** like `node_exporter` to collect system metrics.
5. **Set up Grafana** to visualize metrics (optional but recommended).
6. **Add alerts** to get notified when things go wrong.

---

## Resources

- [Official Website](https://prometheus.io/)
- [Getting Started Guide](https://prometheus.io/docs/introduction/first_steps/)
- [Awesome Prometheus](https://github.com/roaldnefs/awesome-prometheus) - curated list of tools and resources

---

## Summary

Prometheus is a **powerful yet approachable monitoring system** for everyone from hobbyists to large-scale production environments. With its **pull model**, **rich query language**, and **flexible alerting**, it’s a great choice for modern infrastructure monitoring.

---

## Grafana

**Grafana** is an open-source **monitoring and data visualization tool**. It allows you to **explore, visualize, and analyze** data from a variety of sources in real-time using **customizable dashboards**. Grafana is commonly used to monitor the health, performance, and trends of IT systems, servers, applications, and other infrastructure components.

---

## Why Use Grafana?

- **Real-time monitoring**: See your data as it changes.
- **Beautiful dashboards**: Build interactive, customizable visualizations like graphs, charts, and heatmaps.
- **Multiple data sources**: Connect to a wide range of databases and monitoring tools (e.g., Prometheus, InfluxDB, MySQL, Elasticsearch, etc.).
- **Alerting**: Set up alerts to notify you when something goes wrong.
- **Open-source and extensible**: Free to use and has a large community with lots of plugins.

---

## Key Concepts

### 1. **Dashboard**
A dashboard is a collection of **panels** (graphs, charts, etc.) that visually display data. You can have multiple dashboards for different systems or views.

### 2. **Panel**
A panel is a single visualization in a dashboard. For example, a line graph showing CPU usage over time.

### 3. **Data Source**
Grafana pulls data from **external systems** called data sources. Examples include:
- **Prometheus** – for metrics monitoring
- **InfluxDB** – time-series database
- **Elasticsearch** – search and analytics engine
- **MySQL/PostgreSQL** – relational databases

### 4. **Query**
Each panel uses a **query** to fetch data from the data source. Grafana provides a query editor tailored for each data source type.

### 5. **Alerts**
You can set **alert rules** for any panel. If the data meets a certain condition (like CPU > 90%), Grafana can **send a notification** via email, Slack, or other channels.

---

## How Grafana Works (Basic Flow)

1. **Connect** a data source (like Prometheus or InfluxDB).
2. **Create a dashboard** to organize your views.
3. **Add panels** to display different metrics.
4. **Write queries** to fetch the data you want to display.
5. **Customize** the visualizations (colors, axes, time ranges, etc.).
6. **Set alerts** (optional) to be notified when values go out of range.

---

## Typical Use Cases

- Monitoring server performance (CPU, memory, disk usage)
- Visualizing application metrics (request rates, errors)
- Tracking website traffic or API calls
- Observing IoT sensor data
- Business intelligence dashboards

---

## Getting Started

1. **Install Grafana**:
   - On Linux/macOS/Windows
   - Using Docker
   - As a hosted service via [Grafana Cloud](https://grafana.com/products/cloud/)

2. **Access Grafana UI**:
   - Open a web browser and go to `http://localhost:3000` (default)
   - Login with default credentials: `admin` / `admin` (you’ll be asked to change it)

3. **Add your first data source**
   - Go to **Configuration > Data Sources**
   - Select and configure your database or monitoring tool

4. **Create your first dashboard**
   - Go to **+ > Dashboard**
   - Add a panel and start visualizing data!

---

## Summary

Grafana is a powerful tool that helps you:
- Connect to various data sources
- Visualize your metrics in real-time
- Create dashboards and alerts
- Make informed decisions based on your system’s data

It’s widely used in DevOps, system administration, and business analytics due to its flexibility and ease of use.

---

## Additional Resources

- [Grafana Official Website](https://grafana.com/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Grafana Labs YouTube Channel](https://www.youtube.com/c/Grafana)

---

# 📊 Beginner's Guide to Monitoring Kafka with Prometheus & Grafana

This guide walks you through setting up monitoring for **Apache Kafka** using **Prometheus** and **Grafana**.

---

## 📦 Prerequisites

Make sure you have these installed:

- Docker & Docker Compose
- Basic knowledge of Docker
- Kafka running locally (we’ll use a Docker image for Kafka)
- Some free disk space

---

## 🔧 Step 1: Set Up Kafka with JMX Exporter

Kafka doesn’t expose metrics in Prometheus format by default. We use the **JMX Exporter** to make Kafka metrics available.

### Create `docker-compose.yml`

```yaml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.3.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:7.3.0
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_JMX_PORT: 9999
      KAFKA_JMX_HOSTNAME: localhost
    ports:
      - "9092:9092"
      - "9999:9999" # Port for JMX

  kafka-jmx-exporter:
    image: prom/jmx-exporter
    ports:
      - "7071:7071" # Prometheus will scrape from here
    volumes:
      - ./kafka-jmx-config.yaml:/config.yaml
    command:
      - 7071
      - /config.yaml
```

### Create kafka-jmx-config.yaml

This tells the exporter what to collect.

```yaml
startDelaySeconds: 0
hostPort: localhost:9999
lowercaseOutputName: true
lowercaseOutputLabelNames: true
rules:
  - pattern: "kafka.server<type=(.+), name=(.+)><>(Count|Value)"
    name: kafka_$1_$2
    type: GAUGE
    labels:
      instance: kafka1
```


## 🔧 Step 2: Set Up Prometheus

### Create prometheus.yml
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'kafka'
    static_configs:
      - targets: ['kafka-jmx-exporter:7071']
```

### Add Prometheus to docker-compose.yml

Below the Kafka service, add:

```yaml
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    ports:
      - "9090:9090" # Access Prometheus UI
```

## 🔧 Step 3: Add Grafana to Visualize Metrics

### Add Grafana to docker-compose.yml

```yaml
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
```

## 🔧Step 4: Start Everything

### Run the stack with:
```bash
docker-compose up -d
```

## 🔧Step 5: Configure Grafana Dashboard

### Add Prometheus as a Data Source:

In Grafana, go to Settings > Data Sources
Click Add data source
Choose Prometheus
Set URL to: http://prometheus:9090
Click Save & Test

### Import a Kafka Dashboard:

Go to + > Import
Use dashboard ID: 7589 or search for "Kafka"
Choose Prometheus as data source
Click Import

You’ll now see charts with metrics like:

Messages In/Out

Under-replicated partitions

Request latency

---

## Forecasting techniques for data ingestion

One of the key challenges faced by data engineers is predicting future system behaviour to ensure that resources are allocated efficiently and potential issues are mitigated before they escalate. Forecasting is a critical component in managing data ingestion services. By predicting future system behaviour, you can plan capacity, prevent overloads, and optimise costs.

Forecasting is a critical component in managing data ingestion services. By predicting future system behaviour, you can:

1.	**Plan capacity:** Ensure that resources meet demand.
2.	**Prevent overload:** Avoid system failures due to unexpected spikes.
3.	**Optimise costs:** Allocate resources efficiently.

### Introduction to time series forecasting

Time series forecasting involves analysing historical data to predict future values. Common methods include:

-	**ARIMA** (AutoRegressive Integrated Moving Average)
-	**SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors)
-	**Prophet**
-	**Machine Learning Models** (e.g., LSTM networks)

`A stationary time series is a time series whose statistical properties, such as mean, variance, and autocorrelation, do not change over time. In other words, the value of a stationary time series is not dependent on the time at which it is observed.`

GPT ARIMA
GPT SARIMAX
GPT how to forecast and implement ARIMA and SARIMAX in python with an example. Include using the Augmented Dickey-Fuller test to check if the time series is stationary and auto-ARIMA to auto select the best parameters.
GPT how to apply differencing to achieve stationality

### Real-world application

**Capacity planning for a streaming service**
A music streaming company wants to forecast the expected data ingestion rates to ensure that their Kafka cluster can handle peak loads, especially during events like new album releases or holidays.

**As the lead data engineer, how would you set about forecasting the data ingestion rates?**
Your implementation steps would be as follows:

1.	**Collect historical data:**
-	Gather ingestion metrics over the past year.
2.	**Apply SARIMAX Model:**
-	Account for seasonal patterns (e.g., higher usage on weekends).
-	Include exogenous variables like marketing campaigns.
3.	**Forecast future demand:**
-	Predict ingestion rates for the next quarter.
4.	**Plan Infrastructure:**
-	Scale Kafka clusters and allocate resources accordingly.

**The benefits**

-	**Optimised performance:** Prevent overloads and ensure smooth user experience.
-	**Cost efficiency:** Avoid over-provisioning resources, reducing operational costs.
-	**Strategic planning:** Align technical capacity with business initiatives.

## Anomaly detection in data streams

### Anomaly detection techniques

#### Statistical methods
**Z-Score Analysis:**
-	Measures how many standard deviations an element is from the mean.
**Seasonal Hybrid ESD (Extreme Studentised Deviate):**
-	Detects anomalies in seasonal time series data.

#### Machine learning models
**Isolation Forest:**
-	An unsupervised learning algorithm that isolates anomalies based on random partitioning.
**One-Class SVM (Support Vector Machine):**
-	Learns the boundary of normal data to detect outliers.

#### Time series models
**ARIMA/SARIMAX Residual Analysis:**
-	Analyse residuals from forecasting models to detect anomalies.
**Prophet:**
-	A forecasting tool by Facebook that can model and detect anomalies in time series data.

GPT Implementing anomaly detection with Python using Isolation Forest and Seasonal-Hybrid ESD to detect anomalies in data streams.

## Integration with Incident Management Systems

Incident management systems play a vital role in helping organisations respond to and manage unplanned events or service interruptions.

**Popular incident management platforms include:**
-	PagerDuty
-	Opsgenie
-	VictorOps
-	ServiceNow

**The benefits of integration include:**

-	**Centralised alert management:** Consolidate alerts from multiple sources.
-	**On-Call scheduling:** Manage on-call rotations and escalations.
-	**Automated response:** Trigger automated actions or workflows.
-	**Incident tracking:** Log incidents for analysis and improvement.

GPT Integrating Prometheus Alertmanager with incident management. Step by step guide

### Real-world application

**Managing incidents in a healthcare system...**

A hospital uses data ingestion services to process patient data in real-time.
System failures can have critical implications for patient care.
As the lead data engineer, how would you set about implementing an incident management system?

Your implementation steps would be as follows:

1.	**Integrate monitoring with incident management:**
-	Use Prometheus and Alertmanager to monitor ingestion services.
-	Connect Alertmanager to PagerDuty for incident management.
2.	**Define critical alerts:**
-	Set up alerts for high-severity issues like data ingestion failures or significant anomalies.
3.	**Configure on-call rotations:**
-	Ensure that responsible team members are available to respond to incidents promptly.
4.	**Automate responses:**
-	Implement scripts or playbooks that can be triggered to mitigate issues automatically.

#### The benefits
-	**Response times:** Faster resolution of incidents reduces impact on services.
-	**Accountability:** Clear ownership of incidents ensures that issues are addressed.
-	**Continuous improvement:** Incident tracking allows for analysis and process enhancements.

## Addressing real-world use cases and typical ingestion issues

### Common ingestion issues in Kafka and Cloud environments
Data ingestion pipelines can encounter several common issues that impact their performance and reliability. In this section, we'll delve into problems like consumer lag and latency, broker failures, message loss, and security breaches. Understanding the symptoms, causes, and solutions for these issues will help you maintain a robust data ingestion system.

### Consumer lag and latency

**Symptoms**
-	Consumers fall behind the latest messages.
-	Increased message processing delays.

**Causes**
- Insufficient consumer resources.
- Slow processing logic.
- Network congestion.

**Solutions**
- Scale consumer instances.
- Optimise processing code.
- Enhance network bandwidth.

### Message Loss

**Symptoms**
- Missing data in downstream systems.
- Inconsistent data processing results.

**Causes**
- Incorrect producer configurations.
- Insufficient replication.
- Data retention policies.

**Solutions**
- Configure appropriate acknowledgments (acks=all).
- Increase replication factor.
- Adjust retention settings.

### Broker failures

**Symptoms**
- Unavailable partitions.
- Errors in producers and consumers.

**Causes**
- Hardware failures.
- Configuration errors.
- Resource exhaustion.

**Solutions**
- Implement redundancy.
- Use automatic broker recovery.
- Monitor resource utilisation.

### Security Breaches

**Symptoms**
- Unauthorised access to data.
- Suspicious activities in logs.

**Causes**
- Weak authentication.
- Misconfigured access controls.
- Vulnerabilities in the system.

**Solutions**
- Implement robust security measures (SSL, SASL, ACLs).
- Regularly audit security configurations.
- Apply patches and updates promptly.

---

### Real-world applications

**Data loss in a logistics company...**

A logistics company experiences data loss in their tracking system, leading to misplaced shipments.

**Analysis:**

1. **Issue:**
- Messages are lost due to incorrect producer settings (acks=1).

2. **Resolution:**
- Update producer configuration to use acks=all.
- Increase replication factor for critical topics.

---

**Scaling challenges in a social media platform...**

A social media platform struggles to handle increased data ingestion during peak times, resulting in slow content updates.

**Analysis:**

1. **Issue:**
- Consumer lag due to insufficient processing capacity.

2. **Resolution:**
- Implement auto-scaling for consumer applications.
- Optimise processing logic using asynchronous operations.

---

### Best practices for addressing ingestion issues

Implementing best practices is essential for preventing and mitigating ingestion issues. This section will cover strategies like implementing redundancy, optimising configurations, regular monitoring, documentation and automation, and conducting regular audits. These practices will help you build resilient data pipelines capable of handling diverse challenges.


**Implement redundancy:**
- Use multiple brokers and replication to prevent single points of failure.

**Optimise configurations:**
- Tune Kafka settings based on workload and performance testing.

**Regular monitoring:**
- Continuously monitor system metrics to detect issues early.

**Document and automate:**
- Maintain documentation of configurations and automate deployments for consistency.

**Conduct regular audits:**
- Review security settings, resource allocations, and system performance periodically.

### Cloud environment considerations

Managing data ingestion pipelines in cloud environments comes with its own set of considerations. Leveraging cloud services' features and understanding their limitations will enable you to optimise your data ingestion processes in the cloud.

The following are best practice techniques:

- **Resource management:** Utilise cloud services' auto-scaling features. Monitor costs associated with resource usage.
- **Network dependencies:** Be aware of network latency and bandwidth limitations in cloud environments.
- **Service integrations:** Leverage managed services for Kafka (e.g., AWS MSK, Azure Event Hubs) when appropriate.

## Exploring other anomaly detection methods

### Deep learning models

**LSTM Networks (Long Short-Term Memory):**

- Capable of learning long-term dependencies in time series data.
- Useful for complex patterns and sequences.

**Autoencoders**

- Neural networks trained to reconstruct input data.
- Anomalies are detected when reconstruction error exceeds a threshold.

**Clustering techniques**

- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** Identifies clusters and treats outliers as anomalies.

**Implementing advanced monitoring solutions**

- **Elastic Stack (ELK):**
  - **Elasticsearch:** Search and analytics engine.
  - **Logstash:** Data processing pipeline.
  - **Kibana:** Visualisation tool.

`Be careful with Machine Learning auto anomoly detection. It's good but you'll need to ensure you don't brake data privicy or introduce bias`

