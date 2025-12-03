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




