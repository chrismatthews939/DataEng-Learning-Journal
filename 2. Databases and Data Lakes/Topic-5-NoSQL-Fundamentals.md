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

![4 types of NoSQL dtb](https://media.geeksforgeeks.org/wp-content/uploads/20220405112418/NoSQLDatabases.jpg)


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




## lecutre notes
### 

## Topic 5 Reflections



