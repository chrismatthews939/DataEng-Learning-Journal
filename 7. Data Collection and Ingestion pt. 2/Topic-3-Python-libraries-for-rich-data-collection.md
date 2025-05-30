# Topic 3 Python libraries for rich data collection 29/05/2025

# Getting Started with kafka-python

This guide is for **complete beginners** who want to understand how to use **Kafka** in Python using the `kafka-python` library.

---

## 🧠 What is Kafka?

**Apache Kafka** is a distributed system used for **streaming data** — it allows producers to send data and consumers to read it in **real time**. It's commonly used for:

- Logging systems  
- Real-time analytics  
- Communication between microservices  

---

## 🐍 What is kafka-python?

[`kafka-python`](https://github.com/dpkp/kafka-python) is a Python client for Apache Kafka. It lets you create:

- **Producers**: send messages to Kafka  
- **Consumers**: receive messages from Kafka  

---

## 📦 Installation

Install kafka-python via pip:

```bash
pip install kafka-python
```

> ⚠️ Kafka must be running on your system. If you don’t have Kafka running locally, consider using Docker or a cloud provider like Confluent Cloud.

---

## 📝 Example 1: Kafka Producer (Send Messages)

```python
from kafka import KafkaProducer

# Connect to Kafka on localhost
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send a simple message to topic 'test-topic'
producer.send('test-topic', b'Hello, Kafka!')

# Wait for all messages to be sent before exiting
producer.flush()

# Close the connection
producer.close()
```

### 🔍 Explanation

- `KafkaProducer`: creates a producer client.  
- `bootstrap_servers`: address of the Kafka server (localhost:9092 by default).  
- `.send()`: sends a message (must be bytes, use `.encode()` if it's a string).  
- `.flush()`: ensures all buffered messages are sent before the program ends.  

---

## 📝 Example 2: Kafka Consumer (Receive Messages)

```python
from kafka import KafkaConsumer

# Subscribe to 'test-topic'
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Read messages from the beginning
    group_id='my-group'            # Consumer group ID
)

# Read messages forever
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
```

### 🔍 Explanation

- `KafkaConsumer`: creates a consumer client.  
- `auto_offset_reset='earliest'`: read from the beginning if no offset is stored.  
- `group_id`: consumers with the same group ID share the work (important for scaling).  
- `message.value`: the actual message sent by the producer (in bytes, so decode it).  

---

## 🧪 Example 3: End-to-End Test (Producer + Consumer)

Run this code in two separate Python files or terminals.

### 🔁 Producer (`sender.py`)

```python
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(5):
    message = f"Hello #{i}"
    producer.send('test-topic', message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()
producer.close()
```

### 🔁 Consumer (`receiver.py`)

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='test-group'
)

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
```

---

## 💡 Notes for Beginners

- Kafka topics are like message channels.  
- A **producer** writes to a topic.  
- A **consumer** reads from a topic.  
- Both must agree on the topic name.  
- Messages are sent/received as bytes. Encode strings before sending and decode after receiving.  

---

## ⚙️ Troubleshooting

- Make sure Kafka is **running** and accessible at `localhost:9092`.  
- If using Docker, ensure ports are mapped correctly.  
- Check if the topic exists (`kafka-topics.sh --list`).  

---

## 📚 Resources

- Kafka: https://kafka.apache.org/  
- kafka-python: https://kafka-python.readthedocs.io/  
- Kafka Docker: https://hub.docker.com/r/bitnami/kafka  

---

## ✅ Summary

- Install kafka-python: `pip install kafka-python`  
- Use `KafkaProducer` to send messages.  
- Use `KafkaConsumer` to read messages.  
- Use `.encode()` and `.decode()` to handle string messages.  

---

# Integrating Apache Avro for Data Serialization 

## What is Apache Avro?

**Apache Avro** is a data serialization system that allows you to encode data in a compact binary format. It is often used in big data systems (like Apache Kafka, Hadoop) because it's fast, schema-based, and supports rich data structures.

## Why Use Avro?

- **Compact and efficient** binary serialization.
- **Schema-based**, making data self-describing and interoperable across languages.
- Supports both **schema evolution** and **remote procedure call (RPC)**.
- Language support for Java, Python, C++, and many others.

## Key Concepts

- **Schema**: Describes the structure of your data (like a blueprint).
- **Serialization**: Converting data into a format for storage or transmission.
- **Deserialization**: Reading the data back into its original structure.

---

## Step-by-Step: Integrating Avro in Java

### 1. Add Avro Dependency

**For Maven (`pom.xml`)**:

```xml
<dependency>
  <groupId>org.apache.avro</groupId>
  <artifactId>avro</artifactId>
  <version>1.11.1</version> <!-- Use the latest version -->
</dependency>
```

### 2. Define an Avro Schema

Create a file named user.avsc with the following content:
```json
{
  "namespace": "com.example",
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "age", "type": "int"},
    {"name": "email", "type": ["null", "string"], "default": null}
  ]
}
```

### 3. Generate Java Classes from the Schema
Use the Avro tools JAR to generate Java code:

```bash
java -jar avro-tools-1.11.1.jar compile schema user.avsc ./src/main/java
```

### 4. Serialize Data to Avro Format

Create a Java class AvroSerialize.java:

```java
import com.example.User;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.specific.SpecificDatumWriter;

import java.io.File;

public class AvroSerialize {
    public static void main(String[] args) throws Exception {
        User user = new User();
        user.setName("Alice");
        user.setAge(30);
        user.setEmail("alice@example.com");

        DatumWriter<User> userDatumWriter = new SpecificDatumWriter<>(User.class);
        DataFileWriter<User> dataFileWriter = new DataFileWriter<>(userDatumWriter);
        dataFileWriter.create(user.getSchema(), new File("user.avro"));
        dataFileWriter.append(user);
        dataFileWriter.close();

        System.out.println("Data serialized to user.avro");
    }
}
```

### 5. Deserialize Data from Avro

Create another Java class AvroDeserialize.java:

```java
import com.example.User;
import org.apache.avro.file.DataFileReader;
import org.apache.avro.io.DatumReader;
import org.apache.avro.specific.SpecificDatumReader;

import java.io.File;

public class AvroDeserialize {
    public static void main(String[] args) throws Exception {
        File file = new File("user.avro");
        DatumReader<User> userDatumReader = new SpecificDatumReader<>(User.class);
        DataFileReader<User> dataFileReader = new DataFileReader<>(file, userDatumReader);

        while (dataFileReader.hasNext()) {
            User user = dataFileReader.next();
            System.out.println("Deserialized user: " + user);
        }
        dataFileReader.close();
    }
}
```

### Notes and Tips

- Avro supports schema evolution: You can add/remove fields if you follow backward/forward compatibility rules.
- Avro schemas can be reused across systems and languages.
- Supports JSON and binary encoding, but binary is much more compact.
- Used heavily with Kafka, often via Confluent Schema Registry.

---

# Benefits of Combining Kafka, Python, and Avro

## 🎯 Why Combine Kafka + Python + Avro?

Here are the benefits of using all three together:

### 1. ✅ Data Compatibility with Avro
- Kafka stores data as **bytes**. Without a structure, it’s hard to know what those bytes mean.
- Avro gives each message a **clear schema** (like a blueprint), so **both sender and receiver agree** on the data format.

### 2. ⚡ Performance and Efficiency
- Avro is **compact and fast**, which means less load on Kafka and faster transmission.
- Especially helpful when working with **large or frequent data streams**.

### 3. 🛡️ Data Validation and Safety
- With Avro schemas, your Python producer can check if the data fits the expected format **before sending** it to Kafka.
- This reduces bugs and makes your system more **reliable**.

### 4. 🔄 Easy Schema Evolution
- Avro supports **evolving schemas**, meaning you can add new fields to your data without breaking old consumers.
- This is crucial for long-term projects where your data format might change over time.

### 5. 🔧 Python Tools and Ecosystem
- Python has great support libraries like:
  - `kafka-python` – for Kafka interaction.
  - `fastavro` or `avro-python3` – for reading/writing Avro data.

---

## 🛠️ Example Use Case

Imagine you’re building a system to process user clicks on a website:

1. A Python script captures each click event and serializes it using Avro.
2. It sends that data to a Kafka topic.
3. Another Python service consumes the events from Kafka and analyzes them in real time.

Using Avro ensures the **data format is always consistent**, and using Kafka makes the system **scalable and resilient**.

---

## 🧠 Final Thoughts

Combining Kafka, Python, and Avro gives you:
- Real-time data streaming (Kafka),
- Easy development (Python),
- Reliable and efficient data for

---

# Introduction to Schema Registries 

## What is a Schema Registry?

A **Schema Registry** is a centralized service that manages and stores schemas for data. A **schema** defines the structure of data — what fields it contains, their data types, and how the data is organized.

Imagine you have multiple applications or services that exchange data, for example, messages or events. To make sure everyone understands the data in the same way, you use schemas. A Schema Registry helps keep these schemas organized, versioned, and easily accessible.

---

## Why Use a Schema Registry?

- **Consistency:** Ensures all producers and consumers of data agree on the format.
- **Compatibility:** Helps manage changes to schemas over time without breaking existing consumers.
- **Centralization:** One place to manage all data schemas, avoiding duplication and confusion.
- **Validation:** Data can be validated against the schema before sending or after receiving.

---

## Key Concepts

- **Schema:** A definition of the data structure (e.g., a JSON object with specific fields).
- **Subject:** The name or identifier for a schema, usually related to a topic or data stream.
- **Version:** Each schema can have multiple versions as it evolves.
- **Compatibility:** Rules that control how schema changes affect consumers (e.g., backward compatibility).

---

## How Does It Work?

1. **Producer registers a schema** with the Schema Registry before sending data.
2. The **Schema Registry stores the schema** and assigns it an ID.
3. When the producer sends data, it includes the schema ID.
4. The **consumer fetches the schema** from the registry using the ID to deserialize and understand the data.

---

## Example Scenario

- You have a data stream of user information.
- The schema defines fields like `userId` (integer), `name` (string), and `email` (string).
- Your producer registers this schema.
- Later, you want to add a `phoneNumber` field.
- You update the schema and register a new version.
- The Schema Registry helps ensure consumers that understand the old schema can still read the data (if compatibility rules are set correctly).

---

## Common Schema Formats

- **Avro:** A compact binary format, often used with Kafka.
- **JSON Schema:** Defines the structure of JSON data.
- **Protobuf (Protocol Buffers):** A language-neutral, platform-neutral format.

---

## Basic Terms to Remember

| Term            | Meaning                                      |
|-----------------|----------------------------------------------|
| Schema          | Structure or blueprint of data               |
| Schema Registry | Service to manage and store schemas           |
| Subject         | The logical name for a schema (like a topic) |
| Version         | Incremental updates to a schema                |
| Compatibility   | Rules for how schemas can evolve               |

---

## Getting Started Tips

- Start by defining your data schema clearly.
- Use the Schema Registry API or UI to register your schemas.
- Make sure producers and consumers use the schema IDs from the registry.
- Set compatibility rules to avoid breaking changes.
- Test schema evolution with different versions before deploying.

---

## Summary

A Schema Registry is essential for systems that handle large volumes of data across different applications. It ensures that everyone "speaks the same language" when producing or consuming data, making systems more robust and easier to maintain.

---

# Introduction to Scrapy for Web Data Collection

Scrapy is a powerful and popular Python library used for **web scraping** — that is, extracting data from websites automatically. If you want to collect data from web pages, Scrapy helps you do this efficiently by handling the downloading, parsing, and storing of information.

---

## What is Scrapy?

- **Scrapy** is an open-source framework written in Python.
- It is designed specifically for **web crawling** and **web scraping**.
- Scrapy lets you write small programs called **spiders** that visit websites, extract data, and save it in formats like CSV, JSON, or databases.

---

## Why use Scrapy?

- Handles complex websites with many pages.
- Manages requests efficiently (faster scraping).
- Built-in support for handling sessions, cookies, and logging in.
- Allows you to follow links automatically to scrape entire websites.
- Supports exporting data in multiple formats.
- Has a large community and many plugins/extensions.

---

## Basic Concepts

- **Spider:** A class where you define how to scrape a website (which pages to visit, what data to extract).
- **Selector:** A tool to extract data from HTML or XML using XPath or CSS selectors.
- **Item:** A Python dictionary-like object where scraped data is stored.
- **Pipeline:** Processes scraped data before saving (e.g., cleaning, validation).

---

## How to install Scrapy

To install Scrapy, run this command in your terminal or command prompt:

```bash
pip install scrapy
```

### Creating a simple Scrapy project

Writing your first spider
Here's an example spider that scrapes quotes from http://quotes.toscrape.com, a website designed for scraping practice.

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        # Extract each quote on the page
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # Follow pagination link (next page)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

```

### Running the spider

Run the spider from your terminal:

```bash
scrapy crawl quotes -o quotes.json
```

- crawl quotes runs the spider named "quotes".

- **-o quotes.json** saves the output data to a JSON file.

#### What happens in the example?

The spider starts at the first page of quotes.

The parse method extracts text, author, and tags from each quote.

It follows the "next page" link and repeats until no more pages exist.

Data is saved to quotes.json.

### Summary

Scrapy is a powerful Python tool to scrape data from websites.

You write spiders that tell Scrapy what to scrape and where to go next.

Scrapy handles crawling, downloading, and parsing automatically.

Output data can be saved in various formats.

---

# Implementing data validation and processing with Schema registeries

Ingesting data from various sources can lead to inconsistencies and errors. Implementing data validation ensures that the data conforms to expected formats and values before processing. Schema Registries not only store schemas but can also enforce data validation rules, rejecting data that doesn't match the schema.

The validation process:

In data engineering, ensuring the accuracy and consistency of data is paramount. The validation process plays a crucial role in maintaining data integrity by enforcing strict rules and standards. This section outlines the key steps involved in validating data before it enters the processing pipeline.

These steps are as follows:

1. Define strict schemas: Include data types, required fields, default values, and allowed ranges or patterns.
2. Configure compatibility modes: Set the registry to enforce certain compatibility modes, preventing incompatible schema changes.
3. Implement validation in producers: Producers validate data against the schema before sending. Errors are caught early, reducing downstream issues.

### Use case application

Validating user registration data...

Imagine a social media platform collects user registration data.

Ensuring that all required fields are present and correctly formatted is crucial for account creation.

Here is the Schema Definition they would need for this task:

```json
{

 "namespace": "com.socialmedia",

 "type": "record",

 "name": "UserRegistration",

 "fields": [

  {"name": "user_id", "type": "string"},

  {"name": "email", "type": "string", "logicalType": "email"},

  {"name": "password", "type": "string", "minLength": 8},

  {"name": "age", "type": "int", "minimum": 13}

 ]

}
```

### Implementing logical types and constraints

While Avro doesn't natively support all validation constraints, you can extend schemas or use additional validation logic in your application.

Custom validation example

- Email format: Use regular expressions to validate email addresses.
- Password strength: Check for minimum length and character requirements.
- Age restrictions: Enforce minimum age policies.
- Integrating validation with confluent-kafka-python

Modify the producer code to include validation logic before sending data.

Example:

```python
def validate_user_data(user_data):

  if not re.match(r"[^@]+@[^@]+\.[^@]+", user_data['email']):

      raise ValueError("Invalid email format")

  if len(user_data['password']) < 8:

      raise ValueError("Password must be at least 8 characters long")

  if user_data['age'] < 13:

      raise ValueError("User must be at least 13 years old")

  return True

try:

  validate_user_data(user_data)

  producer.produce(topic='user_registrations', value=user_data)

except ValueError as e:

  log.error(f"Validation error: {e}")
```

---


