# Topic 9 - Practical Skills - 30/01/2025

## **Docker for Beginners**

### **What is Docker?**
Docker is a tool that allows you to package your application and its dependencies into containers. Containers are lightweight environments that run the same everywhere.

---

### **Benefits of Docker**
- **Consistency:** Solve the "It works on my machine" problem.
- **Portability:** Run containers on any system with Docker installed.
- **Efficiency:** Faster and lighter than virtual machines.
- **Isolation:** Each container is independent.

---

### **How Docker Works**
- **Docker Image:** Blueprint for a container with all application files and dependencies.
- **Docker Container:** Running instance of a Docker image.
- **Dockerfile:** Instructions for building a Docker image.

---

## Introduction to Kubernetes

Kubernetes (often abbreviated as K8s) is an open-source platform for automating the deployment, scaling, and management of containerized applications. It helps you manage applications in a way that allows them to run smoothly across clusters of machines.

### Key Benefits of Kubernetes:

1. **Automated Deployment & Scaling**  
   Kubernetes automatically deploys and scales applications based on traffic or load, reducing manual intervention.

2. **High Availability**  
   It ensures your applications are always available by distributing them across multiple servers, handling failures gracefully.

3. **Easy Management**  
   Kubernetes abstracts the complexity of infrastructure, making it easier to manage your applications and services.

4. **Container Orchestration**  
   Kubernetes manages containers and ensures they are running as expected, eliminating the need to manage each container individually.

5. **Self-Healing**  
   It can detect failures in your application containers and restart them automatically, ensuring your services stay up.

6. **Resource Efficiency**  
   Kubernetes optimizes the usage of computing resources, enabling efficient use of CPU and memory.

7. **Portability**  
   Applications in Kubernetes can run anywhere – on public cloud, private cloud, or even on your local machine.

### Summary
Kubernetes helps manage containerized applications in a reliable, scalable, and automated way, making it ideal for modern cloud-native applications.


## Data Pipeline Security

**Input Validation**: The organisation implemented strict input validation for all forms collecting patient information, preventing malicious input from compromising their systems.

**Encryption**: All patient data, including medical records and personal information, is encrypted both in transit and at rest. This ensures that even if data is intercepted, it remains unreadable to unauthorised parties.

**Authentication and authorisation**: The organisation uses multi-factor authentication (MFA) for accessing sensitive systems and Role-based access control (RBAC) to restrict access to patient data based on user roles. This ensures that only authorised personnel can view or modify patient information.

**Regular Security Audits**: Quarterly security audits are conducted to identify and mitigate vulnerabilities, ensuring that their security measures are up-to-date and effective.

**Monitoring and Logging**: A security information and event management (SIEM) system is in place to monitor and log all activities within their network, allowing them to detect and respond to potential security incidents in real-time.

**Data masking**: In development and testing environments, patient data is masked to prevent exposure of real patient information, ensuring that sensitive data is not compromised.

## Utilising data visualisation for impact

Data visualisation transforms raw data into visual stories that reveal insights and drive decision-making. Effective visualisation can uncover patterns, trends, and relationships that might be missed in raw data. Imagine presenting quarterly sales data to your company's leadership team. Instead of showing raw numbers, you create an interactive dashboard that highlights trends, outliers, and correlations. This visualisation provides clear insights and helps drive strategic decisions.

### Seaborn

Seaborn is a Python library that provides a high-level interface for drawing attractive and informative statistical graphics.

### Plotly

Plotly is a Python library for creating interactive plots. It allows you to build complex visualisations that users can interact with in real-time.

## Writing effective test suites

Effective test suites are essential for ensuring that your code performs as expected and handles edge cases gracefully. Writing robust tests helps maintain the integrity and reliability of your applications. Imagine deploying a critical update to your data pipeline. Without comprehensive tests, you risk introducing bugs that could disrupt data processing and affect downstream applications. How can you ensure your updates don't break existing functionality?

The key concepts of testing

In the realm of software development, testing is a critical process that ensures the reliability and performance of our applications. Among the various types of testing, unit testing holds a special place due to its focus on individual components of an application. This section will delve into the concept of unit testing, providing an example for better understanding and highlighting its importance in reducing the likelihood of bugs.

#### Key concept 1: Unit testing

Unit testing focuses on testing individual components of your application in isolation. It helps catch errors early in the development process. 


**Example**: Writing a unit test for a function that calculates the total price of items in a shopping cart, ensuring it handles various scenarios correctly.


**Importance**: Unit tests validate that each component of your application behaves as expected, reducing the likelihood of bugs.

#### Key concept 2: Integration testing

Integration testing is a critical step in building robust data pipelines, ensuring that different components work together seamlessly. It helps identify bottlenecks and performance issues across the entire pipeline, providing a comprehensive understanding of how well integrated your system is.

Integration testing involves combining individual units or components of your application and testing them as a group. This type of testing is essential for verifying that the interaction between various modules of the pipeline is functioning correctly and efficiently. Integration testing goes beyond unit tests by checking the data flow and communication between different parts of the system.
