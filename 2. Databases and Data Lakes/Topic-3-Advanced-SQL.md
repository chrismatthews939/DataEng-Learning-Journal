# Topic 3 - Advanced SQL - 07/11/2024
  
## Impacts of upstream data modelling on downstream experience
5 things to ask before pushing schema change to production
1. Is a change management process embedded into your data engineering workflow?
2. What is the structure of your data organisation?
3. What impact up and downstream will the schema change have? 
4. How will you communicate schema changes with the broader data team?
5. Are you measuring the impact of change management on your organisation?

SQL views are saved code displayed as virtual tables
Stored procedure or SPROC is saved code that executes SQL queries norally updating tables

### CRUD
Create / Insert
Read / Select
Update
Delete

### Data Modelling
Data modelling is the process of creating a visual representation of a system or database, where data objects are defined and relationships between these objects are established. It involves the careful design of data structures and schema to ensure data integrity, efficiency in data handling, and alignment with business requirements. This process helps in organising data as well as promoting a clear understanding of the data flow across systems, which is crucial for effective database and application design.

![Data Model](https://images.javatpoint.com/dbms/images/data-models.png)

### Types of Data Model
- Conceptual Data Model
  - This model provides a high-level overview of the database without delving into technical details. It focuses on the broad structure of the database and the relationships between major entities in the system
  - Used for initial planning and agreement between stakeholders on the major entities and relationships in the system
  - Set business rules here
- Logical Data Model
  - This model describes the data in more detail but without concern for how they will be physically implemented in the database. It includes all entities, their attributes, and relationships, along with key constraints that should apply. It is used to translate the conceptual model into a more technical blueprint that database designers can understand and use
  - Define data types and normalisation
- Physical data mart
  - This model outlines how the database will be physically realised on the storage system. It details the complete structure of the database, including tables, columns, data types, constraints, indexes, and how they are physically stored on disk. This model is used to build the actual database according to the specified performance, security, and storage requirements
  - PKs/FKs
  - Views
  - Indexes
 
### Key Definitions
- **Triggers**
  - Database triggers are procedures that automatically execute in response to specific events on a particular table or view in a database. They are used to maintain the integrity of the data across complex business rules and relationships
- **Views**
  - Views are virtual tables based on SQL queries
- **Stored Procedures**
  - Stored procedures are SQL code that you can save, so the code can be reused over and over again
- **Normalisation**
  - Normalisation is a systematic approach of decomposing tables to eliminate data redundancy (repetition) and undesirable characteristics like Insertion, Update, and Deletion Anomalies
- **Redundancy**
  - In the context of database management, redundancy occurs when the same piece of data is stored in two or more separate places, either within the same database or across multiple databases
- **Comprehensive Data Types**
  - These are specific kinds of data attributes that define the kind of data a column can hold in a database. They help in accurately describing the data characteristics, such as integers, decimals, dates, or strings, ensuring that data inputs are processed and stored correctly
- **Constraint Implementations**
  - Constraints in a database ensure the accuracy and reliability of the data in the database. They enforce rules on the data fields, such as primary keys, foreign keys, unique, not null, and check constraints, to maintain data integrity and enforce business rules
- **Indexing Strategies**
  - These are plans or methods implemented to improve database performance. Indexing strategies involve creating indexes on tables to speed up the retrieval of rows at the cost of additional writes and storage space to maintain the index data structures
- **Indexes**
  - Indexes are special lookup tables that the database search engine can use to speed up data retrieval
- **Subquery**
 - These are detailed requirements that describe what the end-users need the database to do, from how data should be input, to how it should be manipulated, accessed, and presented
- **Database Business Requirements**
  - A query embedded within another SQL query. Subqueries can be used in various clauses, including SELECT, FROM, WHERE, and even JOINs, enabling complex data manipulations in a single operation
- **Database User Requirements**
 - These are detailed requirements that describe what the end-users need the database to do, from how data should be input, to how it should be manipulated, accessed, and presented

### ACID
The ACID properties (Atomicity, Consistency, Isolation, Durability) provide a foundation for reliable database transactions, ensuring that all operations within a transaction are completed successfully or not at all

- Atomicity. Transactions are all or nothing.
- Consistency. Only valid data saved
- Isolation. Transactions do not affect each other
- Durability. Written data will not be lost

## Writing Nested CRUD SQL Queries
CREATE
READ
UPDATE
DELETE

### Nested Queries
Execution: Nested queries run once; correlated queries run for each outer row
Dependency: Nested queries are independent; correlated queries rely on the outer query

SELECT * FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders);

When to use: 
Isolate inner results before the outer query runs

### Correlated Queries
Performance: Correlated queries can be slower due to multiple executions
SELECT * FROM Customers c
WHERE EXISTS (
  SELECT 1 FROM Orders o
  WHERE o.CustomerID = c.CustomerID
);

When to use: 
Compare each outer row against a set of changing values

Performance tips:
- Correlated queries are resource-intensive and may be slower
- Consider rewriting correlated queries as joins for efficiency
- Use correlated queries for complex conditions involving row comparisons
- Understanding and using these queries effectively can improve database query performance

## Joins and Database Normalisation
![SQL Joins](https://i.ytimg.com/vi/Yh4CrPHVBdE/sddefault.jpg)

Cross joins are the product matrix.
![Cartesian product](https://www.cs.mtsu.edu/~xyang/3080/images/cartesian.png)

### Normalisation
Normalisation addresses issues of redundancy and integrity by ensuring that each piece of data is stored only once, thus eliminating data anomalies. It systematically organises data attributes into tables according to dependencies and applies a series of rules, or normal forms

- First Normal Form (1NF)
  - Ensures all columns hold atomic values and each record is unique
- Second Normal Form (2NF)
  - Requires that all non-key attributes are fully functional dependent on the primary key
- Third Normal Form (3NF)
  - Ensures that no transitive dependencies exist between non-key attributes and the primary key
 
### Group by
Aggregates data

### Windowing functions
Provide powerful analytical capabilities over a subset of rows, returning a value for each row in the original set
Window functions operate on a set of rows and return a single value for each row from the underlying query. This is useful for running totals, moving averages, and other cumulative or comparative statistics

Over Clause
Specifies the partitioning and ordering of a data set before the window function is applied

Running Totals and Averages
Commonly used for financial and performance tracking over specific intervals

Frame Specification
Allows the window to be defined over a range of rows relative to the current row, providing flexible data analysis options

## Risks and Disaster Recovery, Shards in Database Systems

**Risk Assessment**
Regularly identifying and assessing risks to data security and system integrity. This involves evaluating potential threats and the likelihood of their occurrence.

**Disaster Recovery Planning**
Developing and implementing plans that ensure data can be recovered and systems restored after a disaster. This includes maintaining backups, having redundant systems in place, and ensuring that staff are trained in recovery procedures.

**Continuous Monitoring and Testing**
Regular testing of disaster recovery procedures to ensure they are effective when needed. Continuous monitoring of system performance and security helps in early detection of issues that could lead to data loss.

**Sharding for Scalability and Performance**
Sharding is a database architecture pattern that involves dividing a larger database into smaller, more manageable pieces, or "shards," which can be spread across multiple servers. This not only enhances the performance but also aids in handling larger datasets efficiently.

**Horizontal Partitioning**
Sharding typically involves dividing a database horizontally, where rows of a database table are held separately, rather than dividing the table schema. Each shard contains the same schema with a different subset of data.

**Load Distribution**
By distributing the data across multiple shards, which can be hosted on separate hardware or networked servers, sharding helps in balancing the load and reducing the response time for data queries.

**Data Locality**
Sharding can improve performance by locating data closer to where it is most frequently accessed, reducing latency and speeding up access times.

### SQL help
**Query optimisations**
https://www.geeksforgeeks.org/best-practices-for-sql-query-optimizations/ 

**Windowing functions**
https://mode.com/sql-tutorial/sql-window-functions 

## Topic 3 Reflections
From the notes I think communicating change is something I can improve in my role. We have strict guidelines in place before pushing schema changes to production but I don't think communicating these changes to the team and users is done as best possible.


