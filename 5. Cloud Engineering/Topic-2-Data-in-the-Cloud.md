# Topic 2 - Data in the Cloud 13/03/2025

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







