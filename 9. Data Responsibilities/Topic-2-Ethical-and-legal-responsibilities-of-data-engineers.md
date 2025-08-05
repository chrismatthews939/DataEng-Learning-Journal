# Topic 2 - Ethical and legal responsibilities of data engineers 07/08/2025

# Ethical Considerations in Data Engineering

As a data engineer, it's important to understand that your work doesn't just involve building data pipelines and optimizing systems — it also has real-world ethical implications. Every decision you make, from data collection to processing and storage, can impact individuals, communities, and society at large. Below, we explore some key ethical considerations and trade-offs you'll likely encounter in your role.

---

## Key Ethical Considerations

### 1. **Privacy**
- **Definition**: Respecting and protecting individuals’ personal data.
- **Examples**: Ensuring data is anonymized; not collecting more data than necessary; complying with data protection regulations like GDPR or CCPA.

### 2. **Bias and Fairness**
- **Definition**: Avoiding discrimination and ensuring data and algorithms treat all groups equitably.
- **Examples**: Ensuring datasets are representative; auditing AI models for bias.

### 3. **Transparency**
- **Definition**: Making sure stakeholders understand how data is collected, processed, and used.
- **Examples**: Documenting data lineage; maintaining explainability in AI systems.

### 4. **Accountability**
- **Definition**: Taking responsibility for data engineering decisions and their outcomes.
- **Examples**: Logging data transformations; enabling audits and traceability.

### 5. **Security**
- **Definition**: Protecting data from unauthorized access and breaches.
- **Examples**: Encrypting data at rest and in transit; managing access controls.

---

## Ethical Trade-Offs

### 1. **Innovation vs Privacy**
- **Scenario**: You want to build a personalized recommendation system using user behavior data.
- **Trade-off**: Collecting more user data improves personalization (innovation) but can violate user privacy if not handled properly.
- **Ethical Question**: Are we collecting more data than needed? Have we obtained informed consent?

### 2. **Efficiency vs Fairness**
- **Scenario**: An AI model selects job applicants based on past hiring data.
- **Trade-off**: The model is efficient at finding candidates like those hired in the past but may unintentionally exclude underrepresented groups.
- **Ethical Question**: Does speed and automation justify the risk of perpetuating systemic bias?

### 3. **Profit vs Social Responsibility**
- **Scenario**: A company wants to sell user data to third parties for advertising.
- **Trade-off**: This could generate significant revenue but might harm users if their data is misused.
- **Ethical Question**: Are short-term profits worth long-term reputational or societal harm?

---

## Real-World Case Study: Amazon's AI Recruitment System

### Background
In the mid-2010s, Amazon developed an AI-driven recruitment tool to help automate the hiring process by screening resumes for technical roles. The goal was to improve efficiency by reducing the time spent by recruiters on reviewing applications.

### What Went Wrong
The system was trained on resumes submitted to Amazon over a 10-year period — data that predominantly reflected male candidates, due to existing gender imbalances in the tech industry. As a result, the AI learned biased patterns and began favoring male applicants while penalizing resumes that included terms like “women’s” (e.g., “women’s chess club captain”).

### Ethical Issues Highlighted
- **Bias and Fairness**: The model discriminated against female candidates, reinforcing existing gender disparities.
- **Transparency**: Candidates had no insight into how their resumes were being evaluated.
- **Accountability**: Amazon eventually identified the issue but faced criticism for not catching it sooner.

### Outcome
Amazon ultimately scrapped the project, acknowledging that the AI could not be trusted to make unbiased decisions. This case became a widely cited example of how AI systems can unintentionally perpetuate discrimination when trained on biased historical data.

### Lessons for Data Engineers
- **Audit your data**: Understand the source and potential biases.
- **Monitor model outputs**: Continuously test for fairness and accuracy.
- **Ensure diversity in teams**: Diverse teams can spot issues that homogeneous teams may overlook.

---

## Final Thoughts

As a data engineer, your decisions shape the data infrastructure that powers AI systems and business insights. Ethical data engineering means going beyond technical excellence — it involves critical thinking about the impact of your work on people’s lives. Being mindful of these considerations will make you not only a better engineer but also a responsible one.

---

# So, how are data engineers expected to meet their legal obligations? Hospital Example

## Obligation 1: Secure system design

Hospitals must create systems that prioritise the security of patient records at every stage, from collection to storage.

### Explanation

Secure system design involves encryption, user authentication, and controlled access.

Engineers use encryption protocols like SSL/TLS for data transfer, ensuring that sensitive information like test results cannot be intercepted.

Firewalls and intrusion detection systems prevent unauthorised access to medical records.

### Example 

A hospital encrypts patient data before transmitting it to an external lab for diagnostic analysis.

Authentication measures ensure that only authorised personnel, like doctors, can access test results.

---

## Obligation 2: Documentation and accountability

Accurate records ensure hospitals can demonstrate compliance during audits and investigations.

### Explanation

Documentation includes maintaining logs of data access, processing activities, and breach reports.

This ensures accountability, as organisations can track who accessed patient records, when, and for what purpose.

### Example 

A hospital keeps detailed logs of every staff member who views or edits patient files, helping track suspicious activity and meet GDPR’s accountability requirements.

---

## Obligation 3: Stakeholder communication

Effective communication ensures that hospital staff, regulatory bodies, and patients understand compliance efforts.

### Explanation

Data engineers must clearly communicate compliance measures and security protocols to stakeholders.

This might involve employee training sessions, policy updates, or breach notifications.

### Example 

After a minor breach involving patient scheduling software, the hospital informed affected patients and outlined steps taken to resolve the issue.

Regular updates helped maintain trust and transparency.

---

# Ethical Dilemmas for Data Engineers: 

As a data engineer, you work with vast amounts of data, building systems that collect, process, and store information. While this role is technical, it comes with important ethical responsibilities. Ethical dilemmas arise when decisions about data use impact people’s privacy, safety, or fairness.

Understanding these dilemmas and how to resolve them is crucial for responsible data engineering.

---

## What Are Ethical Dilemmas?

An **ethical dilemma** happens when there are conflicting values or principles, and no option is perfectly right or wrong. For data engineers, this often means balancing things like:

- **Privacy vs. utility:** How much personal data should be used to improve services without invading privacy?
- **Fairness vs. efficiency:** How to avoid biases in data or algorithms that might unfairly harm certain groups?
- **Safety vs. autonomy:** How should automated systems make decisions that affect human lives?

---

## Common Ethical Challenges for Data Engineers

- **Data privacy:** Ensuring personal data is protected and used only for agreed purposes.
- **Bias and fairness:** Preventing algorithms from discriminating against individuals or groups.
- **Transparency:** Making sure decisions made by data systems can be understood and audited.
- **Accountability:** Taking responsibility for mistakes or harmful outcomes caused by data systems.

---

## Real Case Studies

### 1. Driverless Cars: Passenger Safety vs. Pedestrian Harm

**Challenge:**  
Driverless cars rely on AI to make split-second decisions in emergencies. A classic ethical dilemma is when a crash is unavoidable. Should the car prioritize the safety of its passengers or pedestrians who might be hit?

**Solution:**  
Manufacturers and ethicists debate programming cars with ethical frameworks — such as minimizing overall harm or prioritizing passenger safety. Some propose clear guidelines or laws that define acceptable behavior, while others suggest transparency about how decisions are made.

**Outcome:**  
The debate is ongoing. Different companies adopt different ethical priorities, and regulators are working on standards. The challenge is ensuring public trust while balancing complex moral decisions made by machines.

---

### 2. LAPD’s AI Predicting Crime Areas

**Challenge:**  
The Los Angeles Police Department used AI tools to predict "high-risk" areas for crimes to allocate resources. However, the data fed into the system reflected existing biases in policing (over-policing certain neighborhoods), potentially reinforcing discrimination against minority communities.

**Solution:**  
Critics called for greater transparency, audits of the algorithms, and the inclusion of fairness metrics. Some advocated for limiting the use of such predictive policing tools or combining them with community input to avoid unfair targeting.

**Outcome:**  
Due to public backlash and concerns about bias, the LAPD eventually scaled back the use of predictive policing tools. This case highlighted the need for fairness, accountability, and transparency in AI and data systems.

---

## Key Takeaways for Data Engineers

- Ethical dilemmas rarely have perfect solutions; thoughtful consideration and dialogue are essential.
- Always prioritize **transparency**, **fairness**, and **privacy** in your work.
- Understand the broader social impact of the data systems you build.
- Work collaboratively with ethicists, legal experts, and affected communities.
- Stay informed about regulations and best practices in data ethics.

---

# Anonymising Data While Preserving Utility

## Introduction

As a beginner data engineer, one of the important challenges you will face is handling data ethically. A common ethical dilemma arises when you need to **anonymise data** — that is, protect individuals' privacy by removing or disguising personal information — but still want to keep the data useful for analysis or machine learning. Balancing privacy and data utility is tricky because the more you anonymise, the more you might reduce the usefulness of the data.

This document explains the key ethical concerns, common anonymisation methods, how they work, and an example scenario.

---

## The Ethical Dilemma: Privacy vs Utility

- **Privacy:** People’s data contains sensitive information (like names, addresses, health details) that must be protected to prevent misuse or harm.
- **Utility:** Data engineers and analysts want to use the data to gain insights, improve services, or build models.
- **The Challenge:** Strong anonymisation techniques protect privacy but often reduce the quality or detail of the data, making it less useful.
- **Ethical responsibility:** You must find a balance where individuals’ privacy is respected without making the data useless.

---

## Common Methods for Anonymising Data

### 1. **Data Masking (Pseudonymisation)**

- **How it works:** Replace real identifiers (e.g., names, IDs) with fake ones or random values.
- **Example:** Replace “John Smith” with “User1234.”
- **Effect:** Protects direct identifiers but may still reveal information through indirect patterns.
- **Utility impact:** Keeps most of the data structure intact, so analyses can still run, but some linking to real people is lost.

---

### 2. **Generalisation**

- **How it works:** Replace specific values with broader categories.
- **Example:** Replace age 27 with age range “20-30” or replace an exact address with a city name.
- **Effect:** Reduces the chance of re-identification by hiding exact details.
- **Utility impact:** Less precise data but still usable for group-level insights.

---

### 3. **Suppression**

- **How it works:** Remove or hide certain data fields entirely.
- **Example:** Remove the “Social Security Number” column completely.
- **Effect:** Eliminates risk from those fields but can reduce the data’s usefulness.
- **Utility impact:** Useful fields may be lost, reducing what you can learn.

---

### 4. **Noise Addition**

- **How it works:** Add random “noise” or small errors to numeric data.
- **Example:** Adjust a salary of $50,000 by adding or subtracting a random amount within $500.
- **Effect:** Makes exact values uncertain, protecting privacy.
- **Utility impact:** Analysis remains mostly valid if noise is small, but exact values are obscured.

---

### 5. **k-Anonymity**

- **How it works:** Ensure that each record is indistinguishable from at least k-1 others based on identifying attributes.
- **Example:** If k=5, any combination of quasi-identifiers (like age range + ZIP code) must appear in at least 5 records.
- **Effect:** Makes it difficult to identify any single individual.
- **Utility impact:** Often requires generalisation or suppression, reducing detail.

---

### 6. **Differential Privacy**

- **How it works:** Adds carefully calibrated noise to query results or datasets to mathematically guarantee privacy.
- **Effect:** Provides strong privacy assurances even against attackers with external knowledge.
- **Utility impact:** Balances noise to preserve overall data patterns while hiding individual contributions.

---

## Example Scenario: Anonymising Hospital Data for Research

Imagine you have patient records with these fields:

| Patient ID | Name       | Age | ZIP Code | Diagnosis     | Treatment Cost |
|------------|------------|-----|----------|---------------|----------------|
| 12345      | John Smith | 27  | 12345    | Flu           | $500           |
| 12346      | Jane Doe   | 29  | 12345    | Diabetes      | $15,000        |

**Goal:** Share data with researchers without revealing identities but keep it useful for studying treatment costs by age group and location.

### Step 1: Mask direct identifiers
- Replace `Name` and `Patient ID` with random codes.

### Step 2: Generalise quasi-identifiers
- Change `Age` to age ranges (e.g., 20-30).
- Change `ZIP Code` to a broader region or first 3 digits only.

### Step 3: Consider noise addition
- Add a small random amount to `Treatment Cost` to avoid revealing exact figures.

### Resulting anonymised data:

| Patient Code | Age Range | Region | Diagnosis | Treatment Cost (approx.) |
|--------------|-----------|--------|-----------|-------------------------|
| A001         | 20-30     | 123**  | Flu       | $480                    |
| A002         | 20-30     | 123**  | Diabetes  | $15,200                 |

This protects patient privacy but still allows researchers to study cost patterns by age and region.

---

## Summary

- Ethical data engineering requires protecting individuals’ privacy **and** keeping data useful.
- Common anonymisation methods include **masking, generalisation, suppression, noise addition, k-anonymity, and differential privacy**.
- Each method balances privacy and utility differently; often, a combination is used.
- Always consider the risk of re-identification and the purpose of data use.
- Proper anonymisation helps maintain trust and comply with legal regulations.

---




