# Topic 2 - Schemas and Integration - 31/10/2024
  
## The Relational Data Model in Depth. Different types Keys and Relationships
### Objectives
- Recall knowledge on Relational Data Model’s history and evolution.
- Learn to apply primary and foreign keys to establish database relationships and enforce data integrity.

Primary key
- Unique identifier for records in a table
Foreign key
- fields that match to primary key creating a join

## Understanding Schemas and Metadata
### Objectives
- Make a link from using keys to the emergence of schemas
- Explore schemas in more depth by explaining different types and meanings schemas, and remember the crucial role of metadata in managing data, and that schemas are part of metadata
- Explain star schemas and snowflake schemas and their uses
- Compare and contrast a star schema with other ways of structuring data, e.g. flat file structure, hierarchical model, etc

### Database Schema
What it is?
- Skeletal structure representing a logical view of a database
What it does?
- Describes shape of data and how it relates to other models, tables and databases
Examples
- Star schema
- Snowflake schema
- Fact constellation schema (or galaxy schema)

### SQL Schema
What it is?
- A type of database schema that Encompasses functions, indexes, tables and views in a way that uses the Structured Query Language to define the schema
What it does?
- Help define objects at the logical level
Examples
- Virtual table comprised of columns and rows with foreign keys and primary keys representing relationship between tables

### AI Schema
What it is?
- A framework that standardises how AI models interact with structured data 
What it does?
- Provides a standardised way for AI to interact with data by defining the structure and type of data that an AI model can understand or produce
Examples
- In weather prediction, an AI schema might define fields like “temperature”, “humidity”, etc. The AI model’s output, such as { "temperature": 20, "humidity": 80 }, adheres to this schema, making it easily understandable and usable by other systems

### SEO Schema
What it is?
- Meta information that clearly explains relationships among people, products and thing to web crawlers
What it does?
- Enhance search engine results page visibility for images, videos, FAQs and more
Examples
- Schema markup or labels coded in HTML that add context and share important information about the web pages

### API Schema
What it is?
- Virtual instructions manual amplifying programming processes
What it does?
- Describes RESTful API operations and methods for interacting with APIs
Examples
- API Description Languages (API DL) and OpenAPI standard used to create schema

### Psychology Schema
What it is?
- Mental concepts that provide a guide to cognitive processes and behaviour
What it does?
- Informs individual about what they can expect form experiences and situations
Examples
- Event schemas
- Object schemas
- Person schema
- Self-schemas
- Social schemas

Star schema is a common approach in my org. Using dim tables to create facts tables for order etcs 

## Comparison of SQL databases
### Objectives
- Reminder that data can be transformed displayed in a different way by using data manipulation and transformation techniques in SQL
- Awareness that there are different SQL vendors and slight differences in standards and implementations

Understanding the nuances between different database systems is crucial for optimising data architecture. Amazon Redshift and PostgreSQL offer distinct advantages, but cater to different needs. While PostgreSQL is a widely-used open-source relational database system known for its robustness and flexibility in handling complex SQL operations, Amazon Redshift is a cloud-based data warehousing service optimised for online analytical processing (OLAP) tasks. Redshift is designed to handle large scale data analytics workflows more efficiently than PostgreSQL due to its columnar storage and parallel query execution. The importance of open-source solutions like PostgreSQL cannot be overstated. They provide transparency, flexibility, and a community-driven approach to development, which fosters innovation and provides a safety net against vendor lock-in.

When choosing a database solution, it is essential to consider vendor-specific differences. These can include unique features, performance optimisations, cost implications, and integration capabilities with other tools and services. For instance, Redshift integrates seamlessly with other AWS services, making it a preferable choice for businesses already embedded within the AWS ecosystem.





## Lecture notes


## Topic 2 Reflections
Databases I've encountered at work
- On-prem
  - Oracle, Netezza, Postgres. All of these had thei quirks in relation to syntax and functionailty. Only Postgres is opensourced
- Cloud
  - GCP Bigquery. Some training on bigquery was available but it had to be completed outside of working hours

## Topic 2 Applied Exercise 
K15, K24, K17, B5, B1, S7, S9, S27


