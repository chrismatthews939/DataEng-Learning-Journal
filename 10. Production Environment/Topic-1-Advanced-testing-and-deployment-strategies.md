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

### Tuning for Performance

Once the bottlenecks are known, tuning can begin. Techniques include:

- **Parallelisation:** Break tasks into smaller pieces that run in parallel (e.g., multi-threaded file reads, distributed Spark jobs).
- **Caching:** Save repeated computations, especially for static reference data.
- **Query Optimisation:** Use indexes, avoid full-table scans, simplify joins.
- **Infrastructure Scaling:** Vertical scaling: Give more CPU/memory to key components. Horizontal scaling: Add more nodes or workers.

---

# Lesson 3: Deployment Strategies for Data Pipelines

Deployments can be risky. A new feature or change to a data pipeline might seem small, but a single misstep could result in broken dashboards, delayed reports, or even data loss. That’s why smart deployment strategies are essential - they reduce risk, protect uptime, and give teams the control they need to innovate safely. In this lesson, we’ll explore techniques like blue-green, canary, and zero-downtime deployment - plus the tools that help automate it all.

---

### Blue-Green Deployment

- **Blue:** The current, stable production version.
- **Green:** The new version being prepared for release.

Blue-Green deployment ensures seamless transitions between application versions. Instead of updating a live environment directly, you prepare the new version in a separate environment and reroute user traffic only when it's ready. This dramatically reduces downtime and provides an easy way to roll back if something goes wrong.

---

### Canary Deployment

Rather than releasing to all users at once, canary deployment starts small - typically to 5–10% of users or data. This staged approach helps teams catch errors early, before they become widespread.

---

### Zero-Downtime Deployments

Zero-downtime techniques aim to avoid any service interruption. This may involve:

- Updating systems behind load balancers.
- Using rolling updates to change components one at a time.
- Running shadow traffic through the new system to test quietly in the background.

---

### Feature Toggles and Controlled Releases

Sometimes you want to deploy code changes without making new features visible right away. That’s where feature toggles come in. They allow you to turn features on or off without additional deployments. This technique supports gradual rollout, A/B testing, and rapid rollback.

This is especially important for real-time systems like fraud detection pipelines, where any pause could affect user experience or financial outcomes. These types of deployments require robust automation, monitoring, and failover mechanisms to implement.

---

## Rollbacks vs. Roll-Forwards

No deployment is risk-free. When something goes wrong, you need a plan:

- **Rollback:** Revert to the previous known-good version.
- **Roll-Forward:** Deploy a new version that fixes the problem

Rollback is faster and safer in the short term.

Roll-forward is useful when rollback isn’t possible (e.g. irreversible database changes).

---

## Deployment Automation Tools

Manual deployment is error-prone. Most teams automate using tools like:

- **GitHub Actions:**  For building and deploying code on merge or push.
- **Ansible, Chef, or Puppet:** For provisioning infrastructure.
- **Rsync + SSH:** For syncing files to servers in basic setups.

These tools enable repeatable, reliable deployments - and often integrate with CI/CD pipelines to automatically run tests before any release.

---

# Lesson 4: Automating Deployments and Managing Risk

`“If you have to ask, ‘Did it deploy?’, your system isn’t doing its job.”`

Modern data teams can’t afford to treat deployment as a manual chore. Automating your pipeline not only saves time - it ensures quality, consistency, and resilience at scale. In this lesson, you’ll explore the infrastructure, safeguards, and team practices that support reliable automated deployment in real-world data engineering environments.

---

### The Infrastructure Behind Automation

To move from manual to reliable automated deployment, you need more than just a CI/CD tool - you need an environment that supports continuous delivery. Key elements include:

- **Containerisation (e.g. Docker):** Package pipeline components in isolated environments to run consistently anywhere.
- **Infrastructure as Code (e.g. Terraform, Ansible):** Version-control your environments, not just your code.
- **CI/CD Orchestration (e.g. GitHub Actions, GitLab CI):** Trigger tests, builds, and deployments automatically on code events.

---

### Quality Gates, Metrics & Safeguards

What protects production from broken changes? Automated quality gates are your first defence. These may include:

- **Schema validation:** Ensures structure of incoming or transformed data hasn't changed unexpectedly.
- **Test coverage checks:** Require ≥90% coverage for all new pipeline functions.
- **Performance thresholds:** For example, processing must remain under 10 minutes or below 80% memory usage.

---

### Monitoring and Alerting in Production

Once deployed, monitoring ensures your system stays healthy. Effective monitoring includes:

- **Pipeline Health Dashboards:** Job success/failure, run times, delays
- **Data Quality Metrics:** Null values, duplicates, row counts, freshness
- **System Metrics:** CPU/memory usage, disk I/O, queue depth

**Tooling Suggestion:** Combine Prometheus or CloudWatch with Grafana dashboards and Slack alerts for live notifications.

---

### Operational Risk Management in Deployments

Risk isn’t just technical - it’s operational. Effective teams prepare for failure with structure:

- **Deployment Playbooks:** Clear steps for deploying, verifying, and rolling back.
- **Scheduled Releases:** Avoid deploying during high-risk business hours.
- **Stakeholder Coordination:** Alert business units and analysts ahead of updates.
- **Blameless Postmortems:** Learn from failures and update the process.

`Think of deployment like launching a rocket - checklists, communication, and contingency plans are just as important as the launch itself.`

---





