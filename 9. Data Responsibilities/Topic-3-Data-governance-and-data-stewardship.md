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

