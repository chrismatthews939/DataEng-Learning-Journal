# Topic 2 - Introduction to Data Quality - 03/10/2024

## Objectives
- Recognise the core metrics in data engineering essential for ensuring data quality

## Key Concepts
### Data Quality
- Accuracy. How well does our data reflect the real world? Are false items likely?
- Integrity. Completeness. How well does our data cover the real world? Are missing items likely?
- Consistency. How well does our data conform to a single standard? Are discrepancies likely?
- Timeliness. How up-to-date is our data? Are stale items likely?

- The reliability metric. There is also a higher-level meta-metric called reliability encompassing how trustworthy and dependable data is over time and across different use cases.

### Data Metadata and Standards
Open Standards. Open standards are guidelines for technology that anyone can use and contribute to.
Reasons for open standards:
- Compatibility: They help different systems and tools talk to each other smoothly
- Flexibility: You're not locked into using products from just one company
- Innovation: Encourages new ideas and improvements by allowing more people to contribute
- Cost-effective: Often free to use, which can save money on technology costs

Examples of open standards:
- Industry-specific standards (e.g., HL7 in healthcare)
- Cross-industry standards (e.g., Unicode, HTTP, TCP/IP)
- Open data standards (e.g., OData, OpenAPI)

FAIR data standard:
- Findable. Easy for users to find
- Accessible. Access control
- Interoperable. Intergrated with other systems or can be
- Reusable. Lots of metrics so data has many uses

Dublin Core Metadata Initiative (DCMI) offers a set of metadata standards used to describe resources in various domains. Its core elements provide a basic framework for describing digital resources such as documents, images, videos, and web pages. Used to standerdise things like Digital libraries or museums (Title, Creator, Description, Date) as standard.

Challenges the can be overcome with standards:
- Data silos: Without standardised formats and structures, data often becomes siloed within different departments or systems, hindering collaboration and holistic analysis
- Inconsistencies: Lack of standards leads to inconsistencies in data representation, making it difficult to integrate and analyse data across different sources
- Integration issues: Integrating data from disparate sources becomes challenging due to differences in formats, schemas, and semantics

### Navigating quality issues in XML data formats
XXML (Extensible Markup Language) is a markup language designed for structuring and exchanging data between systems, promoting interoperability
- Structured data refers to data that is easily converted into a form usable for data analysis.
  - Found in databases, easy to store, scale, organise (spreadsheet, DP)
- Unstructured data refers to more complex data and is possibly stored in a format that is not easily decoded.
  - Found in warehouses, storage options might be different, requires preprocessing before analysis (social media, video, sensors, PDF)
- Semi structured is somewhere between the two
  - XML, JSON, Often key value pairs

How to choose the right format
- Use case
- Tools available
- Performance (often impacted by file size)
- Interoperability (working between systems)
- Data integrity and security (error detection, encryption support)

Facts about XML
- Human and machine readable. XML is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable
- Tagging. It uses tags to define elements within a document, allowing users to create customised tags to suit their specific needs
- Hierarchical structure. XML documents have a hierarchical structure with nested elements, similar to HTML but with more flexibility and extensibility
- More general purpose than HTML which is similar

Example uses:
- The NHS: XML facilitates the exchange of patient records and medical reports among healthcare providers, improving patient care coordination
- Banks and professional services: Financial institutions utilise XML for financial transactions and regulatory filings, ensuring accurate and transparent financial reporting
- IT, retail, sales, education providers, etc.: XML is employed in sectors like e-commerce and education for tasks such as managing product catalogues, student records, and course materials, supporting efficient operations 

XML Strengths
- Human-readable: As we have learnt, XML documents are easy to read and understand, making them accessible to both humans and machines
- Flexibility: XML allows users to define custom tags and structures, providing flexibility in representing diverse types of data
- Interoperability: XML serves as a universal format for data exchange, enabling seamless communication between different systems and platforms

XML Weaknesses
- Verbose syntax: XML documents can become overly complex and repetitive, especially for large datasets, leading to increased file size and complexity
- Parsing overhead: Processing XML documents requires parsing, which can be computationally intensive, particularly for complex structures or nested elements
- Lack of schema enforcement: XML does not enforce strict data validation rules by default, leading to potential issues with data quality and integrity
- Get parsing errors (computer not being able to understand the structure). Parsing errors occur when XML documents have improper structure or syntax, leading to failures during parsing, which is the process of converting XML data into a usable format. These errors can result from missing or mismatched tags, incorrect nesting of elements, or invalid characters.
To mitigate these issues, it's essential to validate XML documents against predefined schemas, use robust XML parsers, implement error handling mechanisms, sanitise data before parsing, and conduct regular testing and validation
- Character encoding issues arise when XML documents contain characters that are not properly encoded or use inconsistent encoding schemes. This can lead to data corruption, rendering issues, or difficulties in processing the XML data correctly.
- To fix you have three options:
  - Standardise character encoding (use a consistent character encoding scheme throughout XML documents, such as UTF-8 or UTF-16, to ensure compatibility across different systems and platforms)
  - Encode special characters: Properly encode special characters, such as &, <, >, ", and ', using their corresponding character entities (&, <, >, ", and ') to prevent parsing errors and data corruption
  - Validate encoding: Validate XML documents to ensure that character encoding declarations match the actual encoding used within the document. This helps detect and correct inconsistencies or mismatches in encoding

### Navigating quality issues in CSV data formats
CSV (Comma-Separated Values) is a widely used format for storing and exchanging tabular data, commonly used in spreadsheets and for data integration and analysis tasks

CSV Strengths:
- Human readable
- Simple structure

CSV Weaknesses:
- Lack a standardised schema
- Limited data types
- Susceptable to error because of delimiters and line terminators
CSV Common Problems:
- Fixing inconsistent formats
  - Standardise the use of delimiters
- Datatype mismatch
  - Provide a schema alongside
  - Header misalignment 
  - Try to make this consistent

### Navigating quality issues in JSON data formats
JSON (JavaScript Object Notation) is a lightweight, human-readable format primarily used for transmitting data between servers and web applications, enhancing user experiences and performance

JSON has become the preferred data format for web applications and Application Programming Interfaces (APIs) due to its simplicity, flexibility, and compatibility with JavaScript. It is widely used for transmitting data between a server and a web application, making it an integral part of modern web development. 

JSON is the data format that underpins many of the most popular online services we use every day. From social media platforms like X (formerly known as Twitter) and Facebook, to web mapping services like Google Maps, JSON plays a crucial role in enabling the seamless exchange of data. Its lightweight and human-readable nature make JSON an ideal choice for transmitting data between servers and web applications, enhancing user experiences and performance. 

API (application programmable interface). An API is a set of protocols, routines, and tools that specify how software components should interact and communicate with each other. In simpler terms, an API acts as a messenger that allows different software applications to talk to each other and share data or functionality. For example, when you use a mobile app to book a  taxi service, the app communicates with the taxi company's server through an API to request and receive information about available drivers, pricing, and estimated arrival times.  

JSON Strengths:
- Human readable
- Lightweight. Smaller file size than XML because of simple structure
- Native Javascript support

JSON Weaknesses:
- Optionality of schema: Unlike XML, JSON does not have a built-in mechanism for defining a schema, which can lead to issues with data validation and consistency
- Limited data types
- Nesting complexity: Complex nested structures in JSON can complicate parsing and processing, leading to performance issues
JSON Common Problems:
- Complicated (parsing errors). JSON allows for deeply nested structures, where objects can contain other objects or arrays of objects
  - To fix carefully design JSON structures beforehand
- Key value pair integrity (Key-value pairs refer to a data structure where each element in the structure is represented by a unique key and its corresponding value)
  - Establish naming conventions to maintain key value pair integrity
  - Large files can cause issue with memory usage 
  - Think about this beforehand and use thinks like compression if needed
   
### Strategies for Data Quality
Validation Tools
 - Automated validation tools are essential components of data quality management, enabling organisations to identify and correct format-specific issues efficiently.
     - Data quality management platforms (Informatica data quality, Talend Data Quality)
     - Data Profiling Software (SAS Data Quality, Oracle Data Profiling)
     - Data Validation Frameworks (Apache Griffin, Great Expectations)

### Data Testing
Horizontal Tesing
Horizontal testing is a fundamental data quality testing methodology that focuses on ensuring data consistency and integrity across multiple data sources. 

Historical Analysis
Historical analysis plays a vital role in data quality management by enabling organisations to track changes in data quality over time. Understanding historical data trends and patterns allows data engineers to identify anomalies, track changes in data quality metrics over time, and ensure the long-term integrity of the data.

Rule Base Testing
Rule-based testing is an essential component of data quality assurance, involving the validation of data against predefined rules or criteria. As data engineers, understanding rule-based testing methodologies is key to ensuring compliance with quality standards and regulatory requirements.

Statistical Testing
Statistical testing techniques help assess the reliability and quality of datasets by detecting deviations from expected patterns or distributions. Statistical testing techniques empower data engineers to identify anomalies and outliers within datasets using advanced statistical methods. 
  
## Lecture notes
Big Data 5 V's:
- Volume MB, GB etc. Big data will be TB
- Variety
- Velocity. How quickly it becomes stale
- Veracity. How trustworthy it is
- Value

Data Quality Metrics:
- Accuracy, correctness
- Integrity, completeness
- Consistency, uniformity
- Timeliness, availability
- Reliability, robustness

Unique Identifiers (UID) - Unique within a system
Universally Unique ID (UUID) - Globally unique sometimes called Globally Unique Id (GUID)

## Topic 2 Reflections
When designing DPs think about:
- Data quality and reliability. Use time with the stakeholders to understand requirements to drive this. How often is the data needed etc
- Open standards. Are there any existing to be adhered to (Finance etc) is my design cost effective and future proofed. Use FAIR data standard as guideline. For example improve "FIND" from FAIR principals by improving our DP catalogue.
- Make sure I'm using the correct data formats for the task. Think about things like cost, storage, performance, security and interoperability beforehand. For example a JSON output might include string info that's difficult to encrypt and also it this format easy for an end user to query
- ![Use online converter tools if I need to change file formats](https://www.freeformatter.com/xml-to-json-converter.html)
- Utilise the naming conventions guide for DP consistency (downloaded PDF - Naming conventions for data management)
- Use these principals to improve DP veracity (how trustworthy it is) and value
Try and push for a culture change of collaboration and standardisation accross squads
Being a better data steward as a guardian for accuracy, integrity, timeliness
Ensuring we cover all the types of data testing (Horizontal Tesing, Historical Analysis, Rule Base Testing, Statistical Testing). Aim to introduce tool like Pandas to the squad.

## Topic 2 Apply Task 1
![Kaggle Data](https://www.kaggle.com/code/faressayah/ibm-hr-analytics-employee-attrition-performance)
- What is the usability score of this dataset and is it “good” or “bad”?
  - 8.82. Let down by credability
- How is this usability score calculated?
  - Completeness, Compatability, Credibility
- What are the two credibility issues with this dataset and why are they important?
  - Source and Update Frequency. Important if you wanted to build anything robust from this
 
Kaggle file issues
- Inconsistent formatting Y/N or Yes/No
- Employee number is sequential and poor use for a key
- How many columns does this dataset have?
  - 35
- What is the licence for this dataset and how would you summarise the usage rights in your own words?
  - Open data contract. Open for use with disclaimers

My own edited file called Kaggle_Data for Apply Task 1 is saved in this folder.

## Topic 2 Apply Task 2
Arrange a shadowing session with a data engineer or a subject matter expert in your organisation to observe how they leverage automated data quality management tools in their workflow.

Hour with Data Science team
- An overview of the automated data quality management tools you researched. We looked at Dataflow, Airflow and Bigquery
- Key features and capabilities of these tools. Dataflow for error checking and BQ to show logging and scheduling
- Examples of how they are used in your organisation or industry. Running survival curve pipelines
- Potential challenges or limitations you identified. Potential for errors to be flagged but no resoure to fix them in a timely manner
- Best practices and recommendations for effective implementation and usage. Modularisation and simplify DAG components

KSBs covered in this topic and exercises: K4, K5, K7, K9, K10, K11, K16, K17, K21, K28, K30, S1, S12, S22, S26

## Topic 2 Apply Task 3
In this exercise, your task is to create a high-quality dataset by consolidating data 
from three separate low-quality datasets

Steps taken:
- Consolidated datasets into one sheet called 'consolidated' (excel topic2_apply_task3 in this repo)
- Analysed the datasets and concluded consitent fields are HF_NAME and STAR_RATING
- Looked for inconsistent formatting and changed star rating to be a INT64 because it's smaller in case the dataset grows
- I added an extra field for Region. This way if issues are identified you can pin point it to a specific feed and get that fixed
- Some info such as data facilities being private or public was useful but not much good for analysis if it's not available for all areas. I would ask to get this included to all areas
- Added a tab with a JSON schema for the new consolidated dataset

- Created a new CSV dataset with schema attached
- Loaded CSV into Notebook to do EDA using pandas ('topic2_task3.ipynb in this GitHub Repo)
- Check for null values
- Check for dulicates
