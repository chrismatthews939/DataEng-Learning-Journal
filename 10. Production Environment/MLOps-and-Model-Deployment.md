# MLOps and Model Deployment 18/09/2025

# What is MLOps? A practical introduction

Machine Learning Operations - or MLOps - is the discipline that manages the full lifecycle of machine learning models in production. If machine learning models are the engines of intelligent systems, then MLOps is everything that ensures they’re built, tested, deployed, monitored, updated, and governed properly - not just once, but continuously.

1. Version control for data, code, and models
2. Automated testing and deployment pipelines
3. Monitoring for model performance and data drift
4. Collaboration between data science, engineering, and operations

## Understanding MLOPs

To understand MLOps, it helps to know where it came from:

- **DevOps** was created to bridge the gap between software development and IT operations. It introduced CI/CD pipelines, automated testing, and infrastructure as code - all to make software delivery faster and more reliable.
- **DataOps** emerged to solve problems in data pipeline development - improving the quality, governance, and delivery of data for analytics.

But machine learning systems are different. They combine:

- **Software code** (model logic and application code)
- **Training data** (which changes over time)
- **Model artifacts** (which need packaging and serving)
- **Runtime infrastructure** (which must scale reliably)

This makes ML systems more fragile and unpredictable than traditional software.

---

## The building blocks of MLOps

MLOps isn’t a single tool or process. It’s a collection of practices and components that work together. These typically include:

1. **Model Tracking:** Logging every model version, training dataset, configuration, and performance metric.
2. **Model Registry:** A central system for storing and managing model artifacts, often linked to Git and data sources.
3. **CI/CD Pipelines:** Automation for training, testing, and deploying models - reducing manual errors and speeding up delivery.
4. **Monitoring and Observability:** Real-time visibility into how a model is performing in production: accuracy, latency, and data drift.
5. **Collaboration and Handover:** Clear ownership and documentation between data science and engineering teams, avoiding the "throw-it-over-the-wall" problem.

### Without MLOps, organisations often encounter:

- **Unreliable models** that break in production environments
- **Inconsistent environments** between dev and prod
- **No rollback plan** if a model starts underperforming
- **Lack of auditability**, making it hard to explain decisions to regulators or business leaders

### MLOps solves this by:

- **Enforcing reproducibility:** Same model, same data, same results.
- **Enabling continuous improvement:** Automate retraining and redeployment.
- **Ensuring compliance and governance:** Track every decision and configuration.
- **Supporting real-world reliability:** Models that don’t just work, but keep working.

---

## MLOps vs Traditional ML

| **Area**          | **Traditional ML Workflow** | **MLOps Approach**                      |
|--------------------|-----------------------------|------------------------------------------|
| Model development | Manual experimentation      | Version-controlled, tracked              |
| Deployment        | Manual, ad-hoc              | Automated CI/CD pipelines                |
| Monitoring        | Often ignored               | Active monitoring + alerting             |
| Collaboration     | Siloed teams                | Cross-functional integration             |
| Model updates     | Rare, painful               | Continuous retraining + rollback         |

---

# Automating the machine learning lifecycle

![CI/CD](https://substackcdn.com/image/fetch/$s_!dgbK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f968b06-e00e-4e5e-8c8e-17150bea1054_3777x2859.png)

## Model Registry 

A model registry acts as a central hub where machine learning models are versioned, stored, and managed. It brings structure and control to model lifecycle management by clearly documenting which versions of a model are approved for production, which are under review, and which have been deprecated. Imagine a model registry as a digital warehouse. Each model stored inside has a label describing how it was trained, what data it used, and whether it's ready for deployment. When something goes wrong in production, engineers can quickly check the registry, identify the active version, and - if needed - roll back to a previous version that’s known to be stable. The registry becomes especially powerful in collaborative environments. It allows data scientists, ML engineers, and platform teams to share responsibility for models while maintaining visibility and control over their use.

## Tools that support automation: MLflow and Kubeflow

Two popular tools that help bring automation to the ML lifecycle are **MLflow** and **Kubeflow**. MLflow is lightweight and easy to integrate into Python-based workflows, making it a popular choice for small to mid-sized teams. It provides experiment tracking, model packaging, and registry features in a modular setup that works well across different environments. Kubeflow, on the other hand, is built for teams already using Kubernetes. It allows for scalable, production-grade machine learning workflows and supports complex orchestration of tasks like distributed training, hyperparameter tuning, and multi-step pipelines. It’s more infrastructure-heavy but offers excellent flexibility for organisations operating in cloud-native environments.

---

# Deploying machine learning models

`
“A model in a notebook is just an idea. A model in production is a product.”`

Before a model can be deployed, it must be prepared to run outside its original development environment. This process, called **packaging**, makes sure the model can operate reliably on different machines and platforms. Packaging might mean exporting the model into a standard format such as **ONNX** or **TensorFlow SavedModel**. For more complex systems, it often involves placing the model inside a container - for example, with **Docker** - along with all its dependencies. Benefits of containerisation include:

- Consistency between development, testing, and production environments
- Portability across cloud providers and local servers
- Isolation from other system processes, reducing conflicts

---

## Deployment strategies

Choosing how to deploy a model depends on the use case, performance needs, and update frequency. Some common strategies include:

- **Embedded deployment** – the model is shipped within an application, ideal for offline or mobile environments.
- **Model-as-a-Service** – the model is hosted remotely and accessed through an API, allowing frequent updates without changing the application itself.
- **Blue-green deployments – two identical environments are maintained; one is live, one is idle. New models are deployed to the idle environment and swapped in only when validated.
- **Canary releases** – a new model is given to a small percentage of users first, so its performance can be monitored before a wider rollout.

---

## Infrastructure for reliable serving

The infrastructure you choose directly affects a model’s performance, scalability, and cost. Small-scale applications might work well on a single server or virtual machine. For high-traffic scenarios, orchestration systems like **Kubernetes** allow for scaling up resources automatically, balancing workloads, and providing resilience if something fails. Cloud providers also offer managed services such as **AWS SageMaker**, **Azure Machine Learning**, and **Google Vertex AI**, which take care of much of the operational complexity - ideal for teams who want to focus on models rather than infrastructure management.

---

# Monitoring and maintaining models in production

Once a machine learning model is deployed, it doesn’t just run forever at the same level of performance. Over time, the data it sees may drift from the data it was trained on, user behaviour may change, and external factors - like seasonality or market shifts - can alter its accuracy. Without careful monitoring, these changes can lead to silent model decay, where predictions become less reliable without anyone noticing.

## What to Monitor

- **Model performance** - tracking accuracy, precision, recall, or other relevant KPIs over time.
- **Data drift** - identifying when the characteristics of incoming data deviate from the training data.
- **Prediction distribution** - watching for changes in the spread or frequency of certain predictions that might indicate a bias or imbalance.
- **Latency and throughput** - ensuring the model is serving predictions within required timeframes.

---

## Data Drift vs Concept Drift

![Data Drift vs Concept Drift](https://www.deepchecks.com/wp-content/uploads/2025/06/post-data-drift-vs-concept-drift.jpg)

### Data Drift

In the top plot, the target variable is sales, split by sales channel: online (blue) and offline (red). Over time, the feature distribution - in this case, the proportion of sales from each channel - is gradually shifting.

- **What’s changing:** The balance between online and offline sales is moving; online sales are becoming more common (blue proportion increasing), and offline sales are slightly decreasing.

- **What’s not changing:** The relationship between the sales channel and sales outcome remains roughly the same. The model’s logic about how sales channel predicts sales hasn’t changed - only the input distribution has.

**Impact:** If a model was trained on the old distribution, predictions could become less accurate if it wasn’t expecting the new proportion of online vs offline sales.

### Concept Drift

In the top plot here, the feature distribution (sales channel proportions) is stable over time - the mix of online and offline sales channels isn’t changing.

- **What’s changing:** The relationship between sales channel and the target variable (sales) is evolving. At the start, offline sales (red) dominate, but over time, their sales numbers drop significantly. Online sales (blue) start small but eventually hold a larger proportion of sales activity relative to before.

- **What’s not changing:** The mix of sales channels in the data - there are still roughly the same numbers of online and offline transactions.

Even though the input data distribution hasn’t changed, the mapping between features and the target has shifted. The model’s original rules for predicting sales are now outdated because the business reality has changed. 

---

Data drift is one of the most common causes of performance degradation. It occurs when the statistical properties of input data change over time. There are different types:

- **Covariate drift** - when the distribution of input features changes.
- **Prior probability drift** - when the relative frequency of labels changes.
- **Concept drift** - when the relationship between inputs and outputs changes.

Detection methods might include comparing statistical summaries of current data with the training data or using secondary models trained to recognise distribution changes. The goal is to trigger an alert when drift is significant enough to require retraining.

### Responding to model degradation

Once an issue is detected, there are several possible responses:

- **Retraining** - updating the model with new data to reflect the current environment.
- **Rollback** - reverting to a previous, more reliable model version from the model registry.
- **Parameter tuning** - making targeted adjustments without a full retrain.

---

# Managing and evolving deployed models



