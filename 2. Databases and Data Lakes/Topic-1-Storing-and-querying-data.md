# Topic 1 - Storing and querying data - 24/10/2024

## Objectives
- Analyse the economic factors contributing to the decrease in data storage costs over the decades.
- Evaluate the strategic impact of data accumulation and its utilisation in decision-making processes.
- Understand the evolution and functionality of HDFS and its impact on data storage and computation.
- Differentiate between various data storage systems and their applicable use cases.
   
## Why business are not throwing away data
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

### Hadoop Distributed File System (HDFS)
An introduction to Hadoop Distributed File System (HDFS) as a revolutionary technology between 2008-2016, which turned data centres into computing clusters by bringing computation to the data. 

This innovative approach allowed for cheap commodity storage, offering resilience by storing three copies of each file and distribution by ensuring each file resides on at least three different machines. This configuration not only provided a cost-effective solution for managing vast amounts of data but also enhanced data accessibility and analysis capabilities.

![HDFS](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FThe-overview-of-the-Hadoop-Distributed-File-System-HDFS_fig4_348387085&psig=AOvVaw1fzVJPqNwrpJ1YazPlDOCi&ust=1729844082550000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOixisbJpokDFQAAAAAdAAAAABAE)

### Key-value stores
Key-value stores offer a straightforward yet efficient method for storing and retrieving data based on a unique key, tailoring their approach for scenarios where quick data access is critical.

Meanwhile, the Parquet format, designed for efficiency in analytic queries, employs a columnar storage strategy that significantly reduces disk I/O, facilitating faster data processing and enabling schema evolution with minimal overhead.

![key-value stores](https://media.licdn.com/dms/image/v2/C5612AQEvtFIaV3dD5Q/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1575475361265?e=2147483647&v=beta&t=TI1UoyLOCYntNzZnRt4NfGyguPS6tywwDrbmPLGXsxI)

### Storage formats


## Lecure notes
...

## Topic 1 Reflections


## Consolidation Task
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

## Topic 1 Apply Task 1
...





