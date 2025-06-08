# Topic 4 - Monitoring an ingestion service and anomaly detection techniques 05/06/2025

# The importance of monitoring in data engineering

In modern data-driven organisations, data ingestion pipelines are critical components that must operate reliably and efficiently. Monitoring these pipelines is essential to:

-	**Ensure data integrity:** Detect and prevent data loss or corruption.
-	**Maintain performance:** Identify bottlenecks and optimise resource utilisation.
-	**Enhance reliability:** Quickly detect and respond to system failures or anomalies.
-	**Support compliance:** Meet regulatory requirements for data handling and reporting.

**Logs** are records of events
**Metrics** are used to measure performance
**Alerts** notifications of issues
**Dashboards** visualise performance

## Industry-standard monitoring tools

## Introduction to Prometheus 

**Prometheus** is an **open-source monitoring and alerting toolkit** originally developed at SoundCloud. It's now part of the Cloud Native Computing Foundation (CNCF), just like Kubernetes.

Prometheus is designed for **recording real-time metrics** in a time series database, with **powerful queries and alerts**. It’s widely used to monitor servers, containers, databases, applications, and even custom systems.

---

## Key Concepts

Here are some essential concepts to understand Prometheus:

### 1. **Metrics and Time Series**
- A **metric** is a numeric value about a system (e.g., CPU usage, memory used).
- A **time series** is a sequence of metric values, recorded over time.

Example:
```
http_requests_total{method="GET", handler="/api"} 12345
```

- This says: the metric `http_requests_total` counted 12,345 GET requests to `/api`.

### 2. **Pull-Based Model**
- Prometheus **pulls data** from targets at regular intervals (instead of targets pushing data).
- These targets expose an HTTP endpoint (usually `/metrics`) that Prometheus scrapes.

### 3. **Prometheus Server**
- The core of the system. It collects metrics, stores them, and allows querying.

### 4. **Exporters**
- Exporters are small programs that **expose metrics in a Prometheus-friendly format**.
- Example: `node_exporter` exposes OS-level metrics like CPU, memory, and disk usage.

### 5. **PromQL**
- Prometheus Query Language (PromQL) is used to **query and filter metrics**.
- Example: To get the rate of HTTP requests:
```
rate(http_requests_total[5m])
```

### 6. **Alerting**
- Prometheus supports **alerts based on metrics**.
- Alerts are sent to an **Alertmanager**, which can notify you via email, Slack, PagerDuty, etc.

---

## How Prometheus Works

Here’s a simplified flow:

1. Prometheus server is configured with a list of **targets** to monitor.
2. It **scrapes metrics** from the targets periodically (every 15 seconds by default).
3. The metrics are **stored locally** in a time-series database.
4. You can **query the data** using PromQL through:
   - The **Prometheus UI**
   - **Grafana dashboards** (for beautiful visualization)
5. Alerts are evaluated and sent to **Alertmanager** if necessary.

---

## Example Use Case

Let's say you want to monitor a web server:

- You install an **exporter** (like `node_exporter`) on the server.
- Prometheus scrapes metrics from it every 15s.
- You view a **dashboard in Grafana** showing CPU usage, memory, and HTTP requests.
- You set up an **alert** if CPU usage goes above 90% for 5 minutes.

---

## Why Use Prometheus?

- 🆓 **Free and open-source**
- 🧩 **Works well with Kubernetes**
- 🧠 **Powerful query language (PromQL)**
- 📦 **Many ready-to-use exporters**
- 📊 **Integrates easily with Grafana**
- 📣 **Built-in alerting system**

---

## Getting Started (High-Level Steps)

1. **Install Prometheus**: Download or use Docker.
2. **Configure targets** in the `prometheus.yml` file.
3. **Run Prometheus** and access the web UI at `http://localhost:9090`.
4. **Install an exporter** like `node_exporter` to collect system metrics.
5. **Set up Grafana** to visualize metrics (optional but recommended).
6. **Add alerts** to get notified when things go wrong.

---

## Resources

- [Official Website](https://prometheus.io/)
- [Getting Started Guide](https://prometheus.io/docs/introduction/first_steps/)
- [Awesome Prometheus](https://github.com/roaldnefs/awesome-prometheus) - curated list of tools and resources

---

## Summary

Prometheus is a **powerful yet approachable monitoring system** for everyone from hobbyists to large-scale production environments. With its **pull model**, **rich query language**, and **flexible alerting**, it’s a great choice for modern infrastructure monitoring.

---

## Grafana

**Grafana** is an open-source **monitoring and data visualization tool**. It allows you to **explore, visualize, and analyze** data from a variety of sources in real-time using **customizable dashboards**. Grafana is commonly used to monitor the health, performance, and trends of IT systems, servers, applications, and other infrastructure components.

---

## Why Use Grafana?

- **Real-time monitoring**: See your data as it changes.
- **Beautiful dashboards**: Build interactive, customizable visualizations like graphs, charts, and heatmaps.
- **Multiple data sources**: Connect to a wide range of databases and monitoring tools (e.g., Prometheus, InfluxDB, MySQL, Elasticsearch, etc.).
- **Alerting**: Set up alerts to notify you when something goes wrong.
- **Open-source and extensible**: Free to use and has a large community with lots of plugins.

---

## Key Concepts

### 1. **Dashboard**
A dashboard is a collection of **panels** (graphs, charts, etc.) that visually display data. You can have multiple dashboards for different systems or views.

### 2. **Panel**
A panel is a single visualization in a dashboard. For example, a line graph showing CPU usage over time.

### 3. **Data Source**
Grafana pulls data from **external systems** called data sources. Examples include:
- **Prometheus** – for metrics monitoring
- **InfluxDB** – time-series database
- **Elasticsearch** – search and analytics engine
- **MySQL/PostgreSQL** – relational databases

### 4. **Query**
Each panel uses a **query** to fetch data from the data source. Grafana provides a query editor tailored for each data source type.

### 5. **Alerts**
You can set **alert rules** for any panel. If the data meets a certain condition (like CPU > 90%), Grafana can **send a notification** via email, Slack, or other channels.

---

## How Grafana Works (Basic Flow)

1. **Connect** a data source (like Prometheus or InfluxDB).
2. **Create a dashboard** to organize your views.
3. **Add panels** to display different metrics.
4. **Write queries** to fetch the data you want to display.
5. **Customize** the visualizations (colors, axes, time ranges, etc.).
6. **Set alerts** (optional) to be notified when values go out of range.

---

## Typical Use Cases

- Monitoring server performance (CPU, memory, disk usage)
- Visualizing application metrics (request rates, errors)
- Tracking website traffic or API calls
- Observing IoT sensor data
- Business intelligence dashboards

---

## Getting Started

1. **Install Grafana**:
   - On Linux/macOS/Windows
   - Using Docker
   - As a hosted service via [Grafana Cloud](https://grafana.com/products/cloud/)

2. **Access Grafana UI**:
   - Open a web browser and go to `http://localhost:3000` (default)
   - Login with default credentials: `admin` / `admin` (you’ll be asked to change it)

3. **Add your first data source**
   - Go to **Configuration > Data Sources**
   - Select and configure your database or monitoring tool

4. **Create your first dashboard**
   - Go to **+ > Dashboard**
   - Add a panel and start visualizing data!

---

## Summary

Grafana is a powerful tool that helps you:
- Connect to various data sources
- Visualize your metrics in real-time
- Create dashboards and alerts
- Make informed decisions based on your system’s data

It’s widely used in DevOps, system administration, and business analytics due to its flexibility and ease of use.

---

## Additional Resources

- [Grafana Official Website](https://grafana.com/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Grafana Labs YouTube Channel](https://www.youtube.com/c/Grafana)

---



## 📊 Beginner's Guide to Monitoring Kafka with Prometheus & Grafana

This guide walks you through setting up monitoring for **Apache Kafka** using **Prometheus** and **Grafana**.

---

## 📦 Prerequisites

Make sure you have these installed:

- Docker & Docker Compose
- Basic knowledge of Docker
- Kafka running locally (we’ll use a Docker image for Kafka)
- Some free disk space

---

## 🔧 Step 1: Set Up Kafka with JMX Exporter

Kafka doesn’t expose metrics in Prometheus format by default. We use the **JMX Exporter** to make Kafka metrics available.

### Create `docker-compose.yml`

```yaml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.3.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:7.3.0
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_JMX_PORT: 9999
      KAFKA_JMX_HOSTNAME: localhost
    ports:
      - "9092:9092"
      - "9999:9999" # Port for JMX

  kafka-jmx-exporter:
    image: prom/jmx-exporter
    ports:
      - "7071:7071" # Prometheus will scrape from here
    volumes:
      - ./kafka-jmx-config.yaml:/config.yaml
    command:
      - 7071
      - /config.yaml
```

### Create kafka-jmx-config.yaml

This tells the exporter what to collect.

```yaml
startDelaySeconds: 0
hostPort: localhost:9999
lowercaseOutputName: true
lowercaseOutputLabelNames: true
rules:
  - pattern: "kafka.server<type=(.+), name=(.+)><>(Count|Value)"
    name: kafka_$1_$2
    type: GAUGE
    labels:
      instance: kafka1
```


## 🔧 Step 2: Set Up Prometheus

### Create prometheus.yml
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'kafka'
    static_configs:
      - targets: ['kafka-jmx-exporter:7071']
```

### Add Prometheus to docker-compose.yml

Below the Kafka service, add:

```yaml
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    ports:
      - "9090:9090" # Access Prometheus UI
```

## 🔧 Step 3: Add Grafana to Visualize Metrics

### Add Grafana to docker-compose.yml

```yaml
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
```

## 🔧Step 4: Start Everything

### Run the stack with:
```bash
docker-compose up -d
```

## 🔧Step 5: Configure Grafana Dashboard

### Add Prometheus as a Data Source:

In Grafana, go to Settings > Data Sources
Click Add data source
Choose Prometheus
Set URL to: http://prometheus:9090
Click Save & Test

### Import a Kafka Dashboard:

Go to + > Import
Use dashboard ID: 7589 or search for "Kafka"
Choose Prometheus as data source
Click Import

You’ll now see charts with metrics like:

Messages In/Out

Under-replicated partitions

Request latency

---

# Forecasting techniques for data ingestion

One of the key challenges faced by data engineers is predicting future system behaviour to ensure that resources are allocated efficiently and potential issues are mitigated before they escalate. Forecasting is a critical component in managing data ingestion services. By predicting future system behaviour, you can plan capacity, prevent overloads, and optimise costs.

Forecasting is a critical component in managing data ingestion services. By predicting future system behaviour, you can:

1.	**Plan capacity:** Ensure that resources meet demand.
2.	**Prevent overload:** Avoid system failures due to unexpected spikes.
3.	**Optimise costs:** Allocate resources efficiently.

### Introduction to time series forecasting

Time series forecasting involves analysing historical data to predict future values. Common methods include:

-	**ARIMA** (AutoRegressive Integrated Moving Average)
-	**SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors)
-	**Prophet**
-	**Machine Learning Models** (e.g., LSTM networks)

`A stationary time series is a time series whose statistical properties, such as mean, variance, and autocorrelation, do not change over time. In other words, the value of a stationary time series is not dependent on the time at which it is observed.`

---

## ARIMA for Time Series Forecasting

**ARIMA** stands for **AutoRegressive Integrated Moving Average**. It is a popular statistical method used for **forecasting** future values in a **time series**—a sequence of data points collected or recorded at regular time intervals (e.g., daily stock prices, monthly sales, yearly rainfall).

ARIMA is powerful because it models both the **trend** and **patterns** in the data. It works best with **univariate** time series (a single variable over time).

---

### Components of ARIMA

The ARIMA model has three main parts, represented as ARIMA(**p**, **d**, **q**):

- **AR (AutoRegressive)** – The relationship between a value and its past values.
- **I (Integrated)** – How many times the data has been differenced to make it stationary (i.e., stable over time).
- **MA (Moving Average)** – The relationship between a value and past forecast errors.

### 1. AutoRegressive (AR, parameter `p`)
This part uses **lagged values** of the series itself. For example:
> Tomorrow's temperature might depend on the temperatures of the last few days.

If `p = 2`, the model uses the two previous observations to predict the next one.

### 2. Integrated (I, parameter `d`)
Real-world data often has trends or patterns. "Integrated" means we **difference** the data (subtract the previous value from the current one) to make it **stationary**.

If `d = 1`, the model uses the **first difference** of the series:
> `y_t' = y_t - y_(t-1)`

### 3. Moving Average (MA, parameter `q`)
This part models the **error** of the prediction as a combination of past errors.

If `q = 1`, it means the model uses the error from one step ago to help make the current prediction.

---

### Summary of ARIMA(p, d, q)

| Component | Description                             |
|-----------|-----------------------------------------|
| p         | Number of lag observations (AR part)    |
| d         | Degree of differencing (I part)         |
| q         | Size of moving average window (MA part) |

---

### Example: ARIMA(1, 1, 1)

This means:
- Use 1 lag (yesterday’s value) → AR(1)
- Difference the data once to remove trend → I(1)
- Use 1 lag of forecast error → MA(1)

---

### Steps to Use ARIMA

1. **Visualize the data** – Plot the time series to understand trends and seasonality.
2. **Make the data stationary** – Use differencing if needed.
3. **Identify p, d, q** – Use plots like ACF and PACF, or automated tools (like `auto_arima` in Python).
4. **Fit the model** – Use statistical software or libraries (like `statsmodels` in Python).
5. **Validate** – Check residuals (errors) to ensure they look like white noise.
6. **Forecast** – Predict future values using the trained ARIMA model.

---

### Simple Python Example (Optional)

```python
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

# Example data: Monthly sales
data = pd.read_csv("sales.csv", index_col="Month", parse_dates=True)

# Fit ARIMA model
model = ARIMA(data, order=(1, 1, 1))
model_fit = model.fit()

# Forecast next 5 steps
forecast = model_fit.forecast(steps=5)
print(forecast)
```

### When to Use ARIMA
✅ Good for non-seasonal data
✅ When there’s a trend but no strong repeating seasonal pattern
✅ Univariate forecasting (one variable over time)

### Limitations
❌ Not ideal for seasonal data (use SARIMA instead)
❌ Assumes linearity
❌ Can struggle with complex patterns or multiple variables

---

# Introduction to SARIMAX for Time Series Forecasting

If you're new to time series forecasting, **SARIMAX** might sound like a complex concept — but don't worry! This guide breaks it down step-by-step in a beginner-friendly way.

---

**SARIMAX** stands for:

**S**easonal  
**A**uto**R**egressive  
**I**ntegrated  
**M**oving **A**verage  
with e**X**ogenous variables

It's a powerful statistical model used to forecast time series data that may have:

- **Trends** (increasing or decreasing patterns)
- **Seasonality** (repeating patterns over time, like sales going up every December)
- **External factors** (e.g., holidays, marketing campaigns)

---

## 🧠 Breaking Down SARIMAX

### 1. **AR (AutoRegressive)**
This means the model uses **past values** to predict the current value.

Example:  
> Tomorrow’s value depends on values from the last few days.

### 2. **I (Integrated)**
This part helps deal with **trends** by using **differences** between observations.

Example:  
> Instead of using actual sales numbers, use the change in sales from day to day.

### 3. **MA (Moving Average)**
This uses **past forecast errors** to predict current values.

Example:  
> If the model was too high yesterday, maybe it adjusts down today.

### 4. **Seasonal Component (S)**
Adds the same AR, I, and MA ideas — but for **seasonal patterns**.

Example:  
> Weekly, monthly, or yearly cycles — like more ice cream sales every summer.

### 5. **X (Exogenous Variables)**
These are **external influences** that may affect your forecast.

Example:  
> Promotions, holidays, or weather data added to improve the forecast.

---

## ⚙️ SARIMAX Parameters

SARIMAX has **two main sets** of parameters:

### Non-Seasonal Parameters (p, d, q)
- `p` = AR terms (how many past values to include)
- `d` = I terms (how many times to difference the data)
- `q` = MA terms (how many past errors to include)

### Seasonal Parameters (P, D, Q, s)
- `P` = Seasonal AR terms
- `D` = Seasonal differencing
- `Q` = Seasonal MA terms
- `s` = Season length (e.g., 12 for monthly data with yearly seasonality)

### Exogenous Variables (optional)
- `exog` = Extra inputs that help the model

---

## 📦 Example in Python (using `statsmodels`)

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Your time series data
y = [your time series here]

# Optional exogenous variable(s)
exog = [your external data here]  # Can be None if not using

# Fit the model
model = SARIMAX(y, 
                exog=exog, 
                order=(p, d, q), 
                seasonal_order=(P, D, Q, s))

results = model.fit()

# Make predictions
forecast = results.forecast(steps=10, exog=exog_future)
```

### ✅ When to Use SARIMAX
Use SARIMAX if your data has:

- Trend and/or seasonality
- Past behavior that affects the future
- External factors influencing the outcome

### 📚 Final Tips

- Start simple: try basic ARIMA first before adding seasonal or exogenous parts.
- Use plots (like autocorrelation) to decide on parameters.
- Use statsmodels in Python — it's beginner-friendly with solid documentation.

---

## Time Series Forecasting with ARIMA and SARIMAX in Python

This guide will walk you through the process of forecasting time series data using ARIMA and SARIMAX models in Python. We'll cover:

- Checking for stationarity with the **Augmented Dickey-Fuller (ADF) test**
- Automatically selecting the best ARIMA parameters using **auto-ARIMA**
- Implementing **ARIMA** and **SARIMAX** models
- Making predictions and visualizing results

---

### Step 1: Setup Python Environment

Make sure you have the following libraries installed. If not, you can install them via pip:

```bash
pip install pandas numpy matplotlib statsmodels pmdarima
```

### Step 2: Import Libraries and Load Data

We'll use a sample time series dataset for demonstration.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pmdarima as pm  # for auto-ARIMA

# Create date range
date_rng = pd.date_range(start='2010-01-01', end='2013-12-31', freq='M')

# Create synthetic time series data
np.random.seed(42)
data = 10 + 0.5 * np.arange(len(date_rng)) + 5 * np.sin(2 * np.pi * date_rng.month / 12) + np.random.normal(0, 1, len(date_rng))

# Create DataFrame
df = pd.DataFrame(data, index=date_rng, columns=['value'])

# Plot the data
df.plot(title='Synthetic Time Series Data', figsize=(10, 6))
plt.show()

```

### Step 3: Check for Stationarity with Augmented Dickey-Fuller (ADF) Test

Stationarity means the statistical properties of the series do not change over time. ARIMA models require stationarity.

```python
def adf_test(timeseries):
    print('Results of Augmented Dickey-Fuller Test:')
    result = adfuller(timeseries)
    print(f'ADF Statistic: {result[0]:.4f}')
    print(f'p-value: {result[1]:.4f}')
    for key, value in result[4].items():
        print(f'Critical Value ({key}): {value:.4f}')
    
    if result[1] <= 0.05:
        print("Strong evidence against the null hypothesis, reject the null hypothesis. The series is stationary.")
    else:
        print("Weak evidence against the null hypothesis, time series has a unit root, indicating it is non-stationary.")

# Run ADF test on original data
adf_test(df['value'])
```

**Interpretation:**

If p-value **> 0.05** → data is non-stationary → apply differencing.

If p-value **≤ 0.05** → data is stationary → proceed.

### Step 4: Make the Series Stationary (if needed)

If the series is non-stationary, apply differencing:

```python
df_diff = df['value'].diff().dropna()

# Plot differenced data
df_diff.plot(title='Differenced Time Series', figsize=(10, 6))
plt.show()

# Run ADF test again
adf_test(df_diff)
```

### Step 5: Use auto-ARIMA to Select Best Parameters

Instead of guessing ARIMA orders (p, d, q), use pmdarima.auto_arima to find the best model automatically.

```python
# auto_arima to find best params; seasonal=True because data has seasonality
auto_model = pm.auto_arima(df['value'], seasonal=True, m=12,  # m=12 for monthly seasonality
                           trace=True, error_action='ignore', suppress_warnings=True)

print(auto_model.summary())
```

**The output shows the best (p, d, q) and seasonal (P, D, Q, m) parameters.**

### Step 6: Fit the ARIMA / SARIMAX Model

Using parameters from auto_arima, fit the model with SARIMAX:

```python
# Extract parameters from auto_model
order = auto_model.order
seasonal_order = auto_model.seasonal_order

# Fit SARIMAX model
model = SARIMAX(df['value'], order=order, seasonal_order=seasonal_order)
model_fit = model.fit(disp=False)

print(model_fit.summary())
```

### Step 7: Make Forecasts

Let's forecast the next 12 months:

```python
forecast_steps = 12
forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(start=df.index[-1] + pd.offsets.MonthBegin(), periods=forecast_steps, freq='M')
forecast_series = pd.Series(forecast.predicted_mean, index=forecast_index)

# Plot historical and forecast
plt.figure(figsize=(12,6))
plt.plot(df['value'], label='Observed')
plt.plot(forecast_series, label='Forecast', color='red')
plt.fill_between(forecast_series.index, 
                 forecast.conf_int().iloc[:, 0], 
                 forecast.conf_int().iloc[:, 1], 
                 color='pink', alpha=0.3)
plt.title('ARIMA/SARIMAX Forecast')
plt.legend()
plt.show()
```

### Summary

- ADF test helps check if your data is stationary.
- Differencing is used to make data stationary.
- auto-ARIMA automates finding the best ARIMA parameters.
- SARIMAX allows fitting seasonal and non-seasonal ARIMA models.
- You can then forecast future points and visualize results.

---

## Introduction to Differencing for Achieving Stationarity

When working with time series data, a common requirement for many statistical models is that the data be **stationary**. Stationarity means that the statistical properties of the time series, such as mean and variance, do not change over time.

However, many real-world time series are **non-stationary**, showing trends, seasonality, or other patterns that change over time. To use models that assume stationarity (like ARIMA), we often need to **transform** the data to make it stationary.

One simple and common technique to achieve stationarity is **differencing**.

---

### What is Differencing?

Differencing is a method of transforming a time series by subtracting the previous observation from the current observation. This helps remove trends or seasonality that cause non-stationarity.

Mathematically, the first difference of a time series \( Y_t \) is:

\[
Y_t' = Y_t - Y_{t-1}
\]

Where:  
- \( Y_t \) is the value at time \( t \)  
- \( Y_{t-1} \) is the value at the previous time step \( t-1 \)  
- \( Y_t' \) is the differenced value at time \( t \)

---

### Why does Differencing Help?

- **Removes Trend:** If your data has a trend (e.g., increasing sales over time), differencing removes this by focusing on changes between consecutive points rather than absolute values.
- **Stabilizes Mean:** By removing trend and seasonality, differencing can help stabilize the mean over time.
- **Makes Data Stationary:** Many models require stationary data, and differencing helps meet this assumption.

---

### How to Apply Differencing (Step-by-Step)

1. **Visualize the Original Series:**  
   Plot your time series data to see if it has any obvious trend or seasonal patterns.

2. **Calculate the Difference:**  
   Compute the difference between consecutive observations. This can be done by subtracting each value by the previous one.

3. **Plot the Differenced Series:**  
   After differencing, plot the new series to check if the trend has been removed and the series looks more stationary.

4. **Test for Stationarity:**  
   Use statistical tests like the **Augmented Dickey-Fuller (ADF) test** to confirm if the differenced series is stationary.

---

### Example in Python

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Example time series data
data = [100, 105, 110, 120, 130, 150, 170, 200]

# Convert to pandas Series
series = pd.Series(data)

# Plot original series
plt.plot(series)
plt.title("Original Series")
plt.show()

# Apply first differencing
diff_series = series.diff().dropna()

# Plot differenced series
plt.plot(diff_series)
plt.title("Differenced Series")
plt.show()

# Perform ADF test
result = adfuller(diff_series)
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')
```

### Additional Notes

- Sometimes, one round of differencing is not enough. You may need to difference the series twice (second differencing).
- For seasonal data, seasonal differencing (subtracting the value from the same season in the previous cycle) can also be used.
- Over-differencing can lead to loss of important information, so always check for stationarity after differencing.

---

### Real-world application

**Capacity planning for a streaming service**
A music streaming company wants to forecast the expected data ingestion rates to ensure that their Kafka cluster can handle peak loads, especially during events like new album releases or holidays.

**As the lead data engineer, how would you set about forecasting the data ingestion rates?**
Your implementation steps would be as follows:

1.	**Collect historical data:**
-	Gather ingestion metrics over the past year.
2.	**Apply SARIMAX Model:**
-	Account for seasonal patterns (e.g., higher usage on weekends).
-	Include exogenous variables like marketing campaigns.
3.	**Forecast future demand:**
-	Predict ingestion rates for the next quarter.
4.	**Plan Infrastructure:**
-	Scale Kafka clusters and allocate resources accordingly.

**The benefits**

-	**Optimised performance:** Prevent overloads and ensure smooth user experience.
-	**Cost efficiency:** Avoid over-provisioning resources, reducing operational costs.
-	**Strategic planning:** Align technical capacity with business initiatives.

## Anomaly detection in data streams

### Anomaly detection techniques

#### Statistical methods
**Z-Score Analysis:**
-	Measures how many standard deviations an element is from the mean.
**Seasonal Hybrid ESD (Extreme Studentised Deviate):**
-	Detects anomalies in seasonal time series data.

#### Machine learning models
**Isolation Forest:**
-	An unsupervised learning algorithm that isolates anomalies based on random partitioning.
**One-Class SVM (Support Vector Machine):**
-	Learns the boundary of normal data to detect outliers.

#### Time series models
**ARIMA/SARIMAX Residual Analysis:**
-	Analyse residuals from forecasting models to detect anomalies.
**Prophet:**
-	A forecasting tool by Facebook that can model and detect anomalies in time series data.

---

# Anomaly Detection Using Isolation Forest and Seasonal-Hybrid ESD in Python

This guide will walk you through the basics of implementing anomaly detection in data streams using two popular methods:

- **Isolation Forest** (a machine learning based method)
- **Seasonal-Hybrid ESD (S-H-ESD)** (a statistical method for seasonal time series)

---

## 1. Isolation Forest

### What is Isolation Forest?

Isolation Forest is a machine learning algorithm that isolates anomalies instead of profiling normal data points. It builds random trees that isolate observations; anomalies are isolated faster because they are few and different.

---

### Step-by-Step Implementation of Isolation Forest in Python

#### 1. Install required packages

```bash
pip install scikit-learn numpy pandas matplotlib
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Generate sample data: normal data with some anomalies
np.random.seed(42)
normal_data = 0.3 * np.random.randn(100, 1)
anomalies = np.array([[3], [3.5], [4]])
data = np.vstack([normal_data, anomalies])
df = pd.DataFrame(data, columns=['value'])

# Plot the data
plt.figure(figsize=(10, 4))
plt.plot(df.index, df['value'], marker='o', linestyle='-', label='Data')
plt.title('Sample Data with Anomalies')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

# Fit Isolation Forest
iso_forest = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = iso_forest.fit_predict(df[['value']])

# -1 means anomaly, 1 means normal
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})

# Plot anomalies
plt.figure(figsize=(10, 4))
plt.plot(df.index, df['value'], label='Value')
plt.scatter(df.index[df['anomaly'] == 1], df['value'][df['anomaly'] == 1], color='red', label='Anomaly')
plt.legend()
plt.title('Isolation Forest Anomaly Detection')
plt.show()
```

## 2. Seasonal-Hybrid ESD (S-H-ESD)

What is Seasonal-Hybrid ESD?
S-H-ESD is a statistical method designed for detecting anomalies in time series data with seasonality (e.g., daily, weekly patterns). It combines Seasonal decomposition and Extreme Studentized Deviate (ESD) test.

Step-by-Step Implementation of S-H-ESD in Python
**1. Install required packages**

```bash
pip install numpy pandas matplotlib statsmodels
```

**2. Example Code**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy.stats import t

# Generate sample seasonal data
np.random.seed(42)
period = 24
time = np.arange(0, 4 * period)
seasonal_pattern = 10 + np.sin(2 * np.pi * time / period)
noise = np.random.normal(0, 0.5, size=len(time))
data = seasonal_pattern + noise

# Inject anomalies
data[30] += 6
data[50] -= 7

df = pd.DataFrame({'value': data}, index=pd.date_range(start='2023-01-01', periods=len(data), freq='H'))

# Decompose time series
result = seasonal_decompose(df['value'], model='additive', period=period)
residual = result.resid.dropna()

# Function to perform Generalized ESD Test for anomalies
def generalized_esd_test(data, max_anomalies=10, alpha=0.05):
    data = data.copy()
    anomalies = []
    for i in range(max_anomalies):
        n = len(data)
        mean = np.mean(data)
        std = np.std(data, ddof=1)
        if std == 0:
            break
        deviations = abs(data - mean)
        max_deviation = deviations.max()
        max_index = deviations.argmax()

        lam = ((n - i - 1) * t.ppf(1 - alpha / (2 * (n - i)), n - i - 2)) / \
              np.sqrt((n - i - 2 + t.ppf(1 - alpha / (2 * (n - i)), n - i - 2)**2) * (n - i))

        test_stat = max_deviation / std

        if test_stat > lam:
            anomalies.append(data.index[max_index])
            data = data.drop(data.index[max_index])
        else:
            break
    return anomalies

anomalies = generalized_esd_test(residual)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['value'], label='Value')
plt.plot(result.trend.index, result.trend, label='Trend')
plt.plot(result.seasonal.index, result.seasonal, label='Seasonal')
plt.scatter(anomalies, df.loc[anomalies]['value'], color='red', label='Anomalies', zorder=5)
plt.legend()
plt.title('Seasonal-Hybrid ESD Anomaly Detection')
plt.show()
```

### Additional Tips for Beginners

- Understand your data: Is it seasonal? Streaming? Noisy?
- Start with simple visualizations to spot anomalies manually.
- Tune parameters (e.g., contamination for Isolation Forest).
- For real streaming data, consider incremental or online versions of these methods.

### Summary

| **Method**         | **Best for**             | **Key Idea** | **Python Libraries**  |
|-----------------|----------------------------------------------|--------|---------|
| Isolation Forest  | General anomaly detection, non-seasonal data  |  Isolates anomalies via random trees  | scikit-learn |
| Seasonal-Hybrid ESD | Time series with strong seasonality |  Decompose + statistical test on residuals	statsmodels  | scipy | 

---

## Integration with Incident Management Systems

Incident management systems play a vital role in helping organisations respond to and manage unplanned events or service interruptions.

**Popular incident management platforms include:**
-	PagerDuty
-	Opsgenie
-	VictorOps
-	ServiceNow

**The benefits of integration include:**

-	**Centralised alert management:** Consolidate alerts from multiple sources.
-	**On-Call scheduling:** Manage on-call rotations and escalations.
-	**Automated response:** Trigger automated actions or workflows.
-	**Incident tracking:** Log incidents for analysis and improvement.

---

## Integrating Prometheus Alertmanager with Incident Management: A Beginner's Step-by-Step Guide

This guide is designed for complete beginners who want to integrate **Prometheus Alertmanager** with an incident management system. By the end, you'll understand how to send alerts from Prometheus to an incident management tool like PagerDuty, Opsgenie, or any other system.

---

### What is Prometheus Alertmanager?

Prometheus Alertmanager is a tool that handles alerts sent by Prometheus server. It manages alert notifications, grouping, inhibition, and routing them to various communication channels like email, Slack, or incident management tools.

---

### What is Incident Management?

Incident management is the process of detecting, reporting, and resolving incidents (issues) in IT systems. Tools like PagerDuty, Opsgenie, and VictorOps help automate alerting, on-call scheduling, and escalation to reduce downtime.

---

### Why Integrate Alertmanager with Incident Management?

- **Automatic alert routing** to the right on-call person or team.
- **Alert deduplication** and grouping.
- **Escalations** if alerts are not acknowledged.
- **Better incident tracking** and faster resolution.

---

### Prerequisites

- Basic understanding of Prometheus.
- Prometheus and Alertmanager installed.
- Access to an incident management tool (PagerDuty, Opsgenie, etc.) with API credentials.
- A working Linux environment or cloud server.
- Access to your configuration files.

---

### Step 1: Install and Configure Prometheus

If you don’t have Prometheus installed, here’s a quick setup:

1. Download Prometheus:  
   ```bash
   wget https://github.com/prometheus/prometheus/releases/download/v2.46.0/prometheus-2.46.0.linux-amd64.tar.gz
   tar xvf prometheus-2.46.0.linux-amd64.tar.gz
   cd prometheus-2.46.0.linux-amd64
```

### Step 2: Install and Configure Alertmanager

1. Download Alertmanager:

```bash
wget https://github.com/prometheus/alertmanager/releases/download/v0.25.0/alertmanager-0.25.0.linux-amd64.tar.gz
tar xvf alertmanager-0.25.0.linux-amd64.tar.gz
cd alertmanager-0.25.0.linux-amd64
```

2. Create a basic alertmanager.yml configuration file:
``` yaml
global:
  resolve_timeout: 5m

route:
  receiver: 'default'

receivers:
- name: 'default'
```

3. Start Alertmanager:
```bash
./alertmanager --config.file=alertmanager.yml
```

### Step 3: Configure Alertmanager to Send Alerts to Incident Management
Let’s configure Alertmanager to send alerts to PagerDuty as an example. Other tools have similar configs.

1. Get PagerDuty Integration Key from your PagerDuty dashboard (usually called Integration Key or API Key).

2. Edit alertmanager.yml to include PagerDuty receiver:

```yaml
global:
  resolve_timeout: 5m

route:
  receiver: 'pagerduty'

receivers:
- name: 'pagerduty'
  pagerduty_configs:
  - routing_key: 'YOUR_PAGERDUTY_INTEGRATION_KEY'
    severity: '{{ if eq .CommonLabels.severity "critical" }}critical{{ else }}warning{{ end }}'
```

3. Configure Prometheus to send alerts to Alertmanager by editing prometheus.yml:
```yaml
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      - localhost:9093  # Alertmanager address

rule_files:
  - "alert.rules.yml"
```

4. Create a sample alert rule file alert.rules.yml:
```yaml
groups:
- name: example
  rules:
  - alert: InstanceDown
    expr: up == 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "Instance {{ $labels.instance }} down"
      description: "{{ $labels.instance }} of job {{ $labels.job }} has been down for more than 1 minute."
```

5. Restart Prometheus and Alertmanager to apply changes.

### Step 4: Test the Integration

1. Stop a monitored service or simulate the alert condition (for example, stop a service monitored by Prometheus).
2. Wait for Prometheus to detect the alert and send it to Alertmanager.
3. Alertmanager forwards the alert to PagerDuty.
4. Check PagerDuty to see if the alert appears.

### Additional Tips

- Use Alertmanager inhibition rules to suppress alerts if another alert is firing.
- Group related alerts to reduce noise.
- Use multiple receivers and routing to target different teams.
- Monitor Alertmanager and Prometheus logs for troubleshooting.

---

### Real-world application

**Managing incidents in a healthcare system...**

A hospital uses data ingestion services to process patient data in real-time.
System failures can have critical implications for patient care.
As the lead data engineer, how would you set about implementing an incident management system?

Your implementation steps would be as follows:

1.	**Integrate monitoring with incident management:**
-	Use Prometheus and Alertmanager to monitor ingestion services.
-	Connect Alertmanager to PagerDuty for incident management.
2.	**Define critical alerts:**
-	Set up alerts for high-severity issues like data ingestion failures or significant anomalies.
3.	**Configure on-call rotations:**
-	Ensure that responsible team members are available to respond to incidents promptly.
4.	**Automate responses:**
-	Implement scripts or playbooks that can be triggered to mitigate issues automatically.

#### The benefits
-	**Response times:** Faster resolution of incidents reduces impact on services.
-	**Accountability:** Clear ownership of incidents ensures that issues are addressed.
-	**Continuous improvement:** Incident tracking allows for analysis and process enhancements.

## Addressing real-world use cases and typical ingestion issues

### Common ingestion issues in Kafka and Cloud environments
Data ingestion pipelines can encounter several common issues that impact their performance and reliability. In this section, we'll delve into problems like consumer lag and latency, broker failures, message loss, and security breaches. Understanding the symptoms, causes, and solutions for these issues will help you maintain a robust data ingestion system.

### Consumer lag and latency

**Symptoms**
-	Consumers fall behind the latest messages.
-	Increased message processing delays.

**Causes**
- Insufficient consumer resources.
- Slow processing logic.
- Network congestion.

**Solutions**
- Scale consumer instances.
- Optimise processing code.
- Enhance network bandwidth.

### Message Loss

**Symptoms**
- Missing data in downstream systems.
- Inconsistent data processing results.

**Causes**
- Incorrect producer configurations.
- Insufficient replication.
- Data retention policies.

**Solutions**
- Configure appropriate acknowledgments (acks=all).
- Increase replication factor.
- Adjust retention settings.

### Broker failures

**Symptoms**
- Unavailable partitions.
- Errors in producers and consumers.

**Causes**
- Hardware failures.
- Configuration errors.
- Resource exhaustion.

**Solutions**
- Implement redundancy.
- Use automatic broker recovery.
- Monitor resource utilisation.

### Security Breaches

**Symptoms**
- Unauthorised access to data.
- Suspicious activities in logs.

**Causes**
- Weak authentication.
- Misconfigured access controls.
- Vulnerabilities in the system.

**Solutions**
- Implement robust security measures (SSL, SASL, ACLs).
- Regularly audit security configurations.
- Apply patches and updates promptly.

---

### Real-world applications

**Data loss in a logistics company...**

A logistics company experiences data loss in their tracking system, leading to misplaced shipments.

**Analysis:**

1. **Issue:**
- Messages are lost due to incorrect producer settings (acks=1).

2. **Resolution:**
- Update producer configuration to use acks=all.
- Increase replication factor for critical topics.

---

**Scaling challenges in a social media platform...**

A social media platform struggles to handle increased data ingestion during peak times, resulting in slow content updates.

**Analysis:**

1. **Issue:**
- Consumer lag due to insufficient processing capacity.

2. **Resolution:**
- Implement auto-scaling for consumer applications.
- Optimise processing logic using asynchronous operations.

---

### Best practices for addressing ingestion issues

Implementing best practices is essential for preventing and mitigating ingestion issues. This section will cover strategies like implementing redundancy, optimising configurations, regular monitoring, documentation and automation, and conducting regular audits. These practices will help you build resilient data pipelines capable of handling diverse challenges.


**Implement redundancy:**
- Use multiple brokers and replication to prevent single points of failure.

**Optimise configurations:**
- Tune Kafka settings based on workload and performance testing.

**Regular monitoring:**
- Continuously monitor system metrics to detect issues early.

**Document and automate:**
- Maintain documentation of configurations and automate deployments for consistency.

**Conduct regular audits:**
- Review security settings, resource allocations, and system performance periodically.

### Cloud environment considerations

Managing data ingestion pipelines in cloud environments comes with its own set of considerations. Leveraging cloud services' features and understanding their limitations will enable you to optimise your data ingestion processes in the cloud.

The following are best practice techniques:

- **Resource management:** Utilise cloud services' auto-scaling features. Monitor costs associated with resource usage.
- **Network dependencies:** Be aware of network latency and bandwidth limitations in cloud environments.
- **Service integrations:** Leverage managed services for Kafka (e.g., AWS MSK, Azure Event Hubs) when appropriate.

## Exploring other anomaly detection methods

### Deep learning models

**LSTM Networks (Long Short-Term Memory):**

- Capable of learning long-term dependencies in time series data.
- Useful for complex patterns and sequences.

**Autoencoders**

- Neural networks trained to reconstruct input data.
- Anomalies are detected when reconstruction error exceeds a threshold.

**Clustering techniques**

- **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** Identifies clusters and treats outliers as anomalies.

**Implementing advanced monitoring solutions**

- **Elastic Stack (ELK):**
  - **Elasticsearch:** Search and analytics engine.
  - **Logstash:** Data processing pipeline.
  - **Kibana:** Visualisation tool.

`Be careful with Machine Learning auto anomoly detection. It's good but you'll need to ensure you don't brake data privicy or introduce bias`

