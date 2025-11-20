# Topic 1 - Evaluating technology success and managing innovation 20/11/2025

# Metrics for assessing the success of technology implementations

Imagine you’ve been asked: 'Was this new data pipeline successful?' Without pre-agreed metrics, everyone could answer differently. IT might say yes because it meets technical specs, while the business might say no due to delayed reports, and Finance might be unsure because cost savings are unclear. Metrics create a shared understanding between technical teams, management, and users.

`Think of implementing a technology solution like building a new highway. How do you know the highway was a success? You wouldn’t just look at whether it was paved. You’d measure travel time reduction, traffic flow improvements, safety improvements, and maintenance costs. Similarly, for a data pipeline, you measure speed of data movement, reliability, cost to operate, and value added to end users.`

# Categories of Metrics - With Expanded Examples

To effectively assess the success of technology implementations in data engineering projects, it's essential to use a variety of metrics. These metrics can be categorised into **performance**, **cost**, **user**, **quality**, and **business impact** metrics. Each category provides a different perspective on the success of a project, ensuring a comprehensive evaluation. Let's explore these categories with real-world examples to understand why they matter and how they contribute to the overall success of your data solutions.

## Metric Categories

| Metric Category       | Real-world Examples                                                                 | Why It Matters                                                     |
|----------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------|
| **Performance Metrics** | "Average query time reduced from 6 seconds to 1.5 seconds after migrating to a new database." | Users notice faster dashboards and happier reporting cycles.     |
| **Cost Metrics**       | "Cloud storage costs reduced by 20% by switching to more efficient storage classes." | Operational costs matter to CFOs.                                |
| **User Metrics**       | "90% of business users adopted the new self-service BI tool within 3 months."      | Adoption is critical — a technically perfect system unused is a failure. |
| **Quality Metrics**    | "Data freshness improved from 48 hours lag to near-real-time updates."             | Fresh data enables better decision-making.                       |
| **Business Impact Metrics** | "Time to market for new marketing campaigns decreased by 25% due to faster customer segmentation." | Demonstrates clear business value of tech implementation.        |

---

## Practical Scenario: Launching a Data Lake

You work in a retail company. The business launches a new data lake on a cloud platform to centralise customer purchase data from stores and online.

You define success metrics:

- **Performance:** 95% of data ingested within 1 hour of transaction  
- **Cost:** Storage costs stay within £5,000/month budget  
- **User:** 80% adoption by the analytics team within 3 months  
- **Quality:** No critical data quality issues during ingestion  
- **Business Impact:** Sales analysis cycle time reduced from 7 days to 1 day  

**The Result:**  
Because these metrics are clear from the start, after six months you can prove success — or pinpoint where improvements are needed.

---

## How to Apply Metrics Effectively: 3 Golden Rules

Defining and applying metrics is only the first step in ensuring the success of your data engineering projects. To truly leverage these metrics, follow best practices for their application:

### 1. Agree Early
- Define success metrics at the project scoping stage.
- Confirm with both technical and business stakeholders.

### 2. Be Specific
- "Good performance" is too vague.  
- Instead: "Pipeline completes ingestion of daily sales data within 20 minutes."

### 3. Monitor Continuously
- Use operational dashboards (e.g., Grafana, PowerBI).  
- Set automated alerts if KPIs fall outside thresholds.

---

# What is a Post-Implementation Review (PIR)?

After deploying a technology solution, it's crucial to step back and evaluate its performance comprehensively. This is where Post-Implementation Reviews (PIRs) come into play. A PIR is a structured evaluation conducted after a project is completed, aimed at assessing what worked well, what didn't, and what can be improved for future initiatives. In this lesson, we will delve into the importance of PIRs, the key stages involved, and how to conduct them effectively to ensure your technology solutions continually evolve and improve.

# Why do Post-Implementation Reviews (PIRs) Matter?

PIRs are recognised best practice by organisations such as the Government Digital Service (GDS) and the Engineering Council UK, as they:

- Help organisations learn from experience
- Highlight hidden risks
- Celebrate successes and good practices
- Build a culture of continuous improvement
- Improve future technology projects

A good PIR focuses on **facts and future improvements** — not assigning blame.

---

# The Key Stages of a Post-Implementation Review

Conducting a thorough Post-Implementation Review (PIR) involves several key stages, each designed to evaluate different aspects of the project. These stages help ensure a comprehensive assessment of the project's success and areas for improvement. The key stages are:

| PIR Stage           | Purpose                                        | Example Questions |
|--------------------|-----------------------------------------------|-----------------|
| Objectives Review  | Did the project achieve its intended goals?   | Did the data migration improve access speed? |
| Process Evaluation | How effective were project methods and workflows? | Were Agile sprints and ceremonies efficient? |
| Technical Assessment | How well did the technology perform against criteria? | Was downtime within acceptable limits? |
| Stakeholder Feedback | How did users, sponsors, and partners experience it? | Did users find the new dashboards intuitive? |
| Lessons Learned    | What should be repeated or avoided next time? | Should we engage security teams earlier next time? |

---

# Practical Example: PIR for a Data Warehouse Migration

After migrating a company’s data warehouse to the cloud, you conduct a PIR and find:

- **Objective:** Faster access to reports — achieved with a 45-minute refresh cycle  
- **Process:** DevOps automation was delayed due to unclear handovers  
- **Technical:** Overall system performance met expectations  
- **Stakeholders:** Analysts requested better training  
- **Lessons Learned:** Create schema validation scripts earlier; provide training before go-live  

---

# Common Mistakes to Avoid in PIRs

While conducting Post-Implementation Reviews (PIRs) is crucial for continuous improvement, it's equally important to be aware of common pitfalls that can undermine their effectiveness:

| Mistake                   | Impact                              | How to Avoid It |
|----------------------------|------------------------------------|----------------|
| Making the review too technical | Misses broader business lessons | Involve business and technical stakeholders |
| Blame-focused discussions   | Reduces morale and trust           | Focus on process, not individuals |
| Ignoring stakeholder feedback | Misses critical user issues       | Include user surveys or interviews |
| Poor record-keeping         | Lessons are forgotten for future projects | Write and share a formal PIR report |

---

# Example PIR Report

Here is an example of a simple PIR report:

> An example PIR report, image source: [pmmodocs.com](https://pmmodocs.com) (opens in a new tab)

The recommended structure of a simple PIR report is as follows:

1. Executive Summary  
2. Project Objectives and Outcomes  
3. Process Review  
4. Technical Assessment  
5. Stakeholder Feedback  
6. Lessons Learned  
7. Recommendations for Future Projects

---

# Why Analysing Performance and Business Impact Matters

In today's competitive landscape, delivering a technology project is not enough — you must also prove its value. Modern organisations expect data engineers and technology teams to demonstrate both the technical performance and the business impact of their solutions. This lesson will explore why analysing performance and business impact matters, the two dimensions of evaluation, and data-driven methods for evaluating technology success. By grounding your evaluations in data, you ensure that your assessments are based on facts, not opinions, and can clearly show the value your projects bring to the organisation.

# Evaluating Technology Project Success

## The Two Dimensions of Evaluation

Evaluating the success of a technology project involves looking at two critical dimensions: **technical performance** and **business impact**.  

- **Technical performance** focuses on how well the system functions, including aspects like query speeds, system uptime, and error rates.  
- **Business impact** examines how the system affects business outcomes, such as sales growth, time saved, and customer satisfaction.  

Both dimensions are essential — a system that runs perfectly but delivers no business value is not considered successful.

### Summary of Dimensions

| Dimension             | Focus                          | Example                                   |
|----------------------|--------------------------------|-------------------------------------------|
| Technical performance | How the system functions       | Query speeds, system uptime, error rates  |
| Business impact       | How the system affects business outcomes | Sales growth, time saved, customer satisfaction |

---

## Data-Driven Methods for Evaluating Technology Success

To effectively evaluate technology projects, it’s essential to use **data-driven methods**. These methods provide objective, quantifiable insights into both technical performance and business impact.  

### Common Methods

| Method                     | Description                                    | Example Use                                         |
|-----------------------------|-----------------------------------------------|---------------------------------------------------|
| KPI Tracking                | Monitor agreed performance indicators over time | Data pipeline completion time monitored daily     |
| Before-and-After Comparison | Compare key measures before and after implementation | Customer churn rate before vs. after a new analytics model |
| Cost–Benefit Analysis       | Compare project costs against achieved benefits | Cloud migration cost vs. storage savings          |
| User Feedback Surveys       | Collect structured feedback on system use and satisfaction | User satisfaction rating for new dashboard features |
| Business Analytics Dashboards | Track adoption, efficiency gains, and other impacts | Real-time dashboard showing report delivery improvements |

By leveraging these methods, you can ensure that evaluations are grounded in reliable data, demonstrating the true value of technology solutions.

---

## Practical Example: Evaluating a New Data Platform

Your company deployed a new cloud data platform to speed up data analysis for marketing teams.  

**Key evaluation metrics include:**

### Technical Performance
- Query speed improved from 15 seconds to 3 seconds  
- System uptime maintained at 99.95%  
- Data ingestion latency reduced by 60%  

### Business Impact
- Marketing campaign development cycle time reduced by 30%  
- Customer segmentation accuracy improved by 12%  
- Estimated additional £500,000 revenue enabled by faster launches  

This shows the technical success and a clear commercial return.

---

## Common Mistakes When Analyzing Business Impact

Analyzing business impact is crucial for demonstrating value, but common pitfalls can undermine evaluations.  

| Mistake                     | Impact                                  | How to Avoid It                                       |
|------------------------------|----------------------------------------|------------------------------------------------------|
| Only reporting technical success | Business leaders may not see true value | Always translate technical metrics into business terms |
| Focusing only on costs       | Misses opportunity to show efficiency or revenue gains | Highlight productivity improvements, time savings, or revenue growth |
| Ignoring user experience metrics | Risks missing critical adoption challenges | Collect adoption rates and user satisfaction feedback |

---

## Telling the Story of Impact

When presenting evaluation findings:

- Use numbers to prove technical and business outcomes  
- Use before-and-after comparisons to show change  
- Use graphs, charts, and simple visuals to make insights clear  
- Connect metrics directly to business objectives (revenue, cost, speed, compliance)  

**Example:**

> "After launching the new data platform, marketing reduced campaign development times by 30%, leading to an additional £500,000 in seasonal revenue — directly linked to our system improvements."

---

# Managing Innovation and Staying Ahead







