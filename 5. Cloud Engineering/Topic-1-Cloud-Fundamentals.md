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

AWS: Known for its extensive service portfolio and maturity in the cloud market. AWS has a robust ecosystem and a wide range of services catering to diverse needs.

Azure: Strong integration with Microsoft products and services, making it a natural choice for organisations heavily invested in Microsoft technologies.

GCP: Offers competitive pricing and strengths in data analytics and machine learning, leveraging Google's expertise in these areas.

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

---

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

---

## Cloud Computing Data Protection

### What is Cloud Computing?
Cloud computing is the delivery of computing services—like storage, databases, networking, and software—over the internet (the cloud) instead of using local servers or personal computers.

### Why is Data Protection Important in Cloud Computing?
When using cloud services, your data is stored on remote servers. While this makes accessing and managing data easier, it also introduces security risks. Data protection ensures that your information remains safe from loss, theft, and unauthorized access.

### Key Aspects of Cloud Data Protection

#### 1. **Encryption**
   - Encrypts data to make it unreadable without a decryption key.
   - Ensures data is secure both **in transit** (when being sent) and **at rest** (when stored).

#### 2. **Access Control**
   - Uses authentication methods like passwords, multi-factor authentication (MFA), and role-based access control (RBAC).
   - Limits who can access your data.

#### 3. **Backups and Disaster Recovery**
   - Regular backups prevent data loss.
   - Disaster recovery plans help restore data in case of failures, cyberattacks, or natural disasters.

#### 4. **Compliance and Regulations**
   - Cloud providers follow laws like GDPR (for European data protection) and HIPAA (for healthcare data in the U.S.).
   - Ensures data handling follows legal standards.

### 5. **Monitoring and Threat Detection**
   - Uses AI and security tools to detect suspicious activity.
   - Alerts administrators of potential security breaches.

#### 6. **Zero Trust Security Model**
   - Never assumes any user or device is trustworthy by default.
   - Continuously verifies security before granting access.

### How to Protect Your Data in the Cloud
- **Use strong passwords and enable MFA.**
- **Choose a reputable cloud provider with strong security policies.**
- **Encrypt sensitive files before uploading them.**
- **Regularly update security settings and review access permissions.**
- **Have a backup plan to restore data if needed.**

### Conclusion
Cloud computing offers great flexibility and convenience, but data protection is essential to ensure security and privacy. Understanding encryption, access control, backups, and compliance helps keep your information safe in the cloud.

---

## Ethical Big Data Storage

### What is Ethical Big Data Storage?
Ethical big data storage refers to the responsible collection, storage, and management of large datasets while prioritizing privacy, security, and fairness. It ensures that organizations handle data in a way that respects individuals' rights and complies with legal and ethical standards.

### Key Principles of Ethical Data Storage

#### 1. **Privacy Protection**
   - Store only necessary data.
   - Anonymize or encrypt personal information.
   - Follow data protection laws (e.g., GDPR, CCPA).

#### 2. **Security Measures**
   - Use strong encryption methods for data storage and transmission.
   - Implement access controls and authentication mechanisms.
   - Regularly update security protocols to prevent breaches.

#### 3. **Transparency**
   - Clearly communicate data collection and storage practices to users.
   - Allow individuals to access and control their own data.
   - Disclose how data is processed and shared.

#### 4. **Fairness & Bias Prevention**
   - Ensure data is collected and used without discrimination.
   - Regularly audit datasets for biases.
   - Implement fair algorithms to process stored data.

#### 5. **Data Minimization & Retention Policies**
   - Avoid hoarding unnecessary data.
   - Define clear retention policies and delete outdated or unnecessary data.
   - Use techniques like differential privacy to limit excessive data collection.

### Best Practices for Ethical Data Storage

- **Use Secure Cloud Storage:** Opt for trusted cloud providers with strong security certifications.
- **Implement Role-Based Access:** Restrict data access based on user roles to minimize exposure.
- **Regular Audits:** Conduct periodic security and compliance audits.
- **Educate Teams:** Train employees on ethical data handling and security best practices.
- **Obtain Explicit Consent:** Ensure users provide informed consent before data collection.

### Conclusion
Ethical big data storage is essential for maintaining trust, ensuring compliance, and protecting users' rights. By following ethical principles and best practices, organizations can responsibly store and manage big data while mitigating risks related to privacy, security, and fairness.

---

## 8 Data Protection Rights

Data protection laws, like the **General Data Protection Regulation (GDPR)**, give individuals specific rights over their personal data. Here’s a simple breakdown of the **8 data protection rights**:

### 1. The Right to Be Informed
You have the right to know **what personal data** is being collected, **why**, and **how** it will be used. Organizations must provide clear and easy-to-understand privacy notices.

### 2. The Right of Access
You can request a copy of your personal data from organizations. This helps you check what data they have and how they are using it.

### 3. The Right to Rectification
If your personal data is incorrect or incomplete, you can ask for it to be corrected or updated.

### 4. The Right to Erasure ("Right to Be Forgotten")
You can ask for your personal data to be deleted if it is no longer needed or if you withdraw consent. However, some data may need to be kept for legal reasons.

### 5. The Right to Restrict Processing
You can request that an organization **limits** how it uses your data. This means they can store it but not process it further.

### 6. The Right to Data Portability
You can ask to receive your personal data in a format that allows you to move it to another service provider easily.

### 7. The Right to Object
You can object to how your data is used, especially for **marketing**, **profiling**, or **automated decision-making**.

### 8. Rights Related to Automated Decision-Making and Profiling
If a company makes decisions about you using **automated systems** (without human involvement), you have the right to challenge those decisions and request human review.

---
These rights help you **control your personal data** and ensure organizations handle it responsibly. If you believe your rights have been violated, you can file a complaint with the **data protection authority** in your country.

---

## Cloud ROI

Costs:

- **Initial:** Migrating HR data to the cloud, integrating data sources, and developing the dashboard.
- **Ongoing:** Cloud service fees for computing, storage, networking, and specialized services like machine learning.
- **Indirect:** Staff training and changes to IT processes.

Benefits:

- **Tangible:** Reduced maintenance costs, scalability, improved performance, and faster data processing.
- **Intangible:** Agility in deploying updates, better collaboration, and advanced analytics capabilities.

Financial Analysis:

- **ROI Calculation:** If benefits are £500,000 and costs are £200,000, the net benefit is £300,000, resulting in an ROI of 150%.
- **NPV Calculation:** Discount future cash flows to their present value to assess long-term viability.

Additional benefits:

- Flexibility to handle peak processing times without permanent infrastructure.
- Easier integration with other systems and third-party services.
- Enhanced security and compliance with regulations like GDPR.


### Hyperscalers (large cloud service providers (CSPs) such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP))

One of the significant contributions of hyperscalers is their support for **edge computing**, a paradigm that brings computation and data storage closer to the sources of data.

Edge computing is crucial for applications requiring real-time processing and minimal latency, such as Internet of Things (IoT) devices, autonomous vehicles, augmented reality (AR), virtual reality (VR), and online gaming.

By processing data near the edge of the network, organisations can reduce the time it takes for data to travel, resulting in faster responses and improved user experiences.

Hyerscalers are global and have advanced networking capabilities

Hyperscalers offer:

- Machine learning
- Big data and analytics
- Serverless computing
- Security and complience

When choosing a cloud service provider, consider these key factors to align with your organisational needs:

**Pricing Models:** Providers offer different pricing structures, including pay-as-you-go, reserved instances, and spot pricing. Understanding these models helps optimise costs based on usage patterns.

**Service Availability and Reliability:** Assess the provider's uptime guarantees, data centre locations, and redundancy options to ensure high availability and disaster recovery capabilities.

**Integration Capabilities:** Consider how well the provider's services integrate with existing systems and third-party applications. Compatibility with current tools and technologies can reduce migration complexities.

**Support and Service Level Agreements (SLAs):** Evaluate the level of support offered, including technical assistance, documentation, and training resources. Clear SLAs provide assurance regarding service performance and response times.

**Compliance and Security Standards:** Ensure that the provider meets necessary regulatory requirements and industry standards relevant to the organisation, such as GDPR, HIPAA, or ISO certifications.

**Ecosystem and Community:** A strong ecosystem of partners, developers, and community support can enhance the value derived from the provider's services.

**Innovation and Roadmap:** Providers continuously develop new services and features. Aligning with a provider whose innovation roadmap matches the organisation's future needs can offer long-term benefits.



