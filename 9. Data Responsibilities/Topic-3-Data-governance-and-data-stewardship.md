# Topic 3 - Data governance and data stewardship 14/08/2025

# Identifying roles and responsibilities in data governance

### Data Owners

Data Owners are senior leaders who are responsible for ensuring that the data under their domain is managed appropriately.

They play a strategic role by defining access policies, setting data usage guidelines, and ensuring compliance with relevant regulations.

For example, in a healthcare organisation, a Data Owner overseeing patient records ensures compliance with HIPAA standards by establishing rules for data sharing and storage.

Data Owners ensure that data governance policies align with organisational goals, creating a foundation for effective data management (Eryurek & Gilad, 2021; Reis & Housley, 2022).

### Data Stewards

Data Stewards focus on the operational aspects of data governance by maintaining data quality and integrity. They are responsible for implementing data governance policies, resolving data issues, and ensuring that data meets organisational standards.

For instance, in a marketing department, a Data Steward might clean and validate customer email lists to eliminate duplicate or invalid entries, ensuring that campaigns reach the intended audience.

By bridging the gap between strategic policies and daily operations, Data Stewards play a vital role in achieving consistent, reliable, and actionable data (King & Schwarzenbach, 2020; Mertz, 2021).

### Data Custodians

Data Custodians are IT professionals who manage the technical infrastructure that supports data governance. They are responsible for implementing security controls, maintaining system reliability, and managing backups.

For example, in a retail organisation, Data Custodians might implement encryption protocols and access controls to secure customer information stored on cloud-based infrastructure.

These technical safeguards ensure the confidentiality, availability, and integrity of data, enabling Data Stewards and Owners to carry out their responsibilities effectively (Eryurek & Gilad, 2021; Simsion & Witt, 2005).

# Key Components of Data Management Policies

If you are starting out as a data engineer, it’s important to understand that **data management policies** are like the “house rules” for how data is handled in an organization. These rules help ensure that data is **secure, accurate, available, and compliant** with regulations.  
Here are three of the most important components:

---

## 1. Data Access Policies

**Definition:**  
Data access policies define **who** can see or use certain data, **under what conditions**, and **how** they are allowed to use it.

**Purpose:**  
- Protect sensitive or confidential information from unauthorized access.  
- Ensure that people can only access the data they need for their job (principle of least privilege).  
- Prevent misuse or accidental exposure of data.

**Typical Elements:**
- **Roles and Permissions:** Assign access based on user roles (e.g., analyst, engineer, manager).  
- **Authentication and Authorization:** Require secure login methods and verify permissions before granting access.  
- **Monitoring and Auditing:** Track who accessed what data and when.  
- **Data Sharing Rules:** Define when and how data can be shared within or outside the organization.

---

## 2. Data Retention and Disposal Policies

**Definition:**  
These policies set rules for **how long data is kept** and **how it is securely destroyed** once it’s no longer needed.

**Purpose:**  
- Comply with legal or regulatory requirements (e.g., GDPR, HIPAA).  
- Avoid storing outdated or irrelevant data that could become a liability.  
- Reduce storage costs and complexity.

**Typical Elements:**
- **Retention Periods:** Specific timeframes for keeping data (e.g., 7 years for financial records).  
- **Archiving Rules:** How old data is moved to cheaper or slower storage if it must be kept but not actively used.  
- **Disposal Methods:** Secure deletion, shredding of physical media, or data anonymization.  
- **Exception Handling:** Rules for when retention timelines can be extended (e.g., during legal investigations).

---

## 3. Data Classification Policies

**Definition:**  
Data classification policies define how data is **labeled** based on its sensitivity, importance, and required handling procedures.

**Purpose:**  
- Make it clear how different types of data should be stored, shared, and protected.  
- Reduce risk by ensuring sensitive data gets higher protection.  
- Help comply with security and privacy regulations.

**Typical Elements:**
- **Classification Levels:** Common categories include:  
  - **Public:** No harm if disclosed (e.g., marketing brochures).  
  - **Internal:** Only for employees, not for public release.  
  - **Confidential:** Sensitive business information (e.g., client lists, financial data).  
  - **Restricted / Highly Confidential:** Very sensitive data that could cause severe harm if leaked (e.g., personal health data, trade secrets).  
- **Labeling Requirements:** Rules for marking files, databases, or reports with their classification.  
- **Handling Procedures:** Encryption, secure storage, and sharing restrictions depending on classification.  
- **Reclassification Rules:** How to change a data item’s classification if its sensitivity changes.

---

## Why These Policies Matter for Data Engineers

As a data engineer, you will often **design, build, and maintain systems** that must enforce these policies.  
- **Data Access Policies** affect how you set up authentication and permissions in databases or data platforms.  
- **Retention and Disposal Policies** influence data pipeline design, archiving strategies, and cleanup processes.  
- **Classification Policies** determine how you tag and handle different datasets in storage and during processing.

---

**In short:**  
Think of these policies as a **roadmap** for how data moves, lives, and eventually disappears in an organization — safely, legally, and efficiently.

---

### Data Collection Procedures

Procedures for data collection ensure that data is captured accurately and ethically.

For example, an online retailer may implement a double opt-in process for email subscriptions, ensuring compliance with GDPR consent requirements.

### Data Monitoring Procedures

Monitoring procedures involve tracking data usage and identifying anomalies.

For instance, a financial institution may use automated tools to detect unusual access patterns, such as multiple login attempts from unauthorised locations, and take immediate action.

### Data Auditing Procedures

Regular data audits ensure adherence to policies and identify areas for improvement.

For example, a manufacturing company might audit supplier data annually to ensure accuracy and compliance with its data governance framework (Eryurek & Gilad, 2021).

---

# Synthesising Data Governance Frameworks

1. **Define roles and responsibilities:** The organisation appointed a Chief Data Officer (CDO) to oversee data governance initiatives and established data stewards at each hospital to ensure local compliance.

2. **Develop policies:** Data classification, access controls, and retention policies were standardised across all facilities.

3. **Implement technology:** A centralised data catalogue was created, enabling secure access and reducing duplication of patient records.

4. **Measure performance:** Quarterly audits and dashboards tracked compliance, data quality, and operational efficiency.

---

## Roles and responsibilities

A successful framework begins with clearly defined roles, ensuring accountability and consistency, including:

1. **Data Owners:** Responsible for the accuracy, quality, and security of specific datasets. For instance, a sales manager overseeing CRM data ensures it aligns with reporting needs.

2. **Data Stewards:** Enforce policies and procedures to maintain data quality and compliance at the operational level. For example, a healthcare data steward ensures that patient records are complete and compliant with HIPAA.

3. **Governance Committees:** Provide strategic oversight, ensuring alignment between data governance and organisational goals. These committees include representatives from IT, compliance, and business units (Eryurek & Gilad, 2021).

---

### Synthesising the Framework

1. **Assess Organisational Needs:** Identify key pain points and priorities, such as regulatory compliance or improved reporting accuracy. For example, a government agency prioritises data security due to its reliance on citizen information systems.

2. **Define Objectives and Scope:** Determine the framework's goals, such as improving data quality or streamlining access. Define the scope, whether organisation-wide or departmental. For example, a telecom company focuses its initial governance efforts on customer data to enhance billing accuracy.

3. **Design and Implement:** Establish roles, policies, and technology tools to address identified needs. For example, a logistics company implements role-based access controls to prevent unauthorised access to shipment data.

4. **Measure and Refine:** Use metrics like data quality scores and compliance audit results to evaluate performance and make adjustments. For example, a pharmaceutical company updates its governance framework annually based on new FDA regulations.

---

# Principles of Data Stewardship 

## 1. What Is Data Stewardship?

Data stewardship is the practice of **responsibly managing, protecting, and improving the quality of data** throughout its lifecycle.  
Think of it as being the caretaker of a valuable library — except the "books" are datasets, and your role is to ensure they are accurate, secure, and used ethically.

While **data engineering** focuses on building the systems to store, move, and process data, **data stewardship** ensures that the data inside those systems is **trustworthy, compliant, and fit for purpose**.

---

## 2. Core Principles

### 2.1 Data Ownership & Accountability
- Every dataset should have a clearly identified **data owner** (person or team) who is responsible for its correctness and use.
- As a steward, you may not “own” the data, but you ensure it’s managed according to agreed standards.
- Accountability helps prevent the “no one’s in charge” problem.

---

### 2.2 Data Quality
- Data should be **accurate**, **complete**, **consistent**, and **timely**.
- This includes:
  - Removing duplicates
  - Ensuring formats are consistent (e.g., date formats)
  - Avoiding missing or incorrect values
- **Why it matters:** Poor-quality data can cause bad business decisions, faulty analytics, and system errors.

---

### 2.3 Data Security & Privacy
- Protect data from unauthorized access, loss, or corruption.
- Follow security best practices:
  - Encryption at rest and in transit
  - Access controls (role-based permissions)
- **Privacy laws** (e.g., GDPR, CCPA) require special handling of personal information — know what applies to your organization.

---

### 2.4 Data Lineage & Traceability
- **Data lineage** is a record of where the data came from, how it moved, and how it changed over time.
- This helps:
  - Debug issues in data pipelines
  - Prove compliance with regulations
  - Build trust in data by making it transparent

---

### 2.5 Data Lifecycle Management
- Data goes through stages: **creation → storage → usage → archival → deletion**.
- Stewardship ensures:
  - Old or unused data is archived or deleted to reduce risk and storage costs.
  - Active data remains accessible and relevant.
- Prevents “data hoarding,” which can lead to security and compliance issues.

---

### 2.6 Compliance & Ethics
- Understand and apply relevant laws, regulations, and organizational policies.
- Ethical stewardship means:
  - Avoiding misuse of data
  - Being transparent about data usage
  - Respecting user consent and privacy

---

### 2.7 Collaboration & Communication
- Data stewardship is not a solo activity — it involves **coordinating with business users, data engineers, analysts, and legal teams**.
- You act as a bridge between technical systems and business needs, ensuring everyone agrees on definitions, rules, and responsibilities.

---

## 3. Why It Matters for a Data Engineer

Even if your main job is building pipelines or databases:
- **Bad data in = bad results out** — stewardship ensures you’re working with clean, reliable data.
- Data engineers are often the first to notice data problems and can flag them early.
- Knowing stewardship principles helps you design systems that are easier to govern, audit, and maintain.

---

## 4. Key Takeaways

- **Data stewardship** = caring for data so it’s accurate, secure, and responsibly used.
- It’s about **quality, security, compliance, and collaboration**.
- As a data engineer, understanding stewardship helps you build systems that people can trust.

---

# Understanding Data Stewardship 

If you’re just starting your journey as a data engineer, you might already know that data is like the “raw material” of any data-driven organization. But **data stewardship** is what ensures that raw material is trustworthy, well-maintained, and fit for use. Think of it like the role of a careful librarian — not just storing books, but making sure they’re accurate, organized, and easy to find.

---

## What is Data Stewardship?
**Data stewardship** is the practice of managing and overseeing an organization’s data assets to ensure they are **accurate**, **consistent**, **secure**, and **usable** for everyone who needs them. It’s a responsibility that often involves working closely with data owners, analysts, and engineers to keep data in good shape over its entire lifecycle.

---

## Why Does It Matter?
Without proper stewardship, data can:
- Become inconsistent across different systems.
- Contain errors or missing values.
- Lose its meaning due to poor documentation.
- End up being used in ways that break privacy or compliance rules.

This can lead to **bad business decisions**, **compliance violations**, or **loss of trust** in the data.

---

## Key Responsibilities of a Data Steward
1. **Defining Data Standards**
   - Establish clear definitions, formats, and rules for how data should be stored and used.
   - Example: Deciding that all dates must follow the `YYYY-MM-DD` format.

2. **Maintaining Data Quality**
   - Regularly check for errors, duplicates, or incomplete data.
   - Collaborate with data engineers to fix issues at the source.

3. **Ensuring Data Integrity**
   - Keep data consistent and accurate across systems.
   - Monitor for unintended changes or corruption.

4. **Documenting Data**
   - Create and maintain **data dictionaries** and **metadata** so everyone knows what each data element means.
   - Example: Explaining that the “Customer_ID” field is a unique identifier assigned to each registered customer.

5. **Supporting Compliance and Security**
   - Ensure that sensitive data (e.g., personal information) is handled according to privacy regulations like GDPR or HIPAA.
   - Control who can access what data.

6. **Facilitating Communication**
   - Act as a bridge between technical teams (data engineers, architects) and business teams (analysts, managers) to ensure everyone understands the data.

---

## How It Supports Data Quality and Integrity
- **Quality**: By enforcing standards, cleaning up issues, and validating inputs, data stewards ensure that data is correct and complete.
- **Integrity**: By monitoring changes and syncing data across systems, they protect against accidental or malicious alterations.

Think of data stewardship as **quality control plus ongoing maintenance** for your data ecosystem.

---

## The Data Engineer’s Connection to Stewardship
As a data engineer, you will often:
- Build pipelines that align with data standards.
- Implement validation checks defined by data stewards.
- Collaborate to ensure that metadata and documentation stay up-to-date.
- Support processes for correcting bad data at its source.

While data stewards focus on **policy, quality, and governance**, data engineers focus on **building and maintaining the technical infrastructure** to make those policies possible.

---

## In Summary
Data stewardship ensures that:
- Data is **accurate**, **consistent**, and **trusted**.
- The organization can make reliable, data-driven decisions.
- Legal, ethical, and security standards are upheld.

Without it, even the most advanced data engineering pipelines would just move poor-quality data faster — and as the saying goes, **“garbage in, garbage out.”**

---

**Pro Tip:** Good data stewardship is like good kitchen hygiene — if you keep things clean, organized, and clearly labeled from the start, everything runs smoother and you avoid unpleasant surprises later.

---

# Evaluating Strategies for Effective Data Stewardship

1. GOVERNANCE STRUCTURES

COMMUNICATION AND COLLABORATION

Education and training

PERFORMANCE MANAGEMENT AND FEEDBACK
For example, an e-commerce company assigns regional data stewards to monitor customer feedback, ensuring each region aligns with global privacy policies like GDPR (Eryurek and Gilad, 2021).

