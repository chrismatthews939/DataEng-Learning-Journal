# Sustainability Considerations - 04/12/2025

# Evaluating the Environmental Impact of Technology Solutions

> "Every query we run, every pipeline we build, and every model we train leaves a footprint - not just in logs, but on the planet. As data engineers, we’re not just shaping digital systems; we’re influencing real-world energy use and environmental outcomes. In this lesson, we’ll explore why sustainability isn’t just a buzzword - it’s a core responsibility of modern data engineering."

# Why environmental impact matters in data engineering

As data engineers, we help design and operate the systems that consume significant energy and drive digital infrastructure. That means we also have the ability — and responsibility — to reduce their environmental footprint.

Key reasons this matters include:

- **Data infrastructure is energy-intensive:** Data centres, cloud services, and compute-heavy processes can have high carbon emissions.
- **Stakeholder pressure is growing:** Customers, regulators, and shareholders increasingly expect evidence of sustainable practices.
- **Sustainable solutions are cost-effective:** Reducing energy usage can also lower operational costs.

Your ability to evaluate impact helps ensure that the systems you design are not only functional but also responsible.

---

## Where environmental impact comes from

In data engineering, environmental impact typically arises from:

| Source                 | Impact type                                               |
|------------------------|-----------------------------------------------------------|
| Data centres           | High electricity consumption and cooling demand           |
| Cloud infrastructure   | Depends on provider energy sourcing and workload distribution |
| Storage practices      | Insufficient data storage wastes energy and space         |
| ETL / ELT Pipelines    | Poorly optimised jobs can lead to unnecessary compute usage |
| Model training (ML/AI) | Energy-intensive, especially in large-scale training      |

---

## What makes impact evaluation difficult?

Many environmental effects are indirect and not immediately visible. This makes it challenging to:

- Measure emissions at the level of code, queries, or pipelines
- Access provider-specific sustainability metrics (e.g., AWS carbon footprint per workload)
- Compare one solution’s footprint to another (e.g., batch vs. streaming)

Still, there are practical starting points to help you estimate and reduce impact.

---

## Practical metrics and indicators

You won’t always have a full lifecycle analysis — but you can track and compare:

| Indicator                    | Example tool / method                                           |
|-----------------------------|------------------------------------------------------------------|
| Compute time and utilisation| Spark UI, Airflow logs, serverless metrics                      |
| Storage usage over time     | CloudWatch, BigQuery table sizes                                |
| Data redundancy and retention| Manual audits, S3 lifecycle rules                               |
| Carbon intensity (where available) | Azure Sustainability Calculator, Google Cloud Carbon Footprint dashboard |

> **Tip:** Some cloud providers offer region-specific carbon reporting — choosing low-carbon regions or greener defaults makes a measurable difference.

---

## Activity: Scenario reflection

**Scenario: Batch job efficiency**

Your organisation runs a daily batch ETL job on a cloud-based data lake. It extracts and processes raw data from multiple sources. Here are some baseline job metrics:

| Metric                    | Value                  |
|---------------------------|------------------------|
| Data scanned per run      | 3.2 TB                 |
| Useful data in final output | 0.8 TB               |
| Compute time              | 6 hours                |
| Storage format            | CSV                    |
| Job frequency             | Daily                  |
| Cloud carbon region factor (proxy) | 0.0004 kg CO₂ / compute unit |

Which of the following improvements would you choose?

### Option A
Change to incremental processing:

- Data scanned per run: **0.9 TB**
- Compute time: **2 hours**
- Output quality: **same**

---

## 1 — Compare CO₂ Impact

Use this proxy formula:

Estimated Emissions = Compute time (hrs) × Carbon factor
Carbon factor = 0.0004 kg CO₂ per unit per hour

---

# Designing Sustainable and Energy-Efficient Technology Systems

> "Every system we design leaves a legacy - not just in code, but in carbon. As data engineers, we often focus on performance, scalability, and cost. But what if sustainability became a core design metric too? In this lesson, we’ll explore how the choices you make at the architecture stage - from storage formats to compute strategies - can significantly reduce environmental impact. Because designing for sustainability isn’t just good practice - it’s smart engineering."

# Why does sustainable design matter?

Design decisions in data systems have long-term environmental consequences. Inefficient pipelines, excessive storage, and poor scheduling can lead to:

- **High energy use and carbon emissions**
- **Increased cloud costs and infrastructure strain**
- **Reputational and compliance risks as ESG standards rise**

As a data engineer, you are in a position to design for sustainability from the outset, not just optimise later.

---

## Guiding framework: AWS Well-Architected Sustainability Pillar

The AWS Sustainability Pillar provides a widely used, cloud-native framework to design low-impact, high-efficiency systems. While AWS-specific in origin, its principles are broadly applicable across platforms.

### Summary of core principles

| Principle | Description |
|---------|------------|
| Understand your impact | Track carbon and energy usage (e.g., with dashboards or usage estimates) |
| Set sustainability goals | Align workload decisions with ESG or organisational targets |
| Maximise utilisation | Use auto-scaling, serverless, and spot instances to avoid overprovisioning |
| Optimise data storage | Apply compression, partitioning, and lifecycle policies |
| Use energy-efficient regions | Choose cloud regions powered by renewables |
| Optimise over time | Continuously monitor and improve workloads based on usage and emissions |
| Reduce downstream impact | Avoid passing inefficiency to consumers or downstream systems |

These principles are designed to be practical, measurable, and evolving — ideal for use in both SME and enterprise environments.

---

## Applying the AWS Sustainability Pillar to data engineering scenarios

Let’s walk through how a data engineer might apply the AWS Sustainability Pillar when designing a real system.

### Scenario

You’re designing a data platform to collect and analyse sensor data from IoT devices across the UK. The platform receives streaming data, stores historical logs, and supports weekly reporting to stakeholders.

Below is a step-by-step example of how to apply the sustainability pillar to this scenario:

---

### Pillar principle 1 — **Understand your impact**
Review estimated data volumes, storage size, and expected compute cycles.  
Use AWS Cost Explorer or Green House Gas (GHG) proxies to estimate emissions.

### Pillar principle 2 — **Set sustainability goals**
Agree upfront that storage will be limited to 90 days and compute tasks should remain under a fixed carbon threshold.

### Pillar principle 3 — **Maximise utilisation**
Use AWS Lambda or Glue with auto-scaling for ingestion and aggregation to avoid running idle VMs.

### Pillar principle 4 — **Optimise storage and transfer**
Store data in compressed, partitioned Parquet format.  
Set up Amazon S3 lifecycle rules to move old data to Glacier.

### Pillar principle 5 — **Use energy-efficient regions**
Choose a region with high renewable energy usage (e.g., AWS Ireland) unless latency is critical.

### Pillar principle 6 — **Optimise over time**
Implement weekly monitoring of compute and storage usage.  
Set review milestones to improve job logic or eliminate redundancies.

### Pillar principle 7 — **Reduce downstream impact**
Avoid generating bloated reports or unnecessary intermediate files.  
Deliver only what is needed to end users.

---

## Summary

The Sustainability Pillar isn’t a checklist — it’s a thinking tool that prompts you to ask better questions about compute, storage, data flow, and operational impact.

By using the framework during system planning, you can make design decisions that are cost-effective, efficient, and environmentally responsible.

---

# Apply activity: Apply the AWS pillar — Structured process

Use this step-by-step process to apply the AWS Sustainability Pillar to a design choice.

### The scenario

You are designing a weekly reporting pipeline that processes 2 TB of sales data for executive dashboards.  
You have two possible system configurations:

---

## Decision point

| Component | Option A (less sustainable) | Option B (more sustainable) |
|---------|-----------------------------|------------------------------|
| Storage format | CSV in S3 (no compression) | Parquet with gzip compression |
| Compute setup | Always-on EC2 VMs | Auto-scaling serverless compute (e.g., Lambda + Glue) |
| Deployment region | Closest AWS region (no carbon consideration) | Region with 75% renewable energy (e.g., AWS Ireland) |

---

## Step-by-step instructions

### Step 1 — **Define Your Sustainability Goal**
Example: _“Minimise storage footprint and reduce emissions from idle compute.”_

### Step 2 — **Compare Options Using Pillar Principles**

| Pillar Principle | Which option supports it? | Why? |
|-----------------|---------------------------|-----|
| Maximise Utilisation | Option B | Auto-scaling reduces idle compute |
| Optimise Storage & Transfer | Option B | Parquet + gzip compresses data and enables efficient querying |
| Use Energy-Efficient Regions | Option B | Renewable-powered region lowers carbon intensity |

### Step 3 — **Identify Trade-Offs**

- Will Option B cost more in setup time or require new skills?
- Is there a business reason for keeping workloads in the original region?

---

# Sustainability Principles in Data Management and Storage

>"Every byte we store has a cost - not just in cloud bills, but in carbon. As data engineers, we often focus on performance and availability, but rarely stop to ask: do we really need to keep all this data, and at what environmental price? In this lesson, we’ll explore how smart data management - from compression to lifecycle policies - can dramatically reduce our digital footprint. Because sustainable systems start with sustainable storage."

# Why does data management matter for sustainability?

Data management decisions can have a long-term environmental impact. As a data engineer, your choices regarding the following can significantly affect energy use, carbon emissions, and cost:

- **What data is kept**
- **How it’s stored**
- **How often it’s accessed or moved**

According to the **AWS Sustainability Pillar**, reducing unnecessary data storage and applying lifecycle rules are among the most effective ways to improve sustainability in digital systems.

---

## Common sustainability pitfalls in data storage

In this section, we’ll uncover the hidden habits that inflate your carbon footprint — and explore how smarter storage decisions can lead to greener, leaner systems.

| Practice | Sustainability Issue |
|--------|----------------------|
| Keeping all raw data indefinitely | High storage cost and unnecessary emissions |
| Using inefficient file formats | Increases scan time and storage space |
| Duplicated datasets | Multiplies storage and compute load |
| No archiving policy | Causes “data hoarding” and unmanaged growth |
| Defaulting to hot storage tiers | Wastes energy for rarely accessed data |

As noted by **Seagate**, using compression and tiered storage can reduce environmental impact while lowering operational costs.

---

## Applying sustainability principles to data management

Practical strategies aligned with leading frameworks include:

| Sustainability Action | What It Involves |
|----------------------|------------------|
| **Data minimisation** | Store only what’s necessary. Remove low-value or expired data. |
| **Compression & file optimisation** | Use Parquet or ORC formats and apply gzip or Snappy compression. |
| **Lifecycle automation** | Apply deletion or archiving rules using tools like S3 Lifecycle or Azure Blob policies. |
| **Storage tiering** | Move cold or infrequently accessed data to archival tiers (e.g., Glacier). |
| **Partitioning & pruning** | Reduce scan times by partitioning tables (e.g., by date or region). |
| **Audit and review** | Use tools to periodically identify stale or unused datasets. |

These strategies are supported by guidance from **DATAVERSITY** and **Reply**, which emphasise automated lifecycle management and format optimisation as critical levers for greener data systems.

---

## A real-world example

**Scenario:**  
Your organisation stores five years of clickstream logs (~60 TB) in uncompressed JSON format with no retention or archiving policy. You could apply the following sustainable practices:

- Convert to **Parquet** and apply **gzip** compression
- Partition data by **month and region**
- Archive data older than **6 months** using **Glacier**
- Introduce **S3 lifecycle rules** to delete stale logs

As shown in the **AWS Sustainability Pillar**, these changes can cut storage costs, reduce compute emissions, and improve system responsiveness.

---

## Micro-activity: Review and improve

Now it’s your turn to put sustainable thinking into practice. In this activity, you’ll examine a real-world storage setup and identify practical ways to reduce its environmental impact.

**Storage setup:**

- 5 years of sensor logs stored in CSV  
- No compression or partitioning  
- No data ever deleted or archived  
- Full dataset scanned weekly

---

# Introduction to Corporate Social Responsibility

>"Corporate Social Responsibility (CSR) is no longer just a line in a company’s annual report - it’s a strategic priority. From climate action to digital inclusion, organisations are being held accountable for how they impact the world. And technology is at the heart of that transformation. In this lesson, we’ll explore how data systems, cloud platforms, and ethical design choices empower companies to meet their CSR goals - and how you, as a data engineer, can be part of that impact."

# What is CSR and why does it matter in technology?

**Corporate Social Responsibility (CSR)** refers to an organisation’s commitment to operate ethically and sustainably, balancing profit with social and environmental responsibility. Key CSR pillars include the following:

- **Environmental sustainability**
- **Ethical governance and compliance**
- **Diversity, equity, and inclusion**
- **Community engagement and digital access**

Technology enables and strengthens CSR efforts by:

- Providing tools to measure and report impact
- Enabling more efficient, ethical, and inclusive services
- Reducing the environmental footprint of operations through data-driven optimisations

---

## How technology supports CSR

In this section, we’ll explore how different areas of CSR are powered by smart, ethical, and sustainable technology choices — and how your work as a data professional contributes to that mission.

### CSR Focus Areas and Technology Contributions

| **CSR Focus Area**            | **How Technology Contributes**                                                                                 |
|------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Environmental Sustainability | Enables emissions tracking, energy monitoring, and optimisation (e.g., cloud dashboards, smart sensors)        |
| Ethics and Transparency      | Auditable systems support fair data use, AI accountability, and digital trust                                  |
| Community & Inclusion        | Builds accessible tools, inclusive platforms, and community learning services                                  |
| Digital Responsibility       | Guides responsible AI use, carbon-aware compute, and software efficiency                                       |

### In the context of data engineering, your contributions might include:

- Structuring data for accurate sustainability reporting
- Enabling fair, ethical processing in AI pipelines
- Choosing designs that reduce energy use and data waste

---

## Case Study Examples

### Case Study 1: Microsoft — Data and Cloud for CSR

Microsoft’s CSR strategy is deeply embedded in its technology platforms.  
The **Microsoft Cloud for Sustainability** provides real-time emissions monitoring and goal tracking for customers.

> *Image source: techxmedia.com*

Microsoft aims to be carbon negative by **2030** and has committed to removing all historical emissions by **2050**.  
The role of technology in this aim includes the following:

- Emissions dashboards
- AI-powered sustainability analytics
- Open environmental data platforms

---

### Case Study 2: Google — Towards 24/7 Carbon-Free Energy

Google is working toward running all data centres and offices on **24/7 carbon-free energy by 2030**.

> *Image source: devoteam.com*

To achieve this, Google uses advanced AI models, real-time energy data, and carbon-aware scheduling to shift workloads to times and locations where the grid is cleanest.  
The role of technology in this initiative includes:

- Real-time carbon-aware workload scheduling
- Grid carbon data integration
- Forecasting clean energy availability

---

# Strategies for Aligning Technology Practices



