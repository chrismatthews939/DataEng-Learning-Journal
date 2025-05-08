# Topic 4 - Data collection quality and ingestion risks 08/05/2025

## Recap of data quality fundamentals

#### Data Quality Dimensions
1. **Accuracy:** Ensuring data correctly represents real-life entities.
2. **Completeness:** Making sure all required data is present.
3. **Consistency:** Maintaining uniformity in data representation.
4. **Integrity:** Ensuring data is complete, accurate, and consistent.
5. **Reasonability:** Checking if data patterns meet expectations. An example could be a taxi jouney saying it took 5 seconds
6. **Timeliness:** Ensuring data is up-to-date and available when needed. **Latency** is how long it took for the data to arrive after it was created. **Freshness** is how up to date it is.
7. **Uniqueness/Deduplication:** Ensuring no entity exists more than once.
8. **Validity:** Ensuring data values are within defined domains. Some data might be valid for a certain amount of time such as coupon codes.


## Establishing data quality service level agreements

`Service Level Agreements (SLAs) are essential for setting clear expectations and responsibilities regarding data quality within an organisation. This lesson will guide you through the process of establishing effective data quality SLAs, which are crucial for maintaining high standards and accountability in data management.`

#### The main elements of a data quality SLA include:

- Data elements covered by the agreement.
- Business impacts associated with data flaws.
- Data quality dimensions associated with each data element (see previous lesson).
- Expectations for quality for each data element for each of the identified dimensions in each application or system in the data value chain.
- Methods for measuring against those expectations.
- Acceptability threshold for each measurement.
- Data Steward(s) to be notified in case the acceptability threshold is not met.
- Timelines and deadlines for expected resolution or remediation of the issue.
- Escalation strategy, and possible rewards and penalties.

### Develop data quality reporting

The work of assessing the quality of data and managing data issues will not benefit the organisation unless the information is shared through reporting so that data consumers understand the condition of the data. Reporting should focus around:

- Data quality scorecard, which provides a high-level view of the scores associated with various metrics, reported to different levels of the organisation within established thresholds.
- Data quality trends, which show over time how the quality of data is measured, and whether trending is up or down.
- SLA Metrics, such as whether operational data quality staff diagnose and respond to data quality incidents in a timely manner.
- Data quality issue management, which monitors the status of issues and resolutions.
- Conformance of the Data Quality team to governance policies.
- Conformance of IT and business teams to Data Quality policies.
- Positive effects of improvement projects.

## Data quality techniques

**Prevention is better than cure**

`The best way to create high quality data is to prevent poor quality data from entering an organisation. Preventive actions stop known errors from occurring. Inspecting data after it is in production will not improve its quality.`

#### Approches to preventitive action:

**Establish data entry controls** 
- Create data entry rules that prevent invalid or inaccurate data from entering a system.


**Train data producers** 
- Ensure staff in upstream systems understand the impact of their data on downstream users. Give incentives or base evaluations on data accuracy and completeness, rather than just speed.


**Define and enforce rules** 
- Create a data firewall, which has a table with all the business data quality rules used to check if the quality of data is good, before being used in an application such as a data warehouse.
- A data firewall can inspect the level of quality of data processed by an application, and if the level of quality is below acceptable levels, analysts can be informed about the problem.


**Demand high quality data from data suppliers**
- Examine an external data provider’s process to check their structures, definitions, data source(s) and data provenance. Doing so enables assessment of how well their data will integrate and helps prevent the use of non-authoritative data or data acquired without permission from the owner.


**Implement data governance and stewardship**
- Ensure roles and responsibilities are defined that describe and enforce rules of engagement, decision rights, and accountabilities for effective management of data and information assets.
- Work with data stewards to revise the process of, and mechanisms for, generating, sending, and receiving data.


**Institute formal change control**
- Ensure all changes to stored data are defined and tested before being implemented.
- Prevent changes directly to data outside of normal processing by establishing gating processes.

## Fixing the flaws: Effective corrective actions for data quality

Corrective actions are implemented after a problem has occurred and been detected. Data quality issues should be addressed systemically and at their root causes to minimise the costs and risks of corrective actions. ‘Solve the problem where it happens’ is the best practice in Data Quality Management. This generally means that corrective actions should include preventing recurrence of the causes of the quality problems.

#### Automated correction techniques 

Automated correction techniques include rule-based standardisation, normalisation, and correction. The modified values are obtained or generated and committed without manual intervention.

An example is automated address correction, which submits delivery addresses to an address standardiser that conforms and corrects delivery addresses using rules, parsing, standardisation, and reference tables.

Automated correction requires an environment with well-defined standards, commonly accepted rules, and known error patterns. The amount of automated correction can be reduced over time if this environment is well-managed and corrected data is shared with upstream systems.

#### Manually Directed Correction

Use automated tools to remediate and correct data but require manual review before committing the corrections to persistent storage. Apply name and address remediation, identity resolution, and pattern-based corrections automatically, and use some scoring mechanism to propose a level of confidence in the correction.

Corrections with scores above a particular level of confidence may be committed without review, but corrections with scores below the level of confidence are presented to the data steward for review and approval.

Commit all approved corrections, and review those not approved to understand whether to adjust the applied underlying rules. Environments in which sensitive data sets require human oversight (e.g., MDM) are good examples of where manual-directed correction may be suited.

#### Manual Correction

Sometimes manual correction is the only option in the absence of tools or automation or if it is determined that the change is better handled through human oversight.

Manual corrections are best done through an interface with controls and edits, which provide an audit trail for changes.

The alternative of making corrections and committing the updated records directly in production environments is extremely risky. Avoid using this method.

## Introducing statistical process control 

**Statistical Process Control (SPC)** is a method to manage processes by analysing measurements of variation in process inputs, outputs, or steps. The technique was developed in the manufacturing sector in the 1920s and has been applied in other industries, in improvement methodologies such as Six Sigma, and in Data Quality Management. Simply defined, a process is a series of steps executed to turn inputs into outputs. SPC is based on the assumption that when a process with consistent inputs is executed consistently, it will produce consistent outputs. It uses measures of central tendency (how values cluster around a central value, such as a mean, median, or mode) and of variability around a central value (e.g., range, variance, standard deviation), to establish tolerances for variation within a process. The primary tool used for SPC is the control chart, which is a time series graph that includes a central line for the average (the measure of central tendency) and depicts calculated upper and lower control limits (variability around a central value). In a stable process, measurement results outside the control limits indicate a special cause.

### How does SPC work?

SPC measures the predictability of process outcomes by identifying variation within a process. Processes have variation of two types: **Common Causes** that are inherent in the process and **Special Causes** that are unpredictable or intermittent.

When the only sources of variation are common causes, a system is said to be in (statistical) control, and a range of normal variation can be established. This is the baseline against which change can be detected.

SPC is used for control, detection, and improvement. The first step is to measure the process to identify and eliminate special causes. This activity establishes the control state of the process. Next is to put in place measurements to detect unexpected variation as soon as it is detectable.

Early detection of problems simplifies investigation of their root causes. Measurements of the process can also be used to reduce the unwanted effects of common causes of variation, allowing for increased efficiency.

### Introducing Root Cause Analysis

A root cause of a problem is a factor that, if eliminated, would remove the problem itself. Root cause analysis is a process of understanding factors that contribute to problems and the ways they contribute. Its purpose is to identify underlying conditions that, if eliminated, would mean problems would disappear.

---

## Strategies for ingesting PII and sensitive data

Collecting and ingesting Personally Identifiable Information (PII) and sensitive data requires careful planning and adherence to best practices to ensure data security and compliance with regulations. Here are some strategies to consider:

**Data Discovery and Classification**
- **Identify PII and Sensitive Data:** Use automated tools to scan and identify PII and sensitive data within your systems.
- **Classify Data:** Categorise data based on its sensitivity level (e.g., sensitive vs. non-sensitive PII) to apply appropriate security measures.

**Data Minimisation**
- **Collect Only Necessary Data:** Limit the collection of PII to what is strictly necessary for your purposes.
- **Anonymise or Pseudonymise Data:** Where possible, anonymise or pseudonymise data to reduce the risk of exposure.

**Secure Data Storage**
- **Encryption:** Encrypt sensitive data both at rest and in transit to protect it from unauthorised access.
- **Access Controls:** Implement strict access controls to ensure that only authorised personnel can access sensitive data.

**Compliance and Policy Implementation**
- **Regulatory Compliance:** Ensure compliance with relevant regulations such as GDPR.
- **Data Protection Policies:** Develop and enforce data protection policies that outline how PII should be handled.

**Regular Audits and Monitoring**
- **Conduct Regular Audits:** Regularly audit your data handling practices to identify and address any vulnerabilities.
- **Continuous Monitoring:** Implement continuous monitoring to detect and respond to potential data breaches promptly.

**Employee Training**
- **Training Programs:** Educate employees about the importance of data protection and best practices for handling PII.
- **Awareness Campaigns:** Conduct regular awareness campaigns to keep data protection top of mind for all staff.
- **Training Programs:** Educate employees about the importance of data protection and best practices for handling PII.

## Case Study

### Challenges

**Data Discovery and Classification:**

The company had vast amounts of unstructured data, making it difficult to identify and classify PII and sensitive data. Existing data classification methods were inconsistent and lacked automation.

**Data Minimisation:**
- DataSecure Inc. collected more data than necessary, increasing the risk of exposure. There was no process in place for anonymising or pseudonymising data.

**Secure Data Storage:**
- Sensitive data was stored without adequate encryption. Access controls were insufficient, allowing unauthorised personnel to access sensitive information.

**Compliance and Policy Implementation:**
- The company struggled to keep up with evolving regulations such as GDPR. Data protection policies were outdated and not enforced effectively.

**Regular Audits and Monitoring:**
- Audits were infrequent and did not cover all aspects of data handling. There was no continuous monitoring system to detect potential data breaches.

**Employee Training:**
- Employees were not adequately trained on data protection best practices. Awareness of data security risks was low across the organisation.

### Solutions

**Data Discovery and Classification:**
- DataSecure Inc. implemented automated tools to scan and identify PII and sensitive data within their systems.
- They categorised data based on its sensitivity level, applying appropriate security measures for each category.

**Data Minimisation:**
- The company revised its data collection practices to limit the collection of PII to what was strictly necessary.
- They implemented processes to anonymise or pseudonymise data wherever possible, reducing the risk of exposure.

**Secure Data Storage:**
- DataSecure Inc. encrypted sensitive data both at rest and in transit to protect it from unauthorised access.
- They established strict access controls, ensuring that only authorised personnel could access sensitive data.

**Compliance and Policy Implementation:**
- The company ensured compliance with relevant regulations such as GDPR by regularly updating their data protection policies.
- They developed and enforced comprehensive data protection policies that outlined how PII should be handled.

**Regular Audits and Monitoring:**
- DataSecure Inc. conducted regular audits of their data handling practices to identify and address vulnerabilities.
- They implemented continuous monitoring systems to detect and respond to potential data breaches promptly.

**Employee Training:**
- The company launched training programs to educate employees about the importance of data protection and best practices for handling PII.
- They conducted regular awareness campaigns to keep data protection top of mind for all staff.

---

## PII Compliance Checklist 

**PII** stands for **Personally Identifiable Information** — any data that can identify an individual either on its own or when combined with other data.

Protecting PII is critical to comply with privacy regulations like **GDPR**, **CCPA**, **HIPAA**, and others, depending on your location and industry.

---

### 🔒 What Is PII?

PII includes any information that can be used to identify a person. There are two types:

#### 1. **Sensitive PII** (Needs Stronger Protection)
This type of PII can directly lead to identity theft or fraud if exposed.

**Examples:**
- Full name + social security number
- Passport or driver’s license number
- Financial account numbers (e.g., bank, credit card)
- Medical records
- Biometric data (fingerprints, retina scans)
- Full date of birth (MM/DD/YYYY)
- Login credentials (username and password)

#### 2. **Non-Sensitive PII** (Less Risky Alone)
This data may identify a person but doesn't pose as much risk by itself.

**Examples:**
- First and last name (without other details)
- Email address (personal or work)
- Phone number
- Zip code
- Gender
- Job title
- General location (e.g., city or state)

Note: Non-sensitive PII can become **sensitive** when combined with other data.

---

### ✅ PII Compliance Checklist

Use this checklist to help ensure you're handling PII responsibly and in compliance with relevant laws.

#### 🔍 1. **Identify PII**
- [ ] Know what types of PII you collect
- [ ] Categorize data as sensitive or non-sensitive
- [ ] Map where PII is stored, processed, and transmitted

#### 🛡️ 2. **Protect Data**
- [ ] Encrypt sensitive PII in storage and transit
- [ ] Use strong passwords and multi-factor authentication (MFA)
- [ ] Limit access to PII to only necessary personnel
- [ ] Anonymize or pseudonymize data when possible

#### 🔐 3. **Set Access Controls**
- [ ] Role-based access permissions
- [ ] Regularly review and update access rights
- [ ] Log and monitor access to sensitive PII

#### 📜 4. **Document Policies**
- [ ] Create a data privacy policy
- [ ] Train staff on data handling and privacy best practices
- [ ] Maintain records of consent (especially under GDPR)

#### 🧹 5. **Data Minimization & Retention**
- [ ] Only collect data you actually need
- [ ] Set retention periods for PII and stick to them
- [ ] Securely delete PII when it's no longer needed

#### 🚨 6. **Breach Preparedness**
- [ ] Have a breach response plan
- [ ] Know your legal obligations for notifying affected users and regulators
- [ ] Test your plan regularly

---

### 📝 Summary

PII compliance means being responsible with people’s personal data. Know what data you have, secure it, give people control over it, and be prepared in case of a data breach. Even small organizations must take it seriously.

---

## A checklist for responsible data stewardship

### 1. Discover, Identify, Classify, and Categorise PII**

The cornerstone of PII compliance lies in a thorough understanding of your data landscape. Conducting a comprehensive audit becomes the backbone of this process. The journey begins with a meticulous effort to discover the exact locations where PII resides within your organisation's data repositories. Categorisation, based on varying levels of confidentiality, is essential.

### 2.Create a Compliance-Based PII Policy**

This policy serves as the guiding document, articulating the purpose behind the collection of PII, establishing the legal basis for processing, and delineating the measures implemented to safeguard this information. The clarity and precision of this policy are paramount, ensuring that every employee is not only aware of its existence but also adheres to its principles. It becomes the ethical compass that steers the organisation through the complexities of data governance.

### 3.Practice Identity and Access Management  

The implementation of Practice Identity and Access Management (IAM) practices should be designed not only to restrict unauthorised access but also to regularly review and update user access privileges. The alignment of these privileges with job roles and responsibilities becomes the anchor, ensuring that access is not only secure but also purposeful.

### 4.Monitor and Respond

In the ever-shifting landscape of digital security, continuous monitoring becomes the heartbeat of effective PII compliance. Simultaneously, it advocates for the establishment of an incident response plan.

### 5.Regularly Assess Your Organisation’s PII

The journey towards PII compliance is not a one-time endeavour but an ongoing commitment, making periodic assessments of an organisation's PII practices a critical task. Internal audits and risk assessments become the instruments of scrutiny, identifying areas for improvement and addressing emerging threats. It is a proactive stance that ensures the adaptive evolution of PII compliance strategies in tandem with the ever-changing threat landscape.

### 6.Prepare a Data Breach Response Plan

Anticipation and preparedness are the hallmarks of resilient organisations. Despite the most stringent preventive measures, the possibility of a data breach looms. Beyond the blueprint, it emphasises the necessity of practicing and regularly updating this plan. You will learn more about compliance and regulatory requirements, as well as responsibilities related to handling sensitive and personal data, in future modules.


