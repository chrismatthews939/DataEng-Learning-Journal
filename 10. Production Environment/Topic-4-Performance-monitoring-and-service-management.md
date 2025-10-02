# Topic 4 - Performance monitoring and service management 02/10/2025

# Lesson 1 - Advanced Metrics & KPIs for Production Systems

## The signals that matter

1. **Latency** - Latency measures the time it takes for a request to travel from the client to the server and back. It's a critical indicator of the responsiveness of a system.
2. **Traffic** - Traffic measures the demand placed on your system and is typically measured in requests per second.
3. **Errors** - Errors track the rate of failed requests, including HTTP 500 errors, timeouts, or other application-specific failures.
4. **Saturation** - Saturation measures how "full" your system is, reflecting the utilization of resources like CPU, memory, disk space, and network bandwidth. 

## Further info

1. **Latency** - The time it takes to serve a request end-to-end. Track it as a distribution (p50/p95/p99), and treat “slow enough to violate the SLO” as an error. In data pipelines this can be job runtime or event-to-serving latency.
2. **Traffic** - How much demand hits the system. Common units are requests/sec, queries/sec, rows or messages per second, or jobs/hour for batch.
3. **Errors** - The rate of failed or incorrect results. Include explicit failures (5xx, exceptions), implicit ones (timeouts, SLO-breaching latency), and content errors (schema/quality failures in data jobs).
4. **Saturation** - How “full” the service is relative to its limits. Watch sustained utilization of constrained resources (CPU, memory, I/O, thread/connection pools, queue depth, Kafka consumer lag) and how close you are to headroom.

![Read the tail not the avg](https://media.nngroup.com/media/editor/2021/11/29/website-latency-long-tails.jpg)

Averages hide pain. Track latency as a distribution: p50 is typical, p95 and p99 expose the “long tail” that users notice. In a warehouse query or Spark job, a small number of very slow runs can break SLAs even when the mean looks fine. When visualising, place p95/p99 on the same graph as p50 so tail growth is obvious.

### Make the KPIs concrete (formulas you can implement)

- **Freshness:** now() − max(event_time of last successful partition). This should use event time, not ingestion time.
- **Completeness:** Received_records / expected_records for the period, with a data-quality gate if it drops below a threshold.
- **Error rate:** Failed_runs / total_runs for batch, or failed_messages / total_messages for streaming.
- **Throughput:** Rows or messages per second; for Kafka also watch consumer lag (difference between last produced and last consumed offsets).
- **Saturation:** Sustained resource pressure that correlates with user-impacting metrics (e.g., memory pressure alongside soaring p95).
- **Cost per success:** (compute + storage + egress) / number_of_successful_outcomes. Use it to spot noisy retries or inefficient joins.

---

## SLIs, SLOs, SLAs - and the error budget that keeps you honest

- **Service Level Agreements (SLAs):** Service Level Agreements (SLAs) is the agreement you make with your clients or users. You can think of it as the external promise with consequences.
- **Service Level Objectives (SLOs):** Service Level Objectives (SLOs) are the objectives your team must hit to meet that agreement. They’re your internal target(s) (“p95 < 10 minutes, 99% of days”).
- **Service Level Indicators (SLIs):** Service Level Indicators (SLIs) is the numbers you base your performance on. It’s what you measure (e.g., “p95 pipeline end-to-end latency”).
- **Error Budget:** Error Budget is the permissible amount of unreliability or downtime that a service can experience over a defined period without negatively impacting user experience or breaching SLOs.
- **Burn Rate:** Burn Rate measures how quickly a company is spending its available capital over a specific period, typically a month. You could attribute this locally to a budget for a specific tool too.

## Batch versus streaming: what to emphasise

Batch favours runtime distribution, queue wait, and freshness at deadlines (e.g., “by 09:00”). Streaming prioritises end-to-end latency (event time to serving), consumer lag, and backpressure. In both cases, correlate user-facing SLIs with cause indicators: if lag rises while consumer CPU is idle, the bottleneck is upstream or in I/O; if CPU and GC time spike during a shuffle, the constraint is compute or memory.

---

# Lesson 2 - Dashboards & Visualisation Tools

## Start with the story

Begin by choosing the audience. An on-call view answers “Are we breaching our promises right now, and where should I look first?” It needs short time windows, large headline cards, and clear red/amber/green states. A product/ops view answers “Are we on track this week, and what’s costing us?” It favours longer windows and trend lines. Now arrange the page so it reads top-to-bottom like a narrative. Put outcomes at the top: a small set of SLIs with their SLO context, such as p95 latency, error rate, and data freshness. In the middle, show explanations: signals that hint at causes, for example consumer lag for a stream or stage time for a batch job. At the bottom, show resources and dependencies - CPU, memory, I/O, and the health of things you rely on like your warehouse or message broker. This layout means a learner can glance at the top row to see if users are impacted, and then scan downwards to understand why.

`Example: For a daily sales pipeline, the top row might show “Fresh by 09:00” and p95 runtime. The middle row shows queue depth and the slowest transformation stage. The bottom row shows warehouse concurrency and object-store error rate. One story, three layers. `

### Outcome SLIs with SLO context

**Indicators that explain change e.g.:**

- Consumer lag
- Queue depth
- Transformation stage time
- GC %
- Cache hit rate
- Top error types

**Resources and dependencies**

- CPU
- Memory
- I/O
- Connections
- Warehouse/query layer
- Message broker
- Object store

`Tip: Keep units consistent and align time axes so comparisons are instant.`

---

![Visualisation](https://images.veryfront.com/imgproxy/q:75/w:1920/aHR0cHM6Ly9jZG4uY29kZXJzb2NpZXR5LmNvbS91cGxvYWRzL21ldHJpY3MtdHJhY2luZy1sb2dnaW5nLnBuZw==.webp)

Think of your system as a play. Metrics are the applause meter - numbers over time that tell you if the audience is happy (latency, error rate, freshness, lag). Logs are the script - what was said and where it went wrong (messages, exceptions, validation failures). Traces are the stage map - who moved where and which scene dragged (spans across services). When all three share the same identifiers and time window, you can follow the story cleanly from symptom to cause.

`Don’t build your dashboards to be “one and done”`

Connect metrics from your cloud monitor or Prometheus, and keep labels simple and stable - service, environment, region. High-detail identifiers (such as user IDs) belong in logs and traces, not in time-series labels, or your panels will become slow and noisy. Add variables for service and environment and use them in all panel queries and titles. One dashboard can then serve many teams without being cloned and forgotten. Name things exactly as they are (“End-to-end latency p95 (min)”) and always include units. Add a small help note that defines each SLI and states its SLO, so new engineers know what “good” looks like.

---

## Tools

**Grafana**

Grafana is where you show the state of the world. Start with a single dashboard for one pipeline or service. At the top, place a few outcome cards-p95 latency, error rate, and freshness-with each card labelled in plain language and with units. Plot p50, p95, and p99 on the same graph so tail pain is visible. Add variables for service and env so the same dashboard works across contexts, and show the environment in the title to avoid mistakes. Use annotations for deploys so any jump in latency lines up with a visible event. Alerts should mirror your promises: red means the SLO is breached or the error budget is burning too fast-not just that a server spiked briefly.

**Kibana**

Kibana is where you figure out “what kind of failures started, and where?” Send your logs with clear fields-timestamp, service, environment, error type, and a trace or request ID. Create a saved view filtered to your service and environment. A simple layout works well: a small bar chart of errors by type over time, and a table of recent error messages with stack traces. The moment a Grafana panel turns red, this view lets you slice quickly-by dataset, by job name, by error type-until the pattern is obvious. 

## Grafana vs Kibana: 

As a new data engineer, you’ll often hear about **Grafana** and **Kibana** when working with monitoring, logging, and observability tools. Both are **data visualization and exploration platforms**, but they serve slightly different purposes and integrate with different ecosystems. Let’s break it down simply.

---

### What is Grafana?
- **Purpose**: Grafana is a **general-purpose visualization and monitoring tool**.
- **Use Cases**:
  - Building real-time dashboards for system performance (CPU, memory, network).
  - Monitoring infrastructure, applications, and services.
  - Alerting when thresholds are crossed (e.g., disk usage > 90%).
- **Data Sources**:
  - Grafana can connect to **many types of databases** (Prometheus, InfluxDB, MySQL, PostgreSQL, AWS CloudWatch, and more).
  - Think of it as a **universal dashboard layer** that sits on top of your data.
- **Strengths**:
  - Very flexible with multiple integrations.
  - Great for time-series data (metrics that change over time).
  - Strong alerting system and notification integrations (Slack, email, PagerDuty).

---

### What is Kibana?
- **Purpose**: Kibana is a **visualization and exploration tool specifically built for Elasticsearch**.
- **Use Cases**:
  - Searching and analyzing **logs** (e.g., application logs, error logs, security logs).
  - Creating dashboards based on log data stored in Elasticsearch.
  - Running queries to troubleshoot errors (e.g., “Show all error messages in the last 10 minutes”).
  - Security analytics (often used with the Elastic Security SIEM features).
- **Data Sources**:
  - Primarily works with **Elasticsearch**.
  - It’s tightly coupled with the **Elastic Stack (ELK: Elasticsearch, Logstash, Kibana)**.
- **Strengths**:
  - Excellent for full-text search and log exploration.
  - Deep integration with Elasticsearch features.
  - Good for detecting issues, troubleshooting, and auditing events.

---

### Key Differences

| Feature / Aspect      | Grafana                                                                 | Kibana                                                                 |
|------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Primary Use**        | Monitoring, metrics visualization, alerting                            | Log exploration, search, and analytics                                |
| **Ecosystem**          | Works with many data sources (Prometheus, InfluxDB, SQL, Cloud, etc.)  | Part of the Elastic Stack, tied to Elasticsearch                      |
| **Data Focus**         | Time-series metrics (e.g., CPU, memory, request latency)               | Logs, text-based search, event data                                   |
| **Alerting**           | Built-in, strong alerting and notifications                            | Limited alerting (better in Elastic’s paid tiers)                     |
| **Flexibility**        | Multi-database, flexible dashboards                                    | Specialized in Elasticsearch data                                     |
| **Best For**           | Performance monitoring, infrastructure dashboards                      | Log analytics, troubleshooting, security monitoring                   |

---

### Simple Analogy

- **Grafana** is like a **universal dashboard builder**:  
  It can pull performance stats and metrics from many different tools and show them together in one place. Perfect for real-time monitoring.

- **Kibana** is like a **log search engine with charts**:  
  It’s where you go when something breaks, and you need to search through your application or system logs to understand what happened.

---

### When to Use Which?

- Use **Grafana** when:
  - You need **real-time monitoring dashboards** across many systems.
  - You want **alerts** to notify your team about performance issues.
  - Your data comes from **multiple databases and monitoring systems**.

- Use **Kibana** when:
  - You’re working heavily with **Elasticsearch**.
  - You need to **search, filter, and analyze logs** quickly.
  - You’re doing **troubleshooting, root cause analysis, or security analysis**.

---

### Final Takeaway
- **Grafana = Monitoring & Metrics Dashboards (multi-source, time-series focus).**  
- **Kibana = Log Analysis & Search (tied to Elasticsearch).**

As a data engineer:
- Think of **Grafana** for “How are my systems performing right now?”  
- Think of **Kibana** for “What happened in my system logs and why did it break?”  

---

# Lesson 3 - Analysing Performance Trends & Identifying Bottlenecks

`Establish what “normal” looks like`

Keep Little’s Law in mind (items in system ≈ arrival rate × time in system): when arrival stays the same but time increases, the queue length must grow - so look for the step that slowed. Align time axes on your dashboard so these relationships are easy to see at a glance.

https://en.wikipedia.org/wiki/Little%27s_law

Identify the type of bottleneck

## When it comes to bottlenecks, we can focus on three buckets:

### Upstream 

Upstream bottlenecks show up as idle consumers with growing wait times (slow source, network, or storage). 

### Compute

Compute, or midstream, bottlenecks show saturated CPU, long GC, skewed partitions, or expensive joins that inflate stage time. 

### Downstream 

Downstream bottlenecks appear when writes stall - warehouse concurrency is maxed, object store errors spike, or a rate limit kicks in. 

---

# Lesson 4 - Incident Response Essentials

Incidents are about coordination under pressure. This lesson gives you a calm, repeatable rhythm: define what an incident is, assign clear roles, restore service first, and communicate in a way that lowers stress for everyone involved.

An incident is any unplanned event that degrades service or data quality for users or downstream teams. By declaring early, you can downgrade the severity later. It’s best to keep a short, unambiguous scale tied to impact and urgency. For example:

- **Sev1:** User-visible outage or critical data corruption;
- **Sev2:** Partial degradation or missed, time-sensitive data;
- **Sev3:** Have a check-in to discuss progress and align on goals.

## Incident Responce Team Roles

1. The **Incident Commander** (IC) owns decisions and keeps focus;

2. **Resolvers** work the technical steps;

3. A **Comms Lead** updates stakeholders;

4. The **Scribe** captures a clean timeline.

## Communication that lowers stress

Communicate on a predictable cadence and in a predictable format. Good updates answer five things:

**1. What changed**

State the symptom in SLI terms with numbers and trend. Name the metric, its current value, and how far it moved from normal.
Pattern: “p95 ingest latency ↑ from 6m to 18m (+12m) and still rising.”
Batch example: “Freshness breached: dashboard is 35m late (target: by 09:00).”
Streaming example: “Event-to-serve p95 is 3.2s (baseline 900ms).”

**2. Where**

Pinpoint the scope so the right people look in the right place. Include service/pipeline, environment, region, and (if known) the stage/component.
Pattern: “Service orders-ingest in prod/eu-west-2, transform stage.”
Tip: Use your canonical names (exact service ID, dataset, pool name) to avoid ambiguity.

**3. Since when**

Give a timestamp and any correlated change (deploy, feature flag, config). This anchors the timeline and speeds correlation.

Pattern: “Since 10:05 BST, shortly after deploy #42 (feature flag adaptiveJoin=true).”

`Tip: Always include timezone (or UTC) to avoid confusion across teams.`

**4. Current impact**

Describe the user-visible effect in plain language. Tie it to an SLO/SLA if applicable.
Pattern: “Users see stale sales data; ‘fresh by 09:00’ SLO breached. Estimated affected reports: Sales Daily, Finance EOD.”
Streaming variant: “Orders API is slower; 2% of calls exceed SLO. No errors, just elevated latency.”

**5. Next step**

Say exactly what will happen now, who owns it, the time-box, and when the next update will arrive.
Pattern: “Mitigation: raise warehouse load-pool concurrency from 4→8 (owner: Priya), 10-minute time-box. Next update: 10:25 BST.”
If rolling back: “Rollback deploy #42 in progress (owner: Alex), verify p95/lag for 10 minutes, update at 10:20.”

---

# Lesson 5 - Playbooks, Alerting & Real-Time Monitoring

When production misbehaves, you need steps you can actually run and alerts that wake people only for problems that matter. This lesson shows how to write playbooks that work under pressure, design SLO-aware alerts that reduce noise, and watch real-time health so you catch trouble early.

## What is a playbook?

A **playbook** is a short, scenario-specific checklist that anyone on-call can run to restore service safely under pressure. It turns a known failure mode (e.g., “Kafka consumer lag spike”) into a single, executable path: how to confirm it’s really happening, what to try first, when to stop, how to roll back, and how to verify that users are healthy again.

## What a good playbook contains

### Trigger

The condition that tells you to use it (clear metric + threshold + time window).

### Pre-checks

Quick tests to confirm you’re solving the right problem.

### First safe action

Reversible, low-risk step to reduce impact fast.

### Decision points

Time-boxed branches: “if X improves, continue; if not, do Y / escalate.”

### Rollback & exit

How to undo changes and the criteria for stopping.

### Verification

SLI/SLO checks that prove recovery (e.g., “p95 < 10m for 10 min; lag < 5k”).

### Context

Owner/escalation, links to dashboards/logs/traces, date/version.

---

### Alerting that protects sleep and users

Alerts are like promises in motion. Warning notifications are early indicators, like rising lag or queue depth, that aren’t yet harming users. Every page needs context you can act on: what fired, where (service, env, region), since when, a short suggested cause, and a runbook link. The runbook is a routine operational procedure (e.g., “rotate keys”, “restart service”) that gives you suggestions of what to do when there is an issue. Make sure you route by severity and time of day, and group similar alerts and deduplicate to prevent storms. Maintenance windows allow it so that scheduled work doesn’t interfere people. Periodically, it’s worth reviewing noisy alerts (perhaps monthly) - if an alert never changes a decision, demote or delete it. Before rolling out a new rule, test it against real history to see how often it would have paged.

### Real-time monitoring that closes the loop

Real-time health checks buy you minutes when things go wrong. **Heartbeats** can assert liveness from the data’s point of view (a tiny record each minute that must appear at the sink). You can also track **freshness** as “now minus newest good event time,” not ingestion time, so late data shows up as a real risk. You’ll also want to keep a **dead-letter queue** for bad messages and alert on growth, not existence. Add **lightweight synthetic probes** that exercise critical paths end-to-end: a tiny test write that you immediately read back. For streaming, watch **consumer lag** with a short and a long window so you can separate blips from sustained drift. Prefer simple **baseline + deviation** alerts to “clever” anomaly models - clarity beats mystery at 2am.

## Terminology

## Dead-Letter Queue (DLQ) 

### What is a Dead-Letter Queue?
A **Dead-Letter Queue (DLQ)** is a special type of message queue that stores messages that **could not be successfully processed**.  

Imagine you have a system that passes messages (like tasks, events, or data records) from one service to another. Normally, these messages flow smoothly through the pipeline. But sometimes, a message is **badly formatted**, **missing important data**, or repeatedly **causes errors** during processing.  

Instead of losing that message or blocking the entire system, the message is moved into a **dead-letter queue** for later inspection.

---

### Why Do We Need a DLQ?
Without a DLQ:
- A bad message could get retried endlessly, clogging the system.
- You might lose messages completely without knowing why they failed.
- Troubleshooting would be much harder since you wouldn't have access to the failing data.

With a DLQ:
- You **capture problem messages** instead of discarding them.
- You can **analyze the root cause** of failures (e.g., wrong schema, missing fields, system bug).
- You can **decide what to do**: fix and replay, or permanently discard.

---

### Common Scenarios That Lead to DLQ
1. **Invalid data format**  
   Example: A system expects a date in `YYYY-MM-DD` format, but receives `31/12/2025`.
   
2. **Missing required fields**  
   Example: An order message arrives without a customer ID.

3. **Message too large**  
   Some queueing systems have size limits. Oversized messages go to DLQ.

4. **Repeated processing failures**  
   If a message fails multiple retry attempts, it gets redirected to DLQ.

---

### How DLQ Fits into a Data Pipeline
- **Normal Queue**: Handles the flow of valid messages.
- **Processor/Consumer**: Reads from the normal queue and processes messages.
- **DLQ**: Collects messages that the processor cannot handle after a defined number of attempts.

Think of it like an **"emergency inbox"** where all problematic messages are collected for human review or special processing.

---

### Best Practices for Using DLQs
1. **Monitor the DLQ**  
   Set up alerts so that if many messages suddenly end up in DLQ, you’re notified.

2. **Log and Analyze**  
   Use DLQ as a diagnostic tool. Each failed message tells you something about potential issues in upstream systems or data quality.

3. **Plan a Replay Strategy**  
   Sometimes you can fix the error (e.g., correct the data format) and then **reprocess** the message from DLQ.

4. **Don’t Ignore It**  
   DLQs are not just "trash bins." They are **critical debugging and recovery tools**.

---

### Simple Analogy
Think of a **mail sorting center**:
- Normal letters go through smoothly.
- If a letter is **unreadable** or **missing an address**, it gets set aside in a special **“problem letters” box** (the DLQ).
- Later, a worker reviews this box to figure out what went wrong: maybe look up the correct address, fix the mistake, or discard it.

---

### Key Takeaways
- A DLQ is a **safety net** for bad or unprocessable messages.
- It prevents **system failures** and **data loss**.
- It helps with **debugging, monitoring, and recovery** in data pipelines.
- Always treat the DLQ as an **important part of system health monitoring**.

---

# Lesson 6 - Post-Incident Learning, RCA & SLAs

Incidents only create value if they change how the system behaves next time. This lesson shows how to run a short, blameless review, turn findings into trackable improvements, and set SLAs that sit comfortably inside the performance you already achieve.

### Blameless, post-incident reviews that people want to attend

Having a post-incident review is an essential step, yet they are often difficult to manage and end up becoming a “blame game”. To avoid this scenario, we can look at the following tips to help:

- Hold the review soon - while context is fresh - but not in the heat of response.
- Keep it short and consistent.
- Start with the timeline: a clear sequence of facts pulled from dashboards, alerts, and the incident channel.
- Follow with impact in user terms (SLO minutes burned, missed deadlines, customer tickets).
- Then discuss what helped and what made it harder (e.g., missing deploy annotation, noisy alert, undocumented failover).
- Make it blameless by treating actions as outcomes of system conditions - staffing, tools, processes - not personal failings.

**Look at Post-incident review Template saved in repo**


