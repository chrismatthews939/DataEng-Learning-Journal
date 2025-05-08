# Topic 4 - Data collection quality and ingestion risks 08/05/2025

## Recap of data quality fundamentals

#### Data Quality Dimensions
1. **Accuracy:** Ensuring data correctly represents real-life entities.
2. **Completeness:** Making sure all required data is present.
3. **Consistency:** Maintaining uniformity in data representation.
4. **Integrity:** Ensuring data is complete, accurate, and consistent.
5. **Reasonability:** Checking if data patterns meet expectations. An example could be a taxi jouney saying it took 5 seconds
6. **Timeliness:** Ensuring data is up-to-date and available when needed. **Latency** is how long it took for the data to arrive after it was created. **Freshness** is how up to date it is.
7. **Uniqueness/Deduplication:** Ensuring no entity exists more than once.
8. **Validity:** Ensuring data values are within defined domains. Some data might be valid for a certain amount of time such as coupon codes.


## Establishing data quality service level agreements

`Service Level Agreements (SLAs) are essential for setting clear expectations and responsibilities regarding data quality within an organisation. This lesson will guide you through the process of establishing effective data quality SLAs, which are crucial for maintaining high standards and accountability in data management.`

#### The main elements of a data quality SLA include:

- Data elements covered by the agreement.
- Business impacts associated with data flaws.
- Data quality dimensions associated with each data element (see previous lesson).
- Expectations for quality for each data element for each of the identified dimensions in each application or system in the data value chain.
- Methods for measuring against those expectations.
- Acceptability threshold for each measurement.
- Data Steward(s) to be notified in case the acceptability threshold is not met.
- Timelines and deadlines for expected resolution or remediation of the issue.
- Escalation strategy, and possible rewards and penalties.

### Develop data quality reporting

The work of assessing the quality of data and managing data issues will not benefit the organisation unless the information is shared through reporting so that data consumers understand the condition of the data. Reporting should focus around:

- Data quality scorecard, which provides a high-level view of the scores associated with various metrics, reported to different levels of the organisation within established thresholds.
- Data quality trends, which show over time how the quality of data is measured, and whether trending is up or down.
- SLA Metrics, such as whether operational data quality staff diagnose and respond to data quality incidents in a timely manner.
- Data quality issue management, which monitors the status of issues and resolutions.
- Conformance of the Data Quality team to governance policies.
- Conformance of IT and business teams to Data Quality policies.
- Positive effects of improvement projects.

## Data quality techniques

**Prevention is better than cure**

`The best way to create high quality data is to prevent poor quality data from entering an organisation. Preventive actions stop known errors from occurring. Inspecting data after it is in production will not improve its quality.`

#### Approches to preventitive action:

**Establish data entry controls** 
- Create data entry rules that prevent invalid or inaccurate data from entering a system.


**Train data producers** 
- Ensure staff in upstream systems understand the impact of their data on downstream users. Give incentives or base evaluations on data accuracy and completeness, rather than just speed.


**Define and enforce rules** 
- Create a data firewall, which has a table with all the business data quality rules used to check if the quality of data is good, before being used in an application such as a data warehouse.
- A data firewall can inspect the level of quality of data processed by an application, and if the level of quality is below acceptable levels, analysts can be informed about the problem.


**Demand high quality data from data suppliers**
- Examine an external data provider’s process to check their structures, definitions, data source(s) and data provenance. Doing so enables assessment of how well their data will integrate and helps prevent the use of non-authoritative data or data acquired without permission from the owner.


**Implement data governance and stewardship**
- Ensure roles and responsibilities are defined that describe and enforce rules of engagement, decision rights, and accountabilities for effective management of data and information assets.
- Work with data stewards to revise the process of, and mechanisms for, generating, sending, and receiving data.


**Institute formal change control**
- Ensure all changes to stored data are defined and tested before being implemented.
- Prevent changes directly to data outside of normal processing by establishing gating processes.

## Fixing the flaws: Effective corrective actions for data quality

Corrective actions are implemented after a problem has occurred and been detected. Data quality issues should be addressed systemically and at their root causes to minimise the costs and risks of corrective actions. ‘Solve the problem where it happens’ is the best practice in Data Quality Management. This generally means that corrective actions should include preventing recurrence of the causes of the quality problems.

#### Automated correction techniques 

Automated correction techniques include rule-based standardisation, normalisation, and correction. The modified values are obtained or generated and committed without manual intervention.

An example is automated address correction, which submits delivery addresses to an address standardiser that conforms and corrects delivery addresses using rules, parsing, standardisation, and reference tables.

Automated correction requires an environment with well-defined standards, commonly accepted rules, and known error patterns. The amount of automated correction can be reduced over time if this environment is well-managed and corrected data is shared with upstream systems.

#### Manually Directed Correction

Use automated tools to remediate and correct data but require manual review before committing the corrections to persistent storage. Apply name and address remediation, identity resolution, and pattern-based corrections automatically, and use some scoring mechanism to propose a level of confidence in the correction.

Corrections with scores above a particular level of confidence may be committed without review, but corrections with scores below the level of confidence are presented to the data steward for review and approval.

Commit all approved corrections, and review those not approved to understand whether to adjust the applied underlying rules. Environments in which sensitive data sets require human oversight (e.g., MDM) are good examples of where manual-directed correction may be suited.

#### Manual Correction

Sometimes manual correction is the only option in the absence of tools or automation or if it is determined that the change is better handled through human oversight.

Manual corrections are best done through an interface with controls and edits, which provide an audit trail for changes.

The alternative of making corrections and committing the updated records directly in production environments is extremely risky. Avoid using this method.

## Introducing statistical process control 

**Statistical Process Control (SPC)** is a method to manage processes by analysing measurements of variation in process inputs, outputs, or steps. The technique was developed in the manufacturing sector in the 1920s and has been applied in other industries, in improvement methodologies such as Six Sigma, and in Data Quality Management. Simply defined, a process is a series of steps executed to turn inputs into outputs. SPC is based on the assumption that when a process with consistent inputs is executed consistently, it will produce consistent outputs. It uses measures of central tendency (how values cluster around a central value, such as a mean, median, or mode) and of variability around a central value (e.g., range, variance, standard deviation), to establish tolerances for variation within a process. The primary tool used for SPC is the control chart, which is a time series graph that includes a central line for the average (the measure of central tendency) and depicts calculated upper and lower control limits (variability around a central value). In a stable process, measurement results outside the control limits indicate a special cause.

### How does SPC work?

SPC measures the predictability of process outcomes by identifying variation within a process. Processes have variation of two types: **Common Causes** that are inherent in the process and **Special Causes** that are unpredictable or intermittent.

When the only sources of variation are common causes, a system is said to be in (statistical) control, and a range of normal variation can be established. This is the baseline against which change can be detected.

SPC is used for control, detection, and improvement. The first step is to measure the process to identify and eliminate special causes. This activity establishes the control state of the process. Next is to put in place measurements to detect unexpected variation as soon as it is detectable.

Early detection of problems simplifies investigation of their root causes. Measurements of the process can also be used to reduce the unwanted effects of common causes of variation, allowing for increased efficiency.

### Introducing Root Cause Analysis

A root cause of a problem is a factor that, if eliminated, would remove the problem itself. Root cause analysis is a process of understanding factors that contribute to problems and the ways they contribute. Its purpose is to identify underlying conditions that, if eliminated, would mean problems would disappear.

---

## Strategies for ingesting PII and sensitive data


