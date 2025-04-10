# Topic 7 - Designing full-stack cloud solutions 01/04/2025

## Introduction to full-stack cloud solution designs

![Full stack](https://miro.medium.com/v2/resize:fit:1400/0*cl7fc6pt1MHjIF4K.png)

## 🌐 Full-Stack Cloud Solutions

### 🧠 What is a Full-Stack Cloud Solution?

A **Full-Stack Cloud Solution** refers to an application that includes **both frontend (what the user sees)** and **backend (the behind-the-scenes logic and database)**, all deployed and running on the **cloud** (e.g., AWS, Azure, Google Cloud).

Think of it like building a house:
- **Frontend** is the decoration, furniture, and what people interact with.
- **Backend** is the plumbing, electrical system, and everything under the hood.
- **Cloud** is the land your house sits on — accessible from anywhere!

---

### 🔧 Components of a Full-Stack Cloud Solution

#### 1. Frontend (Client Side)
- **What it is**: The part users interact with — web or mobile apps.
- **Tools/Technologies**:
  - HTML, CSS, JavaScript
  - Frameworks: React, Angular, Vue
  - Mobile: Flutter, React Native

#### 2. Backend (Server Side)
- **What it is**: Handles logic, processing, authentication, etc. APIs and services developed in languages like Python, Node.js, or Java, running on cloud infrastructure
- **Tools/Technologies**:
  - Languages: Node.js, Python, Java, Ruby
  - Frameworks: Express, Django, Spring

#### 3. Database
- **What it is**: Stores data like user info, messages, or orders. Cloud-based databases such as Azure SQL Database, Amazon RDS, or NoSQL databases like MongoDB Atlas.
- **Types**:
  - SQL (e.g., PostgreSQL, MySQL)
  - NoSQL (e.g., MongoDB, Firebase)

#### 4. Cloud Hosting
- **What it is**: Where your app lives online. 
- **Providers**:
  - AWS (Amazon Web Services)
  - Google Cloud Platform (GCP)
  - Microsoft Azure
  - Others: Vercel, Netlify, Heroku
 
#### 5.DevOps Tools
- **What it is**: CI/CD pipelines, monitoring, and logging services integrated into the cloud environment.
- **Providers**:
  - Git
  - GitLab

---

### 🚀 Example Workflow of a Full-Stack Cloud App

1. **Frontend** sends a request when a user signs up.
2. **Backend** receives the request and checks the data.
3. **Database** stores the new user info.
4. A success message is sent back to the **frontend**.
5. All of this is hosted on the **cloud**, so it’s available anywhere.

---

### 🏗️ Tools to Build a Full-Stack Cloud App

| Layer       | Tools/Services                  |
|-------------|----------------------------------|
| Frontend    | React, Next.js, Tailwind CSS     |
| Backend     | Node.js + Express, Django        |
| Database    | MongoDB Atlas, Firebase, Supabase|
| Cloud       | Vercel, Heroku, AWS, Netlify     |

---

### 🧪 Example Tech Stack

- **Frontend**: React
- **Backend**: Node.js + Express
- **Database**: MongoDB Atlas (NoSQL database in the cloud)
- **Deployment**: Vercel (Frontend) + Render or Heroku (Backend)

---

### 🧠 Final Thoughts

- You don’t have to be an expert in everything.
- Start with a small app and deploy it using free cloud platforms.
- Learn by doing — build a to-do app, a blog, or a portfolio.

> A Full-Stack Cloud Solution makes your app **accessible from anywhere**, **scalable**, and **maintainable** — key traits of modern web development.

---

## When Cloud is not needed

- **Cost considerations:** For small-scale applications with predictable, low workloads, on-premises solutions may be more cost-effective in the long run.
- **Regulatory constraints:** Some industries have strict data residency and compliance requirements that necessitate keeping data on-premises.
- **Latency sensitivity:** Applications requiring ultra-low latency might perform better when hosted locally.
- **Existing infrastructure:** Organisations with significant investments in on-premises infrastructure may prefer to maximise their current assets.
- **Security concerns:** Although cloud providers offer robust security, some businesses may have specific security policies that favour on-premises deployment.

---

## Designing and deploying a Python data product dashboard

`Imagine a university struggling to track student performance across departments. Grades, attendance, and engagement metrics are scattered, making it hard for educators to get a complete view. A cloud-based data product dashboard can change this. In this lesson, we'll design and deploy a Python-based dashboard in the cloud for an educational institution.`

### The business scenario

Let's explore a practical example of designing and deploying a Python-based data product dashboard in the cloud, integrating it with visualisation tools like Tableau.

**A dashboard for student performance analysis**

An educational institution wants to create a dashboard to analyse student performance data.
The dashboard should provide insights into grades, attendance, and engagement metrics, helping educators tailor their teaching strategies.

**Here are the steps they took to approach this challenge:**

**1. Data collection and storage**
  - **Data sources:** Use of student information systems, learning management systems, and attendance records.
  - **Data storage:** Use of a cloud-based database like Amazon RDS or Azure SQL Database to store the aggregated data securely.

**2. Backend development**
  - **API development:** Creation of a RESTful API using Python frameworks like Flask or Django to serve data to the frontend and visualisation tools.
  - **Data processing**: The implementation of data processing pipelines to clean, aggregate, and prepare data for analysis.

**3. Frontend development** 
  - **Dashboard interface:** Development of a user-friendly interface using web technologies or visualisation tools.
  - **Visualisation integration:** Use of Tableau's free accounts for students to create interactive visualisations and embed them into the dashboard.

**4. Deployment to the cloud**
  - **Infrastructure setup:** Use of Infrastructure as Code tools like Terraform or AWS CloudFormation to provision resources.
  - **Containerisation:** Containerisation of the application using Docker for consistent deployment.
  - **Cloud services:** Deployment of the application on cloud services like AWS Elastic Beanstalk, Azure App Service, or Google App Engine.

**5. Monitoring costs**
  - **Setup costs:** Tracking expenses related to infrastructure provisioning, including compute instances, storage, and network services.
  - **Running costs:** Monitoring of ongoing expenses, considering data transfer costs, storage growth, and compute usage.
  - **Cost optimisation:** Implementing cost-saving measures like reserved instances, spot instances, or serverless architectures where appropriate.

**6. Supporting net-zero objectives**
  - **Right-sizing instances:** Selecting instance types that match the application's workload to avoid over-provisioning.
  - **Auto-Scaling Policies:** Implementing auto-scaling to adjust resources based on demand, ensuring efficient resource utilisation.
  - **Energy-Efficient Practices:** Use of cloud providers' green data centres and consideration of the environmental impact of resource usage.

**7. Continuous monitoring**
  - **Performance monitoring:** Use of tools like AWS CloudWatch, Azure Monitor, or Prometheus to track application performance metrics.
  - **Logging and alerts:** Implementing logging solutions to capture application logs and set up alerts for critical events.
  - **Health checks:** Configuration of health checks to detect and respond to application issues promptly.
  - **User analytics:** Monitoring user engagement and usage patterns to inform future improvements.

### Monitoring setup and running costs

Effectively managing costs is crucial for the sustainability of cloud solutions. Here are strategies to monitor and optimise costs:

- **Cost monitoring tools:** Utilise cloud providers' cost management tools, such as AWS Cost Explorer or Azure Cost Management, to gain insights into spending.
- **Budget alerts:** Set up budgets and alerts to notify stakeholders when spending exceeds predefined thresholds.
- **Resource tagging:** Tag resources with metadata to track costs associated with specific projects, departments, or environments.
- **Regular reviews:** Conduct periodic reviews of resource utilisation to identify and eliminate waste, such as unused instances or orphaned storage volumes.

### Implementing net-zero practices

Adopting practices that contribute to sustainability goals is not only environmentally responsible but can also lead to cost savings. Let's explore how this can be achieved.

| Right-sizing Instances     | Auto-scaling Policies               |
|-------------|----------------------------------|
| Analyse resource usage to select the most appropriate instance sizes    | Implement auto-scaling groups that adjust the number of running instances based on real-time demand  |
| Avoid over-provisioning, which leads to unnecessary energy consumption and costs  | Schedule scaling actions during predictable periods of high or low activity  |
| Utilise performance data to make informed decisions about scaling   | Use serverless architectures where possible to ensure resources are only consumed when needed |

### Continuous monitoring

Continuous monitoring is essential for maintaining the reliability, performance, and security of cloud applications.

**This includes:**

**1. Key monitoring areas**
  - **Application performance:** Response times, error rates, and throughput.
  - **Security events:** Unauthorised access attempts, vulnerabilities, and compliance violations.
  - **User experience:** Load times, availability, and functionality issues.

**2. Monitoring tools**
  - **Cloud-native services:** AWS CloudWatch, Azure Monitor, Google Cloud Monitoring.
  - **Open-source tools:** Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana).
  - **Third-party solutions:** Datadog, New Relic, Splunk.

**3. Best practices**
  - **Alerting:** Set up actionable alerts with appropriate thresholds to detect anomalies promptly.
  - **Dashboards:** Create customisable dashboards for real-time visibility into system health.
  - **Automation:** Automate responses to certain events, such as scaling actions or restarting services.
  - **Logging:** Implement centralised logging for troubleshooting and compliance auditing.

---

# Lecture

## Introduction to Kusto Query Language (KQL)

### What is KQL?

**Kusto Query Language (KQL)** is a powerful query language used to read and analyze large volumes of structured, semi-structured, and unstructured data. It's primarily used in **Azure Data Explorer** and **Azure Monitor**, including **Log Analytics** and **Application Insights**.

KQL is optimized for high-performance querying and is commonly used to explore telemetry data, logs, and monitoring metrics in cloud applications.

---

### Basic Concepts

- **Tables**: Data in Kusto is organized in tables (like SQL).
- **Columns**: Each table has columns with typed data.
- **Records**: Each row in the table is a record.

---

### Basic Syntax

KQL is **case-sensitive** and follows a **pipe-based** syntax, where each command feeds into the next using `|`.

#### 1. Viewing Data

```kusto
TableName
```

Returns all data from `TableName`.

---

#### 2. Filtering

```kusto
TableName
| where ColumnName == "value"
```

Filters rows where `ColumnName` equals `"value"`.

---

#### 3. Selecting Specific Columns

```kusto
TableName
| project Column1, Column2
```

Returns only `Column1` and `Column2`.

---

#### 4. Sorting

```kusto
TableName
| sort by Column1 desc
```

Sorts the results by `Column1` in descending order.

---

#### 5. Counting Rows

```kusto
TableName
| count
```

Returns the total number of rows in the table.

---

#### 6. Aggregation

```kusto
TableName
| summarize TotalCount = count() by ColumnGroup
```

Groups the data by `ColumnGroup` and counts how many rows are in each group.

---

#### 7. Time Filtering (common in logs)

```kusto
TableName
| where Timestamp > ago(1h)
```

Filters rows where `Timestamp` is within the last hour.

---

#### 8. Combining Clauses

```kusto
TableName
| where ColumnA == "example"
| project ColumnB, ColumnC
| summarize Total = count() by ColumnB
| sort by Total desc
```

A full example combining filtering, projection, aggregation, and sorting.

---

### Notes

- Comments use `//` for single-line comments.
- Strings are in double quotes `"like this"`.
- Date/time functions like `ago()`, `now()` are common for filtering logs.

---

### Where is KQL Used?

- **Azure Log Analytics** (monitoring and diagnostics)
- **Azure Application Insights** (application performance)
- **Microsoft Sentinel** (security log analysis)
- **Azure Data Explorer** (big data analytics)

---

### Learn More

Official documentation: [https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)





