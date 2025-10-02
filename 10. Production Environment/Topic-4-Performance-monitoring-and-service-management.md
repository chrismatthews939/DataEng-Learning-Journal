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
