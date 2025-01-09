# Topic 5 - Data Manipulation - 09/01/2025

## Intro to Pandas and DataFrames

In the realm of data manipulation in Python, Pandas reigns supreme, serving as the Swiss army knife of data handling. Whether you are a seasoned data scientist or an emerging analyst, mastering Pandas is the key to elevating your data-handling prowess. In this lesson, we will explore some of the key high-level features of Pandas that allow for streamlined data wrangling and analysis.

### What is Pandas

Pandas is crucial for tasks like data cleaning, transformation, and analysis. It provides fast and efficient data structures, making it an ideal choice for data science and analytics.

Pandas is typically used in data manipulation, including data wrangling, data cleaning, data transformation, data analysis, supporting the building of charts and visuals. Additionally, Pandas even supports in-built time-series functionalities that render intricate date-related calculations effortless, amplifying its value in real-world data science applications.

Pandas stands out in the crowded field of data manipulation tools for several key reasons:

1. **Performance**: Faster and more efficient than Excel
2. **Flexibility**: More customised data manipulation than SQL
3. **Python Ecosystem**: Broader versatility compared to R, compatibility with other Data Analytic libraries in Python (like NumPy, SciPy, Matplotlib, and Scikit-Learn)
4. **Large Datasets**: Overcomes Excel's data size limitations
5. **Automation**: Enables reproducible data pipelines
6. **Built-in Features**: Native data cleaning and time-series support

### Installation and setup 

Getting started with Pandas is straightforward, and involves the following simple steps:

**Installing Pandas**: Installing Pandas is as simple as running a **pip install** pandas command in your terminal
**Importing the Library**: To use Pandas, you must import it first. The common alias for Pandas is **pd**

### Exploring basic data structures 

Pandas offers two primary data structures, including series and dataframe.

### Series

**One-Dimensional**: A Series is like a single column in a spreadsheet, capable of holding various data types.

**Index**: Series have an 'index' for axis labels, which can be numeric or custom labels.

**Operations**: Similar to NumPy arrays, Series support various operations like reindexing and aggregation.

**Creation**: Create a Series from Python lists, dictionaries, or NumPy arrays.

### Dataframe

**Two-Dimensional**: A DataFrame is similar to a SQL table, with rows and columns of different data types.

**Labels**: DataFrames have both row and column labels, where each column is a Series.

**Manipulation**: Allows for quick data reshaping, pivoting, and manipulation.

**Analytical Uses**: Ideal for data processing and analysis.

## Data Import and Export

### Importing Data

- **CSV Files**
  - **Reading CSV**: Use **pd.read_csv()** to read CSV files quickly. This is particularly useful when dealing with plain text files that are delimited by commas or other characters. This is essential when you are working with business data often stored in Excel spreadsheets.

- **SQL Databases**
  - SQL databases can be read directly using **pd.read_sql()** and a connection object. This is ideal when your data is stored in a relational database and you want to pull it into Pandas for further analysis.

- **Excal Files**
  - The pandas library in Python provides a function called **read_excel()** that allows you to import data from Excel files into your Python environment. This functionality is particularly useful when working with structured data, as it allows you to leverage the powerful data manipulation capabilities of pandas directly on your Excel data. It’s a key reason why pandas is a popular library for data analysis in Python.

### Exporting Data

- **CSV Files**
  - To write to a CSV, use **df.to_csv()**. Useful for sharing data in a universally accepted format.

- **SQL Databases**
  - To store data to an SQL database (or other relational databases), you can use **df.to_sql()**.

- **Excal Files**
  - Save back to Excel using **df.to_excel()**. This will make it perfect for reports that can be further edited or viewed in Excel.

### Code Example

```python
import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv("sales_data.csv")
# Display the first 5 rows
print(df.head())
```

## Data Cleaning in Pandas

Imagine data as a precious gem, buried deep within a mine. To extract its true value, you need to refine it, removing impurities and imperfections. This refinement process is what we call data cleaning. Data cleaning is not merely a preliminary step; it is a vital part of the data analysis pipeline. In this lesson, you will be guided through the data-cleaning techniques you can utilise in Pandas, a powerful Python library. 

1. Missing Values
2. Inconsistent Formats
3. Duplicate Data
4. Outliers

### Technique 1: Handling missing values

In data analysis, filling in missing names with a placeholder is a good practice in data cleaning for a number of important reasons.

The **fillna()** function replaces any NaN values with 'Unknown'. The argument inplace=True allows us to operate directly on the dataframe without having to assign the output to df.

```python
df['Name'].fillna('Unknown', inplace=True)
```

**Caution!**

Replacing missing values with the mean or median can introduce bias, especially if the missing data is not random. 

This approach reduces the dataset's variance, potentially leading to models that underestimate variability. 

It also fails to preserve the correlation structure between variables, potentially distorting the data's overall structure. 

Additionally, it ignores patterns in the data that more sophisticated imputation methods could leverage. 

Consequently, the changed dataset may become less trustworthy for individual entries, impacting the reliability of subsequent analyses or models. 

This approach is more suitable for general trends rather than precise predictions for individual cases. 

### Technique 2: Correcting data formats

Often, data might not be correctly interpreted in the right format by Pandas. When we load data from a source e.g. a CSV, pandas tries to infer the data type e.g. assigning a type to a column such as int, float or object.

```python
df['Age'].fillna(df['Age'].median()).astype(int)
```

### Technique 3: Dealing with duplicates

The **drop_duplicates()** function removes rows that have the same values in specified columns (Name and Age). The subset parameter specifies which columns to consider. The **keep='first'** parameter indicates that we'll keep the first occurrence and remove any subsequent duplicate.


```python
df.drop_duplicates(subset=['Name','Age'], keep='first', inplace=True)
```
### Technique 4: Handling outliers

Removing outliers from a dataset is often done to improve the accuracy and reliability of statistical analyses and machine learning models by focusing on data that represents the underlying trend or distribution.

For example, if one student scores 1000 on a test out of 100, that single score could wrongly suggest everyone did much better than they actually did if we took an average of the marks.

```python
# identify outliers
outliers = df[df['Age'] > 100]

# drop them
df = df[df['Age'] > 100]
```

### Full Code Example

```python
import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values, duplicates, and outliers
data = {
'ID': [1, 2, 3, 4, 5, 2, 6],
'Date': ['2022-01-01', '2022-02-15', '2022-03-20', '2022-04-10', '2022-05-05', '2022-02-15', '2022-06-30'],
'Sales': [1000, 1500, np.nan, 2000, 1800, 1500, 2500]
}
df = pd.DataFrame(data)

# Handling missing values
df.dropna(inplace=True)
# df.fillna(df.mean(), inplace=True) # Uncomment to replace missing values with mean

# Correcting data formats
df['Date'] = pd.to_datetime(df['Date'])

# Dealing with duplicates
df.drop_duplicates(subset=['ID'], keep='first', inplace=True)

# Handling outliers (use appropriate method)

print(df)
```

## Data manipulation and subsetting

### Indexing and slicing DataFrames

Selecting data Using **.loc[]** and **.iloc[]**

Pandas provides two essential methods for selecting data: **.loc[]** and **.iloc[]**. These methods are your keys to unlocking data within your DataFrame.

The **.loc[]** method

The **.loc[]** method allows you to select data based on its label or name, in both the row and column dimensions. In our example:

```python
print(df.loc[0, 'Product'])
```

*Here, 0 refers to the row index and 'Product' refers to the column name. So when we use .loc[0, 'Product'], we are specifically asking Pandas to give us the data that sits in the intersection of the first row (index 0) and the column named 'Product'. In simpler terms, it is like saying, "Hey, Pandas! Could you please fetch me the name of the product that's listed in the first row of the DataFrame?"*

On the other hand, **.iloc[]** works based on integer-based positions for both rows and columns. It doesn't care about the labels or names; it simply goes by the position. To put it simply, you're asking Pandas, "Please fetch the data that sits in the first row and first column, whatever it might be."

```python
print(df.iloc[0, 0])
```

### Adding and dropping columns

Adding a column

Let's say you want to add a new column to indicate the 'Stock_Status' based on the 'Stock_Level'. If the stock level is below 100, it should say 'Low'. Otherwise, it should say 'High'.

```python
df['Stock_Status'] = ['Low' if x < 100 else 'High' for x in df['Stock_Level']]
```

*In this code snippet, we create a new column called 'Stock_Status' by evaluating each row's 'Stock_Level' value. If the 'Stock_Level' is less than 100, 'Stock_Status' will be 'Low'; otherwise, it will be 'High'.*

### Data filtering with conditions

Imagine you want to identify which products have a 'Low' stock status. Filtering allows you to focus on specific rows of a DataFrame based on conditions, making the DataFrame more manageable and the information easier to digest. Here is how to filter out rows where 'Stock_Status' is 'Low':

```python
filtered_df = df[df['Stock_Status'] == 'Low']
```
In this line df[df['Stock_Status'] == 'Low'], what we're doing is passing a condition (df['Stock_Status'] == 'Low') to the DataFrame df. This condition is evaluated for each row, and only the rows where the condition is True are retained in the resulting DataFrame filtered_df.

### Full Code Example

```python
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
'A': np.random.randint(1, 100, 20),
'B': np.random.uniform(0, 1, 20),
'C': np.random.choice(['red', 'green', 'blue'], 20),
'Date': pd.date_range(start='2022-01-01', periods=20, freq='D')
}
df = pd.DataFrame(data)

# Indexing and slicing
subset = df.loc[5:10, 'A':'C']

# Filtering data
filtered_df = df[df['B'] > 0.5]

# Basic statistics
summary_stats = df.describe()

print(subset)
print(filtered_df)
print(summary_stats)
```

## Sorting, grouping, and aggregating data with Pandas

Sorting helps you quickly identify patterns or outliers in your data. For instance, you might want to know the youngest and oldest patients in your dataset. 

```python
import pandas as pd

# create dataframe
data = {'Patient_ID': [1,2,3,4,5], 'Age': [25,40,35,50,23]}
df = pd.Dataframe(data)

# sort df by age
sorted_data = df.sort_values('Age')
```

### Grouping vs. Aggregating: A brief introduction

What is Grouping?

Grouping is the process of categorising data based on one or more columns. It allows you to focus your analysis on specific sections of your data. 

```python
# group data
grouped_data = df.groupby('Condition')

# aggregate data
aggregated_data = grouped_data['Age'].mean()
```
Here, grouped_data is your DataFrameGroupBy object, 'Age' specifies the column you're aggregating on, and mean() is your aggregate function. The result, aggregated_data, will be a new DataFrame showing the average age for each condition.

**Advanced Grouping on multiple columns**

```python
# group data
grouped_multi = df.groupby(['Condition', 'Hospital'])

# aggregate data
aggregated_multi = grouped_multi['Age'].mean()
```

*Grouping is like sorting your data into various folders (or groups), and aggregating is about summarising the contents of each folder into a short report. Grouping prepares your data for aggregation, which then lets you draw actionable insights.*

### Full Code Example

```python
import pandas as pd
import numpy as np

# Create a sample sales dataset
data = {
    'Date': pd.date_range(start='2022-01-01', periods=100, freq='D'),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Books'], 100),
    'Sales': np.random.randint(100, 1000, 100),
    'Price': np.random.uniform(10, 100, 100)
}

df = pd.DataFrame(data)

# Grouping and aggregating
grouped_data = df.groupby('Category').agg({'Sales': 'sum', 'Price': 'mean'})

print(grouped_data)
```

## Combining DataFrames in Pandas: Merge, Join, and Concat

### Three ways to combine DataFrames

### Method 1 - Using merge() fr SQL-like Join
The merge() function allows you to combine DataFrames in a manner similar to SQL joins. It is highly flexible and supports inner, outer, left, and right joins.

Parameters:

left and right: The DataFrames you want to merge
on, left_on, right_on: The keys to merge on. These could be column names or arrays with a length equal to the DataFrame lengths

Example: Inner Join

An inner join returns only the records that have matching keys in both DataFrames.
```python
merged_inner = pd.merge(df_temp, df_prec, on='Date')
```

### Method 2 - Using join() for Simpler Joins

The **join()** method is easier to use than merge() and combines DataFrames based on indices by default. However, you can specify keys using the on parameter.

Example: Left Join on Indices

Let's join **df_temp** and **df_prec** based on their indices.

```python
joined_left = df_temp.join(df_prec, lsuffix= '_temp', rsuffix='_prec', how='left')
```
In this example, we use the join() method to perform a left join, keeping all rows from df_temp and appending columns from df_prec. The lsuffix and rsuffix add suffixes to overlapping column names.

The join() operation differs from merge() primarily in that it joins on indices by default rather than requiring you to specify columns. The operation we performed kept all rows from the temperature DataFrame (df_temp) and aligned them with the matching indices in the precipitation DataFrame (df_prec).

### Method 3 - Using concat() for Direct Concatenation

The **concat()** function combines DataFrames along a particular axis, either row-wise (axis=0) or column-wise (axis=1), without needing any keys.

Let's check out our other DataFrame called df_wind with wind speed data:

```python
concatenated = pd.concat([df_temp, df_wind], ignore_index=True)
```

Unlike **merge()** and **join()** which combine DataFrames based on keys or indices, **concat()** simply stitches them together along a specified axis. We used it to append the wind speed DataFrame (df_wind) to the temperature DataFrame (df_temp) in a row-wise fashion, effectively extending the dataset without the need for common identifiers like keys or indices.

### Full Code Example Merge

```python
import pandas as pd

# Load two sample DataFrames

df1 = pd.read_csv('dataset1.csv')

df2 = pd.read_csv('dataset2.csv')

merged_data = pd.merge(df1, df2, on='common_column')

print(merged_data)
```

### Full Code Example Join

```python
joined_data = df1.join(df2.set_index('key_column'), on='common_column')
print(joined_data)
```

## Regular expressions

### Basic Regex concepts

First up: Using Regex for a simple character pattern search

The simplest form of Regular Expressions is a sequence of characters. For example, the Regex pattern "abc" will match any string that contains "abc" in that exact order.

```python
import re

text = "abcdef"
print(re.findall("abc", text))
# output: ['abc']
```

**Regex for matching**

Here is an example of matching patterns of text with Regex. 

```python
import re

# Matches any string that starts with 'My'
print(re.findall(r'^My', 'My story'))

# Matches any string that ends with 'tale'
print(re.findall(r'tale$', 'fairy tale'))

# exact match (starts and ends with "exact match")
print(re.findall(r'^exact match$', 'exact match'))

# matches any string with "text" in it 
print(re.findall(r'text', 'This is text'))
```

**Quantifiers in Regex**

Quantifiers in Regex define how many instances of a character, group, or character class must be present in the input for a match to be found. They include symbols like * (zero or more), + (one or more), and ? (zero or one).

1. **(Zero or More Matches)**
The * quantifier matches 0 or more occurrences of the preceding character or group.

```python
import re

# Match zero or more "a"s followed by "b"
pattern = r"a*b"

# Examples
print(re.match(pattern, "b"))       # Matches: "b" (zero 'a's)
print(re.match(pattern, "ab"))      # Matches: "ab" (one 'a')
print(re.match(pattern, "aaab"))    # Matches: "aaab" (three 'a's)
```

2. **+ (One or More Matches)**
The **+** quantifier matches 1 or more occurrences of the preceding character or group.

```python
import re

# Match one or more "a"s followed by "b"
pattern = r"a+b"

# Examples
print(re.match(pattern, "b"))       # Does not match: needs at least one 'a'
print(re.match(pattern, "ab"))      # Matches: "ab" (one 'a')
print(re.match(pattern, "aaab"))    # Matches: "aaab" (three 'a's)
```

3. **? (Zero or One Match)**
The **?** quantifier matches 0 or 1 occurrence of the preceding character or group.

```python
import re

# Match zero or one "a" followed by "b"
pattern = r"a?b"

# Examples
print(re.match(pattern, "b"))       # Matches: "b" (zero 'a's)
print(re.match(pattern, "ab"))      # Matches: "ab" (one 'a')
print(re.match(pattern, "aab"))     # Does not match: more than one 'a'
```

4. **{n} (Exact Number of Matches)**
The **{n}** quantifier matches exactly n occurrences of the preceding character or group.

```python
import re

# Match exactly 3 "a"s followed by "b"
pattern = r"a{3}b"

# Examples
print(re.match(pattern, "aaab"))    # Matches: "aaab" (exactly 3 'a's)
print(re.match(pattern, "ab"))      # Does not match: only 1 'a'
print(re.match(pattern, "aaaab"))   # Does not match: more than 3 'a's
```

5. **{n,} (At Least n Matches)**
The {n,} quantifier matches at least n occurrences of the preceding character or group.

```python
import re

# Match at least 2 "a"s followed by "b"
pattern = r"a{2,}b"

# Examples
print(re.match(pattern, "aab"))     # Matches: "aab" (2 'a's)
print(re.match(pattern, "aaaab"))   # Matches: "aaaab" (4 'a's)
print(re.match(pattern, "ab"))      # Does not match: fewer than 2 'a's
```

6. **{n,m} (Range of Matches)**
The **{n,m}** quantifier matches between n and m occurrences (inclusive) of the preceding character or group.

```python
import re

# Match between 2 and 4 "a"s followed by "b"
pattern = r"a{2,4}b"

# Examples
print(re.match(pattern, "aab"))     # Matches: "aab" (2 'a's)
print(re.match(pattern, "aaaab"))   # Matches: "aaaab" (4 'a's)
print(re.match(pattern, "aaaaab"))  # Does not match: more than 4 'a's
print(re.match(pattern, "ab"))      # Does not match: fewer than 2 'a's
```

7. .* **(Any Number of Any Character)**
The .* quantifier matches 0 or more of any character (except newline unless re.DOTALL is used).

```python
import re

# Match any string ending with "b"
pattern = r".*b"

# Examples
print(re.match(pattern, "hello worldb"))   # Matches: "hello worldb"
print(re.match(pattern, "b"))             # Matches: "b" (zero characters before 'b')
print(re.match(pattern, "abc"))           # Does not match: does not end with 'b'
```

8. **Combining Quantifiers**
You can combine quantifiers with groups and other characters.

```python
import re

# Match strings with 2 or more "ab" groups
pattern = r"(ab){2,}"

# Examples
print(re.match(pattern, "abab"))     # Matches: "abab" (2 'ab' groups)
print(re.match(pattern, "ababab"))   # Matches: "ababab" (3 'ab' groups)
print(re.match(pattern, "ab"))       # Does not match: only 1 'ab'
```

### Summary of Quantifiers
Quantifier	Description	Example
- *	0 or more	a*b matches b, ab, aaab
- +	1 or more	a+b matches ab, aaab
- ?	0 or 1	a?b matches b, ab
- {n}	Exactly n times	a{3}b matches aaab
- {n,}	At least n times	a{2,}b matches aab, aaaab
- {n,m}	Between n and m times inclusive	a{2,4}b matches aab, aaaab

### Using the OR operator

1. Using **|** to Match One of Several Options
The | operator allows you to specify multiple patterns, and it matches any one of them.

```python
import re

# Match either "cat" or "dog"
pattern = r"cat|dog"

# Examples
print(re.match(pattern, "cat"))     # Matches: "cat"
print(re.match(pattern, "dog"))     # Matches: "dog"
print(re.match(pattern, "cow"))     # Does not match: neither "cat" nor "dog"
```
2. Using **|** with Groups
You can group parts of a pattern with parentheses () and use the | operator inside the group.

```python
import re

# Match either "batman" or "superman"
pattern = r"(batman|superman)"

# Examples
print(re.match(pattern, "batman"))    # Matches: "batman"
print(re.match(pattern, "superman"))  # Matches: "superman"
print(re.match(pattern, "spiderman")) # Does not match: not "batman" or "superman"
```

3. Using **|** in a Complex Pattern
The | operator can be part of a larger pattern.

```python
import re

# Match strings that start with "hello" followed by either "world" or "there"
pattern = r"hello (world|there)"

# Examples
print(re.match(pattern, "hello world"))  # Matches: "hello world"
print(re.match(pattern, "hello there"))  # Matches: "hello there"
print(re.match(pattern, "hello friend")) # Does not match: not "world" or "there"
```

### Practice Regex with this tool

https://regex101.com/

**Google collab Pandas practice file 'L5DE M3T5 Data_Manipulation.ipyng'**

## Topic 5 Reflections

Be careful with data manipulation that you don't change customer info. If you change an email address you might send personal information to the wrong person
