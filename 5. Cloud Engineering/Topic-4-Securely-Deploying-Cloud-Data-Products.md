# Topic 4 - Securely deploying cloud data products 20/03/2025

## CI/CD in the cloud and security risks

![CI/CD](https://www.abtasty.com/wp-content/uploads/2024/07/image-1.png)

Implementing CI/CD in the cloud offers several benefits, including:

1. Accelerates the delivery of new features and bug fixes.
2. Enhances the application’s responsiveness to business needs.
3. Reduces manual errors through automation.
4. Improves the overall quality and reliability of deployments.
5. Leverages scalable resources to handle large workloads and parallel processes efficiently.
6. Integrates security checks and compliance validations into the pipeline.
7. Enforces security policies consistently across all deployments.

#### Security risks of cloud deployments

Deploying applications in the cloud introduces specific security risks that organisations must address to protect their data and systems.

**Common Vulnerabilities**

- Misconfigured Services
- Insecure APIs
- Insufficient Identity and Access Management
- Lack of Encryption

**Detailed Risks**

- **Misconfiguration:** Publicly accessible storage, default security settings.
- **Insecure APIs:** Authentication and authorisation issues.
- **Identity and Access Management:** Privilege escalation, unauthorised activities.
- **Encryption:** Data breaches, eavesdropping.

**Migration Strategies**

- Robust Security Policies
- Principle of Least Privilege
- Regular Audits
- Visibility Tools
- DevSecOps Integration

### Implementing CI/CD with azure DevOps and secure use of Cloud-based APIs

Azure DevOps is a comprehensive set of development tools and services provided by Microsoft, enabling teams to plan work, collaborate on code development, and build and deploy applications. It supports the creation of CI/CD pipelines that integrate seamlessly with Azure cloud services and other platforms.

## Introduction to Azure DevOps

## What is Azure DevOps?
Azure DevOps is a set of development tools and services offered by Microsoft to help teams plan, develop, test, and deliver software efficiently. It provides an end-to-end DevOps solution for managing software projects.

`similar to gitlab`

### Why Use Azure DevOps?
- **Collaboration**: Teams can work together efficiently.
- **CI/CD Pipelines**: Automates build, test, and deployment.
- **Version Control**: Tracks changes in code.
- **Agile Planning**: Supports Scrum and Kanban methodologies.
- **Cloud & On-Premise**: Available as Azure DevOps Services (cloud) and Azure DevOps Server (on-premises).

### Core Components of Azure DevOps

| **Component** | **Description** |
|--------------|----------------|
| **Azure Repos** | Version control using Git repositories. |
| **Azure Pipelines** | Automates CI/CD for build and deployment. |
| **Azure Boards** | Agile project management with Kanban, Scrum, and dashboards. |
| **Azure Test Plans** | Automated and manual testing tools. |
| **Azure Artifacts** | Package management for dependencies (NuGet, npm, etc.). |

## How to Get Started with Azure DevOps
1. **Sign Up**: Go to [Azure DevOps](https://dev.azure.com) and sign up.
2. **Create a Project**: Define a new project to manage your source code, pipelines, and tasks.
3. **Use Azure Repos**: Initialize a Git repository for your code.
4. **Set Up a Pipeline**: Define a CI/CD pipeline using YAML or the visual editor.
5. **Deploy Applications**: Use Azure Pipelines to deploy to Azure, AWS, or on-prem servers.

## Conclusion
Azure DevOps simplifies the software development lifecycle by integrating tools for planning, coding, testing, and deployment. Whether working in the cloud or on-premises, it provides a powerful and flexible solution for DevOps teams.

### What is GitLab?
GitLab is an open-source DevOps platform that provides source code management and CI/CD capabilities in a single application.

#### Key Features of GitLab:
- **Git Repository Management**: Built-in Git-based version control.
- **CI/CD Pipelines**: Automate software build, test, and deployment processes.
- **Issue Tracking & Project Management**: Track bugs and tasks with Kanban boards.
- **Security and Compliance**: Built-in security scanning and vulnerability management.
- **Self-Hosting Option**: Unlike Azure DevOps, GitLab can be self-hosted on your own servers.

#### Example Use Case:
A team can:
- Use **GitLab Repositories** for version control.
- Set up **CI/CD Pipelines** to deploy applications automatically.
- Track bugs and features using **GitLab Issues**.

---

### Differences Between Azure DevOps and GitLab

| Feature           | Azure DevOps | GitLab |
|------------------|-------------|--------|
| **Hosting** | Cloud-based (by Microsoft) | Cloud & Self-hosted |
| **Version Control** | Git & TFVC | Git only |
| **CI/CD** | Azure Pipelines | GitLab CI/CD |
| **Project Management** | Azure Boards | GitLab Issues & Kanban |
| **Security** | Integrated security tools | Advanced security features |
| **Pricing** | Free tier + paid plans | Free, Premium, and Self-hosted options |

---

### Which One Should You Use?
- **Choose Azure DevOps if:**
  - You work in a Microsoft ecosystem (e.g., using Azure, .NET, Visual Studio).
  - You need enterprise-grade project management and security tools.

- **Choose GitLab if:**
  - You prefer an all-in-one DevOps platform with built-in Git and CI/CD.
  - You need a self-hosted option for more control over infrastructure.

---

### How to securely use cloud-based APIs

APIs are essential components in cloud applications, enabling communication between services and access to data. Securing cloud-based APIs is crucial to prevent unauthorized access, data breaches, and other security incidents.

Key practices for securing APIs include:

- **Authentication and Authorisation:** Implement robust authentication mechanisms, such as OAuth 2.0 or API keys, to verify the identity of users and services. Use role-based access control (RBAC) to enforce permissions.
- **Input Validation and Sanitisation:** Validate all inputs to prevent injection attacks, such as SQL injection or cross-site scripting (XSS).
- **Encryption:** Use HTTPS/TLS to encrypt data in transit, protecting sensitive information from eavesdropping.
- **Rate Limiting and Throttling:** Implement rate limits to prevent abuse and protect against denial-of-service (DoS) attacks.
- **Monitoring and Logging:** Keep detailed logs of API requests and responses. Monitor for unusual patterns that may indicate malicious activity.
- **API Gateways:** Use API gateways to manage and secure API traffic, enforce policies, and provide a single entry point for API access.

### How to securely use scalable cloud-based analytics products and lakehouses

Data analytics platforms and lakehouses in the cloud provide powerful tools for processing and analysing large datasets. Securing these platforms involves protecting data at rest and in transit, controlling access, and ensuring compliance with regulations.

Best practices include:

- **Data Encryption:** Encrypt data at rest using cloud provider services like Azure Storage Service Encryption or AWS KMS. Use encryption for data in transit with SSL/TLS.
- **Access Control:** Implement RBAC and use identity providers to authenticate users. Grant the least privilege necessary for users to perform their tasks.
- **Network Security:** Use virtual networks, subnets, and network security groups to isolate resources and control traffic.
- **Compliance and Governance:** Ensure that data handling complies with regulations like GDPR. Use data classification and tagging to manage sensitive data appropriately.
- **Monitoring and Auditing:** Enable auditing features to track access and changes to data. Monitor for unusual activities that may indicate security breaches.
- **Regular Updates and Patch Management:** Keep systems and software up to date with the latest security patches.

### Security in cloud data integration, SRE principles, and Monitoring

**Security considerations of cloud data integration**

We will use Azure Data Factory to illustrate our discussion of security considerations that apply to cloud deployments. Azure Data Factory is a cloud-based data integration service that orchestrates and automates data movement and transformation. Securing data integration processes is vital to prevent data leaks and unauthorised access.

In using Azure Data Factory securely, the following considerations apply:

- **Authentication and Authorisation:** Use Azure Active Directory (AD) for authentication. Assign roles and permissions using RBAC to control who can create, edit, and execute pipelines.
- **Secure Connections:** Use managed identities to access data sources securely without embedding credentials. Configure linked services with secure authentication methods.
- **Data Encryption:** Ensure that data is encrypted during transit between data sources and destinations. Use SSL/TLS for secure connections.
- **Network Isolation:** Deploy Data Factory in a virtual network to limit exposure to the internet. Use private endpoints to connect securely to data sources.
- **Monitoring and Alerts:** Enable diagnostic logging to monitor activities. Set up alerts for failed pipeline runs or suspicious activities.
- **Compliance:** Implement data governance policies to ensure compliance with regulations. Use data masking and anonymisation techniques where necessary.

For example

For example, when setting up a pipeline to move data from on-premises databases to cloud storage, you would:

1. Use a self-hosted integration runtime within a secure network.
2. Authenticate using managed identities or service principals.
3. Encrypt data during transfer using HTTPS.
4. Monitor the pipeline runs and review logs for any anomalies.

By considering these security aspects, you ensure that data integration processes are robust and do not introduce vulnerabilities.

---

In this section, we will compare two powerful Azure services: Azure App Service and Azure Container Apps. Both platforms offer robust solutions for hosting applications, but they cater to different needs and preferences.

### Azure App Service

Azure App Service is a fully managed platform that provides hosting for web applications including websites and web APIs.

It is optimised for web applications and provides a range of features such as automatic scaling, load balancing, and integration with other Azure services.

Azure App Service is a good choice if you want to focus on developing your application and not worry about the underlying infrastructure. It also provides built-in support for popular programming languages and frameworks

### Azure Container Apps

On the other hand, Azure Container Apps is a fully managed platform that provides hosting for containerised applications. It provides more flexibility than Azure App Service as you can use any container image to run your application.

It also provides features such as automatic scaling, load balancing, and integration with other Azure services. Azure Container Apps is a good choice if you want to have more control over the underlying infrastructure and want to use containers to run your application.

### Choosing between Azure app service and Azure container apps

When deciding between Azure App Service and Azure Container Apps, consider the following factors:

- **Flexibility:** If you want to use any container image to run your application, then Azure Container Apps is a better choice. If you want to use a specific programming language or framework, then Azure App Service is a better choice.
- **Control:** If you want more control over the underlying infrastructure, then Azure Container Apps is a better choice. If you want to focus on developing your application and not worry about the underlying infrastructure, then Azure App Service is a better choice.
- **Pricing:** Azure Container Apps can be more cost-effective than Azure App Service if you have a large number of applications to host. However, if you have a small number of applications to host, then Azure App Service may be more cost-effective.
- **Scalability:** Both Azure App Service and Azure Container Apps provide automatic scaling. However, Azure Container Apps provides more granular control over scaling as you can scale individual containers.

### Site Reliability Engineering (SRE) principles

Having deployed your app in the cloud, you need to manage it reliably. Remember that as part of this module’s learning outcomes, you need to be able to evaluate the differences between Site Reliability Engineering (SRE) principles and DevSecOps principles. Site Reliability Engineering (SRE) is a discipline that applies software engineering principles to infrastructure and operations problems. SRE aims to create scalable and highly reliable software systems.

Key principles include the following:

- **Embracing Risk:** Recognise that failure is inevitable and design systems to handle it gracefully.
- **Service Level Objectives (SLOs):** Define measurable targets for system performance and availability.
- **Eliminating Toil:** Automate repetitive manual tasks to improve efficiency and reduce errors.
- **Monitoring and Observability:** Implement comprehensive monitoring to gain insights into system behaviour and detect issues early.
- **Incident Response:** Develop processes for responding to incidents quickly and effectively.
- **Blameless Postmortems:** After incidents, conduct reviews to learn and improve without assigning blame.

## Understanding the Differences Between SRE and DevOps

### Introduction
When working in modern software development and operations, two key methodologies often come up: **Site Reliability Engineering (SRE)** and **DevOps**. While they share similarities, they have distinct philosophies and approaches.

### What is DevOps?
DevOps is a **cultural and technical movement** that aims to break down silos between development and operations teams. It focuses on automation, continuous integration, and continuous delivery (CI/CD) to speed up software development and deployment.

#### Core Principles of DevOps:
- **Collaboration:** Developers and IT operations work together.
- **Automation:** CI/CD pipelines, infrastructure as code (IaC).
- **Monitoring & Feedback:** Continuous performance tracking.
- **Scalability & Security:** Infrastructure and application security built into pipelines.

#### Example of DevOps Workflow:
1. **Developer pushes code** → GitHub/GitLab
2. **Automated build & test** → Jenkins/GitHub Actions
3. **Continuous Integration (CI)** → Merging into the main branch
4. **Continuous Deployment (CD)** → Deploy to production
5. **Monitoring & Logging** → Prometheus, Grafana, ELK Stack

### What is Site Reliability Engineering (SRE)?
SRE is an **engineering discipline** introduced by Google that applies **software engineering** to IT operations. It focuses on reliability, observability, and automation to ensure systems run smoothly in production.

#### Core Principles of SRE:
- **Reliability:** Ensuring high availability and uptime.
- **Error Budgets:** Balancing innovation and stability.
- **Automation:** Reducing manual operations.
- **Incident Management:** Handling failures effectively.

#### Example of SRE Practices:
- **Defining Service Level Objectives (SLOs)** to set uptime goals.
- **Using Error Budgets** to balance feature releases and system stability.
- **Automating Operations** (self-healing systems, runbooks, monitoring).
- **Incident Response** (on-call rotations, post-mortems, root cause analysis).

### Key Differences: DevOps vs. SRE

| **Aspect**         | **DevOps** | **SRE** |
|--------------------|-----------|---------|
| **Focus**         | Development & Operations collaboration | Reliability and automation |
| **Goal**         | Speed, agility, and CI/CD | System reliability and uptime |
| **Approach**      | Culture + tools | Engineering discipline |
| **Automation**    | CI/CD pipelines, infrastructure as code | Self-healing, monitoring, incident response |
| **Who does it?**  | Developers & IT Ops | Software engineers with ops focus |
| **Metrics**       | Deployment speed, lead time | SLAs, SLOs, error budgets |

### Conclusion
- **DevOps** aims to bring development and operations together to ship software faster.
- **SRE** applies software engineering principles to improve system reliability and maintain uptime.
- Both share automation and monitoring goals, but SRE is more focused on reliability, while DevOps focuses on collaboration and efficiency.

Understanding these differences helps organizations choose the right approach based on their needs. 🚀

---

### Walk-through: Monitoring availability and downtime using dashboards

Monitoring is essential for maintaining the health and performance of cloud applications. Dashboards provide visual representations of key metrics, helping teams quickly assess the state of systems.

Here's a guide to setting up monitoring:

- **Step 1: Identify Key Metrics:** Determine which metrics are important for your application, such as CPU usage, memory usage, response times, and error rates.
- **Step 2: Configure Monitoring Tools:** Use cloud provider services like Azure Monitor or third-party tools like Prometheus and Grafana.
- **Step 3: Create Dashboards:** Design dashboards that display metrics in an accessible format, using charts, graphs, and alerts.
- **Step 4:** Set Up Alerts: Configure alerts to notify teams when metrics exceed defined thresholds, indicating potential issues.

For example, in Azure Monitor, you can create a dashboard that shows the availability of your web application, tracking uptime and response times. If the application experiences downtime or performance degradation, alerts can be sent via email or messaging services, prompting immediate investigation.

### Walkthrough of working with cloud logs and spotting and remediating problems

Logs are invaluable for diagnosing issues, understanding system behaviour, and improving applications. Working with cloud logs involves collecting, analysing, and acting on log data.

Steps for working with cloud logs and remediating problems include:

- **Step 1: Enable Logging:** Configure applications and services to generate logs. Use cloud services like Azure Log Analytics to collect logs centrally.
- **Step 2: Log Aggregation:** Collect logs from multiple sources, including applications, servers, and network devices.
- **Step 3: Analysis:** Use query languages or tools to search and analyze logs. Look for patterns, errors, or anomalies that may indicate problems.
- **Step 4: Spotting Issues:** Identify common issues such as failed requests, exceptions, or security breaches.
- **Step 5: Remediation:** Based on the insights from logs, take corrective actions. This may involve fixing code bugs, adjusting configurations, or scaling resources.

For instance, if logs reveal that a database connection is frequently timing out, the team can investigate the cause—perhaps due to network issues or resource constraints—and implement a solution, such as increasing connection limits or optimising queries.



