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
