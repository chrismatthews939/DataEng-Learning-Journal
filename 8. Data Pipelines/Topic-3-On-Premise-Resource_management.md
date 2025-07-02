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


