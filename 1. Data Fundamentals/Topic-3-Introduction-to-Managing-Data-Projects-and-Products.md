# Topic 3 - Introduction to Managing Data Projects and Products - 10/10/2024

## Objectives
- List the limitations of the Waterfall model in the context of data science projects
- Explain how Agile principles and frameworks can foster adaptability and collaboration
- Identify which Lean and SixSigma practices can drive continuous improvement
- Evaluate approaches to collaborating with diverse stakeholders in a way that aligns data-driven initiatives with business objectives
- Argue how a data-driven culture can be championed within your organisation by leveraging the synergies between Agile, Lean and SixSigma approaches

## Key Concepts

Most popular methodologies are Waterfall and Agile.

### Agile
More modern approach. Work in sprints. Best when trends change fast. Spotify is a good example because music trends change fast.

Stages:
- Plan
- Design
- Launch
- Develop
- Test
- Deploy
- Review

Benefits of Agile:
- Nible approach
- Flexible and adaptable
- Great for volitile environments
  
Drawbacks of Agile:
- Demands constant communication
- Costs are unpredicable 

### Waterfall
More traditional linear approach. Best for when requirements are very clear and non flexible. Think of NASA they can't afford to change things the goal is very clear.

Stages:
- Plan
- Design
- Build
- Test
- Maintain

Benefits of Waterfall:
- Predicable
- Easier to manage
  
Drawbacks of Waterfall:
- Lacks the flexibility to repond to changes
- Not ideal for fast moving markets

Key Message:
There's no one-size-fits-all in software development methodologies. Agile is for maximising the business value, especially the value for users. Waterfall is for optimising the balance of constraints, that is, the management of scope, time, and cost constraints in a project. 

Two very different approaches for two very different uses. Applying one for every type of project simply doesn’t work.

Example Failure of Waterfall:
A notable example of Waterfall failing is the NHS IT project in 2002. Despite being planned using Waterfall and gathering requirements the project overran and even with a budget of 6mil it cost over 12bil and many objectives not achieved. The NHS was too compicated for a Waterfall model. Often large scale software projects don't do well with this approach.

The Waterfall model proved to be unsuitable for the NPfIT project due to inadequate understanding of user needs and changing requirements over time. Doctors lacked trust as they were not involved in feedback loops, while admin users resisted centralised decision-making.

How Agile could have helped:
Agile could have improved end user engagement, phased change management, and project scalability by breaking down the NPfIT mega-project into agile sub-projects.
Agile's flexibility and iterative approach would have allowed for ongoing adjustments based on feedback and evolving requirements, making it more suitable for the scenario.

Specific limitiation of Waterfall in Data Science:
- Difficulty accomodating change. When working on data projects, we often learn from the data, especially when exploring unstructured data. This means that our business and user requirements may change over time.
- Lengthy development cycles. The sequential nature of Waterfall can result in lengthy development cycles, failing to keep pace with rapidly changing market conditions and user needs.
- Lack of stakeholder feedback. The Waterfall model limits the ability to obtain timely feedback from stakeholders and end-users, increasing the risk of delivering a solution that no longer meets their needs.
- Challenges with data complexity. Data engineering projects, with their complex data sources and quality issues, pose challenges that the Waterfall model struggles to address due to its lack of flexibility and space for experimentation, limiting opportunities for learning and optimisation.

## Embracing Agile principles for data engineering

- Faster iteration
- Feedback loops
- Enhanced collaboration
- Responsivness to change
- Flexible planning

Two framworks in Agile. Scrum and Kanban

### Scrum
Scrum, a widely adopted Agile framework, emphasises efficient collaboration and streamlined workflows through specific roles and ceremonies. 

### Kanban
Kanban, a methodology emphasising visualising work and limiting work in progress (WIP), is particularly beneficial in environments focusing on bug fixes and testing.

## Navigating roles and responsibilities in Agile Scrum

### Scrum Roles:
- Scrum master
  - The scrum master serves as a guardian of Agile principles, ensuring that the team adheres to the Scrum framework and removing any impediments that hinder progress. 
- Product Owner
  - Representing the voice of the customer, the product owner holds the responsibility of prioritising tasks and features based on business requirements and stakeholder needs. 
- Team Members
  - Comprising data scientists, engineers, and analysts, the team members collectively bring diverse skill sets and expertise to the project. 

### Scrum Ceremonies:
- Stand up
- Sprint review
- Sprint retrospective
- Sprint planning

## Applying Lean and Six Sigma principles
In the world of process improvement methodologies, Lean and Six Sigma stand out as two prominent approaches, each with its own unique focus and principles. While Lean emphasises waste reduction and process optimisation, Six Sigma targets quality improvement.

### Lean Approach
Lean is a continuous improvement methodology focused on eliminating waste and optimising processes. 

Following Lean principles can help to: 
- Identify and address data quality issues, such as missing values, outliers, or inconsistencies
- Streamline data collection, pre-processing, and transformation workflows to improve efficiency
- Avoid running resources that are not being efficiently utilised
- Prevent data pipelines from being used for unnecessary tasks

### Six Sigma Approach
Six Sigma, on the other hand, is a data-driven approach aimed at improving quality by reducing variability and defects. 

Apply Six Sigma can help to:
- Continuously monitor and optimise data pipelines and analytical models to maintain high performance
- Establish rigorous testing and validation procedures to ensure the accuracy and reliability of data-driven insights
- Implement statistical process control techniques to identify and address root causes of data quality issues

Many organisations have found success in combining Lean and Six Sigma methodologies, known as Lean Six Sigma. This hybrid approach leverages the strengths of both frameworks, creating a powerful tool for driving continuous improvement and delivering high-quality, data-driven solutions.

Key Point
Applying Lean and Six Sigma is data engineering. 

Lean methodologies encourage the elimination of non-value-adding activities and focus on streamlining processes. In the context of identifying data sources and understanding data processing concepts and methods, Lean can facilitate quicker and more efficient decision-making regarding which data sources to prioritise and which data processing methods are most efficient for the task at hand. 

Six Sigma adds to this by using data-driven techniques to identify variances in data quality and processing efficiency, allowing for a more precise selection of data sources and methodologies.

Example Applying Six Sigma to a real problem:
A financial services firm uses customer transaction data to detect fraudulent activity. The data, however, is riddled with inaccuracies and inconsistencies, leading to a high rate of false positives and negatives in fraud detection. The firm applies the Define, Measure, Analyse, Improve, and Control (DMAIC) process of Six Sigma to the data cleansing process. 

1. Define: The objective is clearly defined as reducing inaccuracies in transaction data
2. Measure: Current error rates are measured
3. Analyse: The root causes of data inaccuracies are identified (e.g., incorrect data entry, outdated information)
4. Improve: Solutions are implemented, such as automated data validation checks and regular data quality audits
5. Control: New standards and controls are established to maintain the improved data quality level
6. Benefit: The structured approach leads to significantly reduced inaccuracies, enhancing the effectiveness of fraud detection algorithms. This results in reduced operational losses and improved customer trust

### 5 Whys
In Lean Six Sigma, the 5 Whys methodology serves as a powerful tool for root cause analysis. This is a very simple technique to get you started. The basic concept is to ask “why?” five times to dig deep into the root of a problem. The logic behind it is that in the first few questions you will find one of the causes of the problem, and by the 5th question you will see the process failure behind that problem. 

## Effective stakeholder engagement
Methods:
- Capturing requirements with user stories
- Effective communication channels
- Gathering insights through interviews and observations
- Collaborative workshops and personas
- Aligning technical specifications

![power-interest stakeholder management grid](https://www.google.com/search?sca_esv=97958ac28674b0c2&q=power-interest+stakeholder+management+grid&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2jon2iao6KWCaVjfn7ahz_sf9q37Zv4dbJ4TW_6SnErfFZ77vWA-JewUZjVu3roP919JJ7LB0XgUlbeu3TIUlWj0Hp1JHzwq5YPaSgTTkAC-edWrnsX-_paLirvXRRRiouDZnf1O&sa=X&ved=2ahUKEwjov87lz4OJAxWQTkEAHY2XMOMQtKgLegQIExAB&biw=1440&bih=799&dpr=1.5#vhid=asTO3F6TAVz61M&vssid=mosaic)

## Lecure notes
Agile elements
- Sprint planning. Plan the work for next few weeks based on priorities
- Planning poker. Fair assessment of amount of work per task. Group choose a amount and then discuss if they disagree
- Backlog grooming/refinement. Go through backlog
- Sprint Review. Demo to users
- Sprint retro. How did sprint go
- Burndown charts. How close to planning did you deliver
- Definition of done. Define what needs to be done to perfect quality

User story checklist:
- Keep them short
- Keep them simple
- Write from perspective of the user
- Make the value of the story clear
- Describe the functionality
- Write for team to understand
- Add acceptence criteria

## Topic 3 Reflections
Learning about different approaches I can understand why we use Agile in BT. Both the business strategy and stakeholder demand on specific projects is fast changing and Agile helps us readjust to continue delivering at pace.

I have a project that's in the early stages and I'll use the power interest stakeholder management grid to map the various stakeholder groups then focusing engagement efforts on high-power, high-interest stakeholders. I'll also implement more forumns and workshops.

Think about how we structure our stories and epics because I think it's slightly different to the definitions set in the course

## Topic 3 Apply Task 1
topic3_apply_task1.xlsx in this repo

## Topic 3 Apply Task 2
topic3_apply_task2.xlsx in this repo

## Topic 3 Apply Task 3
I've incorporated this into my Reflctions for Topic 3

