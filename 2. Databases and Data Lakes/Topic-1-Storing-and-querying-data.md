# Topic 1 - Storing and querying data - 24/10/2024
  
## Why business are not throwing away data
### Objectives
- Analyse the economic factors contributing to the decrease in data storage costs over the decades.
- Evaluate the strategic impact of data accumulation and its utilisation in decision-making processes.

Cost of storage has dramatically reduced
![cost over time](https://ourworldindata.org/images/published/historical-cost-of-computer-memory-and-storage-desktop.png)

Roles like Chief Data Officer CDO highlight the shift towards data.
CDO:
- Lead the data and analytics agenda of an organisation.
- Establish and deliver technologies, tools, approaches and methodologies to unlock the value in enterprise data assets of an organisation.
- Manage data as a strategic asset and operational data governance, data quality and other controls to sustain the integrity of the data of an organisation.
- Serve as trusted partner to key business executives focused on the customer, enterprise risk management, regulatory compliance and finance.
- Fosters innovation leveraging emerging Big Data and analytics technologies.

### Data Marketplaces
Data marketplaces are online platforms where individuals and organisations can buy, sell, or exchange various types of data. These platforms serve as intermediaries, connecting data providers with data consumers, and facilitating transactions between them. Data marketplaces offer a wide range of datasets, including demographic data, consumer behavior data, financial data, and more. They play a crucial role in the data economy by enabling organisations to access additional data sources to enhance their analytics, decision-making, and innovation efforts.

Examples include:
- Kaggle (subsidiary of google)
- Data.world
- AWS Data Exchange

## Storing Files: HDFS, Key-Value Stores, Columnar – Parquet Format, Filesystems
### Objectives
- Understand the evolution and functionality of HDFS and its impact on data storage and computation.
- Differentiate between various data storage systems and their applicable use cases.
  
### Hadoop Distributed File System (HDFS)
An introduction to Hadoop Distributed File System (HDFS) as a revolutionary technology between 2008-2016, which turned data centres into computing clusters by bringing computation to the data. 

This innovative approach allowed for cheap commodity storage, offering resilience by storing three copies of each file and distribution by ensuring each file resides on at least three different machines. This configuration not only provided a cost-effective solution for managing vast amounts of data but also enhanced data accessibility and analysis capabilities.

![HDFS](https://www.researchgate.net/publication/312185695/figure/fig3/AS:579123831885824@1515085289621/Hadoop-Distributed-File-System-HDFS-structure-and-its-reading-process.png)

### Key-value stores
Key-value stores offer a straightforward yet efficient method for storing and retrieving data based on a unique key, tailoring their approach for scenarios where quick data access is critical.

Meanwhile, the Parquet format, designed for efficiency in analytic queries, employs a columnar storage strategy that significantly reduces disk I/O, facilitating faster data processing and enabling schema evolution with minimal overhead.

![key-value stores](https://media.licdn.com/dms/image/v2/C5612AQEvtFIaV3dD5Q/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1575475361265?e=2147483647&v=beta&t=TI1UoyLOCYntNzZnRt4NfGyguPS6tywwDrbmPLGXsxI)

### Storage formats
This section discusses the trade-offs between using Hard Disk Drives (HDDs) and Solid-State Drives (SSDs) for data storage, touching on aspects of speed, durability, and cost. HDDs, with their mechanical parts, are generally more affordable but slower and more prone to failure compared to SSDs, which offer faster data access but at a higher price point. The Parquet format, by addressing the need for efficient data analytics through its columnar storage approach, enables organisations to conduct analytic queries more efficiently, leveraging schema evolution to adapt to changing data requirements without significant reengineering.

### Parquet
- Parquet files are columnar storage formats, meaning data is stored by column rather than by row. This structure allows for better compression and efficient storage, especially for large datasets with many columns.
- Parquet files are highly optimized for analytical queries, as they allow for selective column reads and efficient compression techniques. This results in faster data processing and reduced I/O overhead compared to CSV and JSON files.
- Parquet files offer advanced features such as schema evolution, predicate pushdown, and efficient encoding schemes. These features make Parquet ideal for data analytics and big data processing frameworks like Apache Spark and Apache Hive
![parquet](https://data-mozart.com/wp-content/uploads/2023/04/Row-groups-1024x576.png)

### CSV
- CSV files are plain text files where each line represents a single row of data, and values are separated by commas or other delimiters.
- CSV files are simple and easy to read/write but may not be efficient for large datasets or analytical workloads due to their row-oriented structure.
- CSV files are widely supported and easy to work with in many programming languages and tools. However, they lack built-in support for nested data structures or data types.

### JSON
- JSON files support nested structures and are commonly used for representing semi-structured data. They are well-suited for web APIs and applications where flexibility is important.
- JSON files offer flexibility and support for complex data structures but can be less efficient in terms of storage and processing compared to more optimized formats.
- JSON files support nested structures and are commonly used for representing semi-structured data. They are well-suited for web APIs and applications where flexibility is important.

### Key-value pairs databases
Key-value stores, such as Redis and DynamoDB, provide a highly efficient mechanism for data retrieval using a simple key. They excel in scenarios requiring rapid access to data, such as session storage, user preferences, or caching. The simplicity of key-value stores allows for high-performance operations, making them an indispensable part of the technology stack where response time is critical. Their scalability and ease of use have made them a popular choice for web applications and microservices architectures, where they can quickly serve data to users and processes.
- Key-value databases are often used as a caching layer in front of a more persistent data store to improve the read performance of an application.
- Key-value databases can be used to store user session data, such as login status, shopping cart contents, or other temporary data.
- Key-value databases can be used to store and process large amounts of data in real -time, such as sensor data, social media feeds and IoT data.
- Key-value databases can be used to store and retrieve high scores and rankings for online games.
- Key-value databases can be used to store data that is distributed across multiple machines, such as distributed hash tables or distributed key-value stores.
- Key-value databases can be used to store and retrieve content such as images, videos and audio.
- Key-value databases can be used to store and retrieve product information, such as description, prices and inventory levels.

Key-value dtb list:
- Redis -
An open-source, in-memory data structure store that can be used as a database, cache, and message broker.

- Riak -
An open-source, distributed key-value database that is designed for high availability and scalability.

- Berkeley DB -
A family of embedded key-value databases that are designed for high performance and low-level storage, and are often used in embedded systems and mobile devices.

- Memcached -
An open-source, in-memory key-value cache that is often used to speed up dynamic web applications by reducing the number of times an external data source must be read.

- RocksDB -
An open-source, persistent key-value store that is based on LevelDB and is optimized for storage on flash and hard disk drives.

- Amazon DynamoDB -
A fully managed, highly available, key-value database service that is part of the Amazon Web Services (AWS) ecosystem.

- Azure Cosmos DB -
A globally distributed, multi-model database service that supports key-value, document, graph, and column-family data models.

- Google Cloud Bigtable -
A fully managed, high-performance, wide-column NoSQL key-value store that is part of the Google Cloud Platform (GCP) ecosystem.

## Data Lakes, Data Warehouses, and Operational Data Stores
### Objectives
- Differentiate between data lakes, data warehouses, and operational data stores, understanding their unique features and use cases.
- Assess the role of each data storage solution in supporting data-driven decision-making and analytics within an organisation.

### Data Lakes
Unstructured Data's Haven: Data lakes act as vast reservoirs of raw, unstructured data, capturing everything from logs and XML files to social media posts. They offer unparalleled flexibility in data storage, allowing businesses to store data in its native format without the need for upfront schema definition. This flexibility makes data lakes an ideal solution for storing large volumes of diverse data, enabling advanced analytics and machine learning models that can drive significant insights and innovation. 

### Data Warehouses
Structured for Analysis: In contrast, data warehouses are highly structured repositories designed to facilitate efficient data analysis and reporting. They resemble a well-organised email system with sub-inboxes and labels, where data is categorised and stored in a manner that makes it easily accessible for specific queries and reports. This structured environment supports complex queries, business intelligence, and data mining efforts, enabling organisations to derive actionable insights from their accumulated data. Data warehouses are essential for businesses that rely on historical data analysis to inform strategic decisions, offering a stable and reliable platform for data storage and retrieval.

### Operational Data Stores (ODS)
Real-Time Data Processing: Operational data stores are designed for the real-time processing of transactional data, supporting day-to-day business operations. They enable the immediate availability of operational data for analysis and decision-making, acting as a bridge between transactional databases and data warehouses or data lakes.

An operational data store (ODS) is a type of database that's often used as an interim logical area for a data warehouse. ODSes are designed to integrate data from multiple sources for lightweight data processing activities such as operational reporting and real-time analysis.

![ODS](https://www.techtarget.com/rms/onlineimages/how_ods_works-f_mobile.png)

### Data Lakehouses
More recently a new term of data lakehouses are emerging. These are a combination of data lakes and data warehouses
![data lakehouse](https://www.databricks.com/wp-content/uploads/2020/01/data-lakehouse-new.png)

## Intro to Data Structuring: Schema-on-Write, Relational Modelling
### Objectives
- Comprehend the principle of schema-on-write and its significance in relational data modelling.
- Apply the concepts of relational modelling to effectively structure and organise data within a database.

### Schema on write
Schema-on-write is a foundational concept in data management, particularly relevant to relational databases. It requires that the schema, or structure of the data, be defined before any data is written to the database. This pre-definition ensures data consistency and integrity, as each data entry must conform to the established schema, including data types, relationships, and constraints. This approach is akin to planning the architecture of a building before construction begins, ensuring that all components fit together as intended and meet specific standards.

Schema on Write	
- Fast reads	
- Slower loads	
- Not agile	
- Structured	 
- Fewer errors	

Schema on Read
- Slower reads
- Fast loads
- Very agile
- Structured / Unstructured
- More errors

### The Fundamentals of Relational Modelling
Relational modelling is a method used to structure data in a database by defining relationships among data points. It involves organising data into tables (relations) that include rows (records) and columns (attributes). Key concepts such as primary keys (unique identifiers for each record) and foreign keys (identifiers that establish relationships between tables) are crucial. Relational models facilitate efficient data retrieval and manipulation through structured queries. This methodical approach to organising data is similar to creating a detailed map of a city, where every element has a specific place and relation to others, enabling easy navigation and management.

![Relational Database Model](https://lh6.googleusercontent.com/proxy/_2f-1E5ZHJroEc64R0VYDnUDj1cdJfsrjKOGt3t9Xpnc7SXviaOXkOBAvCrSa7DegDmx_BIbyAFARejLoU-JcN0f_qMpk0GC-w)

## Storing Data On-Premise vs. In the Cloud
### Objectives
- Articulate the advantages and disadvantages of on-premise and cloud-based data storage solutions.
- Evaluate the implications of on-premise and cloud storage options on data security, scalability, cost, and accessibility.

### On-prem storage
On-premise storage involves maintaining data servers and infrastructure within an organisation's physical premises. This traditional method offers complete control over the data environment, including security protocols and access mechanisms. It is akin to keeping valuable documents in a safe within one's own house, where access and security can be directly managed. However, this comes with the responsibility of managing hardware, software, and ensuring data protection, which can be costly and resource-intensive. On-premise storage is best suited for organisations with high-security requirements or those that handle sensitive data, where regulatory compliance and data sovereignty are paramount.

### Cloud storage
Cloud storage represents the shift towards hosting data on servers managed by third-party providers, accessible over the internet. This model offers flexibility, scalability, and cost-efficiency, as organizations can easily adjust their storage needs and only pay for the capacity they use. The cloud storage model can be compared to renting a safe deposit box in a bank; while it's off-site and managed by another entity, it promises security, accessibility, and scalability. However, it also involves trusting a third party with the data and potentially facing issues related to data transfer speeds and internet dependency. Cloud storage is ideal for organisations looking for operational flexibility, cost savings on hardware, and the ability to scale quickly.

### Hybrid storage
Best of Both Worlds: Many organisations opt for a hybrid approach, combining on-premise and cloud storage to leverage the strengths of both. This strategy allows sensitive data to be kept on-premise for security reasons while utilising the cloud for scalability and flexibility, especially for non-sensitive data and applications that benefit from cloud computing resources.

## Lecture notes
### Storage Options
File systems (File Directories)
Linux assumes everything is a file
Powershell on Windows is a way of navigating the filesystems. Powershell is more functional than cdm prompt. It has "cmdlets" commands which are more detailed than you can do in cmd prompt. cmdlets show as orange in the terminal.
![powershell cheat sheet](https://cdn.comparitech.com/wp-content/uploads/2018/12/PowerShell-Cheat-Sheet-1.jpg)


Example code in powershell to sum up size of files in a directory:
$directory = "C:\Users\helen\OneDrive\Documents\Chris\BPP Level5 Data Engineer\Module2_Databases_and_Data_Lakes"

Get-ChildItem -Path $directory -Directory | ForEach-Object {
 $folder = $_
 $totalSize = (Get-ChildItem -Path $_.FullName -File | Measure-Object -Property Length -Sum).Sum / 1MB
 "{0} has a total size of {1:N2} MB" -f $folder.Name, $totalSize
} 

We practiced using cd to navigate to a directory and then ran these scripts
cd ...
.\script.ps1

Also looked at binary formats, hexidecimal and text files.

Unicode is a bigger file format but supports more characters than ASCII. If you want Japanese characters you might need UTF8 or UTF16 or UTF32. Obviously you want the samllest one possible that supports what you need. You can google the answers to this.

I read the book Code that explained these in great detail.

### MIME
MIME types are files extentions. HTML, TXT, PDF etc

File encryption uses keys. Key is a special type of file with a number in it. We'll cover this in more detail in cyber security module.

### Databases
Moving from files databases are a much more powerful way to query data
- Local database runs on laptop
- Remote database are common and provide access to multiple users. This can be on employers servers and not cloud
- Cloud services providers are outsourced server centers. Or a company could create their own cloud. These are called private clouds.

Types of cloud storage:
- Block storage
  - Offers dedicated, low latency storage
  - Callable and offers high performance
  - Similar to local direct attached storage  or storage area network (SAN)
  - Offers disaster recovery
  - Example Amazon Elastic Block Storage (Amazon EBS)

- File storage
  - Stores data as files
  - Highly scalable
  - Ideal for repos and media stores
  - Example Amazon Elastic File Storage (Amazon EFS)

- Object storage
  - Stores unstructured, semi structured or structured data
  - Highly scalable
  - Offers unique identifier for each object
  - Lower cost to traditional storage
 
### Data modelling
Data modelling skills essentially keep the data tidy
SQL

Data Models have three parts:
- Structure of the data. What does it look like. Schema is conceptual structure. Don't confuse with the phrase 'Data Structure' this is list, arrays, dictionaries in programming
- Operations of the data. What's available
- Constraints of the data. What's allowed. Age > 0 etc. Two catagories domain constraints real world (what you expect, data types, range constraints, format constraints such as email adresses and rule based constraints) and integrity constraints database integrity (primary keys, null values, duplication)

Domain is an old school word for data types VARCHAR, FLOAT etc

ANSI SQL is SQL sntax that works across different systems. SQL server and MYSQL etc. Some syntax is unique to the system
FLOAT is floating value so accepts decimals

Relations means a table
records can mean rows
fields can mean columns
cardinality is number of unquie values

![for sql practice](https://sqlfiddle.com/)

## Topic 1 Reflections
What can I automate with scripts?
Consolidating files locally in powershell
Cloud functions to do these things in the cloud. I want to be able to use GCP pub/sub to trigger a cloud function for event based data loading.

## Consolidation Task 1
Reflect on the dramatic decrease in storage costs over the decades and the strategic implications of this trend for data-driven decision-making within the context of the HR department.
- For HR the impact is that it's far more accessible for a business to use data driven stratagies. A HR data team can use data to understand the workforce, turnover and market behaviours in a way that can be utilised for data driven decision making.

Consider how this data-centric approach could be replicated or adapted to enhance decision-making and operational efficiency in other sectors. 
- Data driven decision making can be used by any company. For example a flower shop with a website could use data for understanding how customers interact with the website and ultimately improve the service. They could also look at the distribution of the products to provide a better service.

Write a brief analysis in your learning journal, focusing on potential impacts on your organisation. 
- In Telecoms data is huge. Better understanding out customers is key to success in very competitive markets. We focus on having a robust data infrastructure to extract data from various source and transform it into something that can be utilised for modelling to create insight on the business.

Identify a stakeholder in your business from whom you could learn more about the effective use of data.
- Personally I think Finance is a department that has a legacy way of working that could benefit from a better understanding of data tools.

Identify a few data sources about competitive trends in the industry, identify the relevant datasets on Google Dataset Search and data marketplaces, and estimate their dataset sizes.
- ![google trends is has data sets for things trending on the internet]([https://trends.google.com/trends/explore?date=now%201-H&geo=GB&q=technology&hl=en](https://trends.google.com/trends/explore?date=all&geo=GB&q=AI&hl=en))
- I used this to look at interest in technology over time. Size of the dataset would be huge 00's of TB

Also investigate how often this data gets updated and when new data becomes available. Estimate the yearly costs involved in storing this data.
- Data is updated hourly. Yearly costs would be high. It's difficult to estimate not knowing the size of the full dataset.

## Consolidation Task 2
Reflect on how different storage solutions—HDFS, key-value stores, and Parquet—can meet the diverse data storage and analysis needs within your organisation.
- We use a range of storage solutions. Cloud storage (uses HDFS) is used for compressed file storage, JSON are used in IaC for table schemas, parquet format is used in bigquery tables and CSVs are used for some output files for non technical users to explore in excel.

Consider the impact of these technologies on data accessibility, analytics capabilities, and overall strategic objectives.
- These technologies allow for a huge amount of accessible data opening the door for a range of analytics and data science use cases. The aim of this is the leverage this data to get insight into business performance and customer behaviour.

Identify a specific data challenge in your organisation and propose a storage solution that addresses this challenge, outlining the benefits and any potential limitations.
- With huge amounts of data. Data storage cost is a big concern. One solution to solve bigquery costs is to move from a pay per query model to a capped slot allowance per day. This will make engineers think differently about how they build their processes to make them as cost effective and slot light as possible.

## Consolidation Task 3
Reflect on a recent project or a data challenge within your organisation.
- Migrating to GCP from on-prem.

How might the choice between HDFS, key-value stores, and Parquet influence the outcome of this project? 
- It would influence the speed of data retrieval and also the way the data can be used by analytics/data science teams.

Consider factors such as data volume, query performance requirements, and the nature of the data (structured vs. unstructured).
- With large volumes and query performance gains you'll want to use structured data. For fast retrieval key-value pairs might work better.

Identifying a stakeholder in your business who could provide further insights or feedback on your proposed solution.
- Solution architects.

## Consolidation Task 4
Investigate a specific example where restructuring data according to relational modelling principles enhanced operational efficiency or decision-making.
- Moving from on-prem to GCP BigQuery
Write down your analysis in your learning journal, including the current challenges, proposed improvements, and the expected benefits.
- BigQuery is optimised for flat tables, so the challenge was taking the on-prem relational architecture and making it optimised for a cloud environment

## Consolidation Task 5
Analyse the data storage strategy currently employed by your organisation. Consider the types of data you manage, their sensitivity, and your organisation's operational needs.
- We have a cloud based model. Telcoms has an enormous amount of data and cloud based solutions are more scalable and manageable.
How could a shift towards a cloud, on-premise, or hybrid storage solution impact your data management practices? Document your thoughts in your learning journal, focusing on potential benefits and challenges.
- I've seen the benefits of moving to cloud for our org. Scalability, lots of products to help with optimisation, orchestration, analysis, storage and compute. The issues have been with having a clear understanding of the costs involved and stopping teams spending money needlessly. With almost infinite CPUs the risk of spending a lot of money is huge.
Discuss your analysis with a colleague or stakeholder who could offer additional insights or perspectives on the feasibility and implications of such a shift.
Discussed with our lead engineer

