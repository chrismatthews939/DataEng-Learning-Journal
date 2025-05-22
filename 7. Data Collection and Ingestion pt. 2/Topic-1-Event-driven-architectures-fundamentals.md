# Topic 1 Event-driven architectures 15/05/2025 (On Holiday this week)

# Introduction to Event-Driven Architectures (EDA)

Event-driven architecture (EDA) is a design pattern used in software systems where components communicate and react to events. It is a powerful and flexible way to build scalable and responsive applications, especially useful in distributed systems like modern web applications, microservices, and cloud-based platforms.

## What Is an Event?

An **event** is simply a signal or message that something has happened. It could be:

- A user action (e.g., clicking a button)
- A change in data (e.g., a new order placed)
- A system update (e.g., a server going down)

Events are typically small messages that describe what happened, and possibly include some context (like a timestamp or additional data).

## Core Concepts

Here are the main concepts you need to understand in EDA:

### 1. Event Producers
These are the components that **generate** or **publish** events. For example, a user interface might publish an event when a user submits a form.

### 2. Event Consumers
These are the components that **listen for** and **react to** events. They take action based on what the event indicates. For instance, a billing service might react to an "OrderPlaced" event by generating an invoice.

### 3. Event Channel (or Event Bus)
This is the **medium** through which events are transmitted from producers to consumers. It decouples the two, meaning the producer doesn’t need to know who will consume the event or how.

### 4. Event
This is the **message** itself. It typically includes:
- A type or name (e.g., `UserRegistered`)
- Some data (e.g., user ID, email)
- Metadata (e.g., time of occurrence)

## Why Use Event-Driven Architecture?

Here are some advantages of EDA:

- **Loose Coupling**: Components are independent, making systems easier to maintain and evolve.
- **Scalability**: Each component can scale independently based on demand.
- **Responsiveness**: The system can react in real-time to events.
- **Flexibility**: It’s easy to add or remove features without disrupting the entire system.

## Real-World Analogy

Imagine a **newsletter subscription**:

- When you sign up (event producer), your email is sent to a mailing list system (event).
- That system doesn’t know or care what happens next.
- Multiple departments (event consumers) might be listening: one sends a welcome email, another adds your info to a database, and another triggers a discount offer.

All of this happens **independently**, based on the **event** of "New Subscriber."

## Common Use Cases

- User activity tracking (e.g., logins, clicks)
- E-commerce (e.g., order placed, payment processed)
- IoT systems (e.g., sensor sends data when triggered)
- Microservices communication

## Summary

Event-driven architecture is about **reacting to change**. Rather than having one part of a system call another directly, each part responds to **events** that signal when something interesting has happened. This makes systems more **modular**, **scalable**, and **adaptive**.

Understanding EDA is key to building modern, flexible software systems.

---

# Introduction to Pub-Sub Model and Messaging

## What is Messaging?

**Messaging** is a way for different parts of a software system to communicate with each other by sending and receiving messages. It allows different applications, services, or components to exchange data without being directly connected or dependent on each other.

Think of messaging like sending letters through the mail. You write a letter (message), send it to a recipient, and they read it when they get it. The sender and the receiver don't have to talk directly or even be active at the same time — the message is delivered asynchronously.

---

## What is the Pub-Sub Model?

**Pub-Sub** stands for **Publish-Subscribe**, and it's a popular messaging pattern used in software systems. It helps decouple the sender (publisher) of a message from the receiver (subscriber).

### How It Works:

1. **Publisher**: A component that sends messages (or "publishes" them) to a common channel or topic.
2. **Subscriber**: A component that receives messages (or "subscribes" to a topic) and acts on them.
3. **Message Broker**: A system that manages the flow of messages from publishers to subscribers. It keeps track of who is subscribed to what and ensures messages are delivered.

### Analogy:

Imagine a radio station:
- The radio station **broadcasts** music (publishes messages).
- Anyone with a radio tuned to that station **hears the music** (subscribes to the topic).
- The station doesn’t know who is listening — and it doesn’t care. It just sends out the music.

That’s the essence of **pub-sub**: the publisher doesn’t know who the subscribers are, and the subscribers don’t know (or care) who is publishing the messages. They are decoupled.

---

## Key Benefits

- **Decoupling**: Publishers and subscribers are independent of each other.
- **Scalability**: New subscribers can join without changing the publisher.
- **Flexibility**: Messages can be processed by multiple subscribers in different ways.
- **Asynchronous Communication**: Components don’t need to operate at the same time.

---

## Common Use Cases

- **Notification systems**: When an event happens (like a new email), notify multiple services or users.
- **Data pipelines**: Stream data from one part of a system to another.
- **Microservices**: Allow services to communicate without tight integration.
- **Event-driven architecture**: Build systems that react to events in real time.

---

## Summary

The **Publish-Subscribe (Pub-Sub)** model is a powerful and flexible messaging pattern that promotes loose coupling between components. By using a message broker and channels (or topics), it allows messages to be shared efficiently and asynchronously across systems.

It’s like a broadcasting system for software: one talks, many can listen — and none of them need to know about each other directly.

--

# Introduction to Apache Kafka 

## What is Apache Kafka?

Apache Kafka is a **distributed event streaming platform** used to build real-time data pipelines and streaming applications. It is capable of handling **high volumes of data**, enabling systems to **communicate with each other** in real-time, efficiently and reliably.

In simpler terms, Kafka helps applications send, receive, store, and process **streams of records** (data) in real-time, like a **messaging system** but much more powerful and scalable.

---

## A Brief History

- **Created at LinkedIn (2010):** Kafka was originally developed by engineers at LinkedIn to handle large-scale activity stream data and log processing.
- **Open-Sourced (2011):** Kafka was open-sourced under the Apache Software Foundation and quickly gained popularity.
- **Apache Top-Level Project (2012):** Kafka became a top-level project within the Apache Software Foundation.
- **Ecosystem Growth:** Over time, Kafka grew into a larger ecosystem with tools like Kafka Connect, Kafka Streams, and integration with various big data and cloud systems.
- **Confluent:** Some of the original creators of Kafka later founded Confluent, a company that provides commercial Kafka-based products and support.

---

## Core Concepts

To understand Kafka, it’s essential to grasp a few key concepts:

### 1. **Producer**
A **producer** is any application or service that **sends data** to Kafka. It **publishes messages** to Kafka **topics**.

### 2. **Consumer**
A **consumer** is any application or service that **reads data** from Kafka topics. It **subscribes** to one or more topics and processes the incoming data.

### 3. **Topic**
A **topic** is a named channel where data is published. Think of it as a **category** or **feed** to which messages are sent and from which consumers read.

- Topics can have multiple **partitions** to allow parallelism and scalability.
- Topics are **append-only** logs; new messages are always added to the end.

### 4. **Partition**
Each topic is split into **partitions**, which are ordered, immutable sequences of messages.
- Partitions allow Kafka to **scale horizontally**.
- Each message within a partition has a unique **offset** (a sequential ID).

### 5. **Broker**
A **broker** is a single Kafka server that stores data and serves clients (producers and consumers). Kafka clusters are made up of multiple brokers.

### 6. **Cluster**
A **Kafka cluster** is a group of brokers working together. Clustering enables Kafka to handle **more data**, provide **fault tolerance**, and support **high availability**.

### 7. **Offset**
An **offset** is a unique identifier for each message within a partition. Consumers use offsets to keep track of which messages they have already read.

### 8. **ZooKeeper** *(legacy, being phased out)*
Kafka traditionally used **Apache ZooKeeper** to manage configuration,

---

# Introduction to Kafka Clusters 

![Kafka cluster](https://www.altoros.com/blog/wp-content/uploads/2018/03/Multi-cluster-deployment-Apache-Kafka-v11.gif)

## Kafka Cluster: The Big Picture

A **Kafka cluster** is a group of servers working together to handle this messaging system. Here's what makes it up:

### 1. **Brokers**

- Each server in a Kafka cluster is called a **broker**.
- A broker receives, stores, and sends messages.
- Brokers work together to share the load and make the system reliable and scalable.
- A single Kafka cluster usually has **multiple brokers**.

### 2. **Topics**

- Messages are organized into **topics**.
- A topic is like a category or folder.
- Producers send messages to a topic.
- Consumers read messages from a topic.

> Example (not code): If you're logging data from different services, you might have topics like `website-logs`, `app-logs`, and `database-logs`.

### 3. **Partitions**

- Each topic is split into **partitions**.
- Partitions allow Kafka to spread data across multiple brokers, enabling parallel processing and better performance.
- Each partition is a sequence of messages, ordered by time.

### 4. **Producers and Consumers**

- **Producers** are systems or applications that send messages to Kafka.
- **Consumers** are systems or applications that read messages from Kafka.

Kafka allows many producers and consumers to interact with the same topic simultaneously.

### 5. **ZooKeeper (Legacy Component)**

- Kafka clusters used to rely on **Apache ZooKeeper** to manage and coordinate brokers.
- ZooKeeper helped keep track of which broker was doing what.
- However, newer versions of Kafka are moving toward **KRaft mode**, which removes the need for ZooKeeper.

## Why Use a Kafka Cluster?

Kafka clusters are designed to be:

- **Scalable**: Add more brokers as your data grows.
- **Fault-tolerant**: If one broker fails, others can take over.
- **High-throughput**: Handles a large volume of messages quickly.
- **Durable**: Messages are stored reliably until consumed.

## Summary

A Kafka cluster is a powerful system for managing real-time data streams. It consists of:

- **Brokers**: Servers handling data
- **Topics**: Categories for messages
- **Partitions**: Subdivisions of topics for scalability
- **Producers**: Senders of data
- **Consumers**: Receivers of data
- **(ZooKeeper/KRaft)**: Cluster coordination (legacy/new)

Kafka is widely used in industries that require fast, reliable, and scalable data movement—such as tech, finance, healthcare, and retail.

---

