# Topic 1 - The legal aspects of data engineering and privacy-by-design 31/07/2025

# Data engineering and data protection laws

# Introduction to GDPR and DPA for Beginner Data Engineers (UK)

As a beginner data engineer working in or with UK-based data, it's essential to understand the legal frameworks that govern personal data. The two main frameworks you need to be aware of are:

- **GDPR** (General Data Protection Regulation)
- **DPA 2018** (Data Protection Act 2018)

---

## 🌍 GDPR: General Data Protection Regulation

The **GDPR** is a European Union law that came into effect on **25 May 2018**. It sets out rules for how personal data must be collected, stored, processed, and shared. Although the UK is no longer in the EU, the GDPR principles still apply under the UK’s own version, known as the **UK GDPR**.

## 🔑 Key Principles of GDPR (with Examples)

The GDPR outlines **seven core principles** that form the foundation of data protection law. These principles guide how personal data should be handled, and are essential for ensuring compliance.

---

### 1. 📜 Lawfulness, Fairness, and Transparency

**What it means:**
Data must be processed in a way that is legal, fair to the individual, and transparent about how it is used.

**Example:**
- A company collects user emails for a newsletter. It must clearly explain:
  - Why it's collecting the data (e.g., to send updates)
  - How the data will be used
  - Who it will be shared with (if anyone)

**Transparency** is often delivered through clear and accessible **privacy notices**.

---

### 2. 🎯 Purpose Limitation

**What it means:**
You must collect data only for a specific, legitimate purpose. You cannot reuse the data for another incompatible purpose later.

**Example:**
- You collect users’ email addresses to send order confirmations.
- You cannot later use those email addresses to send marketing emails unless you get separate, specific consent.

---

### 3. 📉 Data Minimisation

**What it means:**
Only collect the data you actually need for your purpose. Avoid collecting extra or unnecessary information "just in case."

**Example:**
- If you're building a job application form, asking for a candidate’s **passport number** or **marital status** is likely excessive unless there's a clear, legal need.

---

### 4. 🧼 Accuracy

**What it means:**
You must take steps to ensure the personal data you hold is correct and up to date.

**Example:**
- If a customer updates their home address, your system should reflect that change.
- You should also have processes for users to correct inaccurate data (known as the **right to rectification**).

---

### 5. ⏳ Storage Limitation

**What it means:**
Don’t keep personal data for longer than necessary. Define and enforce retention policies.

**Example:**
- If you're storing inactive user accounts indefinitely, that may violate this principle.
- Instead, delete or anonymise old accounts after a set period (e.g., 2 years of inactivity).

---

### 6. 🔐 Integrity and Confidentiality (Security)

**What it means:**
Personal data must be protected against unauthorised access, loss, theft, or damage.

**Example:**
- Encrypt sensitive data (e.g., passwords, financial info) both **at rest** and **in transit**.
- Limit access based on user roles (e.g., engineers shouldn't access HR records unless necessary).

This is also referred to as the **security principle**.

---

### 7. 📋 Accountability

**What it means:**
You must be able to show that you comply with all the above principles. This includes keeping records, conducting audits, and training staff.

**Example:**
- Maintain a **data processing register**.
- Document who has access to which data systems.
- Implement and review data protection policies regularly.

---

> ✅ **Summary Table**

| Principle                         | Summary                                 | Example Use Case                                  |
|----------------------------------|-----------------------------------------|---------------------------------------------------|
| Lawfulness, Fairness, Transparency | Be clear and legal                      | Privacy policy explains data use to customers     |
| Purpose Limitation               | Use data only for intended purposes     | Don’t use support emails for marketing            |
| Data Minimisation                | Only collect what’s necessary           | Avoid collecting DOB if not required              |
| Accuracy                         | Keep data up to date                    | Allow users to edit their profiles                |
| Storage Limitation               | Don't keep data too long                | Auto-delete logs after 90 days                    |
| Integrity and Confidentiality    | Keep data secure                        | Use encryption and access controls                |
| Accountability                  | Show you’re compliant                   | Maintain audit logs and training records          |

---

## 🇬🇧 DPA: Data Protection Act 2018

The **Data Protection Act 2018** is the UK’s implementation of the GDPR and supplements it. It also includes provisions specific to the UK, including rules on:

- Law enforcement processing
- Intelligence services processing
- Children’s data
- Exemptions for journalism, research, and archiving

### Key Differences in the UK

- The **UK GDPR** is the retained version of the EU GDPR after Brexit.
- The **DPA 2018** tailors GDPR provisions for the UK context.
- Together, they form the full picture of data protection law in the UK.

---

## 👥 What is Personal Data?

Personal data means any information that relates to an **identified or identifiable** individual. This includes:

- Name
- Email address
- Location data
- Online identifiers (e.g., IP address)
- Health records, biometric or genetic data

---

## 🎯 Responsibilities of a Data Engineer

As a data engineer, your role in GDPR and DPA compliance may include:

- Ensuring data storage is secure and encrypted
- Supporting data minimisation through efficient database design
- Implementing data retention and deletion policies
- Helping enable users' rights (e.g., right to be forgotten, data portability)
- Documenting data flows and access controls

---

## 🛑 Penalties for Non-Compliance

Organisations that fail to comply with GDPR and DPA can face:

- **Fines**: Up to £17.5 million or 4% of annual global turnover (whichever is higher)
- **Reputational damage**
- **Legal action** from individuals or regulators

---

# British airways' GDPR breach

`In 2019, British Airways faced a massive GDPR fine of £20 million after a data breach exposed over 400,000 customer records. The breach was traced to a weakly secured booking website that allowed attackers to redirect users to a fraudulent page.`

---

# Legal obligations for data engineers

## Obligation 1: Secure system design

### Explanation

Secure system design involves encryption, user authentication, and controlled access.

Engineers use encryption protocols like SSL/TLS for data transfer, ensuring that sensitive information like test results cannot be intercepted.

Firewalls and intrusion detection systems prevent unauthorised access to medical records.

### Example

A hospital encrypts patient data before transmitting it to an external lab for diagnostic analysis.

Authentication measures ensure that only authorised personnel, like doctors, can access test results.

---

## Obligation 2: Documentation and accountability

### Explanation

Documentation includes maintaining logs of data access, processing activities, and breach reports.

This ensures accountability, as organisations can track who accessed patient records, when, and for what purpose.

### Example

A hospital keeps detailed logs of every staff member who views or edits patient files, helping track suspicious activity and meet GDPR’s accountability requirements.

---

## Obligation 3: Stakeholder communication

### Explanation

Data engineers must clearly communicate compliance measures and security protocols to stakeholders.

This might involve employee training sessions, policy updates, or breach notifications.

### Example

After a minor breach involving patient scheduling software, the hospital informed affected patients and outlined steps taken to resolve the issue.

Regular updates helped maintain trust and transparency.

---

# The consequences of non-compliance with data protection

## Case study: Marriot International data breach

In 2018, Marriott International disclosed a data breach that impacted approximately 500 million customers. Sensitive data, including names, passport numbers, and credit card details, was exposed.

### Challenges

- Weak encryption protocols allowed hackers to access customer data.
- Inadequate breach detection delayed response times by months.

### Consequences

- Marriott faced a £18.4 million fine under GDPR.
- Reputational damage resulted in customer attrition, with significant losses in bookings
- The company had to invest heavily in system upgrades and compliance measures.

### Outcome

- Marriott improved its encryption standards and adopted real-time monitoring tools to prevent future breaches.
- While costly, these changes restored some customer trust over time.

---

## Consequence 1: Financial penalties

### Explanation

Under GDPR, organisations can be fined up to €20 million or 4% of their global annual turnover, whichever is higher.

These penalties are designed to ensure businesses prioritise compliance.

### Example

In 2020, British Airways was fined £20 million for failing to secure customer data, impacting over 400,000 customers.

---

## Consequence 2: Reputational damage

### Explanation

Reputational damage occurs when customers lose faith in an organisation's ability to protect their data.

This can lead to customer attrition, reduced sales, and difficulty in attracting new clients.

### Example

The 2017 Equifax breach exposed the personal data of 147 million people.

Following the breach, the company’s stock dropped by 30%, and it faced lawsuits and public criticism.

---

## Consequence 3: Operational disruption

### Explanation

Non-compliance can lead to investigations, audits, and the need to overhaul processes and systems.

This diverts resources from normal operations and increases downtime.

### Example

After a major breach, a healthcare provider had to halt operations for three days while its IT systems were audited and restored, leading to cancelled appointments and delayed treatments.

---

# Understanding privacy-by-design

**Privacy by Design (PbD)** is a foundational concept in modern data engineering and privacy practices. It means that privacy is not an afterthought or add-on—it's embedded into systems, processes, and technologies from the very beginning.

As a data engineer, understanding Privacy by Design helps you build systems that respect users' privacy while remaining compliant with regulations like GDPR or CCPA.

Below are the **seven core principles** of Privacy by Design, each with a simple explanation and a practical example relevant to data engineering.

---

## 1. Proactive not Reactive; Preventative not Remedial

**Explanation:**  
Design systems that prevent privacy issues before they happen, instead of waiting to fix them after a breach or complaint.

**Example:**  
Instead of waiting until a data breach to add encryption, ensure encryption is built into the system from the start.

---

## 2. Privacy as the Default Setting

**Explanation:**  
Users' personal data should be automatically protected. No action should be required from the user to secure their privacy.

**Example:**  
When collecting user data for analytics, ensure that only essential data (like anonymized usage patterns) is collected by default. Additional data collection should require explicit user consent.

---

## 3. Privacy Embedded into Design

**Explanation:**  
Privacy should be integrated into the architecture of the system—it’s not a separate component.

**Example:**  
In a data pipeline, design each component (ETL, storage, access controls) to consider privacy, such as redacting sensitive fields during transformation or masking data before storage.

---

## 4. Full Functionality — Positive-Sum, not Zero-Sum

**Explanation:**  
Design systems where privacy and functionality coexist; you don’t have to sacrifice one for the other.

**Example:**  
Build a recommendation engine that uses aggregated, anonymized data instead of raw user profiles, maintaining user privacy while still offering relevant suggestions.

---

## 5. End-to-End Security — Lifecycle Protection

**Explanation:**  
Ensure privacy protections cover the full data lifecycle: collection, processing, storage, and deletion.

**Example:**  
Implement secure data retention policies that automatically delete user data after a specified period, and ensure that backups follow the same rules.

---

## 6. Visibility and Transparency — Keep it Open

**Explanation:**  
Systems and processes should be transparent to users and stakeholders, with clear privacy practices and open documentation.

**Example:**  
Maintain clear documentation on how personal data is handled, and make privacy policies accessible. Use audit logs to track data access within the system.

---

## 7. Respect for User Privacy — Keep it User-Centric

**Explanation:**  
Give users control over their data and prioritize their privacy preferences.

**Example:**  
Provide users with simple tools to view, export, or delete their data from your systems, such as a self-service data portal.

---

# Case Study: Privacy by Design in an E-Commerce Purchase Flow

This case study walks through a real-world scenario of **Privacy by Design (PbD)** applied to an e-commerce website. It highlights how privacy is embedded throughout the customer purchase journey, from browsing to payment, using the seven core PbD principles.

---

## Scenario Overview

**Customer Action:**  
A user visits an e-commerce website, browses products, adds items to their cart, and proceeds to checkout and payment.

**Goal:**  
Ensure the entire transaction respects and protects user privacy using Privacy by Design principles.

---

## Step-by-Step Flow with Privacy by Design in Practice

### 1. **User Browsing the Website**

- **PbD Principle:** *Privacy as the Default Setting*  
- **Action Taken:**  
  - Non-essential tracking cookies are disabled by default.  
  - Users are prompted to opt in to analytics or marketing cookies.

- **Why It Matters:**  
  User data (e.g., behavior, preferences) is not collected without consent.

---

### 2. **Product Selection and Adding to Cart**

- **PbD Principle:** *Respect for User Privacy*  
- **Action Taken:**  
  - Products added to cart are stored in a privacy-preserving way (e.g., session-based storage, no personal data yet collected).  
  - No user account or identifiable data is required at this stage.

- **Why It Matters:**  
  The system supports anonymous browsing while preserving cart functionality.

---

### 3. **Proceeding to Checkout**

- **PbD Principle:** *Data Minimization*  
- **Action Taken:**  
  - The checkout form only asks for essential information (e.g., name, shipping address, email).  
  - Optional fields (e.g., phone number) are clearly marked and not required.

- **Why It Matters:**  
  Collecting only necessary data reduces risk and exposure.

---

### 4. **Redirecting to the Payment Page**

- **PbD Principle:** *End-to-End Security*  
- **Action Taken:**  
  - Payment is handled through a secure, third-party payment gateway.  
  - Sensitive financial data (e.g., credit card numbers) is never stored or seen by the e-commerce server.  
  - HTTPS is enforced site-wide.

- **Why It Matters:**  
  Payment processing is isolated, encrypted, and secure, reducing liability and improving trust.

---

### 5. **Order Confirmation and Receipt**

- **PbD Principle:** *Transparency and Control*  
- **Action Taken:**  
  - Users receive a confirmation email with clear details on how their data is used.  
  - They are given options to manage communication preferences (e.g., unsubscribe link).

- **Why It Matters:**  
  Users understand what happens with their data and have control over future use.

---

### 6. **Post-Purchase Data Handling**

- **PbD Principle:** *Lifecycle Protection*  
- **Action Taken:**  
  - Personal and transactional data is stored securely and encrypted at rest.  
  - Data retention policies are in place: customer data is deleted or anonymized after a defined period unless consent is given for longer retention (e.g., for loyalty programs).

- **Why It Matters:**  
  Long-term privacy is respected and data is not kept indefinitely without reason.

---

### 7. **Privacy Dashboard for the User**

- **PbD Principle:** *User-Centric Design*  
- **Action Taken:**  
  - Logged-in users can access a dashboard to view, download, or delete their personal data.  
  - Users can revoke consent for marketing communications at any time.

- **Why It Matters:**  
  Users remain in control of their data even after the transaction.

---

## Summary: Key Takeaways

| Step                        | Privacy Feature                        | PbD Principle                  |
|----------------------------|----------------------------------------|-------------------------------|
| Browsing                   | Consent banner                         | Privacy by Default            |
| Cart & Selection           | No personal data collected             | Respect for User Privacy      |
| Checkout                   | Minimal required fields                | Data Minimization             |
| Payment                    | External secure gateway                | End-to-End Security           |
| Confirmation Email         | Clear communication & choices          | Transparency and Control      |
| Data Retention             | Secure storage & deletion policy       | Lifecycle Protection          |
| User Dashboard             | Self-service privacy tools             | User-Centric Design           |

---

# Privacy Techniques for Data Engineers

As a data engineer, embedding privacy into data systems is a critical responsibility. Privacy isn't just a legal requirement (e.g., GDPR, CCPA)—it's essential for protecting customer trust and reducing business risk.

Below are fundamental techniques to help you design privacy-preserving data systems.

---

## 1. **Data Minimisation**

### What It Is:
Data minimisation means collecting, processing, and storing **only the data that is necessary** to achieve a specific purpose.

### Why It Matters:
- Reduces exposure in case of a data breach.
- Minimizes the risk of violating data protection laws.
- Makes your system simpler and easier to secure.

### Example:
If your service only needs a user's email to send notifications, don’t collect additional data like their phone number or home address.

---

## 2. **Privacy Enhancing Technologies (PETs)**

### What They Are:
PETs are tools and techniques designed to protect personal data while still enabling valuable data processing.

### Common Types of PETs:
- **Differential Privacy**: Adds mathematical "noise" to data to prevent individual identification.
- **Secure Multi-Party Computation (SMPC)**: Allows parties to jointly compute a function over their data without revealing it to each other.
- **Federated Learning**: Trains machine learning models across decentralized devices holding local data samples.

### Example:
A company wants to analyze user behavior across apps without accessing raw data from each user. It could use **federated learning** to train a model without collecting any individual data centrally.

---

## 3. **Role-Based Access Control (RBAC)**

### What It Is:
RBAC is a method of restricting access to data based on a user's role within an organization.

### Why It Matters:
- Ensures only authorized personnel can view or manipulate sensitive data.
- Helps enforce the principle of least privilege.

### Example:
- **Data Analyst**: Can view anonymized customer data for trend analysis.
- **Customer Support Agent**: Can view contact details but not full payment information.
- **Admin**: Full access (only if absolutely necessary).

RBAC is typically managed through user groups and permission levels in your data systems.

---

## 4. **End-to-End Encryption (E2EE)**

### What It Is:
E2EE ensures that data is encrypted on the sender’s side and decrypted only by the recipient. No third party—including the service provider—can read the data while it’s in transit or at rest.

### Why It Matters:
- Prevents interception or unauthorized access.
- Protects sensitive customer data during transfer and storage.

### Example:
A messaging app encrypts messages on the user’s device before sending and decrypts only on the recipient’s device. The server storing the messages cannot read them.

Apply E2EE to:
- Personal identifiers (e.g., names, email addresses)
- Financial information
- Health records

---

## 5. **Pseudonymisation Techniques for Analytics**

### What It Is:
Pseudonymisation replaces identifying fields in data records with artificial identifiers or pseudonyms.

### Why It Matters:
- Reduces risk of identification while preserving data utility for analytics.
- Required by regulations like GDPR when full anonymisation isn't possible.

### Example:
Instead of storing a user’s name and email in an analytics database, you could use a unique identifier like `user_12345`.

**Important**: Pseudonymised data can still potentially be re-identified, so it must be protected with the same care as personal data.

---

## Summary Table

| Technique                  | Purpose                                       | Example Use Case                                  |
|---------------------------|-----------------------------------------------|---------------------------------------------------|
| Data Minimisation         | Collect only what’s needed                    | Don’t collect birthdates if not required          |
| Privacy Enhancing Tech    | Allow analysis while preserving privacy       | Use federated learning to train models            |
| RBAC                      | Restrict access based on user roles           | Analysts see only anonymized data                 |
| End-to-End Encryption     | Prevent unauthorized access                   | Encrypt messages or personal records in transit   |
| Pseudonymisation          | Obscure identities during analysis            | Replace emails with unique IDs in data warehouse  |

---




