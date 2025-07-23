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

- **Text formatting:** Convert names and addresses into a consistent case (e.g., “John Doe” instead of “john DOE” or “JOHN doe”).

- **Date formats:** Align dates to a universal format like ISO 8601 (YYYY-MM-DD) to avoid confusion between “03/07/2023” and “07/03/2023.”

- **Units of measurement:** Convert between miles and kilometres, or pounds and kilograms, to unify reporting.

- **Category normalisation:** Convert “St.” to “Street” and “Rd.” to “Road” so they can be grouped correctly in geographic analysis.

- **Data Type Validation:** This ensures that the data entered matches the defined type for the field (e.g., string, integer, date). If a grade is expected to be a number, entering “Year 3” would fail this check. However, note that type alone isn't enough to guarantee correctness.

- **Data Range Validation:** This checks whether a value falls within acceptable boundaries. For example, if school grades must be between 1 and 12, a value of 13 (even though it’s a valid number) should be rejected.

- **Data Constraint Validation:** This applies more specific rules, like content or format constraints. Using the same school grades example, values must be whole numbers - so 11.5 would fail. Constraints can also include character length (e.g., usernames must be 3–15 characters).

- **Data Consistency Validation:** Here, the system ensures that the data makes sense in relation to other fields. A classic example: a shipping date should not be earlier than the production date. While both dates might be in the correct format, the relationship between them is invalid.

- **Code Structure Validation:** This ensures that data follows the expected structure or schema. For instance, a JSON object might follow a schema with required keys - if those keys are missing or misplaced, the structure fails validation. On websites, a page might appear structurally correct but still display inaccurate or misleading content.

- **Code Validation (System-Level):** This is often built into applications and includes automated checks based on all of the above - for instance, ensuring that text fields do not allow invalid characters, or that multiple types of validation (like data type and range) are triggered together. However, system-level validation can miss edge cases if poorly designed - like allowing multiple data types in a field or failing to enforce strict boundaries.


# Tools for data cleansing

**OpenRefine: powerful data wrangling for tabular data**

![Open Refine](https://upload.wikimedia.org/wikipedia/commons/e/e0/OpenRefine_logo_color.png)

OpenRefine (formerly Google Refine) is a free, open-source tool that runs locally in your browser. It’s designed for cleaning and transforming messy data.

Key features:
1. **Faceting:** Helps you group and filter values in a column - great for spotting variants like “UK,” “U.K.,” and “United Kingdom.”
2. **Clustering:** Uses algorithms to find and group similar strings - helpful for deduplication and typo correction.
3. **Transformations:** Offers powerful text functions and regular expressions to clean up fields (e.g., removing extra whitespace, formatting dates).
4. **Undo/Redo history:** Every step is logged, making changes reversible and auditable.


