# Topic 5 - Migrations, archiving, monitoring and disaster recovery - 27/03/2025

# Crisis management - Case Study
## A cyber security scenario: 'Disaster Looms!'

`In the heart of London, nestled within the bustling financial district, a mid-sized fintech company, Sterling Finance, encounters an unforeseen calamity. It's a crisp autumn morning when a cyber-attack cripples their trading platform, halting transactions and sowing panic among clients and staff alike.`

### Techniques for comprehensive crisis management

**Business Continuity Management (BCM)**

BCM is the comprehensive approach by which organisations prepare for, and ensure the maintenance of, critical functions in the face of disruptive events.

At Sterling Finance, the BCM plan includes not just the restoration of IT services, but also the broader aspects such as maintaining essential operations, managing communication with stakeholders, and safeguarding legal and regulatory compliance.

For instance, even as the cyber-attack unfolds, a pre-established BCM strategy ensures that client services continue via secondary systems and manual processes, thus upholding the firm’s operational integrity.

**Disaster Recovery (DR)**

This aspect focuses specifically on the recovery of IT infrastructure and data access after a disaster strikes.

It is a subset of BCM but with a narrower scope, concentrating primarily on technical recovery and data integrity.

In the case of Sterling Finance, the DR protocol kicks in immediately after the attack is detected, involving steps such as switching to a backup data centre, restoring data from secure backups, and deploying advanced malware removal tools to cleanse the network, aiming for a swift resumption of services.

**Incident Response (IR)**

IR deals with the immediate reaction to an incident, aiming to limit damage and reduce recovery time and costs.

This process involves detailed planning that includes incident identification, escalation procedures, mitigation steps, and documentation.

At Sterling Finance, the IR team springs into action by first containing the breach to prevent further damage, followed by forensic analysis to understand the breach’s extent and origins.

This team also communicates internally to ensure that all staff are informed and externally to manage public relations and client communications.

## Cloud migration

Cloud migration can be a useful strategy to strengthen BCM, DR and IR. Cloud migration involves moving applications, data, and infrastructure from on-premises environments to cloud platforms. While many organisations have successfully migrated to the cloud, others have faced challenges that led to failed projects. Analysing different case studies helps in understanding the factors that contribute to success or failure and provides valuable insights for future migrations.

You should use the power/interest matrix to help you plan your communications strategy before you begin:
![Power interest matrix](https://jocando.co.uk/wp-content/uploads/2020/09/power-interest-grid.png)

### Case study 1:

Successful migration of a retail company's E-commerce platform

A leading retail company decided to migrate its e-commerce platform to the cloud to handle increasing traffic during peak shopping seasons.

The company adopted a phased migration strategy, starting with non-critical applications to gain experience.

They conducted thorough planning, involving cross-functional teams to assess application dependencies, data requirements, and compliance considerations.

**Key factors contributing to success included:**

1. **Comprehensive Planning:** Detailed assessment of the existing infrastructure and clear migration roadmap.
2. **Stakeholder Engagement:** Involving IT, business units, and external partners to ensure alignment.
3. **Testing and Validation:** Rigorous testing in a staging environment before production deployment.
4. **Training and Support:** Providing training for staff to manage and operate cloud services effectively.

### Case study 2:

Failed Migration of a Financial Institution's Legacy Systems

A financial institution attempted to migrate its legacy core banking systems to the cloud to reduce operational costs.

The project faced significant challenges, ultimately leading to failure and reverting to on-premises systems.

**Key factors contributing to failure included:**

1. **Lack of Compatibility:** Legacy systems were not compatible with the cloud environment, requiring extensive re-engineering.
2. **Insufficient Planning:** Underestimating the complexity of migrating mission-critical systems.
3. **Security and Compliance Issues:** Failure to meet regulatory requirements for data protection and privacy.
4. **Resistance to Change:** Lack of buy-in from key stakeholders and insufficient training for staff.

## The importance of robust archiving policies and frameworks

### So, what is archiving?

### The importance of robust archiving policies and frameworks

Archiving is the process of securely storing historical data that is not actively used but may be needed for future reference, compliance, or analysis. Robust archiving policies and frameworks are essential for effective data management, ensuring that archived data is preserved, accessible, and protected over the long term.

**The significance of archiving:**

- **Regulatory Compliance:** Many industries are subject to regulations that require data retention for specific periods (e.g., financial records, medical data).
- **Legal Considerations:** Archived data may be needed for legal proceedings or audits.
- **Business Intelligence:** Historical data can provide valuable insights for strategic decision-making.
- **Cost Management:** Archiving reduces storage costs by moving infrequently accessed data to cost-effective storage solutions.

**Best practices for archiving:**

- **Policy Development:** Define clear policies outlining what data should be archived, retention periods, and access controls.
- **Classification of Data:** Categorise data based on sensitivity, importance, and regulatory requirements.
- **Secure Storage Solutions:** Use reliable and secure storage options, such as cloud-based archival storage (e.g., Azure Archive Storage, Amazon Glacier).
- **Data Integrity and Preservation:** Implement measures to ensure data integrity over time, including checksums and regular validation.
- **Access Management:** Control who can access archived data, implementing strict authentication and authorisation mechanisms.
- **Disaster Recovery Integration:** Include archived data in disaster recovery plans to ensure it can be restored if needed.

**Challenges in Archiving:**

- **Data Growth:** Managing the increasing volume of data requires scalable archiving solutions.
- **Format Obsolescence:** Ensuring that data remains readable despite changes in technology and file formats.
- **Security Risks:** Protecting archived data from unauthorised access and breaches.

## Introducing redundancy for performance and availability

**Redundancy for performance and availability**

Data redundancy involves storing copies of data in multiple locations or systems. Introducing redundancy enhances performance and availability by providing alternative pathways for data access and recovery in case of failures. Redundancy is a fundamental principle in designing resilient systems that can withstand hardware failures, network issues, or other disruptions.

**These benefits include:**

- **Improved Availability:** Redundant systems, such as systems following the Active/Standby set-up, ensure that services remain accessible even if one component fails.
- **Enhanced Performance:** Distributing data across multiple systems can balance loads and reduce latency.
- **Data Protection:** Redundant data storage protects against data loss due to hardware failures or corruption.
- **Disaster Recovery:** Redundancy facilitates faster recovery times during disasters by having backups readily available.

**Best practices for implementing redundancy include:**

- **Replication Strategies:** Use data replication techniques, such as synchronous or asynchronous replication, to keep data copies up to date.
- **Geographical Distribution:** Store redundant data in different geographic locations to protect against regional disasters.
- **Redundant Infrastructure:** Implement redundant network paths, power supplies, and hardware components.
- **Regular Testing:** Conduct failover tests to ensure that redundant systems function correctly when needed.
- **Monitoring and Alerts:** Monitor redundant systems for synchronisation issues or failures, setting up alerts for timely intervention.
- **Cost-Benefit Analysis:** Balance the costs of redundancy with the benefits, ensuring that investments align with business priorities.

**Challenges in redundancy**

- **Complexity:** Managing redundant systems adds complexity to infrastructure and operations.
- **Consistency:** Ensuring data consistency across redundant systems requires careful planning and coordination.
- **Cost Considerations:** Implementing redundancy incurs additional costs for hardware, storage, and maintenance.

## Focus on disaster recovery policies including incident response

So, what are Disaster Recovery (DR) policies?

Disaster Recovery (DR) policies outline the procedures and processes that an organisation follows to restore operations after a disruptive event, such as natural disasters, cyber-attacks, or system failures. Incident response is a critical component of DR, focusing on the immediate actions taken to mitigate the impact of incidents.

**Key components of DR policies include:**

1. **Risk Assessment:** Identify potential threats and vulnerabilities that could impact operations.
2. **Business Impact Analysis (BIA):** Evaluate the potential consequences of disruptions on critical business functions.
3. **Recovery Objectives:**
    - **Recovery Time Objective (RTO):** The maximum acceptable length of time that a system can be down.
    - **Recovery Point Objective (RPO):** The maximum acceptable amount of data loss measured in time.
4. **DR Plan Development:** Create detailed plans outlining recovery strategies, roles and responsibilities, communication protocols, and resource requirements.
5. **Data Backup Strategies:** Implement regular backups, ensuring that data can be restored from recent points.
6. **Testing and Drills:** Conduct regular tests and simulations to validate the effectiveness of DR plans.
7. **Continuous Improvement:** Update DR policies based on lessons learned from tests and real incidents.

**Incident response strategies include:**

1. **Preparation:** Establish incident response teams, roles, and communication channels.
2. **Detection and Analysis:** Implement monitoring systems to detect incidents promptly and assess their scope.
3. **Containment and Eradication:** Take actions to contain the incident, prevent further damage, and eliminate the cause.
4. **Recovery:** Restore affected systems and data to resume normal operations.
5. **Post-Incident Review:** Analyse the incident to identify root causes, impacts, and areas for improvement.

**Best practices in DR and incident response:**

1. **Documentation:** Maintain up-to-date documentation of all DR procedures and contact information.
2. **Employee Training:** Educate staff on their roles during incidents and how to respond effectively.
3. **Third-Party Coordination:** Include vendors and partners in DR plans when they are integral to operations.
4. **Compliance Considerations:** Ensure that DR policies comply with industry regulations and standards.

**Challenges in redundancy**

- **Resource Constraints:** Allocating sufficient resources for DR planning and execution.
- **Changing Environments:** Adapting DR plans to evolving technology landscapes and business processes.
- **Communication Barriers:** Ensuring clear communication during crises, especially across different teams and locations.

## Writing and deploying a cloud-native monitoring service in Python

Building a custom monitoring service allows for tailored observability of specific applications or systems.

Using Python, a versatile and widely used programming language, you can create a cloud-native monitoring application that collects metrics, processes data, and integrates with monitoring platforms.


