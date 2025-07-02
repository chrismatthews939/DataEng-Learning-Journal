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


