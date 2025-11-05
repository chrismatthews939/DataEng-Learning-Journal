# Topic 4 - Data visualisation and storytelling - 06/11/2025

# Principles of Effective Data Visualisation

Effective data visualisation transforms raw data into clear, meaningful insights that support decision-making. Poorly designed visuals can lead to misinterpretation, confusion, or lost insights. To create effective visualisations, designers must focus on clarity, accuracy, accessibility, and engagement (Few, 2012).

![Chart types](https://www.datocms-assets.com/42764/1664970413-chart-selection-diagram.png)

# Key Principles of Data Visualisation

## Choosing the Right Chart Type
- **Line charts** show trends over time.  
- **Bar charts** compare categories.  
- **Scatter plots** display relationships between variables.  
- **Heatmaps** reveal patterns in large datasets (Cairo, 2013).

**Example:**  
A retail business comparing monthly sales across different stores should use a **bar chart** for easy comparison rather than a table of numbers.

---

## Use of Colour and Contrast
- Use colour strategically to highlight important trends.  
- Avoid using too many colours, which can cause confusion (Tufte, 2001).  
- Ensure sufficient contrast for accessibility, particularly for colour-blind users.

**Example:**  
A climate change dashboard might use a **gradient colour scale** to show temperature changes over time, making patterns easier to spot.

---

## Accessibility and Inclusivity
- Ensure text is legible and font sizes are appropriate.  
- Use alternative text and tooltips for screen reader users.  
- Follow **Web Content Accessibility Guidelines (WCAG)** for designing accessible charts (Reis & Housley, 2022).

**Example:**  
A government agency’s unemployment report should use **high-contrast colour schemes** and provide **alternative text descriptions** to ensure accessibility for all users.

---

## Simplicity and Clarity
- Avoid unnecessary complexity by reducing clutter (Few, 2012).  
- Use clear labels, legends, and annotations to guide interpretation.  
- Remove *chartjunk* (e.g., excessive colours, 3D effects) that distracts from key insights.

**Example:**  
A financial dashboard displaying profit trends over time should use a **simple line chart** rather than an overcrowded **3D pie chart** that may distort proportions (McCandless, 2019).

---

# Example Visualisations

The **Data Visualisation Catalogue** is a comprehensive resource that showcases a wide array of data visualisation techniques, each tailored to represent specific data insights effectively. Below are examples of various visualisation types, along with their typical use cases:

---

## Arc Diagram

**Description:**  
Displays relationships between entities using arcs, useful for visualising patterns in data sequences.

**Example:**  
Visualising repeated motifs in a DNA sequence.

> A diagram showing three nodes connected by a horizontal line at the bottom, labeled *"Nodes."*  
> Two green arcs above the line, labeled *"Arc-Links,"* connect the nodes.  
> The first arc connects the first and second node, while the second larger arc connects the first and third node.  
> *Diagram illustrating nodes and arc-links in a network.*

---

## Area Graph

**Description:**  
Depicts quantitative data graphically, with the area between the axis and the line filled in, illustrating volume.

**Example:**  
Showing the cumulative sales over a year.  
[datavizcatalogue.com](https://datavizcatalogue.com)

> A graph with the x-axis labeled *"Intervals"* ranging from 0 to 6 and the y-axis labeled *"Value Scale"* ranging from 0 to 6.  
> Points plotted on the graph are marked with an *X* at coordinates (2,1), (4,2), (3,3), (6,4), (5,5), and (2,6).  
> The shaded area is under the line connecting these points.  
> *Graph showing shaded area under a line connecting plotted points.*

---

## Bar Chart

**Description:**  
Uses rectangular bars to represent data values, ideal for comparing different categories.

**Example:**  
Comparing the population of different cities.

> A horizontal bar chart with two categories, *Category A* and *Category B.*  
> Category A has a value of 6, and Category B has a value of 3.5.  
> The x-axis is labeled *"Scale"* and ranges from 0 to 6.  
> Text in the image indicates *"Bar length = value amount."*  
> *Horizontal bar chart comparing values of Category A and Category B.*

---

## Box & Whisker Plot

**Description:**  
Summarises data by displaying its distribution through quartiles, highlighting the median and potential outliers.

**Example:**  
Analysing test scores to understand the spread and identify any anomalies.

---

## Bubble Chart

**Description:**  
Similar to a scatter plot but with an added dimension of data represented by the size of the bubbles.

**Example:**  
Visualising the correlation between advertising spend, sales, and market share.

> A scatter plot with circles of varying sizes positioned on a coordinate plane.  
> The x-axis is labeled *"Variable B"* and the y-axis is labeled *"Variable A."*  
> Circles are color-coded with labels: *Label 1 (red), Label 2 (orange), and Label 3 (yellow).*  
> Each circle's area corresponds to *"Variable C."*  
> Below the scatter plot, there are two mathematical formulas:  
> `Circle Area = π × Radius²`  
> `Circle Diameter = (sqrt(Area / π)) × 2`  
> *Scatter plot illustrating relationships between three variables.*

---

## Chord Diagram

**Description:**  
Illustrates relationships between different entities in a circular layout, showing inter-connections.

**Example:**  
Displaying trade flows between countries.

---

## Choropleth Map

**Description:**  
A map where areas are shaded in proportion to a statistical variable, useful for geographic data representation.

**Example:**  
Mapping population density across regions.

> A map divided into different regions, each shaded in varying colors of yellow, orange, and brown.  
> Below the map is a value legend labeled *"Magnitude,"* indicating that the colors represent different magnitudes, ranging from light yellow (lowest magnitude) to dark brown (highest magnitude).  
> One of the regions on the map is labeled.  
> *A choropleth map showing regions shaded by magnitude.*

---

## Heatmap

**Description:**  
Represents data values through variations in colouring, useful for identifying patterns and correlations.

**Example:**  
Displaying user activity on a website over time.

> Comparison of heatmaps using numerical and categorical data.

---

## Network Diagram

**Description:**  
Shows how different entities are interconnected, ideal for illustrating complex networks.

**Example:**  
Mapping social media interactions among users.

> A diagram of a network with nodes and links.  
> The top part shows a central node connected to four other nodes via links.  
> Below this, there are two smaller diagrams: one labeled *"Undirected network"* showing nodes connected by lines without arrows, and another labeled *"Directed network"* showing nodes connected by lines with arrows indicating direction.  
> *Diagram illustrating different types of network connections.*

---

## Treemap

**Description:**  
Displays hierarchical data using nested rectangles, with area size representing a quantitative variable.

**Example:**  
Visualising the composition of a company's revenue streams.

---

# Creating Interactive Visualisations and Dashboards

Interactive visualisations allow users to engage with data dynamically, filtering, drilling down, and customising views to extract meaningful insights. Unlike static charts, interactive dashboards provide real-time updates, user-driven exploration, and multiple perspectives, making data more accessible, actionable, and engaging (Cairo, 2013).

# Key Features of Interactive Visualisations

Interactive visualisations are powerful tools that enhance data exploration and decision-making. By allowing users to dynamically filter, drill down, and customise views, these visualisations transform static data into actionable insights.

This section explores key features that make interactive visualisations effective, including filtering capabilities, real-time updates, interactive elements, and customisable dashboards.

---

## 🧩 Key Features of Interactive Dashboards

### 1. Filtering and Drill-Down Capabilities
Users can filter data based on parameters such as time range, categories, or geographical regions (Few, 2012).  
Drill-down features allow users to click on data points to reveal more granular insights.

**Example:**
> A sales dashboard allows managers to filter sales performance by region, product category, and time period, helping them pinpoint underperforming areas.

---

### 2. Real-Time Data Updates
Dashboards can pull live data from databases and APIs, ensuring the latest information is always displayed.  
Useful for financial trading, logistics tracking, and web analytics (Davenport, 2020).

**Example:**
> A retail stock dashboard shows real-time inventory levels, automatically updating when new stock arrives or products are sold.

---

### 3. Interactive Charts and Dynamic Elements
Users can hover over charts to see tooltips with additional context.  
Clickable elements allow for side-by-side comparisons and alternative views (Reis & Housley, 2022).

**Example:**
> A COVID-19 tracking dashboard provides interactive charts where users can click on different countries to view infection trends and vaccination rates.

---

### 4. Customisable Dashboards
Users can personalise dashboards by selecting metrics, chart types, and layouts that suit their needs.  
Ensures that different stakeholders see only the data relevant to their role (Kimball & Ross, 2013).

**Example:**
> A marketing analytics dashboard allows teams to customise views for social media performance, ad spend, and customer engagement metrics.

---

## 🛠️ Tools and Technologies for Interactive Data Visualisation

To create effective interactive visualisations, it's essential to leverage the right tools and technologies. This section highlights some of the most popular and powerful tools available for building dynamic and engaging data visualisations.

| Tool | Key Features | Use Case |
|------|---------------|----------|
| **Tableau** | Drag-and-drop interface, real-time dashboards, integrations with databases | Business intelligence, analytics reporting |
| **Power BI** | Microsoft ecosystem integration, AI-powered analytics, interactive dashboards | Finance, sales reporting, enterprise analytics |
| **D3.js** | Customisable JavaScript visualisations, advanced interactivity | Web-based data visualisation, interactive storytelling |
| **Google Data Studio** | Free, cloud-based dashboards, seamless Google Analytics integration | Marketing performance tracking, web analytics |
| **Plotly (Dash)** | Python-based interactive graphs, API integration | Scientific data visualisation, IoT dashboards |

---

## 💡 Example Scenario: Building an Interactive Customer Insights Dashboard

An e-commerce company wants to create an interactive dashboard that provides insights into customer behaviour, sales trends, and product performance.

Previously, sales reports were shared as static PDFs, making it difficult to explore data dynamically.

---

### 🔍 Challenges Identified

| Challenge | Issue |
|------------|-------|
| Static reports lack interactivity | Users cannot filter data or view insights in real-time |
| No ability to drill down into specific metrics | Requires manual analysis of spreadsheets |
| Delayed reporting | Decisions are made based on outdated data |

---

### ✅ Implemented Solutions

1. **Tableau-powered interactive dashboard** for real-time exploration of sales and customer data.  
2. **Filters** for product categories, time periods, and customer segments, allowing deeper analysis.  
3. **Dynamic charts and tooltips**, providing quick insights when hovering over data points.  
4. **Automated daily data updates**, ensuring the dashboard always reflects the latest trends.

---

### 📈 The Outcome

| Metric | Before Implementation | After Implementation | Target | Status |
|--------|-----------------------|----------------------|---------|---------|
| Time to generate reports | 4 hours | Instantly updated | Real-time | ✅ Achieved |
| User engagement with data | 30% | 85% | Above 80% | ✅ Achieved |
| Accuracy of business decisions | 65% | 92% | Above 90% | ✅ Achieved |

---

By adopting **interactive visualisations**, the company improved **data accessibility**, **efficiency**, and **decision-making**, enabling teams to explore insights in real time rather than relying on static reports.

---

# Tools and Technologies for Data Visualisation

Data visualisation tools help transform complex datasets into clear, interactive, and meaningful insights. Different tools offer varying levels of customisability, automation, and interactivity, making them suitable for different use cases. The choice of tool depends on business needs, technical expertise, and data complexity (Cairo, 2013).

# Comparison of Popular Data Visualisation Tools

Choosing the right data visualisation tool is crucial for effectively transforming data into actionable insights.  
This section compares some of the most popular tools available, highlighting their key features and best use cases.  
Whether you need business intelligence, web-based custom visualisations, or scientific data analysis, understanding the strengths of each tool will help you make an informed decision.

---

## Overview Table

| **Tool**            | **Key Features**                                                                 | **Best For**                                          |
|----------------------|----------------------------------------------------------------------------------|--------------------------------------------------------|
| **Tableau**          | Drag-and-drop interface, real-time dashboards, AI-powered insights              | Business intelligence, analytics reporting             |
| **Power BI**         | Microsoft ecosystem integration, machine learning analytics, cloud-based sharing | Enterprise analytics, finance, sales reporting         |
| **D3.js**            | JavaScript-based custom visualisations, advanced interactivity                  | Web-based applications, interactive storytelling       |
| **Google Data Studio** | Free, cloud-based, Google Analytics integration                               | Marketing performance tracking, web analytics          |
| **Plotly (Dash)**    | Python-based, interactive graphs, API integration                               | Scientific research, IoT dashboards                    |

---

## 1. Tableau – Business Intelligence and Interactive Dashboards

- Drag-and-drop interface makes it easy for non-technical users to create dashboards.  
- Real-time data updates allow for live decision-making.  
- AI-driven analytics suggest insights based on data trends *(Few, 2012)*.

**Example:**  
A UK healthcare provider uses Tableau to visualise hospital admission rates, patient demographics, and waiting times, enabling NHS managers to optimise resources.

---

## 2. Power BI – Enterprise Analytics and Cloud Reporting

- Seamless integration with Microsoft tools (Excel, Azure, SharePoint).  
- AI-powered analytics provide predictive insights and automated reporting.  
- Cloud-based sharing enables collaboration across teams *(Davenport, 2020)*.

**Example:**  
A financial services firm uses Power BI to track real-time trading activity, compliance reporting, and risk assessments across global markets.

> *Image source:* [learn.microsoft.com](https://learn.microsoft.com)

---

## 3. D3.js – Custom Visualisations for Web Applications

- JavaScript library that allows developers to create unique and interactive data visualisations.  
- Highly flexible, making it ideal for complex, custom dashboards.  
- Requires coding knowledge but provides full creative control *(Reis & Housley, 2022)*.

**Example:**  
A news organisation uses D3.js to build an interactive election results map, showing live updates of votes across UK regions.

---

## 4. Google Data Studio – Free Cloud-Based Data Visualisation

- Integrates with Google Analytics, Ads, and BigQuery for real-time marketing data.  
- Customisable reports allow teams to track KPIs dynamically.  
- Free to use, making it ideal for startups and SMEs *(Cairo, 2013)*.

**Example:**  
A digital marketing agency uses Google Data Studio to track website traffic, ad performance, and user engagement metrics for its clients.

---

## 5. Plotly (Dash) – Python-Based Visualisation for Data Science

- Python-powered interactive visualisations used in scientific and business applications.  
- Supports real-time data streaming and dashboards.  
- Integrates with machine learning and IoT platforms *(Few, 2012)*.

**Example:**  
A climate research team uses Plotly to create interactive dashboards displaying live temperature and pollution levels across different regions.

---

## Example Scenario: Choosing the Right Tool for a UK Retail Business

A UK-based retail company wants to implement a dashboard for tracking sales performance, customer demographics, and marketing effectiveness.

### Challenges Identified

| **Challenge**                     | **Requirement**                          | **Best Tool**                  |
|----------------------------------|------------------------------------------|--------------------------------|
| Need for real-time data updates  | Live insights on sales performance       | Power BI, Tableau              |
| Interactive customer analytics   | Filter data by region, product category, customer type | Tableau, Google Data Studio    |
| Custom visualisation for website analytics | Need for embedded web-based graphs       | D3.js                          |

---

### Implemented Solutions

1. **Power BI** for internal reporting and real-time sales monitoring.  
2. **Google Data Studio** for marketing analytics, tracking online ad performance.  
3. **D3.js-based visualisation** embedded on the company’s website to show live customer trends.

---

### The Outcome

| **Metric**                      | **Before Implementation** | **After Implementation** | **Target**         | **Status**  |
|----------------------------------|---------------------------|---------------------------|--------------------|--------------|
| Time spent on generating reports | 3 hours                   | 10 minutes                | Under 30 minutes   | ✅ Achieved  |
| Stakeholder engagement with insights | 50%                      | 90%                       | Above 85%          | ✅ Achieved  |
| Customer trend analysis speed    | Slow                      | Real-time                 | Instant updates    | ✅ Achieved  |

---

By selecting the right tools for different use cases, the company improved decision-making, marketing efficiency, and operational reporting.

---

# Crafting Compelling Narratives using Data

Data storytelling combines data, narrative, and visuals to communicate insights effectively. While data provides the facts and evidence, the narrative gives it context and meaning, helping audiences understand and engage with insights. A well-crafted data story can drive better decision-making, highlight trends, and persuade stakeholders (Davenport, 2020).

# Key Elements of Data Storytelling

Crafting a compelling data story involves more than just presenting numbers; it requires a thoughtful approach to ensure the insights are clear, engaging, and actionable. 

This section outlines the key elements of effective data storytelling, including **understanding your audience**, **establishing a clear narrative structure**, **choosing the right visualisations**, and **highlighting key takeaways**. By mastering these elements, you can transform raw data into powerful stories that drive informed decisions.

---

## 📊 The Key Elements of Data Storytelling

1. Understanding the audience  
2. Establishing a clear narrative structure  
3. Choosing the right visualisations for storytelling  
4. Highlighting key takeaways and insights  

---

## 🎯 Understanding the Audience

Tailor the message to the knowledge level of your audience.

- Consider whether the audience is **technical** (e.g., data analysts) or **non-technical** (e.g., executives, customers) (Cairo, 2013).  
- Focus on insights that matter to the audience’s goals and challenges.

**Example:**  
> A financial analyst preparing a quarterly business report would highlight profit trends and market risks rather than raw financial data.

---

## 🧩 Establishing a Clear Narrative Structure

A compelling data story follows a structure similar to traditional storytelling:

1. **Setup (Context):** Introduce the problem or question.  
2. **Conflict (Insights & Evidence):** Present key data points that highlight patterns or challenges.  
3. **Resolution (Action & Conclusion):** Provide recommendations or next steps based on the insights (Few, 2012).

**Example:**  
> A retail business report might present declining customer retention rates, analyse possible causes, and recommend personalised marketing strategies to improve loyalty.

---

## 📈 Choosing the Right Visualisations for Storytelling

- Use **line charts** for trends over time.  
- Use **bar charts** for category comparisons.  
- Use **heatmaps** to highlight patterns and anomalies (Tufte, 2001).  
- Ensure that charts are **clear, labelled, and easy to interpret**.

**Example:**  
> A marketing manager presents social media engagement trends over six months using a line chart, making it easy to see fluctuations.

---

## 💡 Highlighting Key Takeaways and Insights

- Use **annotations, headlines, and summaries** to draw attention to critical findings.  
- Avoid presenting too much data — focus on what matters most (Reis & Housley, 2022).  
- Provide **actionable recommendations** based on insights.

**Example:**  
> A data dashboard for sales performance includes headline metrics like  
> “Revenue increased by 15% last quarter,” making key takeaways immediately clear.

---

# 🛒 Example Scenario: Telling a Data Story for an E-Commerce Business

A **UK-based e-commerce company** wants to understand why customer retention has dropped.  
The **data analytics team** is tasked with creating a story-driven report to present to executives.

---

## 🔍 Challenges Identified

| **Challenge** | **Data Insights** |
|----------------|-------------------|
| Customer churn has increased | 20% of repeat customers stopped purchasing |
| Drop in engagement with marketing emails | Open rates fell by 30% |
| Customer satisfaction scores declining | Negative feedback mentions high delivery times |

---

## 🧠 Data Story Framework

1. **Setup (Context):**  
   “Our customer retention rate has declined by 20% in the past six months, which could impact long-term revenue.”

2. **Conflict (Insights & Evidence):**  
   “Email engagement has dropped by 30%, and 40% of negative customer reviews mention slow delivery.”

3. **Resolution (Action & Conclusion):**  
   “To address this, we recommend optimising delivery times and personalising email marketing to re-engage customers.”

---

## 📊 The Outcome

| **Metric** | **Before Storytelling Approach** | **After Implementing Insights** | **Target** | **Status** |
|-------------|----------------------------------|----------------------------------|-------------|-------------|
| Customer churn rate | 20% | 12% | Below 15% | ✅ Achieved |
| Email open rates | 30% drop | 10% increase | Above previous levels | ✅ Achieved |
| Customer satisfaction | 3.5/5 | 4.2/5 | Above 4.0 | ✅ Achieved |

---

By presenting insights in a **narrative format**, the business could understand the root cause of retention issues and take targeted action to improve customer experience.

---

# Presenting Data Insights to Non-Technical Audiences

Non-technical audiences, such as executives, marketers, and policy-makers, may not have the expertise to interpret raw data or statistical models. Effective data communication ensures that insights are clear, engaging, and actionable, without oversimplifying the meaning behind the data. This requires choosing the right visualisations, simplifying jargon, and focusing on key takeaways (Few, 2012).

# Key Strategies for Presenting Data to Non-Technical Audiences

Presenting data effectively to non-technical audiences requires clarity, simplicity, and storytelling. Below are key strategies to make your data actionable and understandable.

---

## 1. Focus on Key Takeaways
- Avoid overwhelming the audience with too much data or unnecessary details.
- Highlight only the most relevant insights that support decision-making.
- Use headlines, summary points, and call-to-actions to guide interpretation.

**Example:**

> Instead of presenting a complex spreadsheet, a financial report should highlight:  
> **"Profits increased by 12% this quarter, driven by a 20% rise in online sales."**

---

## 2. Use Storytelling Techniques
- Frame data insights as a story with a beginning (problem), middle (insights), and end (solution).
- Use real-world examples and analogies to make data relatable.
- Add context to numbers—e.g., "20% growth in sales" is more meaningful if compared to industry benchmarks (Cairo, 2013).

**Example:**

> Instead of stating "Customer churn rate is 15%", present:  
> **"One in six customers left our service last quarter. The main reason cited was slow response times from customer support."**

---

## 3. Choose the Right Data Visualisations
- Use bar charts, pie charts, and heatmaps for comparisons.
- Use line charts for trends over time.
- Avoid technical graphs like boxplots unless necessary (Tufte, 2001).

**Example:**

> Instead of presenting a raw dataset of customer engagement metrics, a social media manager could use a bar chart showing engagement levels per platform (Facebook, Instagram, LinkedIn).

**Recommended Visualisations for Non-Technical Audiences:**

| Data Type                          | Best Visualisation          |
|-----------------------------------|----------------------------|
| Sales performance over time        | Line chart                 |
| Market share distribution          | Pie chart                  |
| Regional variations in customer activity | Heatmap               |
| Comparing revenue by product category   | Bar chart               |

---

## 4. Eliminate Jargon and Simplify Explanations
- Replace technical terms with plain language.
- Explain complex calculations in simple, digestible steps.
- Provide real-life comparisons (Davenport, 2020).

**Example:**

> Instead of saying "Our AI model predicts churn probability with an RMSE of 0.23," say:  
> **"Our AI model predicts customer churn with 90% accuracy."**

---

## 5. Example Scenario: Presenting Customer Insights to a Retail Leadership Team

**Context:**  
A UK-based retail chain wants to understand why foot traffic in stores has declined. The data team must present findings to executives who are not data specialists.

### Challenges Identified

| Challenge                          | Data Insights                                           |
|-----------------------------------|--------------------------------------------------------|
| Executives do not have time to review detailed reports | Use a one-page summary with key findings             |
| Data is too complex                | Convert findings into simple charts and key takeaways |
| Decision-makers need actionable insights | Provide clear recommendations                       |

### Data Presentation Framework

1. **Problem (Setup)**  
   > "Over the past six months, foot traffic in stores has declined by 18%."

2. **Insights (Conflict)**  
   - Customer surveys show that 60% prefer online shopping due to convenience.  
   - Heatmap analysis of store locations reveals that areas with increased online ads had 12% more store visits.

3. **Action (Resolution)**  
   - Expand targeted online campaigns to drive foot traffic.  
   - Offer exclusive in-store discounts to encourage visits.

### The Outcome

| Metric                           | Before Implementation | After Implementation | Target       | Status   |
|---------------------------------|--------------------|--------------------|-------------|---------|
| Foot traffic decline             | 18%                | 5%                  | Below 8%     | Achieved |
| Store revenue impact             | -10%               | +7%                 | Positive growth | Achieved |
| Engagement with targeted online ads | 50%             | 85%                 | Above 80%    | Achieved |

> By simplifying data insights into a structured narrative, the leadership team was able to make data-driven decisions without needing technical expertise.

---


