# Topic 3 - Technical debt management and software maintenance 25/09/2025

---

# Understanding Technical Debt

![Tech Debt](https://chrisfenning.com/wp-content/uploads/2023/06/technical-debt-1-600x530.png)

As a beginner data engineer, you’ll often hear the term **technical debt**. It might sound complicated, but the concept is actually quite simple once you break it down. Let’s go through it step by step.

---

## What Is Technical Debt?

Think of technical debt like **financial debt**:

- When you borrow money, you get cash quickly but need to pay it back later **with interest**.
- When you take a technical shortcut (like writing quick, messy code or skipping documentation), you save time now but create **extra work later**.

In other words, technical debt is the **trade-off between doing something fast versus doing it properly**. The "interest" is the extra time and effort you’ll spend in the future to fix or improve what was done quickly.

---

## Why Does Technical Debt Happen?

Technical debt builds up for several reasons:

1. **Deadlines and pressure**  
   Teams often cut corners to deliver results faster.

2. **Lack of experience**  
   Beginners might choose a quick solution without realizing its long-term cost.

3. **Changing requirements**  
   The business might shift directions, leaving you with code or pipelines that no longer fit well.

4. **Ignoring best practices**  
   Skipping documentation, testing, or monitoring saves time in the short run but creates problems later.

---

## Examples in Data Engineering

Here are some non-code examples of what technical debt might look like in your work:

- **Poor naming conventions**  
  Tables, columns, or pipelines have unclear names (`table1`, `new_data`, `final_final.csv`), making them hard to understand later.

- **No data quality checks**  
  Data is loaded into the warehouse without validation. It works for now, but when errors appear, fixing them is messy and time-consuming.

- **Hard-coded logic**  
  Instead of making a pipeline flexible, someone hard-codes paths, queries, or parameters. Changing them later means digging into code everywhere.

- **Lack of documentation**  
  The pipeline runs, but nobody remembers why certain steps exist. New team members waste hours figuring it out.

---

## Why Technical Debt Matters

If not managed, technical debt can:

- **Slow down future work**: Every new feature takes longer because you need to work around messy systems.
- **Increase risk**: Undocumented or fragile processes are more likely to break unexpectedly.
- **Frustrate the team**: Engineers spend more time fixing problems than building useful solutions.
- **Cause business impact**: Incorrect or late data can harm decisions.

---

## Is Technical Debt Always Bad?

Not necessarily. Sometimes, taking on **intentional technical debt** is smart:

- You might need to deliver a quick proof of concept to test an idea.
- A temporary shortcut can be fine if you plan to come back and fix it soon.

The danger comes when **temporary debt becomes permanent**, or when no one tracks it.

---

## How to Manage Technical Debt 

1. **Be aware of it**  
   Recognize when a shortcut is being taken.

2. **Communicate**  
   Tell your team if you’re creating debt so it’s not hidden.

3. **Document**  
   Leave notes explaining why something was done a certain way.

4. **Balance speed and quality**  
   Sometimes speed is necessary, but know the cost.

5. **Plan repayment**  
   Just like money debt, set aside time to "pay it off" by refactoring, adding tests, or cleaning up.

---

## Key Takeaway

Technical debt is not about being “bad” at engineering—it’s about **choices and trade-offs**. Every data team accumulates it. The important part is to **manage it intentionally**, instead of letting it quietly pile up until it slows everything down.

---


# Software Maintenance 

As a data engineer, building software systems is only the beginning. Once a system is deployed, it must be maintained to remain reliable, secure, and useful over time. **Software maintenance** refers to all the activities required to keep a system running smoothly after its initial release.

---

## Why Software Maintenance Matters
- **Data changes constantly** – new sources, updated schemas, or evolving business needs.
- **Technology evolves** – libraries, frameworks, and cloud services are updated regularly.
- **Errors happen** – bugs and unexpected behaviors may appear in production.
- **Business needs shift** – requirements change, and the software must adapt.

Without proper maintenance, systems degrade, break, or become too costly to manage.

---

## Types of Software Maintenance
1. **Corrective Maintenance**
   - Fixing bugs, errors, or defects found in production.
   - Example: repairing a broken ETL pipeline that stops loading data.

2. **Adaptive Maintenance**
   - Updating the system to work in a new environment.
   - Example: modifying scripts when a database vendor updates its API.

3. **Perfective Maintenance**
   - Improving performance, readability, or usability.
   - Example: optimizing queries to run faster or cleaning up messy code.

4. **Preventive Maintenance**
   - Making changes to reduce future problems.
   - Example: adding monitoring, tests, or documentation before issues occur.

---

## Key Practices in Software Maintenance
- **Documentation**: Keep system diagrams, code comments, and runbooks up to date so others can understand and maintain the system.
- **Monitoring & Alerts**: Use tools to track system health and get notified when something fails or slows down.
- **Version Control**: Track changes in code and configuration to roll back safely if issues arise.
- **Testing**: Automate tests to catch errors before they hit production.
- **Dependency Management**: Regularly update libraries and frameworks to avoid security risks and incompatibilities.
- **Code Reviews**: Have peers review changes to ensure quality and knowledge sharing.
- **Automation**: Automate repetitive tasks (e.g., deployments, backups) to reduce human error.

---

## Common Challenges
- **Keeping pace with changes** in both business requirements and technical environments.
- **Balancing fixes vs. improvements** – deciding what to prioritize.
- **Avoiding "quick hacks"** that solve immediate issues but create long-term problems.
- **Managing technical debt** – accumulated shortcuts or outdated code that make future work harder.

---

## Mindset for a Data Engineer
Think of software as a **living system**. Just like a garden, it needs regular care:
- Remove weeds (bugs).
- Add new plants (features).
- Water and fertilize (monitoring and optimization).
- Protect from pests (security updates).

By approaching maintenance with this mindset, you ensure that your data systems stay healthy, reliable, and valuable for the business.

---

