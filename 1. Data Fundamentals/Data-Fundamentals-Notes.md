# Topic 1 - Fundamentals of the data-driven enterprise - 28/09/2024

## Objectives
- Data Driven Culture
- Fundamentals of Data
- Engineering best Practices
- Data Types

## Key Concepts
### Building a Data Driven Culture
- Data driven culture is one where decisions are based on facts rather than guesswork, authority, legacy etc.
- Five V's Framework describles the attributes of a good data landscape:
  - volume (amount)
  - variety (structured/unstructured)
  - velocity (speed it's generated and processed)
  - veracity (reliabilty and accuracy)
  - value (insights generated from it)
### Data Types
- Qualitive (Not numbers)
  - Bionominal. 1/0, True/False
  - Nominal. Catagories, Red, Yellow, Green
  - Ordinal. In an order. Poor, Medium, Good
- Quantitative (numbers)
  - Discreet. Counted values. No of people
  - Continuous. Measured. Height, Distance
### Identifying Standards and Best Practice
![API standards](https://learn.bpp.com/pluginfile.php/1253474/mod_scorm/content/2/scormcontent/assets/Rest-API.png)
- Restful API principals. This term refers to the client-server architecture for designing networked applications, promoting statelessness and resource-based URLs for efficient data manipulation.
- OpenAPI. This term refers to the standard specification for building and documenting RESTful APIs, accelerating development cycles and enhancing collaboration.
- AWS Cloud framework. Many web applications, including social media platforms and e-commerce websites, rely on JSON for seamless communication.
- Azure Cloud Framework. Financial institutions often use CSV files for data integration and analysis.
- Regulatory requirements
  - GDPR is an EU regulation governing data privacy and consent, impacting European government agencies' data handling processes
  - ISO 27001. ISO 27001 is an international standard that provides guidelines and best practices for establishing, implementing, maintaining, and continuously improving an Information Security Management System (ISMS). In the context of data engineering, adhering to ISO 27001 regulations is crucial for ensuring the confidentiality, integrity, and availability of data and information assets
- Data Stewardship. Responsible for:
  - Data governance
  - Data quality
  - Data ethics
- Data Engineering best practices:
    - Scalability
    - Reliability
    - Security
    - Performance
    - Documentation
### Data Types
![Used google collab for coding practice](https://colab.research.google.com/)
- JSON. Lightweight. Best for web apps
- CSV. Tabular. Best for Finance
- XML. Markup language. Best for exchanging data between systems

- Pandas. Library for working with structures data in python. Puts data in dataframes for performance. Basically python SQL with more functionaility
- Python. Programming language. Easy to read, good for ML and stats
  
## Topic 1 Reflections
- Transitioning to a data driven culture requires both technical and cultureal shifts.
- I'll aim to introduce this into my team by reinforcing the benefits of evidence based decision making.
- I'll also aim to adhere to the engineering best practices listed above.

# Topic 2 - Introduction to data quality - 03/10/2024

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
- Open Standards. Open standards are guidelines for technology that anyone can use and contribute to.
- Reasons for open standards:
  - Compatibility: They help different systems and tools talk to each other smoothly
  - Flexibility: You're not locked into using products from just one company
  - Innovation: Encourages new ideas and improvements by allowing more people to contribute
  - Cost-effective: Often free to use, which can save money on technology costs
- Examples of open standards:
  - Industry-specific standards (e.g., HL7 in healthcare)
  - Cross-industry standards (e.g., Unicode, HTTP, TCP/IP)
  - Open data standards (e.g., OData, OpenAPI)
- FAIR data standard:
  - Findable. Easy for users to find
  - Accessible. Access control
  - Interoperable. Intergrated with other systems or can be
  - Reusable. Lots of metrics so data has many uses
- Dublin Core Metadata Initiative (DCMI) offers a set of metadata standards used to describe resources in various domains. Its core elements provide a basic framework for describing digital resources such as documents, images, videos, and web pages. Used to standerdise things like Digital libraries or museums (Title, Creator, Description, Date) as standard.
- Challenges the can be overcome with standards:
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
- How to choose the right format
  - Use case
  - Tools available
  - Performance (often impacted by file size)
  - Interoperability (working between systems)
  - Data integrity and security (error detection, encryption support)
- Facts about XML
  - Human and machine readable. XML is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable
  - Tagging. It uses tags to define elements within a document, allowing users to create customised tags to suit their specific needs
  - Hierarchical structure. XML documents have a hierarchical structure with nested elements, similar to HTML but with more flexibility and extensibility
  - More general purpose than HTML which is similar
- Example uses:
 - The NHS: XML facilitates the exchange of patient records and medical reports among healthcare providers, improving patient care coordination
 - Banks and professional services: Financial institutions utilise XML for financial transactions and regulatory filings, ensuring accurate and transparent financial reporting
 - IT, retail, sales, education providers, etc.: XML is employed in sectors like e-commerce and education for tasks such as managing product catalogues, student records, and course materials, supporting efficient operations 

- XML Strengths
  - Human-readable: As we have learnt, XML documents are easy to read and understand, making them accessible to both humans and machines
  - Flexibility: XML allows users to define custom tags and structures, providing flexibility in representing diverse types of data
  - Interoperability: XML serves as a universal format for data exchange, enabling seamless communication between different systems and platforms
- XML Weaknesses
  - Verbose syntax: XML documents can become overly complex and repetitive, especially for large datasets, leading to increased file size and complexity
  - Parsing overhead: Processing XML documents requires parsing, which can be computationally intensive, particularly for complex structures or nested elements
  - Lack of schema enforcement: XML does not enforce strict data validation rules by default, leading to potential issues with data quality and integrity
  - Get parsing errors (computer not being able to understand the structure). Parsing errors occur when XML documents have improper structure or syntax, leading to failures during parsing, which is the process of converting XML data into a usable format. These errors can result from missing or mismatched tags, incorrect nesting of elements, or invalid characters.
    - To mitigate these issues, it's essential to validate XML documents against predefined schemas, use robust XML parsers, implement error handling mechanisms, sanitise data before parsing, and conduct regular testing and validation
  - Character encoding issues arise when XML documents contain characters that are not properly encoded or use inconsistent encoding schemes. This can lead to data corruption, rendering issues, or difficulties in processing the XML data correctly.
    - To fix you have three options:
      - Standardise character encoding (use a consistent character encoding scheme throughout XML documents, such as UTF-8 or UTF-16, to ensure compatibility across different systems and platforms)
      - Encode special characters: Properly encode special characters, such as &, <, >, ", and ', using their corresponding character entities (&, <, >, ", and ') to prevent parsing errors and data corruption
      - Validate encoding: Validate XML documents to ensure that character encoding declarations match the actual encoding used within the document. This helps detect and correct inconsistencies or mismatches in encoding

### Navigating quality issues in CSV data formats
CSV (Comma-Separated Values) is a widely used format for storing and exchanging tabular data, commonly used in spreadsheets and for data integration and analysis tasks
- CSV Strengths:
  - Human readable
  - Simple structure
- CSV Weaknesses:
  - Lack a standardised schema
  - Limited data types
  - Susceptable to error because of delimiters and line terminators

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

- API (application programmable interface). An API is a set of protocols, routines, and tools that specify how software components should interact and communicate with each other. In simpler terms, an API acts as a messenger that allows different software applications to talk to each other and share data or functionality. For example, when you use a mobile app to book a  taxi service, the app communicates with the taxi company's server through an API to request and receive information about available drivers, pricing, and estimated arrival times.  

- JSON Strengths:
  - Human readable
  - Lightweight. Smaller file size than XML because of simple structure
  - Native Javascript support
- JSON Weaknesses:
  - Optionality of schema: Unlike XML, JSON does not have a built-in mechanism for defining a schema, which can lead to issues with data validation and consistency
  - Limited data types
  - Nesting complexity: Complex nested structures in JSON can complicate parsing and processing, leading to performance issues

## Topic 2 Reflections
- When designing DPs think about:
  - Data quality and reliability. Use time with the stakeholders to understand requirements to drive this. How often is the data needed etc
  - Open standards. Are there any existing to be adhered to (Finance etc) is my design cost effective and future proofed. Use FAIR data standard as guideline
  - Make sure I'm using the correct data formats for the task. Think about things like cost, storage, performance, security and interoperability beforehand. For example a JSON output might include string info that's difficult to encrypt and also it this format easy for an end user to query
  - 
