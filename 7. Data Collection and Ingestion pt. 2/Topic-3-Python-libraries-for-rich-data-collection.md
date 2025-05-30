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

--

