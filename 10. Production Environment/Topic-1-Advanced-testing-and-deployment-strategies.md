# Topic 1 - Advanced Testing and Deployment Strategies 10/09/2025

# Lesson 1: User Acceptance Testing (UAT)

`“It doesn’t matter how elegant your pipeline is if your users can’t use it, you’ve failed.”`

## Why UAT Matters

User Acceptance Testing is the final verification step before a data pipeline is declared “production ready.” It answers a crucial question: does the output meet the expectations and day-to-day needs of business users? While functional testing proves the pipeline behaves as intended from a technical perspective, UAT determines if that functionality translates into real-world value.

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

