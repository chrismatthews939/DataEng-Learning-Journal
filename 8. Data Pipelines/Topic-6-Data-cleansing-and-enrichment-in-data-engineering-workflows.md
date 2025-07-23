# Topic 6 - Data cleansing and enrichment in data engineering workflows 24/07/2025

# Identifying and correcting data quality issues

- **Incomplete information:** Fields that are blank or populated with placeholders like “N/A” or “unknown.” For example, a missing date of birth in a loyalty system might prevent age-based segmentation.

- **Duplicate data:** Repeated records can emerge from multiple systems feeding into a single data store. A customer who signs up twice might appear to be two people unless duplicate detection logic is in place.

- **Data Inconsistency:** This includes variations in how data is written - e.g., “Jan 1st 2023”, “01-01-2023”, and “2023/01/01” all refer to the same date but may not be recognised as equivalent in a query.

- **Inaccurate data:** Manual entry or integration issues can cause "France" to appear as “Frnace” or “FRNC.” Even small differences can break grouping logic in reports.

- **Outliers and anomalies:** An employee birth year of 1901 or a sale amount of £100,000 for a pencil order should raise red flags. Outliers may indicate fraud, system bugs, or simple human error.

## Tools and Techniques

- **Value counts:** How many unique values are in a column? Are some clearly wrong?
- **Summary statistics:** Use min, max, mean, and standard deviation to check for oddities.
- **Data profiling tools:** Platforms like OpenRefine, Pandas Profiling, or Great Expectations can highlight inconsistencies quickly, and some even suggest fixes.

# Standardisation, deduplication, and validation techniques

