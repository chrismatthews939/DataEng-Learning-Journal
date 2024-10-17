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

Benefits 

## Lecure notes


## Topic 4 Reflections
Previously I've just made up diagrams to try and visualise processes to a user but now I have a better grasp of the best practices I will think about the type of diagram best suited for the job. 
I've learned in this module that most of my work is in the data processing layer. Knowing this will enable me to better design solutions by seperating from the other layers.

## Topic 4 Apply Task 1
...




