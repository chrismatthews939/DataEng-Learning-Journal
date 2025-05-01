# Topic 3 - APIs and microservices for data engineers 01/05/2025

## APIs and Microservices in Data Engineering

### What is an API?
**API** stands for **Application Programming Interface**. In simple terms, it's a way for different software programs to talk to each other.

> Think of an API as a waiter in a restaurant. You (the client) tell the waiter what you want (a request), and the waiter brings it to the kitchen (the server), then returns with your food (the response).

In data engineering, APIs are often used to:
- Access external data sources (e.g., social media, financial data, weather).
- Send or receive data between systems.
- Trigger data processing tasks.

### What is a Microservice?
A **microservice** is a small, independent program that does one specific thing very well. It's part of a larger system but runs on its own.

> Imagine a factory where each worker does just one task—cutting, painting, or packing. Each worker is a microservice. Together, they make a complete product.

In data engineering, microservices might:
- Extract data from a database.
- Transform data into a cleaner format.
- Load data into a data warehouse.

---

## ⚙️ How They Work Together

Let’s look at an example in a data pipeline:

1. **Microservice A** connects to a weather API and downloads weather data every hour.
2. **Microservice B** cleans the raw data (e.g., removes errors or fills in missing values).
3. **Microservice C** loads the cleaned data into a cloud data warehouse (like Snowflake or BigQuery).
4. Another system (like a dashboard or analytics tool) uses **an API** to query the warehouse for reports.

Each step can happen independently, and each microservice communicates via APIs or messaging queues (like Kafka).

---

## ✅ Benefits

### APIs
- **Easy Integration**: Connects systems regardless of language or platform.
- **Real-time Access**: Fetch live data when needed.
- **Reusable**: One API can serve multiple apps or services.

### Microservices
- **Scalable**: Each service can grow independently (e.g., handle more data).
- **Maintainable**: Easier to update or fix one part without breaking everything.
- **Flexible**: Use different programming languages or databases for each service.
- **Resilient**: One microservice can fail without crashing the whole system.

---

## 🧠 Summary

| Concept       | What it is                        | Role in Data Engineering                |
|---------------|-----------------------------------|-----------------------------------------|
| API           | A way for software to communicate | Access and share data across systems    |
| Microservice  | A small, independent program      | Performs specific tasks in data pipelines |

---

## 📌 Final Thought
APIs and microservices let data engineering systems be modular, scalable, and efficient—just like building with Lego blocks instead of one giant machine.

---

## Microservices Architecture 

### 📘 What is Microservices Architecture?

**Microservices architecture** is a way of designing software systems where the application is divided into small, independent services. Each service focuses on a specific business function and can be developed, deployed, and scaled independently.

Each microservice:
- Runs its own process
- Communicates with other services over a network (often via HTTP/REST or messaging)
- Can be written in a different programming language or use a different data store

> 🧠 Think of it like a company with many specialized teams — each doing one thing well, but working together to deliver a complete product.

---

### 🏗️ Comparison with Other Architectures

#### 1. **Monolithic Architecture**

- **Definition**: The entire application is built as one large unit where all parts are interconnected.
  
**Pros**:
- Simple to develop at first
- Easy to deploy (just one application)
- Good performance (no inter-service communication)

**Cons**:
- Difficult to scale specific parts
- Hard to understand and modify as it grows
- One bug can bring down the entire application
- Slows down development (all teams work on one codebase)

---

#### 2. **Microservices Architecture**

- **Definition**: The application is divided into many small, self-contained services, each responsible for a specific feature or task.

**Pros**:
- Easier to scale parts independently
- Faster development (teams work in parallel)
- Better fault isolation (if one service fails, others continue)
- Can use different tech stacks per service

**Cons**:
- Complex to design and maintain
- Requires DevOps and monitoring setup
- Network latency and failures can occur between services
- Data consistency can be harder to manage

---

#### 3. **Serverless Architecture** *(Bonus)*

- **Definition**: Code is deployed as functions and run on-demand in the cloud. No need to manage servers.

**Pros**:
- Very scalable and cost-efficient
- No infrastructure management
- Ideal for event-driven tasks

**Cons**:
- Vendor lock-in (dependent on cloud provider)
- Cold starts can delay response time
- Not ideal for long-running processes

---

### 🧩 When to Use Microservices?

Use microservices when:
- Your team is large and needs to work independently
- Your system is complex and growing
- You need to scale different parts separately
- You’re adopting DevOps, CI/CD, or cloud-native patterns

Avoid microservices if:
- Your app is small or simple
- Your team lacks experience with distributed systems

---

### 📦 Summary Table

| Architecture     | Best For                 | Pros                                      | Cons                                   |
|------------------|--------------------------|-------------------------------------------|----------------------------------------|
| Monolithic        | Small to medium apps     | Simple, fast, easy to deploy              | Hard to scale, maintain, debug         |
| Microservices     | Large, complex systems   | Scalable, independent teams, fault-tolerant | Complex setup, inter-service issues    |
| Serverless        | Event-based, on-demand   | Cost-effective, no server management      | Cold starts, limited execution time    |

---

### 🔚 Final Thought

Microservices aren't always the right choice — but for large, scalable, cloud-native apps, they offer a powerful way to build resilient and maintainable systems. Start simple, and evolve your architecture as your app grows.

---

## Understanding the Role of APIs in Microservices Architecture

### What is Microservices Architecture?

Microservices architecture is a way of designing software applications as a collection of small, independent services that work together. Each microservice focuses on a specific business function and can be developed, deployed, and scaled independently.

For example, an e-commerce application might have separate microservices for:
- User accounts
- Product catalog
- Shopping cart
- Payment processing

### What is an API?

API stands for **Application Programming Interface**. It's like a set of rules or a contract that allows different software components to talk to each other.

You can think of an API as a **menu in a restaurant**. The menu provides a list of dishes you can order, along with a description. When you specify what you want, the kitchen (the service) prepares it and returns the result (your meal). You don't need to know how the kitchen works—just how to place an order.

### The Role of APIs in Microservices

In a microservices architecture, each microservice needs a way to communicate with other microservices. This is where APIs come in.

#### 1. **Communication Between Services**
Each microservice exposes an API that defines:
- What data it accepts (inputs)
- What actions it can perform
- What data it returns (outputs)

Other microservices use these APIs to request information or trigger actions. This keeps the system modular and flexible.

#### 2. **Loose Coupling**
APIs help microservices stay **loosely coupled**, meaning they are not tightly dependent on each other’s internal details. They only need to know how to use each other's APIs, not how they are implemented. This makes it easier to update or replace individual services.

#### 3. **Standardization**
APIs follow standard communication protocols, most commonly HTTP with REST (Representational State Transfer), or other formats like gRPC or GraphQL. This standardization helps services interact seamlessly.

#### 4. **External Access**
In addition to internal communication, APIs can also be exposed to the outside world. For example, a mobile app might use an API to fetch product listings from the product microservice.

### Simple Example

Imagine a user places an order on a website:

1. The **Frontend** sends a request to the **Order Service API**.
2. The **Order Service** uses the **User Service API** to verify the user’s identity.
3. It then uses the **Inventory Service API** to check product availability.
4. Finally, it uses the **Payment Service API** to process payment.

Each service is doing its own job but relying on APIs to coordinate the complete process.

### Summary

- Microservices break down an application into smaller, focused parts.
- APIs are the communication bridges that allow these parts to work together.
- They enable modular, maintainable, and scalable systems.
- By using APIs, developers can build complex systems where each part can evolve independently.

Understanding APIs is essential for working with microservices, as they are the glue that holds the architecture together.

---

`An analogy for standardised APIs...
Standardised API are like standardised electrical outlets in the country where you live. If you bought a hairdryer in the UK, you don’t have to wonder if it’s going to work in a hotel in Edinburgh or in Cardiff.
Similarly, standardised APIs allow organisations to quickly plug and unplug microservices as businesses change or scale, without having to recode the entire project and risk a catastrophic failure.`


---

## Building a Serverless Ingestion Microservice with Net-Zero Benefits

### 📘 Scenario Overview

**Fictional Company:** EcoWheels  
**Business:** Electric bike rentals in smart cities  
**Goal:** Collect and process ride data from IoT-enabled e-bikes in a serverless way, aligning with net-zero sustainability goals.

---

### 🔄 What Is an Ingestion Microservice?

An **ingestion microservice** collects data from various sources (like sensors, apps, or APIs) and sends it to a processing or storage system. It's the *first step* in a data pipeline.

A **serverless** microservice means you don’t manage servers—it scales automatically and only runs when triggered.

---

### 🛠️ Tools & Technologies

- **AWS Lambda** – Serverless compute
- **Amazon API Gateway** – HTTP endpoint for receiving data
- **Amazon S3** – Storage for raw data
- **AWS CloudWatch** – Logging & monitoring
- **AWS IAM** – Permissions and security
- **Python** – Programming language
- **Sustainability Principle:** Pay only for what you use = lower carbon footprint

---

### 🌱 Net-Zero Benefit

Serverless architecture helps **reduce idle infrastructure**, a common source of unnecessary energy use. This contributes to your **net-zero carbon goals** by:

- Minimizing always-on servers
- Scaling with demand (less waste)
- Using cloud providers' renewable energy options

---

1. **Choose a Serverless Platform**
- Select a serverless platform (e.g., AWS Lambda, Azure Functions, Google Cloud Functions).
- These platforms automatically manage server provisioning, scaling, and resource allocation.

2. **Define the microservice**
- Identify the specific functionality of your ingestion microservice.
- Keep it focused and independent (single responsibility).

3. **Event-driven architecture**
- Design your microservice to be event-driven.
- Trigger the microservice based on events (e.g., file upload, API request).

4. **Data Ingestion**
- Ingest data from various sources (files, APIs, databases).
- Process the data (e.g., transform, validate, clean).

5. **Net-Zero Benefits**
- Optimise resource usage:
  - Use serverless functions that automatically scale based on workload.
   -Leverage ephemeral instances that spin up and shut down as needed.

- Cost efficiency:
  - Pay only for actual usage (no idle resources).
  - Use reserved capacity for predictable workloads.

- Environmental impact:
  - Serverless platforms manage infrastructure efficiently.
  - Reduced energy consumption due to automatic scaling and resource allocation.

6. **Implement security measures**
- Secure data transmission (HTTPS, encryption).
- Implement access controls (IAM roles, permissions).
- Monitor and audit your microservice for security vulnerabilities.

7. **Testing and monitoring**
- Write unit tests for your microservice.
- Monitor performance, errors, and resource usage.
- Set up logging and alerts.

8. **Deployment and continuous integration**
- Deploy your microservice to the chosen serverless platform.
- Set up CI/CD pipelines for automated deployment and updates.

9. **Documentation**
- Document your microservice’s functionality, endpoints, and usage.
- Include information on how to contribute or extend the microservice.

10. **Net-Zero Pledge**
- Commit to net-zero emissions by offsetting any remaining carbon footprint.
- Consider using renewable energy sources for your serverless infrastructure.

---

### Fine-grained resource allocation

With selective scalability and concurrency come the benefits of detailed control over the resource allocation priorities. In Lambda functions, each (micro)service can have different levels of memory allocation, according to its needs and purposes. Customer-facing services can have higher memory allocated since it will contribute to faster execution times. Internal services that are not sensitive to latency can be deployed with optimised memory settings. The same applies to storage mechanisms. A DynamoDB table or Aurora Serverless database can have different levels of capacity unit allocation according to the needs of the particular (micro)service they are supposed to serve.

---

## API Keys, Service Mesh, and API Gateways

This guide explains three important concepts in modern software development: **API Keys**, **Service Mesh**, and **API Gateways**. These are tools and practices used in managing how software components communicate with each other, especially in cloud and microservices environments.

---

### 1. What is an API Key?

#### ✅ Simple Definition:
An **API key** is like a password that lets a program or app use another service.

#### 🔧 What It Does:
- Identifies **who** is making a request to an API (like a login name for software).
- Can help **limit** how often someone uses an API.
- Used to **track usage** or detect misuse.

#### 🧠 Example:
Imagine a weather app on your phone. When it asks a weather API for the forecast, it includes an API key so the weather service knows which app is making the request.

---

### 2. What is a Service Mesh?

#### ✅ Simple Definition:
A **service mesh** is a tool that helps different parts of an app (called **microservices**) talk to each other **safely**, **reliably**, and **efficiently**.

#### 🔧 What It Does:
- Manages communication between services **automatically**.
- Adds features like **traffic control**, **encryption**, **retries**, and **monitoring**.
- Works in the **background**, so developers don’t need to write extra code for these tasks.

#### 🧠 Example:
In a shopping app, the "checkout" service might need to talk to the "payment" and "inventory" services. A service mesh makes sure these messages are sent properly, even if there's a failure or delay.

---

### 3. What is an API Gateway?

#### ✅ Simple Definition:
An **API gateway** is like a **front door** for all requests going into your app. It helps **manage**, **filter**, and **route** those requests to the correct place.

#### 🔧 What It Does:
- Controls **who** can access your services (authentication).
- Limits request speed to prevent overload (**rate limiting**).
- Combines multiple API calls into one (called **aggregation**).
- Translates or transforms data formats if needed.

#### 🧠 Example:
If your app has services for login, profile, and notifications, the API gateway makes sure each request gets to the right service and applies rules like checking if the user is logged in.

---

### 🔁 How They Work Together:

- The **API key** identifies the client making a request.
- The **API gateway** receives that request and decides where to send it.
- The **service mesh** helps the internal services talk to each other smoothly once the request is inside.

Think of it like:
> 🔑 API Key = Your ID badge  
> 🚪 API Gateway = The front desk/security at a building  
> 🛜 Service Mesh = The internal phone system connecting departments

---

### Final Thoughts:

You don’t need to be an expert in these tools to start building applications, but understanding what they do can help you design better systems and debug issues faster as you grow into larger, more complex projects.

---

## Service Mesh vs API Gateway 

When building modern applications using **microservices**, two tools often come up: **API Gateways** and **Service Meshes**. While they might seem similar at first, they serve different purposes in managing how services communicate with each other.

---

### 🔄 What is an API Gateway?

An **API Gateway** is the **front door** to your microservices.

#### ✅ Key Functions:
- **Routing**: Directs incoming requests to the correct service.
- **Authentication & Authorization**: Verifies users or applications before allowing access.
- **Rate Limiting**: Controls how many requests a client can make.
- **Load Balancing**: Distributes requests evenly among services.
- **Request/Response Transformation**: Modifies headers, formats, or protocols.

#### 📍 Where it lives:
- It sits **at the edge** of your system, handling **external traffic** (from users, mobile apps, etc.).

#### 📦 Example:
When a mobile app requests user data, the request goes through the API Gateway, which authenticates it, routes it to the User Service, and sends back the response.

---

### 🌐 What is a Service Mesh?

A **Service Mesh** manages **internal communication** between microservices.

#### ✅ Key Functions:
- **Service-to-service communication**: Handles how services talk to each other.
- **Traffic Management**: Fine control over routing, retries, and timeouts.
- **Security**: Encrypts traffic between services (mTLS).
- **Observability**: Tracks metrics, logging, and tracing of service interactions.
- **Resilience**: Automatically retries requests or redirects if something fails.

#### 🛠️ How it works:
- Typically uses **sidecar proxies** (like Envoy) deployed alongside each service.
- The mesh handles all communication **transparently**, without needing to modify service code.

#### 📍 Where it lives:
- **Inside** your system, managing **internal traffic** only.

---

### 🔍 Summary of Differences

| Feature                | API Gateway                        | Service Mesh                          |
|------------------------|------------------------------------|----------------------------------------|
| **Main Purpose**       | Manage **external** requests       | Manage **internal** service traffic    |
| **Common Use Case**    | Handling mobile/web requests       | Secure and monitor service-to-service calls |
| **Typical Features**   | Auth, routing, rate limits         | mTLS, retries, metrics, traffic shaping |
| **Deployment**         | One centralized component          | Distributed sidecars with each service |
| **Traffic Type**       | North-South (in/out of cluster)    | East-West (within the cluster)         |

---

### 🧠 Quick Analogy

Imagine your microservices are like buildings in a city:
- The **API Gateway** is the **city gate** — controlling what gets in or out.
- The **Service Mesh** is the **city roads & traffic lights** — managing internal travel between buildings.

---

### ✅ When to Use Each

- Use an **API Gateway** if:
  - You're exposing APIs to clients or external users.
  - You need centralized control over authentication, request transformation, or rate limiting.

- Use a **Service Mesh** if:
  - You have many microservices communicating internally.
  - You want better observability, security, and traffic control between services.

---

### 🔚 Final Thoughts

You don’t always need both, but in large, complex systems, using both **together** makes your application more secure, manageable, and resilient.

API gateway tools or platforms are less likely to be open source. However, most API gateways work with any type of application or architecture.

Conversely, there are many open-source options for service mesh support, such as Istio, Linkerd and Envoy. Keep in mind, however, that some service mesh tools are designed only to work in certain types of environments.

AWS App Mesh only works within the AWS cloud, for example. Other service mesh options, like Linkerd, are built to support microservices that are deployed via Kubernetes.

---

## Understanding API Keys: 

### What is an API?

An **API** (Application Programming Interface) is a set of rules that allows one software application to talk to another. For example, a weather app on your phone might use an API to get current weather data from a remote weather service.

Think of an API as a waiter in a restaurant. You (the app) tell the waiter (the API) what you want, and the waiter brings back the information (like weather data) from the kitchen (the server).

---

### What is an API Key?

An **API key** is like a unique password or ID used when accessing an API. It helps the API provider:

- Identify **who** is using the API.
- **Control** how the API is used (for example, limit how many requests someone can make).
- **Protect** the API from abuse or unauthorized access.

API keys are usually a long string of letters and numbers, something like:

---

`An API key is issued by an API provider and given to a registered API consumer, who includes it with each request. The API server then checks the API key to validate the consumer’s identity before returning the requested data.
API keys are not as effective as other forms of API authentication, such as OAuth and JWT, but they still play an important role in helping API producers monitor usage while keeping sensitive data secure.`

---

## Understanding Different Types of API Keys

If you're just getting started with programming or using APIs (Application Programming Interfaces), you might have come across the term **API key**. An API key is a code that identifies and authenticates an application or user making a request to an API. Think of it like a password for software talking to other software.

There are a few different **types of API keys**, depending on how they're used and what kind of access they grant. Here's a simple breakdown:

---

### 🔑 1. Public API Keys

- **Purpose**: Identify the application making the request.
- **Security**: Not secure by themselves — can be exposed in frontend code.
- **Usage**: Often used with open or limited-access APIs, like Google Maps or YouTube.
- **Example Use Case**: Embedding a map on a website.

📌 *Tip*: These should not be used for anything sensitive because they can be seen by users.

---

### 🔐 2. Private API Keys (Secret Keys)

- **Purpose**: Authenticate the application or user securely.
- **Security**: Must be kept secret — never expose in frontend code.
- **Usage**: Used in server-to-server communication, or when making changes to user data or databases.
- **Example Use Case**: Accessing a payment gateway (like Stripe) from a backend server.

📌 *Tip*: Store these in environment variables or secure storage.

---

### 👤 3. User API Keys (or Access Tokens)

- **Purpose**: Identify and authorize a specific user.
- **Security**: Should be kept secret — often short-lived and used with OAuth.
- **Usage**: Used when a user logs in and gives your app permission to access their data.
- **Example Use Case**: A user authorizing your app to access their Google Drive files.

📌 *Tip*: Usually expires after a time and needs refreshing.

---

### 🧪 4. Test or Sandbox API Keys

- **Purpose**: Used for development and testing.
- **Security**: Safer to use during development — often isolated from live data.
- **Usage**: Used in staging environments or during app development.
- **Example Use Case**: Testing payment processing without real transactions.

📌 *Tip*: These usually have limited or no access to production data.

---

### 🧭 5. Admin or Master API Keys

- **Purpose**: Full access to all features and data in the API.
- **Security**: Extremely sensitive — should never be shared or exposed.
- **Usage**: Used by administrators or internal tools only.
- **Example Use Case**: Managing users, settings, or critical backend features.

📌 *Tip*: Use with extreme caution and only in secure environments.

---

### Summary Table

| Type                 | Use Case                          | Keep Secret? | Common Location       |
|----------------------|-----------------------------------|--------------|------------------------|
| Public API Key       | Identify app for public APIs      | ❌           | Frontend code          |
| Private API Key      | Authenticate app securely         | ✅           | Backend/server         |
| User API Key/Token   | Authenticate specific user        | ✅           | Server or secure client|
| Test/Sandbox Key     | Development and testing           | ✅           | Dev environment        |
| Admin/Master Key     | Full system access                | ✅✅✅        | Internal systems only  |

---

### 🛡️ Best Practices for Using API Keys

#### 1. **Keep It Secret, Keep It Safe**
- **Never share your API keys publicly.**
- Avoid uploading them to GitHub or other version control systems.
- Use a `.gitignore` file to exclude files that contain your API keys.

#### 2. **Use Environment Variables**
- Store API keys in **environment variables** instead of hardcoding them in your code.
- Example in `.env` file:
- Load it in code using a library like `dotenv` (Node.js) or `os.environ` (Python).

#### 3. **Restrict the Key's Permissions**
- Only allow the key to do exactly what it needs—nothing more.
- Use **scopes** or **roles** provided by the API provider to limit access.

#### 4. **Use IP or Domain Restrictions**
- If possible, limit the usage of the API key to specific IP addresses or domains.
- This prevents unauthorized users from using your key even if it's leaked.

#### 5. **Regenerate If Compromised**
- If you think your API key has been exposed, **revoke or regenerate it immediately**.
- Update your application with the new key.

#### 6. **Don’t Log Sensitive Keys**
- Avoid printing or logging your API keys in the console or log files.
- Logs can be shared or stored insecurely without realizing it.

#### 7. **Use Separate Keys for Different Environments**
- Have different keys for **development**, **testing**, and **production**.
- This reduces risk if a key is accidentally exposed during testing.

#### 8. **Rotate Keys Regularly**
- Periodically **rotate** (change) your keys to minimize the impact of a potential leak.
- Update your applications with the new key after rotation.

---

### 📌 Summary

| Best Practice                  | Why It's Important                           |
|-------------------------------|----------------------------------------------|
| Don't hardcode keys           | Prevents accidental leaks                    |
| Use environment variables     | Keeps code clean and safe                    |
| Limit permissions             | Reduces damage if compromised                |
| Set IP/domain restrictions    | Adds an extra security layer                 |
| Revoke compromised keys       | Stops unauthorized access                    |
| Avoid logging keys            | Prevents leaks in logs                       |
| Use separate environment keys | Limits exposure per environment             |
| Rotate keys regularly         | Maintains long-term security                 |

---

### ✅ Final Tips

- Think of your API key like a **house key**. Keep it private, secure, and under your control.
- Follow these practices from the start—it’s easier than fixing a breach later.

---

# Lecture Notes





