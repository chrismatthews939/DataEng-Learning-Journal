# Topic 4 - Administration-and-optimisation - 14/11/2024
  
## Database Administration Best Practices

### Choosing the right Database Management System (DBMS)
- **Scalability** -
Scalability refers to the ability to handle increasing data volumes and user loads
- **Performance** -
Performance focuses on efficient query processing and response times
- **Data consistency** -
Data consistency ensures data integrity and consistency across the database
- **Data consistency** -
Data consistency ensures data integrity and consistency across the database
- **Transaction** -
Transaction support handles concurrent transactions and maintains data consistency

Choosing the right DBMS also requires skilled database administrators with expertise in the chosen DBMS, knowledge of database administration best practices, and the ability to optimise database performance and troubleshoot issues.

Designing for scalability and performance involves considering:

- Data volume and growth rate
- Query patterns and performance
- Partitioning and sharding
- Caching mechanisms
- Monitoring and performance tuning
- Estimating current data volume and expected growth helps in planning for storage capacity and scalability, while considering data archival and retention strategies. Analysing common query patterns and their frequency, identifying performance-critical queries, and optimising queries through indexing, normalisation, and query rewriting are crucial for ensuring optimal performance

### Database Performance Metrics
- **Query performance** -
Poorly formatted or overly general queries can introduce slowdowns
- **User and Query Conflicts** -
Slowdowns can occur when multiple users are accessing the database
- **Business Transactions** -
Look at end-user experience of real-time performance
- **Capacity** -
Consider CPUs, disk performance, memory, configurations and network connections
- **Configuration** -
Be sure to change default settings for elements like buffer and query caches

### 6 Tips to Increase Database Performance
1. Optimise Queries
2. Improve Indexes
3. Defragment Data
4. Increase Memory
5. Strengthen CPU
6. Review Access

Partitioning and sharding techniques distribute data across multiple nodes or servers, either through horizontal partitioning (sharding) based on a key or range or vertical partitioning based on columns or data types. This improves query performance and scalability. Caching mechanisms, such as implementing caching layers (e.g., Redis, Memcached) and storing frequently accessed data in memory, reduce database load and improve response times. Regular monitoring of database metrics, identifying performance bottlenecks and slow queries, tuning database parameters and configurations, and analysing and optimising query execution plans are essential for maintaining optimal performance.

### Security
Implementing security measures is crucial for protecting sensitive data and ensuring data integrity

- **Authentication** -
- **Auditing and logging** -
Slowdowns can occur when multiple users are accessing the database
- **Data integrity verification** -
Implementing regular data backups, testing backup integrity and restore procedures, establishing a disaster recovery plan, and ensuring data availability and minimising downtime are essential for data protection and business continuity
- **Data privacy protection** -
- **Data encryption** -
Data encryption, using strong encryption algorithms and key management, protects sensitive data at rest and in transit, mitigating the risk of unauthorized access and data breaches
- **Authorisation and access controls** -
Access controls and authentication mechanisms, such as setting up user accounts and roles, implementing strong authentication, and restricting access based on the principle of least privilege, help in securing the database. Role-based access control (RBAC) allows defining user roles and permissions, granting access based on user roles and responsibilities, and regularly reviewing and updating role assignments

## SQL and NoSQL Databases

**SQL**
SQL databases are suitable for applications with structured and consistent data, complex queries and transactions, and strong data integrity and consistency requirements. Examples include financial systems, e-commerce platforms, and content management systems

SQL databases enforce ACID properties ensuring:
- Atomicity. Transactions are treated as a single unit of work
- Consistency. Database remains in a consistent state before and after transactions
- Isolation. Concurrent transactions are isolated from each other
- Durability. Committed transactions are permanently stored

- Data relationships in SQL databases are established using primary keys, which uniquely identify each record in a table, and foreign keys, which establish relationships between tables. 
- Normalization is the process of organising data to minimise redundancy and dependency. 
- SQL databases use Structured Query Language (SQL), a standardised language for defining and manipulating relational databases. 
- SQL provides commands for data definition (CREATE, ALTER, DROP) and manipulation (SELECT, INSERT, UPDATE, DELETE), along with powerful querying capabilities with joins, aggregations, and filtering.

**NoSQL**
NoSQL databases are suitable for applications with large volumes of unstructured or semi-structured data, high scalability and performance requirements, and flexible and evolving data schemas. Examples include social networks, real-time analytics, and content delivery networks.

- Designed to handle large volumes of unstructured or semi-structured data.
- Utilise non-relational data models, such as key-value stores (data stored as key-value pairs), document databases (data stored as semi-structured documents like JSON or XML), columnar databases (data stored in columns instead of rows), and graph databases (data represented as nodes and edges in a graph structure).
- Offer a flexible schema, allowing for dynamic and evolving data structures. They follow a schema-less or schema-on-read approach, accommodating unstructured and semi-structured data. 
- NoSQL databases are designed for horizontal scalability across multiple servers, with a distributed architecture for handling large-scale data. They are optimised for high-performance read and write operations. 
- NoSQL databases often prioritise eventual consistency, relaxing strict consistency in favour of availability and partition tolerance. This allows for temporary inconsistencies that are eventually resolved, making them suitable for applications that can tolerate eventual consistency.

### Database Changes: Impacts and Costs 
- **Data stream** -
Changes in upstream database systems can impact downstream applications and data consumers
- **Schema** -
Schema changes, such as adding or modifying columns in SQL databases, may require updates to downstream applications, whereas NoSQL databases have more flexibility to accommodate schema changes
- **Data format** -
Data format changes, such as introducing new data types or changing data representations, may impact data processing pipelines, requiring data engineers to assess the impact and coordinate necessary adaptations
- **Performance** -
Performance optimisations, like indexing or partitioning changes, can affect query performance and resource utilisation, emphasising the importance of monitoring and communication to ensure downstream systems are not adversely affected
- **Processing and storage costs** -
Processing and storage costs vary between SQL and NoSQL databases. SQL databases typically have lower storage costs due to efficient storage of structured data but can have higher processing costs for complex queries involving joins and aggregations. NoSQL databases may have higher storage costs due to the overhead of storing unstructured or semi-structured data but often have lower processing costs for simple queries and high-volume data ingestion. Factors affecting costs include data volume and growth rate, query complexity and frequency, indexing and partitioning strategies, hardware and infrastructure requirements, and licensing and support costs

## Monitoring and Optimising Database Performance
Monitoring metrics:
- **Responce time** -
Query response time measures the time taken to execute and return the results of a query, helping identify slow-running queries that may impact overall performance and optimize query execution and indexing strategies
- **Thoughput** -
Throughput tracks the number of queries or transactions processed per unit of time, measuring the system's capacity to handle a certain workload and identifying performance bottlenecks and scaling requirements
- **Concurrency** -
Concurrency monitors the number of concurrent users or connections accessing the database, ensuring the database can handle the expected level of concurrency and identifying contention issues and optimising resource allocation
- **Resource utilisation** -
Resource utilisation metrics include CPU usage, which monitors the utilisation of CPU resources by the database processes, memory usage, which tracks the memory consumption of the database and its components, and disk I/O, which measures the read and write operations performed on the storage disks. These metrics help in identifying resource-intensive queries and optimising system resources
- **Indexing** -
Indexing effectiveness analyses the usage and performance of indexes, identifies missing or inefficient indexes that impact query performance, and helps optimise indexing strategies based on query patterns

### Monitoring tools

**Query profiling**
Query logging and analysis, also known as query profiling,  involves examining executed queries from users and their performance metrics, analysing query logs to identify slow queries, inefficient patterns of usage, and opportunities for improving things – such as rewriting queries or reshaping tables. Regular performance reviews are conducted to assess database health, identify improvement areas, analyse trends, identify bottlenecks, make data-driven optimization decisions, and collaborate with stakeholders to align performance goals with business requirements.

**Indexing strategies**
Database performance optimisation techniques also include indexing strategies, database configuration tuning, horizontal scaling (sharding), and vertical scaling (adding more computing resources). Indexing strategies focus on creating appropriate indexes on frequently queried columns, choosing the right index types based on data characteristics and query patterns, and monitoring index usage and performance to identify redundant or underutilised indexes.

**Database configuration**
Database configuration tuning involves adjusting database configuration parameters to optimize performance, such as memory allocation, buffer sizes, caching mechanisms, and parallelism settings, based on workload characteristics and hardware resources. Horizontal scaling (sharding) distributes data across multiple database instances or servers, partitioning data based on a key or range to distribute the workload and enable parallel processing and improved scalability for large datasets. Vertical scaling adds more resources (CPU, memory, storage) to a single database server, suitable for scenarios where the database can benefit from increased hardware capabilities but requires careful capacity planning and monitoring to avoid resource saturation.

**Collaboration**
Collaboration between data engineers and database administrators (DBAs) is essential for smooth integration and optimization of databases within the data ecosystem. Data engineers focus on data pipelines, data integration, and overall data architecture, while DBAs specialize in database management, performance tuning, and security. Effective communication, regular discussions on database requirements, performance goals, and optimization strategies, and collaboration on database design, schema changes, and migration plans are crucial. Knowledge sharing, conducting joint performance reviews and analysis sessions, and continuously learning from each other's expertise help improve overall database management.





## Topic 4 Reflections
