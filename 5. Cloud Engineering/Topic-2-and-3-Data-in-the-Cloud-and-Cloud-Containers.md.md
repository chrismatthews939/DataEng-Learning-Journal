# Topic 2/3 - Data in the Cloud and Containers and Orchestration 13/03/2025

## Introduction to data cloud management 

### Collating and reviewing business requirements for Cloud data movement and storage

Organisations start by cataloguing their existing data assets, identifying data types such as structured data in relational databases, semi-structured data like JSON documents, and unstructured data including images and videos. Recognising the characteristics and sensitivity of each data type is crucial, as it influences storage solutions, access controls, and compliance requirements. Additionally, understanding data volume, velocity, and variety helps in designing scalable and efficient cloud architectures.

### Introduction to cloud compute types and costs

#### Columnar storage and data egress costs

Consider a company using columnar storage like Amazon Redshift or Google BigQuery for data warehousing and analytics. Large datasets might be exported for processing or shared with external partners, leading to substantial egress costs if not managed properly.

Suppose the company needs to transfer 10 terabytes (TB) of data per month out of the cloud. If the provider charges £0.07 per gigabyte (GB) for data egress, the monthly cost would be:

**10,000 GB x £0.07/GB = £700**

Over a year, this amounts to £8,400 solely for data egress of columnar data. Implementing data compression or optimising query practices can reduce the volume of data transferred, thereby lowering costs.

#### Key-value stores and frequent data transfers
Key-value stores, like Amazon DynamoDB or Azure Table Storage, are optimised for high-speed read/write operations. Frequent small data transfers can accumulate significant costs over time.

For example, if an application makes 1 million requests per day, each transferring 1 kilobyte (KB) of data out of the cloud, the daily egress is:

**1,000,000 requests x 1 KB = 1,000 MB = 1 GB**

At £0.07 per GB, the daily cost is £0.07, and the monthly cost (assuming 30 days) is £2.10. While this seems minimal, scaling up the number of applications or request sizes can increase costs significantly.

#### Relational databases and backup costs

Relational databases, used for structured transactional data, may incur egress costs due to data replication, backups, or reporting services accessing data from outside the cloud. Suppose a business performs daily backups of a 50 GB database to an on-premise location.

The monthly egress cost would be:

**50 GB x 30 days v £0.07/GB = £105**

Over a year, this results in £1,260 in egress costs just for backups. Alternatives like in-cloud backups or using data deduplication techniques can help reduce these expenses.

#### Blob storage and media streaming costs

Blob storage, such as Amazon S3 or Azure Blob Storage, holds unstructured data like media files. Streaming or distributing large files can lead to substantial egress charges.

For example, if a media company streams 5 TB of video content to users outside the cloud provider's network each month, the egress cost is:

**5,000 GB x £0.07/GB = £350**

#### Strategies to optimise data egress costs

`Data egress refers to the movement of data out of a network, system, or application, typically to external locations like cloud storage, websites, or email, and is the opposite of data ingress (data moving into the network). `

To optimise data egress costs, businesses can implement strategies such as:

- **Data Compression:** Reducing data size before transfer.
- **Caching:** Storing frequently accessed data closer to the user.
- **CDNs:** Leveraging networks of servers to distribute content efficiently.
- **Data Transfer Acceleration Services:** Using specialised services provided by cloud vendors to reduce costs.

---

## Understanding cloud data access control methods

```
Cloud environments present unique challenges for data access control due to their distributed nature and the variety of services they offer. Traditional network perimeters are less effective in the cloud, necessitating data-centric security measures.

Organisations must balance the need for stringent security with operational efficiency and user convenience. Understanding the different methods available for controlling access in the cloud helps businesses select the most appropriate strategies for their specific needs.
```

### Understanding data access methods

**Attribute-Based Access Control (ABAC)**

Attribute-Based Access Control (ABAC) extends the capabilities of RBAC by incorporating attributes of users, resources, and the environment into access decisions. Attributes can include user department, security clearance level, resource sensitivity, and even contextual factors like time of day or location. ABAC allows for fine-grained access control policies that adapt to dynamic conditions. For example, a policy could permit access to financial data only during business hours and only from within the corporate network. While ABAC offers greater flexibility, it can be more complex to implement and manage due to the increased number of variables involved.

**Shared Keys**

Shared Keys involve using a secret key or password that grants access to a resource, such as a storage account or database. This method is straightforward and easy to implement, allowing quick access without additional authentication mechanisms. However, it poses significant security risks if the key is compromised, as it often provides unrestricted access to the resource. Managing and rotating shared keys can be challenging, especially when multiple users or applications require access. In large environments, this method can lead to poor key management practices and increased vulnerability to attacks.

**Integration with Identity Providers**

Integration with Identity Providers, such as Active Directory (AD) or cloud-based identity services like Azure Active Directory or AWS IAM, allows organisations to leverage existing authentication and authorisation infrastructures. By using identity providers, businesses can enforce consistent security policies across on-premises and cloud environments. Features like single sign-on (SSO), multi-factor authentication (MFA), and password policies enhance security and user experience. Identity provider integration supports both RBAC and ABAC models, providing a flexible framework for access control. However, setting up and maintaining this integration can be complex, particularly in hybrid or multi-cloud environments.

**Shared Access Signatures (SAS)**

Shared Access Signatures (SAS) are tokens that grant delegated access to resources in a controlled and time-limited manner. Originating from the need to provide temporary access without exposing master credentials, SAS tokens specify permissions (e.g., read, write, delete), resource scope (e.g., specific files or containers), and expiration times. This method enhances security by limiting access to what is necessary for a particular task and for a defined period. SAS is particularly useful when sharing resources with external partners, clients, or applications that require restricted access. However, managing SAS tokens requires careful handling to prevent leakage and unauthorised use.

**OAuth 2.0 and OpenID Connect**

OAuth 2.0 and OpenID Connect are open standards for authorisation and authentication, respectively. These protocols enable applications to access resources on behalf of a user without requiring the user's credentials. By utilising access tokens and refresh tokens, OAuth 2.0 allows for secure, delegated access to APIs and services. OpenID Connect builds upon OAuth 2.0 to provide authentication services, verifying user identities. These methods are commonly used in applications that integrate with external services, such as social media platforms or third-party APIs. They enhance security by reducing the need to store sensitive credentials and by enabling granular access scopes.

**Role-Based Access Control (RBAC)**

Role-Based Access Control (RBAC) is a widely adopted approach where permissions are assigned to roles rather than individual users. Users are then assigned to these roles, inheriting the associated permissions. This model simplifies the management of user access, especially in large organisations with many employees. By grouping permissions into roles such as "Data Analyst" or "Database Administrator," organisations can ensure consistency and reduce the risk of privilege creep. RBAC is supported by all major cloud providers, making it a foundational element of cloud security.

### Example Implementation

**Step 1**

Implementing **Role-Based Access Control (RBAC)**
The bank begins by implementing Role-Based Access Control (RBAC) to assign permissions based on job functions. HR managers are granted roles that allow them to access employee data relevant to their responsibilities.

By defining roles such as "HR Manager," "Recruiter," and "Payroll Specialist," the bank ensures that users have appropriate access without over-privileging. This approach simplifies permission management and reduces the risk of unauthorised access.

**Step 2**

**Integration with AD infrastructure**
To enhance security further, the bank integrates the dashboard with its existing **Active Directory (AD)** infrastructure. This integration allows employees to authenticate using their corporate credentials, enabling single sign-on (SSO) and enforcing consistent password policies.

By leveraging AD, the bank can also implement **Multi-Factor Authentication (MFA)**, requiring users to provide additional verification, such as a one-time code sent to their mobile device. This adds an extra layer of security, protecting against credential theft and unauthorised access.

**Step 3**

**Utilising Shared Access Signatures (SAS)**
For situations where external consultants or auditors need temporary access to specific data, the bank utilises **Shared Access Signatures (SAS)**.

By generating SAS tokens with limited permissions and expiration times, the bank can grant access to necessary resources without exposing master credentials or over-privileging users.

For example, an external auditor may receive a SAS token that allows read-only access to compliance reports for a two-week period. This method ensures that access is controlled, monitored, and automatically revoked after the specified time.

**Step 4**

**Implementing Attribute-Based Access Control (ABAC)**
The bank also considers implementing **Attribute-Based Access Control (ABAC)** to manage more complex access scenarios. For instance, access to certain data might be restricted based on the user's department, location, or security clearance level.

By defining policies that incorporate these attributes, the bank can enforce more granular and dynamic access control. While ABAC offers enhanced flexibility, the bank must weigh the increased complexity against the benefits, ensuring that policies are well-defined and manageable.

**Step 5**

**Using OAuth 2.0 for integrating third-party services**
In the development of the HR dashboard, the bank decides to use **OAuth 2.0** for integrating with third-party services, such as training platforms or benefits providers.

By using OAuth 2.0, the bank's application can access external APIs on behalf of users without requiring them to share their credentials.

This enhances security and simplifies the user experience, as employees can seamlessly access integrated services through the dashboard.

```
What can we learn from this case study?

By combining these access control methods, the bank achieves a comprehensive and robust security posture for its HR dashboard.

RBAC and AD integration provide a solid foundation for internal user access management, while SAS tokens offer secure ways to grant temporary access to external parties.

The use of OAuth 2.0 facilitates secure integration with external services, and MFA adds an extra layer of protection against unauthorised access.
```

## Exploring the CQRS pattern and related concepts

In today's data-driven applications, managing data efficiently is paramount for achieving high performance and scalability. One architectural approach that addresses these challenges is the **Command Query Responsibility Segregation (CQRS)** pattern. CQRS separates the operations that modify data (commands) from those that read data (queries), allowing each to be optimized independently. This separation can lead to significant improvements in system responsiveness and scalability, especially in cloud environments where applications must handle large volumes of data and user interactions.

Documenting and reviewing requirements for CQRS

When considering the adoption of the CQRS pattern, it's crucial to thoroughly document and review the requirements to ensure that it aligns with the application's needs. The following steps outline how to approach this process:

1. Identify use cases and business needs

- Determine if the application has distinct read and write workloads that could benefit from separation.
- Assess whether read operations are complex and resource-intensive compared to write operations.
- Consider if the application requires high scalability for either reads, writes, or both.

2. Analyse Data Access Patterns

- Examine how data is accessed and modified within the application.
- Quantify the volume and frequency of read and write operations.
- Identify any performance issues in the current architecture that CQRS could address.

3. Assess Consistency Requirements

- Decide whether eventual consistency between the read and write models is acceptable.
- Understand the impact of potential delays in data propagation from writes to reads.
- Consider if strong consistency is required and how it might be implemented within CQRS.

4. Evaluate Scalability and Performance Goals

- Define the scalability targets for both read and write operations.
- Determine if independent scaling of read and write components would provide significant benefits.
- Set performance benchmarks that the new architecture should meet or exceed.

5. Select Appropriate Technologies

- Choose databases and technologies that align with the specific needs of the read and write models.
- For write operations, consider databases optimized for fast writes and high availability (e.g., key-value stores).
- For read operations, select databases that support complex queries and analytics (e.g., relational databases).

6. Plan Data Synchronisation Mechanisms

- Design how changes in the write model will be propagated to the read model.
- Implement event handling or data replication processes to keep the read model up-to-date.
- Ensure that the synchronization process is reliable and efficient.

7. Consider Development and Maintenance Effort

- Acknowledge that implementing CQRS introduces additional complexity.
- Ensure the development team has the necessary expertise and resources
- Plan for ongoing maintenance and potential challenges in debugging and support.

8. Assess risks and mitigation strategies

- Identify potential risks, such as increased architectural complexity or synchronisation issues.
- Develop strategies to mitigate these risks, including thorough testing and monitoring.
- Evaluate whether the benefits of CQRS outweigh the potential drawbacks.

### Example benefits 

**Performance Improvement:** By separating read and write operations, the bank achieves better performance and responsiveness in both areas.

**Scalability:** Each component can be scaled independently based on demand, optimising resource utilisation.

**Enhanced Reporting:** The read database provides HR managers with faster and more flexible reporting capabilities.

**Auditability:** Event sourcing provides a complete history of changes, aiding in compliance and audit processes.

---

## Evolution of containerisation and orchestration

- 'Works on My Machine' Problem
- Docker, introduced in 2013, revolutionised the software development process by providing a standardised way to package applications with their dependencies, ensuring consistency across environments.
- Rise of DevOps practices
- As applications grew in complexity, managing containers manually became impractical, leading to the development of orchestration tools.
- Kubernetes, originally developed by Google and released as an open-source project in 2014, addressed this challenge by automating the deployment, scaling, and management of containerised applications.
- Serverless computing emerged as another paradigm shift, allowing developers to focus solely on writing code without worrying about the underlying infrastructure.

## The key skill of visual modelling for container design

![taxonomy in docker](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/container-docker-introduction/media/docker-containers-images-registries/taxonomy-of-docker-terms-and-concepts.png)

## Visual Modeling for Container Design

### Introduction

Visual modeling for container design is the practice of representing the architecture and relationships of containerized applications using diagrams. This helps developers and DevOps teams understand how different components interact within a containerized environment.

### Why Visual Modeling?
- **Clarity**: Helps visualize how containers communicate.
- **Scalability**: Assists in planning for growth.
- **Troubleshooting**: Identifies potential failure points.

A simple way to model container design is using diagrams that represent containers, networks, and storage as boxes and arrows.

### Basic Taxonomy in Docker
Before diving into container design, let's understand key Docker concepts:

| **Term** | **Definition** |
|----------|--------------|
| **Container** | A lightweight, standalone, executable software package that includes everything needed to run an application. |
| **Image** | A blueprint or template for creating containers. |
| **Dockerfile** | A script that contains instructions to build a Docker image. |
| **Volume** | Persistent storage that containers can use to save data. |
| **Network** | A virtual network connecting multiple containers for communication. |
| **Container Engine** | Software that runs and manages containers (e.g., Docker, Podman, containerd). |

### Example: Simple Docker Container Design

Consider a basic web application with a database. Here's how we can visually model it:

```
+-----------------+      +----------------+
|  Web Container  | <--> |  DB Container  |
| (Node.js)       |      | (PostgreSQL)   |
+-----------------+      +----------------+
         |                     |
         |                     |
    +-----------------------------+
    |         Docker Network       |
    +-----------------------------+
```

#### Example Docker Compose File
A `docker-compose.yml` file can represent this setup:

```yaml
version: '3'
services:
  web:
    image: node:14
    ports:
      - "8080:8080"
    networks:
      - app-network
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    networks:
      - app-network
networks:
  app-network:
    driver: bridge
```

### Understanding a Container Engine
A **container engine** is responsible for running containers. Examples include:

- **Docker**: Most popular, user-friendly.
- **Podman**: Rootless, daemonless alternative to Docker.
- **containerd**: Lightweight, used internally by Docker.

#### Example: Running a Container with Docker
```sh
docker run -d -p 8080:80 nginx
```
This command:
- Downloads the `nginx` image if not already available.
- Runs it in detached mode (`-d`).
- Maps port 8080 on the host to port 80 in the container.

### Conclusion
Understanding container modeling helps you design scalable, maintainable applications. Visualizing components, using YAML configurations, and working with container engines like Docker will set a strong foundation for managing containers efficiently.

---

# Docker Containers vs Virtual Machines

## Introduction
Docker containers and virtual machines (VMs) are both used to deploy applications, but they operate differently. Understanding their differences helps in choosing the right technology for your needs.

## Key Differences: Docker Containers vs Virtual Machines

| Feature            | Docker Containers       | Virtual Machines (VMs) |
|-------------------|----------------------|----------------------|
| **Architecture**  | Shares the host OS kernel | Has a full OS per VM |
| **Startup Time**  | Fast (seconds)        | Slow (minutes) |
| **Resource Usage**| Lightweight (less RAM/CPU) | Heavy (requires more resources) |
| **Isolation**     | Process-level isolation | Full OS-level isolation |
| **Portability**   | Easy to move across environments | Less portable, OS-dependent |

## Sustainability Considerations
Using Docker instead of VMs can contribute to sustainability by:
- **Reducing hardware usage**: Containers use fewer system resources, meaning less energy consumption.
- **Efficient scaling**: More containers can run on a single machine compared to VMs, reducing infrastructure needs.
- **Faster deployments**: Lower energy use by minimizing idle resources and optimizing load balancing.

## Practical Example: Serverless Deployment with Docker
Serverless computing allows you to run applications without managing servers. AWS Fargate, Google Cloud Run, and Azure Container Instances are examples of serverless container deployment platforms.

### Example: Deploying a Simple App in Serverless Mode
We’ll deploy an Nginx web server using AWS Fargate.

### 1. Define the Container Image
Create a simple `Dockerfile`:
```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

### 2. Push to a Container Registry
```sh
docker build -t my-nginx-app .
docker tag my-nginx-app:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-nginx-app:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-nginx-app:latest
```

### 3. Deploy to AWS Fargate
Define a task definition in `task-definition.json`:
```json
{
  "family": "my-nginx-app",
  "containerDefinitions": [
    {
      "name": "nginx-container",
      "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-nginx-app:latest",
      "memory": 512,
      "cpu": 256,
      "essential": true,
      "portMappings": [
        {
          "containerPort": 80,
          "hostPort": 80
        }
      ]
    }
  ]
}
```

Run the deployment:
```sh
aws ecs create-service --cluster my-cluster --service-name my-nginx-app --task-definition my-nginx-app --launch-type FARGATE
```

## Conclusion
Docker containers are lightweight and efficient compared to virtual machines, making them a more sustainable choice for modern applications. Serverless deployments further optimize resources by scaling only when needed, reducing waste and energy consumption.

---

# Deploying a Simple Python Application: Docker, Kubernetes, and Serverless

## Introduction
Deploying a Python application can be done in several ways. We'll explore three modern approaches:
1. **Docker** – Containerization for consistent deployment.
2. **Kubernetes** – Orchestrating multiple containers at scale.
3. **Serverless** – Deploying without managing infrastructure.

Each technology has unique benefits depending on the application's needs.

## 1. Deploying with Docker

### What is Docker?
Docker, launched in 2013, is a platform that packages applications into lightweight containers, ensuring they run consistently across different environments.

### Setting Up Docker
Install [Docker](https://www.docker.com/) and create a simple Python app.

#### **Step 1: Create a Python App**
Create `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### **Step 2: Create a Dockerfile**
Create `Dockerfile` to define the container:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python", "app.py"]
```

#### **Step 3: Build and Run the Container**
```sh
docker build -t python-app .
docker run -d -p 5000:5000 python-app
```
Visit `http://localhost:5000` in your browser.

---

## 2. Deploying with Kubernetes

### What is Kubernetes?
Kubernetes, created by Google in 2014, is a container orchestration platform that automates deployment, scaling, and management.

Kubernetes, often abbreviated as **K8s**, is an **open-source container orchestration platform**. It was originally developed by **Google** based on their internal system **Borg** and later released as an open-source project in 2014.

### Why Kubernetes?
Before Kubernetes, running multiple containers required complex manual management. Kubernetes automates:

- **Deployment**: Easily launch and scale applications.
- **Load balancing**: Distributes traffic to prevent overload.
- **Self-healing**: Restarts failed containers automatically.
- **Service discovery**: Ensures services can find and communicate with each other.

### Basic Kubernetes Components

| **Component** | **Description** |
|--------------|---------------|
| **Pod** | The smallest unit, containing one or more containers. |
| **Node** | A machine (virtual or physical) running Kubernetes worker processes. |
| **Cluster** | A group of connected nodes. |
| **Deployment** | Manages the lifecycle of pods, ensuring desired state. |
| **Service** | Exposes applications to the network. |

**The sustainability impact**

Kubernetes' ability to auto-scale and self-heal applications contributes to efficient resource utilisation.

By adjusting the number of running instances based on demand, it reduces unnecessary energy consumption and supports net-zero objectives.

### Setting Up Kubernetes Deployment
#### **Step 1: Create a Deployment File**
Create `deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-app
  template:
    metadata:
      labels:
        app: python-app
    spec:
      containers:
      - name: python-app
        image: python-app:latest
        ports:
        - containerPort: 5000
```

#### **Step 2: Apply Deployment**
```sh
kubectl apply -f deployment.yaml
```

#### **Step 3: Expose the Service**
```sh
kubectl expose deployment python-app --type=LoadBalancer --port=5000
```
Check the assigned external IP and visit `http://<EXTERNAL-IP>:5000`.

---

## 3. Deploying Serverless with AWS Lambda

### What is Serverless?
Serverless computing, pioneered by AWS Lambda in 2014, allows developers to deploy functions without managing servers.

**Serverless computing** lets developers run applications without managing infrastructure. It emerged as a cloud-native approach to reduce operational complexity.

### Why Serverless?
With traditional servers or Kubernetes, developers must:
- Manage infrastructure.
- Scale resources manually or automatically.

Serverless removes this burden by:
- **Auto-scaling**: No need to manage instances.
- **Pay-as-you-go**: Costs only for execution time.
- **Event-driven execution**: Runs functions only when triggered.

### Popular Serverless Platforms
- **AWS Lambda** (Amazon Web Services)
- **Google Cloud Functions**
- **Azure Functions** (Microsoft)
- **OpenFaaS** (Open-source alternative)

**Sustainability impact**

Serverless deployments inherently promote efficient resource usage by consuming resources only when functions are executed.

This efficiency reduces energy consumption and supports sustainability goals.

### Setting Up AWS Lambda Deployment
#### **Step 1: Create a Python Handler**
Create `lambda_function.py`:

```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, Serverless!'
    }
```

#### **Step 2: Package and Deploy with AWS CLI**
```sh
zip function.zip lambda_function.py
aws lambda create-function --function-name python-app \
    --runtime python3.9 --role <IAM_ROLE> \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip
```

Invoke the function:
```sh
aws lambda invoke --function-name python-app response.json
cat response.json
```

---

## Conclusion
Each deployment method serves different needs:
- **Docker**: Simple and consistent deployment.
- **Kubernetes**: Best for scaling and managing multiple containers.
- **Serverless**: Ideal for event-driven applications with no infrastructure management.

Choose the approach that best fits your project!

---

# Lecture notes

## Introduction to Containers (Computing)

### What Are Containers?

Containers are a lightweight way to package and run applications. They include everything an application needs to run—code, runtime, libraries, and dependencies—so they work consistently across different environments.

### Why Use Containers?

- **Portability**: Run the same containerized application on any system with a container runtime.
- **Consistency**: Avoid "works on my machine" issues by bundling dependencies.
- **Efficiency**: Containers share the host OS kernel, making them more lightweight than virtual machines (VMs).
- **Scalability**: Easily scale applications up or down.

### Containers vs Virtual Machines

| Feature          | Containers                     | Virtual Machines (VMs) |
|----------------|--------------------------------|-------------------------|
| **Isolation**  | Process-level isolation       | Full OS isolation       |
| **Size**      | Small (MBs)                    | Large (GBs)             |
| **Startup Time** | Fast (seconds)               | Slow (minutes)          |
| **Efficiency** | Shares OS kernel, less overhead | Requires full OS per VM |

### How Containers Work

1. **Images**: A container is created from an image, which is a lightweight, standalone package with all dependencies.
2. **Container Runtime**: A container runtime (e.g., Docker, containerd) runs and manages containers.
3. **Orchestration**: Tools like Kubernetes help manage multiple containers at scale.

### Popular Container Tools

- **Docker**: Most popular containerization tool.
- **Kubernetes**: Manages and scales containerized applications.
- **Podman**: A daemonless alternative to Docker.

### Basic Docker Commands

```sh
# Pull an image
docker pull nginx

## Run a container
docker run -d -p 80:80 nginx

## List running containers
docker ps

## Stop a container
docker stop <container_id>
```

## Conclusion

Containers make it easier to build, deploy, and manage applications in different environments. They are a key technology in modern cloud computing and DevOps practices.

---

## Introduction to Docker

### What is Docker?
Docker is an open-source platform that allows developers to automate the deployment, scaling, and management of applications using **containers**. A container is a lightweight, portable, and self-sufficient unit that includes everything needed to run an application, such as the code, runtime, libraries, and dependencies.

### Why Use Docker?
Docker simplifies the process of creating, deploying, and running applications in different environments without compatibility issues. It ensures that software runs reliably across different computing environments.

### Benefits of Docker

#### 1. **Portability**
- Docker containers include all dependencies, making it easy to run applications across various environments (development, testing, production) without changes.

#### 2. **Lightweight**
- Unlike virtual machines (VMs), containers share the host operating system, making them much more efficient and using fewer system resources.

#### 3. **Consistency Across Environments**
- Ensures that applications run the same way in development, testing, and production environments, reducing the "it works on my machine" problem.

#### 4. **Faster Deployment and Scaling**
- Containers start in seconds, making them much faster than traditional VMs.
- Easily scale applications up or down to handle different workloads.

#### 5. **Isolation**
- Each container runs in its own isolated environment, ensuring that applications do not interfere with each other.

#### 6. **Simplified Dependency Management**
- With Docker, you package dependencies inside containers, eliminating the need to install software manually on different machines.

### Key Docker Components

#### - **Docker Engine**
  - The core software that enables containerization.
  
#### - **Docker Image**
  - A lightweight, stand-alone package that includes everything needed to run a piece of software.

#### - **Docker Container**
  - A running instance of a Docker image.
  
#### - **Docker Hub**
  - A cloud-based registry where users can find and share container images.

### Getting Started with Docker
1. **Install Docker** from [Docker's official website](https://www.docker.com/get-started).
2. **Run a simple container** using:
   ```sh
   docker run hello-world
   ```
3. **List running containers:**
   ```sh
   docker ps
   ```
4. **Stop a container:**
   ```sh
   docker stop <container_id>
   ```
5. **Remove a container:**
   ```sh
   docker rm <container_id>
   ```

### Conclusion
Docker revolutionizes software development by providing a consistent, portable, and efficient way to deploy applications. By using containers, developers can ensure their applications run smoothly in any environment with minimal setup.

For more details, visit the [Docker documentation](https://docs.docker.com/).

---

`Note: A virtual machine is specific to a machine but a container can be run on any laptop or computer`

## Amazon Elastic Container Service (ECS)

### What is Amazon ECS?
Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that allows you to run, manage, and scale containerized applications easily. It supports Docker containers and integrates with AWS services like EC2 and AWS Fargate for flexible deployment.

### How Does Amazon ECS Work?
Amazon ECS enables you to run applications in a containerized environment. Here’s how it works step by step:

1. **Define a Container Image**: You create an image of your application using Docker and store it in a container registry (e.g., Amazon Elastic Container Registry - ECR).
2. **Create a Task Definition**: A task definition is like a blueprint for your containerized application. It specifies container settings like CPU, memory, networking, and environment variables.
3. **Launch a Task or Service**:
   - A **task** runs one or more containers together.
   - A **service** ensures that a specified number of tasks are always running.
4. **Choose a Launch Type**:
   - **EC2 Launch Type**: Runs containers on an Amazon EC2 cluster.
   - **Fargate Launch Type**: Runs containers without managing infrastructure (serverless option).
5. **Manage and Scale**:
   - ECS allows auto-scaling of tasks based on traffic and demand.
   - It integrates with AWS services like Elastic Load Balancing (ELB) and CloudWatch for monitoring and management.

### Benefits of Amazon ECS

- **Fully Managed**: AWS handles infrastructure management, reducing operational overhead.
- **Scalability**: Easily scale applications up or down based on demand.
- **Flexibility**: Supports both EC2 and Fargate launch types, allowing different hosting strategies.
- **Cost Efficiency**: Pay only for the resources you use with Fargate, reducing unnecessary costs.
- **Security**: Integrates with AWS IAM for access control and AWS VPC for secure networking.
- **High Availability**: Distributes workloads across multiple Availability Zones for reliability.

### Conclusion
Amazon ECS simplifies container management by providing a scalable, secure, and cost-effective solution for deploying applications. Whether you use EC2 or Fargate, it ensures that your containerized workloads run efficiently without the complexity of self-managed infrastructure.

![Amazon Elastic Container Service](https://cdn.prod.website-files.com/6340354625974824cde2e195/65a7f6783b833c93eea544a4_Img2.gif)

## Amazon ECS Cluster Options

Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that allows you to run and scale containerized applications. An ECS **cluster** is a logical grouping of resources where your tasks and services are managed.

### Cluster Options in Amazon ECS

ECS offers multiple options for running your clusters, depending on your infrastructure preferences:

#### 1. **Fargate (Serverless)**
- **What it is:** AWS manages the infrastructure, so you don’t need to provision or manage EC2 instances.
- **Best for:** Applications that require scalability without managing servers.
- **Key Features:**
  - No need to manage EC2 instances.
  - Pay only for the compute and memory your containers use.
  - Supports auto-scaling.
  - Works well for microservices and batch jobs.

#### 2. **EC2 (Self-Managed Compute)**
- **What it is:** You provision and manage a fleet of Amazon EC2 instances to run your containers.
- **Best for:** Workloads that need more control over infrastructure.
- **Key Features:**
  - You control the EC2 instances' size, type, and networking.
  - Allows you to use Spot Instances for cost optimization.
  - Suitable for workloads that require custom configurations.

#### 3. **External (On-Premises or Other Cloud Providers)**
- **What it is:** Run Amazon ECS workloads on infrastructure outside AWS, such as on-premises data centers or other cloud providers.
- **Best for:** Hybrid or multi-cloud deployments.
- **Key Features:**
  - Uses **Amazon ECS Anywhere** to manage tasks.
  - Brings ECS features to your own infrastructure.
  - Works with AWS Systems Manager for security and monitoring.

### Choosing the Right Cluster Option
| Option   | Managed by AWS | Customizable | Best Use Case |
|----------|--------------|-------------|--------------|
| **Fargate** | ✅ Yes | ❌ No | Serverless, auto-scaling workloads |
| **EC2** | ❌ No | ✅ Yes | Custom configurations, cost optimization with Spot Instances |
| **External** | ❌ No | ✅ Yes | Hybrid/multi-cloud environments |

### Summary
Amazon ECS provides flexible deployment options, allowing you to choose the best fit for your workload. If you prefer a **fully managed** environment, Fargate is the way to go. If you need **more control**, EC2 clusters allow deeper customization. For **hybrid environments**, ECS Anywhere lets you run containers on external infrastructure.

---

# Cloud Automation and Orchestration: A Beginner's Guide

## Introduction
Cloud automation and orchestration are essential concepts in modern IT operations. They help businesses manage cloud infrastructure efficiently, reduce manual tasks, and improve scalability. This guide provides an overview of these concepts, their benefits, and common tools used in the industry.

---

## What is Cloud Automation?
Cloud automation refers to the process of using scripts, tools, or software to perform tasks in cloud environments without manual intervention. These tasks include provisioning servers, managing networks, configuring storage, and deploying applications.

### Examples of Cloud Automation:
- Automatically provisioning virtual machines
- Scaling resources based on demand
- Managing backups and disaster recovery

---

### What is Cloud Orchestration?
Cloud orchestration is the coordination of multiple automated processes to achieve a seamless workflow. It ensures that different cloud resources, applications, and services interact efficiently.

#### Examples of Cloud Orchestration:
- Deploying an entire application stack with networking, databases, and compute resources
- Managing cloud security policies across different environments
- Handling complex multi-cloud deployments

---

### Benefits of Cloud Automation and Orchestration
#### 1. **Efficiency**
   - Reduces manual work and human errors
   - Speeds up deployment and management

#### 2. **Cost Savings**
   - Optimizes resource usage, reducing operational costs
   - Automates cost management policies (e.g., shutting down unused instances)

#### 3. **Scalability**
   - Enables businesses to grow without infrastructure bottlenecks
   - Supports dynamic scaling based on workload demand

#### 4. **Consistency and Compliance**
   - Ensures standardized configurations across environments
   - Helps enforce security and compliance policies

#### 5. **Improved Security**
   - Automates security patches and updates
   - Reduces vulnerabilities caused by manual errors

---

### Popular Cloud Automation and Orchestration Tools
#### 1. **Terraform** (by HashiCorp)
   - Infrastructure as Code (IaC) tool for managing cloud resources
   - Supports multiple cloud providers (AWS, Azure, Google Cloud)

#### 2. **Ansible** (by Red Hat)
   - Open-source configuration management and automation tool
   - Uses YAML playbooks for simple, agentless automation

#### 3. **Kubernetes**
   - Orchestration platform for containerized applications
   - Automates deployment, scaling, and management of containers

#### 4. **AWS CloudFormation**
   - Automates AWS infrastructure provisioning
   - Uses JSON or YAML templates to define resources

#### 5. **Google Cloud Deployment Manager**
   - Automates resource provisioning on Google Cloud
   - Uses configuration files for defining infrastructure

#### 6. **Azure Resource Manager (ARM)**
   - Manages and automates deployments in Microsoft Azure
   - Uses templates for consistent infrastructure deployment

---

### Conclusion
Cloud automation and orchestration help businesses streamline operations, reduce costs, and improve security. By leveraging tools like Terraform, Ansible, and Kubernetes, organizations can efficiently manage cloud environments and scale their infrastructure with ease.

---

## Best Practices for Automation Tools

Automation tools help streamline repetitive tasks, improve efficiency, and reduce human error. Here are some best practices for using them effectively:

### 1. Define Clear Objectives
- Identify the tasks that need automation.
- Set specific goals such as reducing manual effort, improving accuracy, or increasing speed.

### 2. Choose the Right Tool
- Research different automation tools to find one that fits your needs.
- Consider factors like ease of use, integration capabilities, and scalability.
- Some popular automation tools include:
  - **UI-based automation**: Selenium, UiPath
  - **Task automation**: Zapier, Power Automate
  - **Script-based automation**: Python, Bash scripting

### 3. Start Small and Scale Gradually
- Begin with simple automation tasks to build confidence.
- Test and refine before expanding automation to complex workflows.

### 4. Ensure Proper Documentation
- Keep records of automation scripts, workflows, and configurations.
- Use comments in code to explain complex logic.

### 5. Implement Robust Error Handling
- Plan for potential failures and unexpected issues.
- Use logging and alerts to monitor errors and troubleshoot effectively.

### 6. Maintain Security and Compliance
- Ensure automated processes follow security best practices.
- Avoid storing sensitive information in scripts.
- Comply with industry regulations and organizational policies.

### 7. Monitor and Optimize Regularly
- Continuously track performance and effectiveness.
- Update automation tools and scripts as technology and requirements evolve.

### 8. Test Before Deployment
- Use test environments to validate automation before implementing in production.
- Perform user acceptance testing (UAT) to confirm functionality.

### 9. Encourage Collaboration and Training
- Train team members on how to use and maintain automation tools.
- Foster collaboration between developers, IT, and end-users to improve automation processes.

### 10. Keep an Eye on Emerging Trends
- Stay updated on new automation technologies and best practices.
- Experiment with AI-driven automation for enhanced efficiency.

By following these best practices, you can maximize the benefits of automation tools while minimizing risks and inefficiencies.

---

## Introduction to Apache Mesos

### What is Apache Mesos?
Apache Mesos is an open-source cluster manager that simplifies running applications on a distributed infrastructure. It abstracts CPU, memory, storage, and other computing resources, enabling efficient resource sharing and management across different workloads.

### Key Features
- **Resource Abstraction**: Mesos pools resources from multiple machines and presents them as a single entity.
- **Scalability**: It is designed to handle thousands of nodes efficiently.
- **Fault Tolerance**: Supports leader election and failover mechanisms.
- **Multi-Tenant**: Allows multiple frameworks (like Spark, Kubernetes, and Hadoop) to run on the same cluster.
- **Fine-Grained Resource Sharing**: Allows frameworks to specify resource requirements dynamically.

### How Apache Mesos Works
Mesos operates based on a **two-level scheduling model**:
1. **Resource Offers**: The Mesos Master determines available resources and offers them to registered frameworks.
2. **Task Scheduling**: Frameworks accept offers and schedule tasks on suitable nodes.

#### Architecture
- **Mesos Master**: Central component managing cluster resources and scheduling frameworks.
- **Agents (Slaves)**: Machines that run tasks assigned by frameworks.
- **Frameworks**: Applications (e.g., Apache Spark, Marathon) that request resources and execute workloads.
- **Schedulers**: Components of frameworks that request resources and launch tasks.

### Use Cases
- **Big Data Processing**: Running Apache Spark, Hadoop, and other big data tools.
- **Container Orchestration**: Managing Docker containers efficiently.
- **Machine Learning**: Deploying distributed ML workloads.
- **Web Services**: Running scalable web applications and microservices.

### Comparison with Other Technologies
| Feature         | Apache Mesos    | Kubernetes       | Docker Swarm    |
|----------------|----------------|-----------------|----------------|
| Primary Use    | Cluster Management | Container Orchestration | Container Orchestration |
| Scalability    | Very High       | High            | Moderate       |
| Multi-Tenancy | Yes             | Limited         | No             |
| Fault Tolerance | High           | High            | Moderate       |

### Getting Started
To install Mesos on a Linux-based system:
```sh
sudo apt-get update
sudo apt-get install mesos
```
After installation, start the Mesos master and agent processes:
```sh
mesos-master --work_dir=/var/lib/mesos
mesos-agent --master=<master-ip>:5050
```

### Conclusion
Apache Mesos is a powerful cluster management tool that enables efficient resource sharing across diverse workloads. It is ideal for organizations looking to optimize distributed computing infrastructure.

For more details, visit the [official Apache Mesos documentation](http://mesos.apache.org/).

---

## Kubernetes

### What is Kubernetes?

Kubernetes (often abbreviated as **K8s**) is an open-source platform designed to automate the deployment, scaling, and management of containerized applications. It is used to manage containers, which are lightweight, portable units that contain everything needed to run an application—such as the code, runtime, libraries, and dependencies.

In simpler terms, Kubernetes helps manage **containerized applications** across a cluster of machines.

---

### Why Use Kubernetes?

Before Kubernetes, applications were usually deployed on a single server or a small set of servers. As applications grow, they become harder to manage. Kubernetes helps by providing several features:

- **Scalability**: Automatically adjust the number of containers running based on demand (e.g., more containers when there’s more traffic).
- **Self-Healing**: Automatically restarts or replaces containers if they fail.
- **Load Balancing**: Distributes traffic evenly among containers to ensure smooth performance.
- **Declarative Configuration**: You define your desired state (e.g., which containers should run), and Kubernetes works to ensure that your system matches this state.

---

### Key Concepts in Kubernetes

#### 1. **Pods**

- A **pod** is the smallest unit in Kubernetes and is a group of one or more containers. These containers share the same network and storage resources.
- Typically, containers in the same pod work together, like an app and its associated database.

#### 2. **Nodes**

- A **node** is a machine (physical or virtual) that runs containers. Nodes are part of a Kubernetes cluster.
- There are two types of nodes:
  - **Master node**: Controls and manages the Kubernetes cluster.
  - **Worker node**: Executes the tasks assigned by the master, such as running containers.

#### 3. **Clusters**

- A **cluster** is a collection of nodes that run containerized applications. It consists of at least one master node and multiple worker nodes.

#### 4. **Services**

- A **service** in Kubernetes is an abstraction that defines a set of pods and a way to access them. It enables communication between pods and external clients.
- Services ensure that traffic is routed to the appropriate pods, even when pods are created or destroyed.

---

### Basic Kubernetes Workflow

Here’s how Kubernetes typically works in a basic scenario:

1. **Define Desired State**: You define the desired state of your application using a configuration file (usually written in YAML or JSON). This file specifies which containers should run, how many instances, and how they should be configured.
   
2. **Kubernetes Schedules Work**: The Kubernetes master node schedules tasks to be carried out by worker nodes in the cluster. It ensures the correct number of pods are running and that they meet the desired state.

3. **Monitor and Adjust**: Kubernetes continuously monitors the state of the system. If any pods fail or need to be scaled up or down, Kubernetes automatically adjusts to meet the desired state.

---

### Kubernetes vs Docker

You may have heard of Docker in relation to containers. Docker is a platform that helps developers build, ship, and run containers. While **Docker** is great for creating containers, **Kubernetes** is used to orchestrate and manage them in production environments, especially when you have many containers to manage across multiple machines.

---

### Common Kubernetes Commands

Here are some commonly used `kubectl` commands to interact with a Kubernetes cluster:

```bash
# View cluster nodes
kubectl get nodes

# View pods in the default namespace
kubectl get pods

# Create a resource (e.g., a pod)
kubectl apply -f my-pod.yaml

# View services
kubectl get services

# Get detailed information about a specific pod
kubectl describe pod <pod-name>

# Delete a resource (e.g., a pod)
kubectl delete pod <pod-name>
```
### Conclusion

Kubernetes simplifies the process of managing containerized applications at scale. With Kubernetes, you can automate many tasks involved in application deployment, scaling, and management, which ultimately leads to greater efficiency, reliability, and flexibility.

---

## Reflection

Get in touch with Ingestion team and look at using Kubernetes


