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

# Lehman's Laws for Tech Debt Evolution 

When building software systems, teams often accumulate **technical debt** — shortcuts, quick fixes, or outdated decisions that make future changes harder. Over time, this debt “evolves” as the system grows. Manny Lehman, a computer scientist, studied how software changes over its lifetime and summarized his findings in what are now called **Lehman’s Laws of Software Evolution**.  

As a data engineer, understanding these laws can help you see why systems become more complex, harder to change, and more costly to maintain if debt isn’t managed.

---

## 1. **Continuing Change**
> *A system must continuously adapt, or it becomes less useful.*

- Software that doesn’t change will eventually fail to meet new business needs or adapt to new environments.  
- For data engineers, this means your pipelines, models, and data systems must evolve as new data sources, regulations, and technologies appear.  
- **Connection to tech debt**: The longer you delay updates, the more “interest” your debt builds, because catching up later is harder.

---

## 2. **Increasing Complexity**
> *As a system changes, its complexity increases unless work is done to reduce it.*

- Every fix, feature, or patch adds layers of complexity.  
- For data systems, that might mean more ETL steps, more scripts, or hard-to-follow workflows.  
- **Connection to tech debt**: If you never refactor (clean up and simplify), the debt compounds, making the system fragile.

---

## 3. **Self-Regulation**
> *Software evolution is a self-regulating process, with measures like workload and product quality showing trends over time.*

- Teams can observe how their pace of delivery and error rates balance out naturally.  
- **Connection to tech debt**: If debt gets too high, velocity slows down — the system “pushes back,” forcing you to deal with underlying issues.

---

## 4. **Conservation of Organizational Stability (Invariant Work Rate)**
> *Over time, the average rate of development (useful work done) remains roughly constant.*

- No matter how much management wants faster progress, teams usually stabilize at a natural pace.  
- **Connection to tech debt**: Adding debt may give short-term speed boosts, but long-term delivery speed will flatten or even decline.

---

## 5. **Conservation of Familiarity**
> *To successfully evolve a system, a team must keep its complexity within the limits of what people can understand.*

- Humans can only keep so much in their heads. If a system grows beyond that, it becomes unmanageable.  
- **Connection to tech debt**: Poor documentation, inconsistent naming, or hidden logic can overwhelm new engineers, slowing progress and creating risk.

---

## 6. **Continuing Growth**
> *Software must keep growing to remain useful.*

- Users demand new features, integrations, and performance improvements.  
- **Connection to tech debt**: If you only patch and never invest in cleaning up, growth gets harder and harder until you can’t deliver new features at all.

---

## 7. **Declining Quality**
> *Unless actively maintained, the quality of a system will appear to decline over time.*

- External standards (like security, performance, compliance) keep rising, making unmaintained systems feel worse.  
- **Connection to tech debt**: Without intentional quality work (tests, monitoring, refactoring), the system feels outdated and buggy even if nothing “breaks.”

---

## 8. **Feedback System**
> *Software evolution is a multi-loop feedback system — changes trigger consequences, which loop back into future changes.*

- Decisions you make today affect tomorrow’s complexity, cost, and risk.  
- **Connection to tech debt**: Skipping best practices creates feedback loops where fixes cause more issues, which then require more fixes.

---

# Putting It All Together

- **Lehman’s Laws describe why tech debt doesn’t stay still — it grows and evolves with your system.**  
- For a beginner data engineer, the takeaway is this:
  - **Always expect change.**
  - **Refactor regularly to control complexity.**
  - **Recognize that short-term shortcuts create long-term drag.**
  - **Invest in documentation, testing, and maintainability early.**

By respecting Lehman’s Laws, you can balance delivering new features with managing tech debt, ensuring your data systems remain reliable and adaptable.

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

