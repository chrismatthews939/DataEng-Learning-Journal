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


