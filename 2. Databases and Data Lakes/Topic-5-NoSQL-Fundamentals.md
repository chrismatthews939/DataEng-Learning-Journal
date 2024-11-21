# Topic 5 - NoSQL Fundamentals - 21/11/2024
  
## Understanding NoSQL databases

### NoSQL
What are NoSQL databases?

NoSQL databases, standing for "Not Only SQL," are a type of database that can store and retrieve data that is modelled in ways other than the tabular relations used in relational databases. 
They are particularly useful when dealing with a large volume of data where the data's nature does not require a relational model.

The importance of NoSQL databases stems from their ability to handle varied data types, including unstructured and semi-structured data. Their flexible and scalable nature makes them ideal for handling large volumes of data, leading to faster, more efficient data processing.

![SQL vs NoSQL](https://cdn-blog.scalablepath.com/uploads/2023/01/sql-vs-nosql-databases-1-1024x576.png)

## Types of NoSQL Databases

The four main types of NoSQL database

The four main types of NoSQL database are as follows:
1. Document databases
2. Key-Value stores
3. Wide-column stores
4. Graph databases

![4 types of NoSQL database](https://media.geeksforgeeks.org/wp-content/uploads/20220405112418/NoSQLDatabases.jpg)


- **Document databases** -
Document databases store data in documents like JSON (JavaScript Object Notation) objects. Each document contains pairs of fields and values. The values can typically be a variety of types including strings, numbers, booleans, arrays, or objects, and their structure doesn't have to be predefined.

  - Example: MongoDB is a popular document database. If you were building a blog, each blog post might be a document. The post title, content, author, and tags might each be different fields in the document.

- **Key-Value stores** -
Key-value stores are the simplest type of NoSQL database. Every single item in the database is stored as an attribute name (or 'key'), together with its value. They are great for caching, session management, and maintaining a shopping cart for an e-commerce website.

  - Example: Redis is a well-known key-value store. In a shopping cart application, each user's cart could be stored as a value with the user's ID as the key.

- **Wide-column stores** -
These databases store data in columns instead of rows which can be quickly searched and aggregated. They can query large data volumes faster than relational databases. They're best for analysing large datasets and are often used in data warehousing and big data space.

   - Example: Cassandra is a column-family NoSQL database. A large telecommunications company might use Cassandra to store call records. The call time, duration, caller id, and receiver id might all be stored in separate columns.

- **Graph databases** -
Graph databases use graph structures (a network of nodes and edges) for semantic queries. Nodes represent entities and edges represent relationships between entities. They are ideal for handling data where relationships are at the core, like social networks, recommendation engines, etc.

  - Example: Neo4j is a popular graph database. In a social network application, each user could be a node and each relationship (like a friend connection) could be an edge.

![Popular NoSQL databases](https://ares.decipherzone.com/blog-manager/uploads/ckeditor_Top%2010%20NoSQL%20Databases%20in%202022.png)

## Discovering MongoDB

### MongoDB
MongoDB Offers
- A flexible schema
- Scalability
- Robust querying capabilities
- A JSON-like document model
- An ability to handle large volumes of unstructured and semi-structured data

### How MongoDB Stores data

- **Collections** -
**Analogous (equivalent) to tables in SQL databases**. A collection holds documents, and does not require its documents to have the same schema.

- **Documents** -
Documents - Consists of key-value pairs and are the basic unit of data in MongoDB. They are analogous to rows in an SQL table but can contain data of any type and structure.

![Mongo DB vs MySQL Naming Conventions](https://media.geeksforgeeks.org/wp-content/uploads/terminology-differences-gfg-1.png)

MongoDB stores data records as Binary JSON (BSON) documents. BSON is a binary representation of JSON documents, it follows the same structure as JSON, though it contains more data types. 
![MongoDB documents are composed of field-and-value pairs and have the following structure:](https://studio3t.com/wp-content/uploads/2018/10/mongodb-document-structure.png)

For the BSON spec see here (https://bsonspec.org/)

For the Mongo spec see here (https://www.mongodb.com/docs/manual/reference/bson-types/)

**Extracting Unstructured Data**
- Extract from: Web pages, logs, multimedia files, social media feeds
- Retrieve with: Web scraping tools, APIs, file parsers
- Complexity: Can be challenging due to the diverse nature of sources and lack of structure
- Tools: Beautiful Soup (for web scraping), multimedia and Machine Learning processing libraries

**Transforming Unstructured Data**
- Nature of data: Includes text, images, videos, logs. No predefined schema
- Cleansing: Text: remove stop words, stemming. Images: resize, normalise
- Enrichment: Extract metadata, sentiment analysis on text, extract features from images
- Transformation: Text: convert to numerical format (TF- IDF, embeddings). Images: convert to pixel values
- Schema evolution: More flexible to changes due to schema-less nature, but ensuring consistency is challenging
- Complexity: Complexity in pre-processing and converting to a structured format
- Tools: Text: NLTK, spaCy. Images: OpenCV, TensorFlow

## Unstructured data from MongoDB to SQL
Before reporting it's best practice to move this data into a SQL database

## Challenges when moving the data into SQL ETL
MongoDB, a NoSQL database, offers flexibility in handling diverse and evolving data structures.
However, when data maturity reaches a point, or structured querying and analysis are required, SQL databases become indispensable.

### Transformation challenges
**Data Quality** 
- Solution: Data cleaning using tools/libraries like pandas
**Computational intensity** 
- Solution: Use efficient algorithms or distribute computation
**Evolution of data** 
- Regularly review transformation logic and maintain modular code

### Loading challenges
**Scalability** 
- Opt for scalable databases or partitioning strategies
**Data integrity** 
- Implement data validation checks before loading
**Performance** 
- Regularly index databases and optimise queries

### Advantages of loading NoSQL data into a SQL database
- Structured querying - SQL databases excel at complex query operations, which can be invaluable for intricate analysis
- Data integrity - SQL databases often enforce ACID (Atomicity, Consistency, Isolation, Durability) properties more strictly
- Integration with Business Intelligence (BI) tools - Many BI tools have built-in connectors and optimisations for SQL databases
- Schema stability - As the business evolves, the data model in MongoDB might undergo frequent changes. SQL databases, with their stable schema, can offer more predictability

## lecture notes
### 

## Topic 5 Reflections



