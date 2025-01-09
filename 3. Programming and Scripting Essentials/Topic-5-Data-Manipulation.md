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




## Lecture Notes



## Topic 5 Reflections
