# Topic 1 Cloud Fundamentals - 06/03/2025
# Full day lecture

## Cloud Computing History

Started from grid computing, which is solving problems with multiple machines connected as a grid.

The benefits are users can use cloud as a service rather than owning everything themselves and the grid element keeps everything going if one element brakes.

## Introduction to Cloud Computing

### What is Cloud Computing?
Cloud computing is the delivery of computing services—such as storage, processing power, databases, networking, and software—over the internet (the "cloud") instead of using local servers or personal computers.

#### Simple Analogy
Think of cloud computing like renting a car versus buying one:
- **On-Premises (Traditional IT):** You buy a car, maintain it, pay for repairs, and use it whenever needed.
- **Cloud Computing:** You rent a car when required, paying only for the duration you use it. No maintenance, no repairs, just pay-as-you-go.

### A Brief History of Cloud Computing
- **1960s:** Concept of time-sharing on mainframe computers.
- **1990s:** Internet boom led to the rise of web-based applications.
- **2000s:** Amazon Web Services (AWS) launched in 2006, kickstarting modern cloud computing.
- **2010s-Present:** Growth of cloud providers like Microsoft Azure, Google Cloud, and advancements in AI, machine learning, and scalable infrastructure.

![Cloud computing history](https://cdn.prod.website-files.com/5ff66329429d880392f6cba2/63629ae985bdf45474e96a45_History%20of%20Cloud%20Computing%C2%A0.jpg)

### Major Cloud Providers
The cloud computing market is dominated by a few key players:
1. **Amazon Web Services (AWS)** – The leader in cloud services.
2. **Microsoft Azure** – Strong in enterprise and hybrid cloud solutions.
3. **Google Cloud Platform (GCP)** – Known for AI and data analytics.
4. **IBM Cloud** – Focuses on AI and enterprise services.
5. **Oracle Cloud** – Strong in databases and business applications.
6. **Alibaba Cloud** – A leading provider in Asia.

![cloud market leaders](https://cdn.statcdn.com/Infographic/images/normal/18819.jpeg)

## How Cloud Computing Works
Cloud computing works by offering computing resources over the internet. These resources are housed in massive data centers owned by cloud providers. Users can access these services remotely without needing to buy or maintain physical hardware.

### Key Cloud Services
Cloud computing offers various services, generally categorized into three main types:

### 1. **Infrastructure as a Service (IaaS)**
- Provides virtualized computing resources like servers, storage, and networking.
- Example: AWS EC2 (virtual machines), Google Compute Engine.

### 2. **Platform as a Service (PaaS)**
- Provides a development environment with tools for building, testing, and deploying applications.
- Example: Microsoft Azure App Services, Google App Engine.

### 3. **Software as a Service (SaaS)**
- Provides fully functional software applications over the internet.
- Example: Google Drive, Dropbox, Microsoft 365.

## Benefits of Cloud Computing
- **Scalability:** Easily scale resources up or down based on demand.
- **Cost-Effective:** Pay only for what you use; no upfront investment in hardware.
- **Reliability:** High availability and disaster recovery solutions.
- **Security:** Advanced security measures implemented by cloud providers.
- **Flexibility:** Access services from anywhere with an internet connection.

Cloud services are **elastic** meaning they scale up and down

![cloud computing](https://www.chaossearch.io/hs-fs/hubfs/C2020/Graphics/Blog/Cloud%20Data%20Platform%20Architecture/Example%20of%20AWS%20Data%20Lakehouse%20Architecture.png?width=1000&height=586&name=Example%20of%20AWS%20Data%20Lakehouse%20Architecture.png)

### Conclusion
Cloud computing has revolutionized how businesses and individuals access technology. Instead of investing in costly hardware, companies can leverage the cloud to scale efficiently, reduce costs, and focus on innovation.

## Introduction to Cloud Computing Services and Microservices

### What is Cloud Computing?
Cloud computing is the delivery of computing services—such as servers, storage, databases, networking, software, and more—over the internet (the cloud). Instead of owning and maintaining physical data centers or servers, businesses and individuals can use cloud services provided by companies like AWS, Microsoft Azure, and Google Cloud.

#### Benefits of Cloud Computing:
- **Cost-effective**: No need to buy and maintain physical hardware.
- **Scalability**: Easily scale resources up or down based on demand.
- **Reliability**: Cloud providers ensure uptime and data redundancy.
- **Security**: Cloud providers implement robust security measures.

### What are Microservices?
Microservices is an architectural style where an application is built as a collection of small, independent services that communicate with each other. Each microservice is designed to perform a specific function and can be developed, deployed, and scaled independently.

#### Key Characteristics of Microservices:
- **Independence**: Each microservice operates independently.
- **Decentralized Data Management**: Each service manages its own database.
- **Scalability**: Individual microservices can be scaled without affecting the entire system.
- **Technology Diversity**: Different microservices can be built using different programming languages and frameworks.

### How Cloud Computing Supports Microservices
Cloud computing provides the perfect environment for running microservices because of its flexibility and scalability. Some cloud services that support microservices include:

- **Container Services**: Docker and Kubernetes help in deploying and managing microservices.
- **Serverless Computing**: AWS Lambda, Azure Functions, and Google Cloud Functions run microservices without needing to manage infrastructure.
- **Managed Databases**: Cloud providers offer databases optimized for microservices, such as Amazon RDS and Google Firestore.
- **API Gateways**: Services like AWS API Gateway help manage communication between microservices.

### Conclusion
Cloud computing and microservices work together to build modern, scalable, and efficient applications. Microservices break applications into smaller, manageable components, while cloud computing provides the necessary infrastructure to run them seamlessly.

---

`Microsoft Azure Demo`
https://portal.azure.com/#home

---

## Common Misconceptions About Cloud Computing

### 1. **"The Cloud is Just Someone Else’s Computer"**
While this phrase is often used to simplify cloud computing, it doesn't capture its full scope. The cloud is a vast network of distributed data centers, sophisticated management tools, and services that offer scalability, security, and efficiency far beyond a single computer.

### 2. **"Cloud Computing is Not Secure"**
Many believe that storing data in the cloud is less secure than on-premises storage. However, reputable cloud providers implement advanced security measures, including encryption, firewalls, and regular audits, often exceeding what most organizations can afford to implement on their own.

### 3. **"You Lose Control Over Your Data"**
While cloud storage means your data is hosted externally, reputable providers give users extensive control over access permissions, encryption keys, and data backup policies. Cloud providers also comply with stringent data protection regulations.

### 4. **"Cloud Computing is Expensive"**
Cloud computing follows a pay-as-you-go model, meaning you only pay for the resources you use. This can be more cost-effective than maintaining physical servers, as it reduces expenses related to hardware maintenance, power consumption, and IT staff.

### 5. **"Cloud Services Always Require an Internet Connection"**
While an internet connection is typically required to access cloud resources, many cloud services offer offline functionality. Data can be synchronized once connectivity is restored.

### 6. **"All Clouds Are the Same"**
There are different types of cloud environments: public, private, hybrid, and multi-cloud. Each has different use cases and benefits, depending on the needs of the business.

### 7. **"Migration to the Cloud is Too Complex"**
While cloud migration requires planning, many cloud providers offer tools, services, and expert guidance to streamline the process. A phased approach can help organizations transition smoothly without major disruptions.

### 8. **"Cloud Computing is Only for Large Companies"**
Small businesses and startups can benefit significantly from cloud computing, as it allows them to scale resources as needed without large upfront investments in hardware.

### 9. **"Once in the Cloud, You're Locked In"**
Many cloud providers support multi-cloud and hybrid-cloud strategies, allowing businesses to distribute workloads across different providers to avoid vendor lock-in.

### 10. **"The Cloud is a Fad"**
Cloud computing is a foundational technology that continues to evolve and expand. Businesses worldwide rely on it for storage, computing power, artificial intelligence, and much more.

