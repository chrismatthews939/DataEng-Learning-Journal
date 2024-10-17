# Topic 4 - Introduction to reliable data architectures - 17/10/2024

## Objectives
1. Design reliable and compliant data architectures by employing visual modelling and diagramming techniques
2. Mitigate fundamental data risks within architectures
3. Develop strategies for effective metadata management
   
## Key Concepts
Three main types of design in data engineering:
1. Unified modelling language (UML) diagrams
2. Entity-relationship diagrams (ERDs)
3.Architecture diagrams (e.g. Layered architecture, microservices architecture) 

## Diagrams

### Unified Modelling Language (UML) diagrams
![UML Diagrams](https://miro.com/blog/wp-content/uploads/2021/12/image2-1.png)

### Use Case Diagrams
A use case diagram is a diagram that provides a visual representation of how users interact with a system. It illustrates the various interactions between users (actors) and the system to accomplish specific tasks or goals. 

Use case diagrams play a crucial role in system analysis and design by providing a visual representation of user-system interactions, aiding in communication between stakeholders, and guiding the development process towards building a system that fulfils user requirements effectively.

### Use Case Diagram Best Practice
- Using standardised notation and symbols
- Clearly depicting data flow and transformations
- Highlighting dependencies and relationships
- Maintaining clarity and readability

### EDRs
An entity relationship diagram (ERD) serves as a powerful visualisation tool for understanding the relationships between different entities within an application or database.

### DFDs
Data Flow Diagrams (DFDs) are particularly useful for visualising the flow of data through a system, including sources, destinations, and any intermediate transformations or processes. 

### Logical Diagrams
Logical diagrams are designed to illustrate the high-level flow of data within our system without referencing any specific vendors.
![Logic Diagram](https://images.edrawsoft.com/articles/data-architecture-diagram/big-data-pipeline.png)

### Solution Diagram
A solution diagram provides a more detailed representation of our system architecture, including specific vendor solutions or platforms.
It highlights the exact systems and technologies involved at each stage of data processing, offering a more concrete view of our solution landscape.
![Solution Diagram](https://www.gliffy.com/sites/gliffy/files/image/2021-03/GCParchitecturediagramexample.png)

Prior to cloud technologies taking over in the pipeline space Hadoop was the main play for orchestrating services.

## Layered Architecture
![Three layered architecture](https://th.bing.com/th/id/OIP._IXn5RXEi_KUKwCazKo6NgHaE0?rs=1&pid=ImgDetMain)

### Data Storage Layer
This layer is where all the data utilised by the system is stored, encompassing both structured and unstructured data like text, images, and video. It is commonly managed using a relational database management system (RDBMS), a NoSQL database, or a data lake.

Benefits of a storage layer:
- Scalability: Separating data storage from processing allows the system to scale more efficiently to handle larger volumes of data.
- Security: It is possible to secure the data storage layer independently, which helps mitigate the risk of unauthorised access.
- Data integrity: The data storage layer maintains data consistency and accuracy by enforcing data integrity constraints like unique keys and foreign key relationships.
  
### Data Processing Layer
This layer handles operations on the data, such as filtering, sorting, aggregation, and transformation. It typically uses data processing frameworks like Apache Spark or Apache Flink, or stream processing engines like Apache Kafka. 

Benefits of processing layer:
- Performance: By processing data in parallel, this layer can achieve high throughput and low latency.
- Flexibility: The data processing layer supports a diverse range of data processing tasks, from simple filtering to complex machine learning algorithms.
- Resilience: It provides fault tolerance and automatic recovery, helping the system handle failures smoothly and stay operational.

### Data Presentation Layer
The data presentation layer is responsible for displaying the data to end-users in a useful manner, this layer is usually implemented through a web application or business intelligence tools like Tableau or Power BI.

Benefits of data presentation layer:
- Usability: A user-friendly interface makes it straightforward for end-users to interact with the data and gain insights.
- Customisation: The presentation layer can be tailored to meet a wide array of use cases and user preferences, offering a flexible and adaptable interface.
- Integration: It can integrate with other applications and services to provide a seamless user experience, enabling users to utilise the data across different contexts.

## Microservices Architectures
In a monolithic architecture, an application is built as a single, indivisible unit, making it challenging to introduce new features, scale specific components, or maintain and update parts of the system independently. This can lead to longer development cycles, increased risk of system-wide failures, and difficulties in scaling and adapting to changing requirements.

A microservices architecture breaks down an application into small, independent services, each responsible for a specific business capability or domain. These services are loosely coupled, meaning they can be developed, deployed, and scaled independently without affecting the entire system.

You can think of a microservices architecture as a city, where each available service represents a specialised service provider (e.g., a grocery store, a hospital, a bank). Just as these service providers operate independently and specialise in their respective domains, microservices are self-contained units that focus on a specific business capability. They communicate with each other through well-defined APIs, much like how residents of a city interact with different service providers to fulfil their needs.

Benefits of microservices:
- Decentralised services - Each service is a separate codebase, managed by a small development team, allowing for faster development cycles and easier maintenance.
- Independent deployment - Services can be updated and deployed independently, without impacting the rest of the application, enabling faster bug fixes and feature releases.
- Polygot programming - Services can be written in different programming languages and technologies, allowing teams to choose the best tools for their specific needs.
- Scalability - Individual services can be scaled independently based on demand, optimising resource utilisation and improving cost-efficiency.
- Fault isolation - If one service fails, it does not bring down the entire application, ensuring better resilience and availability.
- API Gateway - The API gateway acts as a single-entry point for clients, decoupling them from the internal services and enabling cross-cutting concerns like authentication, logging, and load balancing.

## Designing Data Product Visually

## Data Products
Data products encompass a wide range of deliverables, including dashboards, reports, APIs, and data feeds. What sets data products apart is their ability to provide actionable insights, facilitate decision-making, and drive business outcomes. They are characterised by their relevance, accuracy, timeliness, and usability, making them indispensable assets for data-driven organisations.

### A good DP
- Aligns with business KPIs
- Deep understanding of pain points
- Iterative development and feedback loops

### Visualising a DP
Overview:
- Wireframes:
  - Purpose: Provide a basic structural outline of the data product, emphasising functionality over aesthetics.
  - Example: A wireframe for an HR dashboard shows the arrangement of elements and user interactions without detailed styling.
![wireframe example](https://i.pinimg.com/736x/a7/b1/c8/a7b1c89df7f1c1b5c9141bacd9b4149e.jpg)

- Mockups:
  - Purpose: Add aesthetic elements like colour schemes and fonts to wireframes, offering stakeholders a more realistic view of the final product.
  - Example: A mockup of the HR dashboard includes colour, typography, and preliminary interactive designs.
- Prototypes:
  - Purpose: Simulate user interactions with the product, instrumental in identifying usability issues before final development.
  - Use in usability testing: Central to testing user interactions and behaviours, providing insights for improvement.

*Remember to communicate with stakeholders during this design*

## Navigating data seas with architectural governance
### The Open Group Architecture Framework (TOGAF)
![TOGAF Link](https://www.opengroup.org/togaf)
1. Usage patterns - Understanding how different user groups interact with the system aids in designing user-centric architectures.
2. Data flow - Visualising how data moves through systems identifies potential bottlenecks and security risks.
3. Physical setup - Considering the physical deployment of resources impacts performance, redundancy, and disaster recovery strategies.
4. Networking - Outlining network topologies and protocols ensures efficient data transfer and compliance with security policies.

- Data Dictionaries
- Data Catalogues
- Metadata management 

## Lecure notes
UML is a broad title that covers lots of diagram types. 

Design vs architecture diagrams
Design diagrams are the abstract idea for stakeholders. Will have people in in.

Architecture diagrams are the more technical boundaries. These are strategic and don't include technical detail

To get into the detail add layers you can drill down into

Team task to draw diagram for renting a book.
(https://lucid.app/lucidchart/d261fb27-6691-4c94-b8b8-2130536f4361/edit?viewport_loc=108%2C98%2C1672%2C933%2C.Q4MUjXso07N&invitationId=inv_f0100800-6093-4eed-acd2-53e70c6711aa)

Tips for drawing diagrams:
- Version control, so you can see changes over time.
- Simplify where possible
- Create logical groupings
- Include descriptions
- Avoid too many acronyms

![Deployment architecture diagram](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screen_Shot_2022-02-16_at_12.33.28_PM.max-2600x2600.png)

Data Mesh is another architecture framework

## Topic 4 Reflections
Previously I've just made up diagrams to try and visualise processes to a user but now I have a better grasp of the best practices I will think about the type of diagram best suited for the job. 
I've learned in this module that most of my work is in the data processing layer. Knowing this will enable me to better design solutions by seperating from the other layers.
Improve how I visualise the DPs I work on for the users
Spend an hour shadowing our architects to go through diagrams
Draw a diagram for the process I'm building at work. Use this as evidence. Think about the use cases.

## Topic 4 Apply Task 1
...




