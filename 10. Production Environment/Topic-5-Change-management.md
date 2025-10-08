# Topic 5 - Change management 09/10/2025

# Lesson 1 - Quality Assurance for Safer Change

Every production change is a small risk. Quality assurance (QA) turns that risk into a controlled experiment by combining layered tests, quality gates, runtime monitoring, and structured logs. In practice, QA means rigorous review and validation, defect tracking, and risk assessment embedded in a clear change process - so releases are predictable and auditable rather than hopeful. In production, the only meaningful metrics are the ones users feel. This lesson moves you beyond server dials to outcome signals such as tail latency, data freshness, and error-budget burn. You’ll learn how to define Service Level Indicators (SLIs), set realistic SLO targets, and pick a compact set of KPIs that keep your pipelines reliable without drowning you in noise.

## Quality Assurance

Every production change is a bet. Quality Assurance (QA) makes those bets safe by combining systematic review and validation, defect tracking, and risk assessment inside a repeatable change process. In practice, QA ensures a change is functionally correct, aligned to business outcomes, and reversible if something goes wrong. Treat QA as a set of controls rather than a final checkbox; it protects reliability, performance and compliance as your system evolves.

![Four layers of testing](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNrm-TXDA1Rl6np7-FUqAgOQhV_3jS9722JQ&s)

1. Unit tests - Protect core logic.
2. Integration tests - Verify behaviour across boundaries.
3. System test - Is checks that the whole system can run.
4. Acceptance tests - Ensure the users/stakeholders are happy.

A quality gate is a rule the change must satisfy before it can progress: green automated suites, an approved review, a passed security scan, and a written rollback plan. Gates enforce consistency across teams, reduce variance in how “done” is defined, and keep institutional memory in the record (PR + ticket).

## Integration testing with structured logs

When you integrate, tests should be supported by logs that are **structured**, not free-text. Emit fields such as event, version, input_rows, output_rows, null_rate_price, join_mismatch_count, and duration_ms. This turns logs into machine-checkable evidence of schema adherence, cardinalities and performance, closing the gap between “tests passed” and “works in production.” Pair this with a small **golden dataset** (100–500 representative rows) and assert known-good aggregates.

## Risk assessment and defect tracking

Before approving, ask: what’s the blast radius if this is wrong? Look at performance impact, dependencies, data integrity, and compliance. Capture the risks and mitigations in the change record; if an incident occurs, the defect tracker should connect the symptom to the change, the fix, and the regression test that prevents recurrence. Over time, run retrospectives and tighten your gates where the evidence shows they’re too loose.

Example:

`Marketing wants a new orders_v2 table with normalised currency and an extra attribution field. Downstream BI is sensitive to double-counts.`

# Lesson 2 - Robustness & Scalability for Confident Releases

When traffic surges or a node fails, robust pipelines keep working and recover on their own. Robustness reduces the blast radius of faults; scalability keeps performance steady as load grows. Together, they protect SLAs and user trust. Think in terms of availability targets (uptime, RTO/RPO), eliminating single points of failure, and choosing scale-out patterns that match your workload.

## Design for Availability First

Start by writing down what “available” means for this workload: target uptime, a recovery time objective (how quickly you must recover), and an acceptable data-loss window (RPO). These numbers guide real architectural choices rather than wishful thinking. In a trading feed, that might be 99.9% uptime, sub-second failover, and near-zero data loss.

Once requirements are explicit, remove single points of failure. Duplicate the things that matter - ingest endpoints, processing nodes, storage - and decide where you need active-active (all nodes share traffic) versus active-passive (a warm standby takes over). Redundancy is what turns one broken component into a non-event.

Failures still happen, so contain them. Use circuit breakers to stop calling a sick dependency, add retries with backoff for transient errors, and make consumers idempotent so a retried message doesn’t produce duplicates. The goal is graceful degradation: core paths keep working while optional features take the hit.

Recovery should be automatic. Health checks promote standbys; load balancers steer traffic away from unhealthy nodes; clustered databases fail over without a human in the loop. Practise this - schedule failover drills and watch both technical metrics (errors, latency) and business KPIs (events processed, data quality) to prove your design works under stress.

When load rises, decide whether to add more workers or make one worker bigger. Horizontal scaling spreads work across additional nodes and partitions and is usually your first lever for parallel workloads. Vertical scaling makes a single machine stronger and suits tasks that are inherently serial or license-bound; use monitoring to know which path fits your bottleneck.

Traffic must be shared intelligently. Load balancers should use health-based routing and sensible algorithms (round-robin, least-connections, or weighted for beefier nodes). If users are worldwide, steer requests geographically to cut latency; only pin sessions to a server if you truly have to.

Decoupling is your friend. Queues and event streams let producers and consumers move at their own pace; consumers can scale out when depth rises and scale in when it falls. This is how you smooth spikes and avoid head-of-line blocking in ingestion.

Keep workers stateless so replicas are easy to add and safe to kill. Put state in durable stores and caches, not in process memory. Then use caching for the hot path - read-through caches for frequently requested dimensions or profiles can slash database pressure and shave hundreds of milliseconds off tail latency. Watch the hit ratio and design sensible TTLs and invalidation rules so the cure doesn’t become the cause of stale data.

As data grows, lift the ceiling by sharding. Split large datasets along access patterns - by geography, tenant, or key range - so I/O and memory pressure are distributed. Many modern databases provide built-in sharding and rebalancing, which reduces the amount of custom plumbing you have to write.`

You don’t have to build everything yourself. Cloud platforms bundle auto-scaling, managed load balancers and HA storage so you can focus on pipeline logic. Pick services on performance and integration fit, and let monitoring and simple automation adjust capacity in response to real-time metrics.

# Vertical vs Horizontal Scaling for High Availability 

As a data engineer, one of your key responsibilities is ensuring **high availability** — meaning your systems stay **up and running** even when traffic spikes, components fail, or data volumes grow.  
To achieve this, you often have to **scale** your systems. There are two main ways to scale: **vertical** and **horizontal**.

---

## 🧱 What Is Scaling?

**Scaling** simply means increasing the capacity of your system so it can handle more load — whether that’s more users, more data, or more requests.

There are two main types:

- **Vertical Scaling (Scaling Up)**
- **Horizontal Scaling (Scaling Out)**

---

## ⬆️ Vertical Scaling (Scaling Up)

### **Definition**
Vertical scaling means **adding more power to a single machine**.  
This could be:
- Upgrading the CPU
- Adding more RAM
- Using faster disks
- Moving to a more powerful server

### **Example**
Imagine you have one database server that’s getting slow.  
You move from a **4-core, 16GB RAM** machine to a **16-core, 64GB RAM** machine.

You didn’t add more servers — you just made **one server stronger**.

### **Advantages**
✅ Easier to implement — usually just a hardware upgrade or a configuration change.  
✅ No need to modify your application or infrastructure architecture much.  
✅ Great for smaller systems or when simplicity is important.

### **Disadvantages**
❌ **Single point of failure** — if that one server crashes, everything goes down.  
❌ **Limited by hardware** — you can only scale up so much before hitting physical or financial limits.  
❌ **Downtime risk** — upgrading hardware often means shutting down the system temporarily.

### **When to Choose Vertical Scaling**
- When your system is small or just starting out.
- When the application isn’t designed for distributed systems.
- When simplicity and quick setup matter more than extreme availability.
- When scaling requirements are predictable and moderate.

---

## ➗ Horizontal Scaling (Scaling Out)

### **Definition**
Horizontal scaling means **adding more machines** instead of making a single one stronger.  
Each machine shares part of the workload.

This could mean:
- Adding more web servers behind a load balancer.
- Sharding (splitting) your database across multiple servers.
- Distributing data processing tasks across a cluster.

### **Example**
Your application starts getting thousands of new users.  
Instead of upgrading your single server, you **add 5 more servers** and use a **load balancer** to split traffic between them.

Now, even if one server fails, others can handle the load.

### **Advantages**
✅ **High availability** — no single point of failure.  
✅ **Scales almost infinitely** — just add more machines.  
✅ **Improved fault tolerance** — one machine can fail without taking everything down.  
✅ **Better suited for modern distributed data systems** (e.g., Hadoop, Kafka, Spark, Kubernetes).

### **Disadvantages**
❌ **More complex** — you need tools for coordination, load balancing, and data consistency.  
❌ **Requires architectural changes** — not all applications can easily scale horizontally.  
❌ **More systems to manage and monitor.**

### **When to Choose Horizontal Scaling**
- When uptime and availability are critical (e.g., 24/7 systems).  
- When you expect unpredictable or massive traffic spikes.  
- When working with distributed data systems or cloud-native infrastructure.  
- When long-term scalability and fault tolerance matter most.

---

## ⚖️ Choosing Between Vertical and Horizontal Scaling

| Factor | Vertical Scaling (Up) | Horizontal Scaling (Out) |
|--------|------------------------|---------------------------|
| **Complexity** | Simple | Complex |
| **Cost (Short-Term)** | Cheaper initially | Higher setup cost |
| **Scalability Limit** | Limited | Virtually unlimited |
| **High Availability** | Low (single point of failure) | High (redundancy) |
| **Maintenance** | Easier | Requires more management tools |
| **Downtime Risk** | Possible during upgrades | Minimal if designed correctly |

---

## 💡 Real-World Analogy

Think of a restaurant:

- **Vertical scaling**: Hire a better chef and buy bigger ovens — one kitchen doing more work.  
- **Horizontal scaling**: Open multiple restaurants with the same menu — more kitchens sharing the load.

Both work, but for **high availability**, you’d rather have **multiple kitchens** (horizontal scaling) so one failure doesn’t stop all operations.

---

## 🧠 Summary

| Term | Description | Best For |
|------|--------------|----------|
| **Vertical Scaling** | Making one server more powerful | Simplicity and low-moderate load |
| **Horizontal Scaling** | Adding more servers to share the load | High availability, fault tolerance, and large-scale systems |

---

### 🏁 Final Takeaway

- Start **vertically** when you’re small — it’s simpler and cheaper.  
- Move **horizontally** as your system grows and requires **high availability** and **fault tolerance**.  
- Modern cloud platforms (like AWS, GCP, and Azure) make horizontal scaling easier through **auto-scaling groups**, **load balancers**, and **container orchestration** tools.

---


