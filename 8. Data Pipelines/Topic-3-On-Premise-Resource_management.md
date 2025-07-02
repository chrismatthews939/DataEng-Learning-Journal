# Topic 3 On-Premise Resource Management

# Setting Up On-Premise Infrastructure for Data Workloads

Setting up your own on-premise infrastructure for handling data workloads means you're running servers and related equipment in your own facility, rather than in the cloud (like AWS or Azure). This can give you more control, better performance for local users, and potentially lower costs over time — but it also comes with responsibilities.

This guide breaks everything down into four main areas:

1. **Hardware and Capacity Management**
2. **Network Topology**
3. **Environment Configuration**
4. **Security Hardening**

---

## 1. Hardware and Capacity Management

This is about selecting, installing, and managing the physical machines and storage that will process and store your data.

### Key Components:
- **Servers**: These are powerful computers that run your applications and store data.
- **Storage**: Hard drives or SSDs (Solid State Drives) where your data will be saved.
- **RAID (Redundant Array of Independent Disks)**: A system that uses multiple hard drives to increase performance and provide redundancy (so you don’t lose data if one drive fails).
- **Power Backup (UPS)**: Uninterruptible Power Supplies to keep systems running during power outages.
- **Cooling Systems**: Hardware gets hot. You'll need fans, air conditioning, or other cooling solutions to maintain a safe temperature.

### Tips:
- Estimate how much data you’ll store now and in the future.
- Plan for extra capacity (called **headroom**) to allow for growth.
- Use **rack-mounted servers** if you’re building a larger setup — they’re space-efficient and easier to manage.

---

## 2. Network Topology

This is about how your devices (servers, users, routers, etc.) are connected to each other.

### Key Concepts:
- **LAN (Local Area Network)**: A private network that connects computers in a limited area, like an office or building.
- **Router**: Directs traffic between your LAN and the outside world (e.g., the internet).
- **Switch**: A device that connects multiple devices inside your LAN, allowing them to talk to each other.
- **Firewall**: Controls what traffic is allowed in or out of your network.
- **IP Addressing**: Every device on the network needs a unique IP address (like a home address, but for computers).

### Topology Types:
- **Star Topology**: All devices connect to a central switch. This is common and easy to manage.
- **Mesh Topology**: Devices are interconnected, offering more redundancy (used in critical systems but more complex).

### Tips:
- Use **Gigabit Ethernet** or faster for high data throughput.
- Assign **static IP addresses** to servers so they don’t change.
- Separate different types of traffic (e.g., management vs. data) using **VLANs** (Virtual LANs).

---

## 3. Environment Configuration

This involves setting up the software and services that will run your data workloads.

### Operating Systems:
- Use **Linux** distributions like Ubuntu Server or CentOS for most data workloads (they are stable and widely supported).
- Windows Server may be used for specific applications that require it.

### Services to Configure:
- **Database systems** (e.g., PostgreSQL, MySQL, MongoDB)
- **File storage** (e.g., NFS, SMB/CIFS)
- **Job schedulers** (e.g., Cron, Apache Airflow for data pipelines)
- **Monitoring tools** (e.g., Prometheus + Grafana, Nagios)

### Configuration Management:
- Use tools like **Ansible**, **Puppet**, or **Terraform** to automate setup and keep configurations consistent.

### Tips:
- Keep your system updated regularly to receive security patches.
- Document your configurations and setup process.
- Use version control (e.g., Git) for your config files if possible.

---

## 4. Security Hardening

This is about protecting your infrastructure from unauthorized access, data loss, and other threats.

### Key Practices:
- **Physical Security**: Lock server rooms. Limit who can access hardware.
- **User Accounts**: Create individual accounts. Avoid using shared credentials.
- **SSH (Secure Shell)**: Use SSH keys instead of passwords to securely access servers remotely.
- **Firewall Configuration**: Only open ports you need (e.g., port 22 for SSH, port 5432 for PostgreSQL).
- **Encryption**:
  - **At rest**: Encrypt stored data using tools like LUKS or BitLocker.
  - **In transit**: Use SSL/TLS for encrypted communication between systems.
- **Backups**:
  - Automate regular backups.
  - Test your backup restoration process.
  - Store backups offsite or in a secure cloud location.

### Tips:
- Disable unused services and ports.
- Set up automatic security updates where possible.
- Use logging and intrusion detection (e.g., Fail2Ban, OSSEC).

---

## Summary

| Area                     | Focus                                                                 |
|--------------------------|-----------------------------------------------------------------------|
| **Hardware & Capacity**  | Choose and manage servers, storage, and power/cooling requirements.   |
| **Network Topology**     | Plan how systems connect and communicate securely.                    |
| **Environment Config**   | Set up operating systems, applications, and automation tools.         |
| **Security Hardening**   | Protect systems from attacks and ensure data safety.                  |

---

# Maintaining On-Premise Infrastructure for Data Workloads

This guide provides a beginner-friendly explanation of maintaining on-premise infrastructure for data workloads. "On-premise" (or "on-prem") means that your servers, storage, and networking equipment are physically located on-site (such as in your office or data center), rather than in the cloud.

We’ll break it down into four essential areas:

---

## 1. Patch and Update Management

**What is it?**  
Keeping your systems (like servers and applications) up to date with the latest software patches and updates.

**Why it matters:**  
- Fixes security vulnerabilities
- Improves system performance and stability
- Adds new features or removes bugs

**Beginner tips:**  
- Set a regular schedule to check for updates (e.g. weekly or monthly).
- Use tools like **WSUS (Windows Server Update Services)** for Windows servers or **YUM/APT** for Linux systems to automate updates.
- Always **test updates in a safe environment** (called a staging environment) before applying them to live systems.
- Keep an **inventory** of all systems and their update status.

---

## 2. Monitoring and Logging

**What is it?**  
Watching over your systems to ensure they are running correctly and keeping logs (records) of what happens.

**Why it matters:**  
- Helps detect problems early (like hardware failure or security breaches)
- Provides insight into system performance
- Keeps track of user activity and errors

**Beginner tips:**  
- Use tools like **Nagios**, **Zabbix**, or **Prometheus** for monitoring.
- Use **Syslog** or **Windows Event Logs** to collect system logs.
- Set up **alerts** (e.g. emails or texts) for critical issues such as low disk space or failed backups.
- Regularly **review logs** to identify unusual activity.

**Explanation of key term:**  
- **LAN (Local Area Network):** A group of computers and devices connected within a short distance (like in an office building). It allows devices to communicate and share data.

---

## 3. Backup and Recovery

**What is it?**  
Creating copies of your important data and systems so you can recover them in case of failure, disaster, or accidental deletion.

**Why it matters:**  
- Protects against data loss
- Enables quick recovery after hardware failures or cyberattacks
- Ensures business continuity

**Beginner tips:**  
- Use the **3-2-1 rule**: Keep 3 copies of your data, on 2 different media types, with 1 copy stored offsite.
- Automate backups using tools like **Veeam**, **Acronis**, or **rsync**.
- Regularly **test your recovery process** to make sure backups work when needed.
- Document what is being backed up, how often, and where the backups are stored.

---

## 4. Documentation and Knowledge Transfer

**What is it?**  
Writing down important information about your systems, processes, and procedures so others (and your future self) can understand and use it.

**Why it matters:**  
- Makes it easier for others to help or take over tasks
- Reduces mistakes by following clear instructions
- Helps during troubleshooting or onboarding new team members

**Beginner tips:**  
- Document system configurations, network layout (including your LAN), and server roles.
- Create step-by-step guides for common tasks (e.g. "How to restart a server" or "How to apply updates").
- Use simple tools like **Markdown files**, **Google Docs**, or **Confluence**.
- Keep documentation **up to date** and easily accessible.
- Encourage team members to contribute and review documentation.

---

## Trade-Offs - Why On-Prem

- **Data Sovereignty Requirements** (e.g. keeping sensitive data within national borders)
- **Low-Latency** edge use cases (e.g. local processing of sensor data)
- **Cost Predictability** in environments with steady, high-volume workloads
- **Regulatory Compliance** that favours physical control over infrastructure

---

# Guide to CPU, RAM, Disk I/O, and Networks (for Data Engineers)

As a new data engineer, you'll be working with data pipelines, databases, and cloud infrastructure — all of which depend on fundamental computer hardware and networking concepts. This guide breaks down four essential components of computing systems:

---

## 1. CPU (Central Processing Unit)

**What it is:**  
The CPU is the brain of the computer. It processes instructions from programs and performs calculations.

**Think of it like:**  
A chef in a kitchen. The CPU follows recipes (instructions) to cook meals (complete tasks). The faster the CPU, the more recipes it can follow in less time.

**Why it matters to you:**  
When processing large datasets or running complex algorithms (like transformations in Spark or ETL jobs), a powerful CPU ensures faster execution.

---

## 2. RAM (Random Access Memory)

**What it is:**  
RAM is temporary memory that stores data and instructions the CPU is actively using. It is fast but only keeps data while the system is on.

**Think of it like:**  
A kitchen counter where the chef (CPU) keeps all the ingredients and tools needed for a current recipe. The bigger the counter (more RAM), the more items you can work with at once.

**Why it matters to you:**  
More RAM allows data pipelines to hold more in-memory data at once — crucial for performance in frameworks like Apache Spark, Pandas, or Dask.

---

## 3. Disk I/O (Input/Output)

**What it is:**  
Disk I/O refers to how data is read from or written to the disk (like SSDs or HDDs). It's the speed and volume of how fast your computer can save or access stored data.

**Think of it like:**  
A pantry or refrigerator — where ingredients are stored long-term. It takes time to fetch items from it. The speed at which the chef (CPU) can get ingredients affects how fast cooking can begin.

**Why it matters to you:**  
Data engineers work with huge datasets. If reading/writing files (CSV, Parquet, JSON, etc.) is slow due to poor Disk I/O, your entire pipeline suffers. SSDs are generally faster than HDDs.

---

## 4. Networks

**What it is:**  
A network allows computers to communicate with each other and share data. This includes local networks and the internet.

### Common Terms:

- **LAN (Local Area Network):**  
  A small network in a limited area, like inside an office or data center. It connects servers, computers, and devices locally.

- **WAN (Wide Area Network):**  
  A larger network that spans cities, countries, or the internet.

- **Bandwidth:**  
  The amount of data that can be transferred over the network in a given time (usually measured in Mbps or Gbps).

- **Latency:**  
  The delay it takes for data to travel from one point to another (measured in milliseconds).

**Think of it like:**  
Roads for delivery trucks. Bandwidth is the number of lanes (how much can be moved), and latency is how fast the truck reaches the destination.

**Why it matters to you:**  
When working with distributed systems (like cloud storage, databases, or Hadoop clusters), data needs to move between machines. High latency or low bandwidth can cause bottlenecks in your data pipeline.

---

## Final Thoughts

Understanding how these four components interact will help you design better, faster, and more efficient data workflows:

- **CPU** = Fast thinking
- **RAM** = Short-term memory for speed
- **Disk I/O** = Long-term storage and access speed
- **Networks** = Communication between machines

These form the backbone of your data infrastructure — optimize them, and your pipelines will thank you!

---

# Practical Technical Guide for Data Engineers to Manage CPU, RAM, Disk I/O, and Networks

This guide is designed for complete beginners in data engineering. It explains how to manage key computing resources — CPU, memory (RAM), Disk I/O, and networks — focusing on optimizing on-premise data pipelines. It also covers how to evaluate trade-offs between performance and resource consumption, and how to use scheduling, batching, and buffering to improve system efficiency.

---

## Key Concepts

- **CPU (Central Processing Unit):** The "brain" of the computer that processes instructions.
- **RAM (Random Access Memory):** Temporary memory used to store data for quick access while programs are running.
- **Disk I/O (Input/Output):** The process of reading and writing data to storage disks.
- **Network:** The system that allows computers to communicate, such as LAN (Local Area Network) — a network that connects computers within a limited area like an office.

---

## 1. Optimizing CPU, Memory, and I/O Usage in On-Premise Pipelines

When working with data pipelines on physical servers ("on-premise" means the servers are located within your organization, not in the cloud), efficient use of CPU, RAM, and Disk I/O is critical for speed and stability.

### CPU Optimization
- **Understand workload patterns:** Know which tasks require heavy computation (like data transformations) and which are lightweight.
- **Parallel processing:** Split tasks into smaller parts that can run simultaneously on multiple CPU cores to speed up processing.
- **Avoid CPU bottlenecks:** Monitor CPU usage and reduce the complexity of tasks if CPU usage is consistently high.

### Memory (RAM) Optimization
- **Manage data size:** Load only necessary data into memory. Large datasets can consume too much RAM and cause slowdowns.
- **Use memory efficiently:** Use data structures and algorithms that require less memory.
- **Prevent memory leaks:** Make sure programs release memory when no longer needed to avoid exhausting RAM.

### Disk I/O Optimization
- **Reduce unnecessary disk access:** Read and write data in larger chunks instead of many small operations.
- **Use faster disks or RAID setups:** Solid State Drives (SSDs) and RAID (Redundant Array of Independent Disks) configurations can improve speed.
- **Cache data in memory:** Temporarily keep frequently accessed data in RAM to reduce disk reads.

---

## 2. Evaluating Trade-offs Between Performance and Resource Consumption

When optimizing, improving one resource might use more of another. For example:

- **Faster CPU usage vs. higher power consumption:** Running many processes in parallel can speed up a task but increases CPU usage and energy costs.
- **More memory usage vs. fewer disk I/O operations:** Holding more data in RAM can reduce slow disk reads but risks running out of memory.
- **Network bandwidth vs. local processing:** Transferring data across the network (LAN) can offload processing but may cause network congestion.

**How to evaluate:**

- **Set clear goals:** Decide if speed, cost, or resource availability is most important.
- **Monitor resources:** Use tools to measure CPU, memory, disk, and network usage during pipeline runs.
- **Test different configurations:** Try different approaches and measure their impact on performance and resource use.
- **Balance resource use:** Aim for a solution that meets your needs without wasting resources.

---

## 3. Using Scheduling, Batching, and Buffering to Improve System Efficiency

### Scheduling
- **Definition:** Deciding when to run different tasks or pipelines.
- **Practical use:** Run heavy tasks during off-peak hours to avoid overwhelming CPU or disk during busy times.
- **Benefits:** Smoother resource usage and avoids bottlenecks.

### Batching
- **Definition:** Grouping multiple smaller tasks or data units together to process at once.
- **Practical use:** Instead of processing each data record individually, collect many records and process them as a batch.
- **Benefits:** Reduces overhead from repeated task startup and improves disk I/O efficiency by reading/writing larger blocks.

### Buffering
- **Definition:** Temporarily storing data in memory or disk between pipeline stages.
- **Practical use:** If one step produces data faster than the next step can consume it, use a buffer to hold this data temporarily.
- **Benefits:** Prevents pipeline stalls, smooths out spikes in data flow, and optimizes CPU and disk use by balancing work.

---

## Summary

- **Optimize CPU:** Use parallelism wisely, avoid bottlenecks.
- **Optimize RAM:** Load only necessary data, manage memory carefully.
- **Optimize Disk I/O:** Minimize small reads/writes, use caching.
- **Balance trade-offs:** Consider resource costs vs. performance gains.
- **Improve efficiency:** Use scheduling, batching, and buffering.

By understanding and applying these principles, you can build and maintain efficient data pipelines that make the best use of your on-premise infrastructure.

---

# Introduction to Load Balancing and Scheduling in Data Engineering

## What is Load Balancing?

Load balancing is a technique used to distribute work evenly across multiple resources—like servers, databases, or data processing nodes—so that no single resource becomes overwhelmed. Imagine you have many tasks to complete, and several workers available. Instead of giving all tasks to one worker, you spread them out evenly so everyone is busy but not overloaded. This helps systems run faster and more reliably.

In data engineering, load balancing ensures that data processing jobs or requests are spread out across multiple machines or services. This prevents bottlenecks and improves the overall efficiency and stability of data pipelines.

### Why is Load Balancing Important?

- **Improves performance:** By distributing tasks, the workload is shared, reducing delays.
- **Increases reliability:** If one resource fails, others can take over, preventing downtime.
- **Enhances scalability:** Systems can handle more data or users by adding more resources.
- **Prevents resource exhaustion:** Avoids overloading any single machine or service, which can cause crashes or slowdowns.

## What is Scheduling?

Scheduling in data engineering refers to deciding *when* and *how* data jobs or tasks should run. These jobs might include moving data from one place to another, transforming data, or running analyses.

Scheduling is like setting a calendar or timetable for your data tasks. Instead of running everything all at once or manually starting each task, you automate their execution based on specific times, events, or dependencies.

### Why Does Scheduling Matter?

- **Ensures timely data availability:** Data tasks run at the right time, so fresh and accurate data is ready when needed.
- **Manages dependencies:** Some jobs depend on others finishing first; scheduling makes sure tasks happen in the correct order.
- **Optimizes resource use:** By scheduling jobs during off-peak hours or spacing them out, it avoids overloading systems.
- **Enables automation:** Reduces manual work, saving time and minimizing human error.

## How Load Balancing and Scheduling Work Together

Effective data engineering requires both load balancing and scheduling. Scheduling decides *when* tasks run, while load balancing ensures *where* they run so that resources are used efficiently and reliably.

Together, they help build data systems that are:

- **Efficient:** Tasks complete faster and use resources wisely.
- **Reliable:** Systems stay up and running, even if some parts fail.
- **Scalable:** Can grow to handle more data or users without major redesigns.
- **Maintainable:** Easier to manage and automate complex workflows.

---

Understanding load balancing and scheduling is key for anyone starting in data engineering, as these concepts help build strong, dependable data pipelines that power modern applications and analytics.

---

## Common Strategies for Load Balancing in On-Premise Data Workloads

1. **Round Robin Distribution**  
   Tasks are assigned cyclically across resources to ensure an even spread.

2. **Resource-Based Distribution**  
   Tasks are assigned based on current load or capacity of each resource (e.g., CPU usage, memory).

3. **Data Locality-Aware Distribution**  
   Assign tasks to servers where the required data already exists to minimize data transfer time.

4. **Priority-Based Load Balancing**  
   Certain high-priority jobs get assigned to less busy or faster resources.

5. **Failover and Redundancy**  
   Keep backup servers ready to take over if one resource fails.

---

## Common Strategies for Scheduling in On-Premise Data Workloads

1. **Time-Based Scheduling**  
   Jobs are triggered at fixed times (e.g., daily at midnight) or intervals.

2. **Event-Based Scheduling**  
   Jobs start when a specific event occurs, such as new data arrival or completion of another task.

3. **Dependency Scheduling**  
   Workflows are broken into dependent tasks where subsequent tasks wait for predecessors.

4. **Resource-Aware Scheduling**  
   Jobs are scheduled considering current system load to avoid overloading.

5. **Batch vs. Real-Time Scheduling**  
   - **Batch:** Run large jobs during off-peak hours to maximize throughput.  
   - **Real-Time:** Schedule smaller, immediate jobs that require quick responses.

---

## Common Tools for Load Balancing and Scheduling On-Premise

### Load Balancing Tools

- **HAProxy**  
  A popular open-source load balancer primarily used for distributing network and HTTP traffic but also applicable for balancing API or data services.

- **Linux Virtual Server (LVS)**  
  A kernel-level load balancer suitable for distributing network connections across multiple servers.

- **Kubernetes (On-Premise Cluster)**  
  Though often associated with cloud, Kubernetes can run on-premise and handle load balancing across containerized workloads.

- **Apache Hadoop YARN**  
  Manages cluster resources and load balancing across distributed data processing tasks.

---

### Scheduling Tools

- **Apache Airflow**  
  Widely used open-source workflow scheduler to programmatically author, schedule, and monitor data pipelines.

- **Apache Oozie**  
  A workflow scheduler specifically for Hadoop jobs.

- **Cron**  
  A simple time-based job scheduler available on most Unix/Linux systems, good for straightforward task scheduling.

- **Azkaban**  
  Batch workflow job scheduler created at LinkedIn to run Hadoop jobs in a reliable way.

- **Kubernetes CronJobs**  
  For containerized environments, Kubernetes offers native scheduling capabilities.

- **Prefect**
  Popular in high-performance computing, allows fine control over job queues, priorities, and system usage.

- **SLURM**
  Popular in high-performance computing, allows fine control over job queues, priorities, and system usage.
  
---

## Summary

| Concept        | What it Does                         | Example Strategy                     | Common Tool Examples               |
|----------------|------------------------------------|------------------------------------|----------------------------------|
| Load Balancing | Distributes tasks evenly            | Round Robin, Resource-based         | HAProxy, LVS, Hadoop YARN, Kubernetes |
| Scheduling     | Automates when and how jobs run     | Time-based, Event-based, Dependency | Apache Airflow, Oozie, Cron, Azkaban  |

---

## Final Tips for Beginners

- Start by understanding your current resource capacity and workload patterns.
- Use simple scheduling tools like **cron** for small tasks and gradually move to sophisticated tools like **Airflow** for complex workflows.
- Monitor system performance regularly to identify bottlenecks.
- Design workflows to minimize data movement by leveraging data locality.
- Keep fault tolerance and failover plans in place for reliability.

---




