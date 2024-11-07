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
- Triggers
  - Database triggers are procedures that automatically execute in response to specific events on a particular table or view in a database. They are used to maintain the integrity of the data across complex business rules and relationships
- Views
  - Views are virtual tables based on SQL queries
- Stored Procedures
  - Stored procedures are SQL code that you can save, so the code can be reused over and over again
- Normalisation
  - Normalisation is a systematic approach of decomposing tables to eliminate data redundancy (repetition) and undesirable characteristics like Insertion, Update, and Deletion Anomalies
- Redundancy
  - In the context of database management, redundancy occurs when the same piece of data is stored in two or more separate places, either within the same database or across multiple databases
- Comprehensive Data Types
  - These are specific kinds of data attributes that define the kind of data a column can hold in a database. They help in accurately describing the data characteristics, such as integers, decimals, dates, or strings, ensuring that data inputs are processed and stored correctly
- Constraint Implementations
  - Constraints in a database ensure the accuracy and reliability of the data in the database. They enforce rules on the data fields, such as primary keys, foreign keys, unique, not null, and check constraints, to maintain data integrity and enforce business rules
- Indexing Strategies
  - These are plans or methods implemented to improve database performance. Indexing strategies involve creating indexes on tables to speed up the retrieval of rows at the cost of additional writes and storage space to maintain the index data structures
- Indexes
  - Indexes are special lookup tables that the database search engine can use to speed up data retrieval
- Database Business Requirements
  - These are specifications derived from business needs that outline what the business intends to achieve with the database
- Database User Requirements
 - These are detailed requirements that describe what the end-users need the database to do, from how data should be input, to how it should be manipulated, accessed, and presented


## Lecture notes


## Topic 3 Reflections
From the notes I think communicating change is something I can improve in my role. We have strict guidelines in place before pushing schema changes to production but I don't think communicating these changes to the team and users is done as best possible.


