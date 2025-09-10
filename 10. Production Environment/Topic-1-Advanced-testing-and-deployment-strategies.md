# Topic 1 - Advanced Testing and Deployment Strategies 10/09/2025

# Lesson 1: User Acceptance Testing (UAT)

`“It doesn’t matter how elegant your pipeline is if your users can’t use it, you’ve failed.”`

---

## Why UAT Matters

User Acceptance Testing is the final verification step before a data pipeline is declared “production ready.” It answers a crucial question: does the output meet the expectations and day-to-day needs of business users? While functional testing proves the pipeline behaves as intended from a technical perspective, UAT determines if that functionality translates into real-world value.

---

## Defining Business Requirements

### Examples 

- **Data Accuracy** “Customer gender must be correctly inferred from title in at least 98% of cases
- **Output Timeliness** “Order-to-dashboard time should not exceed 15 minutes”
- **Business Rule Application** “Inactive users (no login in 6 months) should be excluded from campaign eligibility”

### Engaging Real Users

Too often, UAT is handled solely by technical teams but real insights come from those
who use the data. These could be:

- Marketing analysts testing audience segmentation logic.
- Finance teams reviewing monthly spend reports.
- Product managers checking if product engagement metrics
align with internal dashboards.

Real users bring unique insights. They might notice:

- The filters are in the wrong order.
- The date formats don’t match what they need for Excel.
- Certain metrics are missing context (e.g., “engagement score” without a definition).

---

### Testing Business Scenarios

Realistic UAT scenarios are essential. These should mirror the workflows users perform, not just generic technical tasks. Think of these as mini-stories that simulate a typical day in the life of the business. For example:

- A retail pipeline might simulate the end-of-day aggregation of all store transactions during a seasonal promotion.
- A customer service team might want to test how complaints data appears during a product recall scenario.
- A fraud detection pipeline could be tested using both common transactions and deliberately inserted anomalies.

**Good UAT scenarios should include:**

1. **Normal Operations:** Typical traffic, regular schedules
2. **Peak Usage Periods:** Monthly financial close, Black Friday sales
3. **Edge Cases:** Empty records, malformed input, missing IDs

---

### Validating the User Experience

Beyond business logic, UAT should check how the data is consumed. Is the pipeline output intuitive, clean, and easy to act on? This includes:

- **Column Naming:** Are labels clear? (“Cust_ID” might be obvious to devs, not to users).
- **Navigation:** Can users quickly find the info they need?
- **Data Export:** Can users extract the data into formats they use (e.g., Excel, PDF)?
- **Performance:** Does the dashboard load in under 5 seconds? Can reports be generated without lag?

User experience (UX) is not fluff; it directly impacts efficiency. If the output slows down daily workflows or requires extra cleanup steps, it won’t be trusted or used. Even small improvements (like clearer dropdowns or consistent colour codes) can greatly enhance satisfaction.

`Consider running a brief usability survey alongside UAT. Ask users to rate ease-of-use, clarity, and confidence in the data.`

---

### Setting Acceptance Criteria

Finally, it’s critical to define what “success” looks like in measurable terms. Acceptance criteria remove ambiguity and reduce conflict at sign-off time. Each test case should have a pass/fail condition aligned with the original business requirement. Examples include:

- “Pipeline must process 95% of incoming data within 15 minutes of arrival”
- “Dashboard should display latest data without requiring a manual refresh”
- “Exported reports must contain all fields specified in the agreed template”

It’s best to write these in collaboration with stakeholders and document them in a shared UAT plan or spreadsheet. This ensures mutual understanding and creates a paper trail for auditing.

---

# Lesson 2: Stress Testing and Performance Tuning

`“You don’t know how strong your system is… until it breaks.”`

---

## What is Load Testing vs. Stress Testing?

Load testing and stress testing are two sides of the same coin - both explore how your pipeline behaves under pressure, but from different angles:

### Load Testing

Load Testing checks how the system handles expected conditions. For example, simulating the average daily volume of data processed or the number of concurrent users accessing a dashboard.

### Stress Testing

Stress Testing goes beyond expectations, deliberately overwhelming the system to discover breaking points, recovery behaviour, and weak spots in infrastructure.

### Key Performance Metrics to Track

Interpreting test results means knowing which metrics to watch. Common ones include:

- **Throughput:** How much data is processed per second or per job? A drop here may indicate a bottleneck.
- **Latency:** How long does it take to complete a task or load a dashboard? High latency can signal inefficient queries or under-provisioned infrastructure.
- **CPU and Memory Usage:** Spikes may reveal inefficient transformations or resource-starved components.
- **Error Rates:** Even minor error rates under stress might lead to data loss or broken pipelines during peak events.

---

### Bottleneck Detection: Where Things Go Wrong

Bottlenecks can appear at any stage in the pipeline:

- **Data Ingestion:** API rate limits or slow file parsing.
- **Transformation:** Poorly optimised joins, sorting, or aggregations.
- **Storage:** Slow reads/writes to the database.
- **Output:** Heavy dashboards or inefficient visualisation queries.

Use profiling tools or logging (e.g., Spark UI, SQL query plans, resource monitors) to trace delays. Focus your investigation on the slowest part of the pipeline - fixing that can lead to big performance gains.

---

# Tuning for Performance

Once the bottlenecks are known, tuning can begin. Techniques include:

- **Parallelisation:** Break tasks into smaller pieces that run in parallel (e.g., multi-threaded file reads, distributed Spark jobs).
- **Caching:** Save repeated computations, especially for static reference data.
- **Query Optimisation:** Use indexes, avoid full-table scans, simplify joins.
- **Infrastructure Scaling:** Vertical scaling: Give more CPU/memory to key components. Horizontal scaling: Add more nodes or workers.

