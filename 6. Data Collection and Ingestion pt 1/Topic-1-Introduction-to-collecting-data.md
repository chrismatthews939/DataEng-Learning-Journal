# Topic 1 - Introduction to collecting data 17/04/2025

# Definitions

### Data collection

Data collection is the process of gathering raw data from various sources and compiling it into a central location for analysis.

It is typically the first step in the data analysis process.

### Data ingestion

Data ingestion is the process of taking data from various sources and setting it up for analysis.

This can involve data preparation and automation, so that data can be easily and repeatedly analysed.

### Data preparation

Data preparation involves cleaning, transforming and organising data so that it is in the right shape for your analysis.

### The key difference between data collection and ingestion are as follows:

- **Data collection** involves gathering raw data from various sources, whereas **data ingestion** involves processing and preparing data for analysis.
- **Data collection** is typically a one-time process, whereas **data ingestion** can be an ongoing process.
- **Data collection** can involve manual entry of data, while **data ingestion** is typically an automated process.
- **Data collection** can be a time-consuming and resource-intensive process, while **data ingestion** can be faster and more efficient.
- **Data collection** is often done in a decentralised manner, while **data ingestion** can be centralised.

### Data Collection Methods

| Method    | Description                 |Tools/example               |
|-------------|----------------------------------|----------------------------------|
| Survey    | Collect data from individuals or groups. Conducted in person, over the phone, or online.  |Microsoft forms, SurveyMonkey  |
| Sensors   | Automatically collect data such as temperature, humidity, or motion. Installed in various locations to monitor performance and prevent failures.     |Temperature sensors, motion detectors  |
| Web scraping   | Extract data from websites. Used to collect information like prices, reviews etc.|Web scraping tools, custom scripts   |

### Data Ingestion

**ETL Tools**
ETL (Extract, Transform, Load) tools are used to extract data from various sources, transform the data into a structured format, and load it into a data warehouse or other data storage system. Examples of ETL tools include **Talend**, **Informatica**, and **Apache NiFi**.

**API Integrations**
**API (Application Programming Interface)** integrations allow data to be collected from various sources automatically. APIs can be used to extract data from social media platforms, marketing automation tools, or other third-party applications.

**Log File Analysis Tools**
Log file analysis tools can be used to ingest and analyse log files from web servers, applications, or other systems. These tools can help identify errors or performance issues and provide insights into user behaviour.

**Data Preparation Tools**
Data preparation tools can be used to clean, transform, and prepare data for analysis. These tools can be used to remove duplicates, fill missing values, or convert data to a standardised format. Examples of data preparation tools include **Trifacta**, **OpenRefine**, and **Google Data Prep**.

**Data Integration Platforms**
Data integration platforms allow data to be collected from multiple sources and integrated into a single data store.

These platforms can be used to create a unified view of data from various sources, such as **Customer Relationship Management (CRM)** systems, marketing automation tools, or social media platforms. Examples of data integration platforms include **MuleSoft**, **Dell Boomi**, and **Informatica Cloud**.

## Understanding Dirty Data

Types of dirty data:

1. Missing values
2. Outliers
3. Duplicates
4. Erroneous data
5. Inconsistencies

## Cleaning data in Python

### Essential best practices

Data cleaning is a critical step in any data analysis or machine learning project. Here are the essential best practices to keep in mind as you streamline your data cleaning process:

- Store raw data separately.
- Use version control and always keep the original.
- Document your data-cleaning decisions and justifications.
- Add comments to your code to explain the purpose of each cleaning step and any assumptions made.

# 🧹 Data Cleaning with Python 

Welcome! This guide will walk you through **data cleaning in Python** using `pandas` and `regex`, with step-by-step explanations and beginner-friendly code comments. 📘🐍

---

## 📦 Setup

```python
# Import the pandas library for data manipulation
import pandas as pd

# Import regex module for advanced string matching
import re
```

---

## 📁 Sample Dataset

```python
# Create a simple dataset as a Python dictionary
data = {
    'Name': [' Alice ', 'Bob', None, 'David', 'Eve'],  # Includes leading/trailing spaces and a missing value
    'Age': [25, 30, None, 22, 29],                     # One missing value
    'Email': ['alice@example.com', 'bob@example.com', 'carol@@example.com', None, 'eve@example.com'],  # One invalid and one missing
    'Phone': ['+1-800-555-1234', '800.555.2345', '(800) 555-3456', None, '8005554567'],  # Mixed formats + missing
    'Salary': [50000, 54000, 58000, None, 60000]       # One missing salary
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Display the data
print(df)
```

---

## 🧼 Data Cleaning Steps with Explanations

---

### 🔍 Step 1: Identifying Missing Data

```python
# Check where values are missing (True means missing)
print(df.isnull())

# Count missing values in each column
print(df.isnull().sum())
```

---

### 🧯 Step 2: Handling Missing Data

```python
# Fill missing Age with the average of existing values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Replace missing Name with a placeholder
df['Name'].fillna('Unknown', inplace=True)

# Replace missing Email with a default string
df['Email'].fillna('noemail@domain.com', inplace=True)

# Fill missing Salary with the median value
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# Fill missing Phone with a dummy number
df['Phone'].fillna('0000000000', inplace=True)
```

---

### 📤 Step 3: Removing Duplicates

```python
# Add a duplicate row for demonstration
df.loc[5] = df.loc[1]

# Drop duplicate rows
df = df.drop_duplicates()
```

---

### 🧹 Step 4: Cleaning Whitespace

```python
# Remove leading and trailing spaces from the Name column
df['Name'] = df['Name'].str.strip()
```

---

### 🔄 Step 5: Converting Data Types

```python
# Convert Age and Salary to integer type for analysis
df['Age'] = df['Age'].astype(int)
df['Salary'] = df['Salary'].astype(int)
```

---

## 🧾 Regex-Based Cleaning (String Pattern Matching)

---

### ✅ Validate Email Format Using Regex

```python
# Only keep rows where the email looks valid (basic check)
df = df[df['Email'].str.contains(r'^\S+@\S+\.\S+$', na=False)]
```

Explanation:
- `\S` = any non-space character
- `+` = one or more
- `^` = start of string, `$` = end of string

---

### 📞 Standardize Phone Numbers

```python
# Remove all non-digit characters (like -, ., (), etc.)
df['Phone'] = df['Phone'].str.replace(r'\D', '', regex=True)

# Reformat phone number as (XXX) XXX-XXXX
df['Phone'] = df['Phone'].str.replace(r'(\d{3})(\d{3})(\d+)', r'(\1) \2-\3', regex=True)
```

---

### 🔍 Extracting Parts of Strings

```python
# Extract just the domain name from email addresses
df['Email_Domain'] = df['Email'].str.extract(r'@([\w\.-]+)')
```

Explanation:
- `@` looks for the "@" symbol
- `[\w\.-]+` matches any letters, numbers, dots, or dashes after it

---

### 🧪 Bonus: Regex with Python’s `re` Module

```python
# Example using the re module to extract patterns
sample = 'User ID: #123-456'
match = re.search(r'#(\d{3})-(\d{3})', sample)

if match:
    print('Groups:', match.groups())  # Output: ('123', '456')
```

---

## ✅ Best Practices

- 📊 **Always inspect** your data first using `df.head()`, `df.info()`
- 💾 Backup raw data before modifying
- 🔍 Use regex for advanced string cleaning (emails, phones, codes)
- 🧪 Validate the cleaned data
- 📝 Document each transformation step

---

## 📊 Final Cleaned Data Preview

```python
# Show final cleaned DataFrame
print(df)
```

---

**Sample Output:**

```
     Name  Age              Email        Phone  Salary   Email_Domain
0   Alice   25  alice@example.com  (800) 555-1234   50000   example.com
1     Bob   30    bob@example.com  (800) 555-2345   54000   example.com
4     Eve   29    eve@example.com  (800) 555-4567   60000   example.com
```

---

You’re now ready to clean messy real-world datasets like a pro! 🧼🐍🎉




















