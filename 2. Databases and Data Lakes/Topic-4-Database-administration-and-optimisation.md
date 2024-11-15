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






## Topic 4 Reflections
