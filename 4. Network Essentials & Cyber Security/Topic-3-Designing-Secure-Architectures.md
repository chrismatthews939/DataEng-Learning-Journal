# Topic 3 Designing Secure Architectures 20/02/2025

## The three phases of cybersecurity architecture

Designing secure data products and pipelines is centred around the idea of the three phases of cybersecurity architecture based on developing, implementing, and monitoring (using standards and best practices).

### Phase 1 Develop

**Objective**: To design a robust cybersecurity framework tailored to the organisation’s needs.

**Description:** The development phase involves creating the foundational elements of the cybersecurity architecture.

This includes identifying the organisation's specific security requirements, assessing risks, and defining security policies and procedures.

During this phase, architects will reference established standards and best practices such as ISO/IEC 27001, NIST Cybersecurity Framework, etc.

These standards provide guidelines for creating a comprehensive security strategy that addresses various aspects of cybersecurity, including data protection, access control, and risk management.

The outcome is a detailed security plan that outlines the necessary controls, processes, and technologies to be implemented.

### Phase 2 - Implement

**Objective:** To deploy the cybersecurity measures designed in the development phase.

**Description:** In the implementation phase, the strategies and plans devised during the development phase are put into action.

This involves setting up technical controls like firewalls, antivirus software, encryption tools, and intrusion detection systems.

Administrative controls, such as security policies, training programmes, and incident response plans, are also established.

It's crucial to ensure that all implementations align with the predefined standards and best practices.

This phase often includes extensive testing to verify that the security measures function as intended and provide adequate protection against identified threats.

### Phase 3 - Monitor

**Objective:** To ensure the ongoing effectiveness and efficiency of the cybersecurity measures.

**Description:** The monitoring phase focuses on continuously observing and assessing the performance of the implemented security measures. This involves real-time monitoring of systems and networks for any unusual activities or potential security incidents.

Tools such as Security Information and Event Management (SIEM) systems, automated threat detection, and regular audits are employed. Continuous monitoring allows for the timely detection of vulnerabilities and threats, ensuring that security measures remain effective against evolving risks.

Additionally, this phase includes reviewing and updating security policies and procedures to adapt to new standards, technologies, and threat landscapes. Regular reporting and analysis help in refining and improving the cybersecurity architecture.

## What is secure network design?

**Elements of secure network design:**

**Defence in Depth (Layered Security)**
- Implement multiple layers of security measures to protect network resources. If one layer fails, others still provide protection, including physical security, network segmentation, and application firewalls.

**Network segmentation**
- Divide the network into smaller, secure segments using physical or virtual separation. This limits an attacker's ability to move laterally within the network and contains potential breaches to smaller segments.

**Secure by default**
- Devices and software should be deployed with the most secure configuration possible. Unnecessary services and features should be disabled to minimise potential vulnerabilities.

**Zero trust architecture**
- Operate under the assumption that threats can originate from both outside and inside the network. Verify the identity and integrity of devices, users, and software at all times, regardless of location.

**Encryption**
- Use strong encryption for data at rest and in transit to protect sensitive information from interception and ensure confidentiality.

**Regular updates and patch management**
- Keep all systems, software, and devices updated with the latest security patches to protect against known vulnerabilities.

**Intrusion detection and prevention**
- Implement systems that can detect and block suspicious activities or known attack patterns in real-time.

**Comprehensive monitoring and logging**
- Continuously monitor network activity and maintain detailed logs to detect unusual behaviour patterns, security incidents, and help in forensic analysis.

**Resilience and redundancy**
- Design the network to maintain essential functions and quickly recover from any disruption. This includes redundant network paths, failover systems, and regular backups.

**Secure remote access**
- Provide secure and controlled remote access methods, such as VPNs with strong authentication, to ensure secure connectivity for remote users.

**Security awareness and training**
- Regularly educate employees about security best practices, potential threats, and their roles in maintaining cybersecurity.

**Least Privilege Access**
- Limit user and device access rights to only those necessary for performing a defined set of tasks. This minimises the potential damage from accidental or malicious actions.

## The five rules of networking

*Success is the sum of small efforts, repeated day in and day out.*

#### Rule 1 - Redundancy
 
Network redundancy is a critical infrastructure design strategy that involves creating additional or alternative instances of network devices and communication mediums to ensure network availability and reliability.

This approach is used to prevent or minimise downtime and service interruptions in the event of hardware failures, software crashes, network congestion, or other issues that can affect the primary network pathways.

```
By implementing redundant components such as routers, switches, data paths, and connections, organisations can ensure that if one part of the network fails, the data traffic can automatically reroute through another, maintaining continuous operation.

Redundancy can be achieved through various methods, including duplicate hardware, failover clustering, load balancing, and having multiple data centres.

The goal is to provide a seamless experience for users and maintain business operations without disruption, enhancing the overall resilience of the network against faults and failures.
```

#### Rule 2 - Scalability

Network scalability refers to the ability of a network to grow and manage increased demand without compromising performance or requiring a complete overhaul of the infrastructure.

A scalable network is designed to accommodate growth in the number of users, devices, traffic volume, or application services efficiently and cost-effectively.

This is achieved through thoughtful planning and the use of scalable network architectures, such as modular hardware, flexible software solutions, and technologies like cloud services and virtualisation.


```
Scalability allows for the incremental expansion of network resources (such as bandwidth, storage, and processing capacity) to meet evolving needs, ensuring that the network remains robust, responsive, and capable of supporting new applications and technologies as they emerge.

In essence, network scalability is crucial for ensuring that the network can adapt to future demands, facilitating seamless expansion and upgrades as an organisation or its services grow.

Cloud Scalability is called elasticity - Cloud elasticity refers to the ability of a cloud computing environment to dynamically allocate and de-allocate resources as needed to accommodate fluctuating workloads.
```

#### Rule 3 - Security

Network security encompasses a broad set of policies, practices, and tools designed to protect the integrity, confidentiality, and accessibility of computer networks and data using both hardware and software technologies.

It aims to safeguard against unauthorised access, cyberattacks, and other threats that can compromise network operations and sensitive information.

```
Effective network security involves a layered approach that combines multiple defensive mechanisms at the edge and within the network.

This includes firewalls, antivirus software, intrusion detection and prevention systems (IDPS), virtual private networks (VPNs), and strict access controls alongside regular security assessments, vulnerability scanning, and user education.

By addressing a wide range of potential security risks, network security ensures that organisations can maintain the trust of their customers and partners, comply with regulatory requirements, and protect their assets from both internal and external threats.
```

#### Rule 4 - Manageability

Network manageability refers to the ease with which a network can be monitored, configured, maintained, and optimised to ensure its efficient and effective operation.

It encompasses the tools, processes, and policies that network administrators use to manage network resources, performance, and security.

```
Good network manageability allows for quick identification and resolution of issues, efficient allocation of resources, and adaptation to changing demands and threats.

This is achieved through a combination of network management software that provides comprehensive visibility into network activity, automated alerting systems for early detection of problems, and configuration management tools that enable rapid adjustments to network settings.

Ultimately, network manageability ensures that networks remain robust, secure, and able to support the ongoing needs of the organisation or users it serves.
```

#### Rule 5 - Functionality

Network functionality encompasses the range of capabilities and services that a network is designed to provide to support communication among devices and facilitate the efficient and effective transmission of data.

This includes basic services such as connectivity, routing, and switching, which allow devices to connect to the network and communicate with each other, as well as more advanced functionalities like load balancing, fault tolerance, quality of service (QoS), and security measures designed to optimise network performance and protect data.

```
Network functionality also extends to support for various applications and protocols that enable a wide array of activities, from simple file sharing and email to complex cloud computing and online streaming services.

Ensuring robust network functionality requires careful planning, implementation, and management of the network infrastructure and services to meet the specific needs and expectations of its users, whether they are individual consumers, businesses, or larger organisations.
```

## Defence in Depth (DID) and Zero-Trust Architecture (ZTA)

### Understanding Defence in Depth

The cybersecurity concept of 'defence in depth' is a strategy that employs multiple layers of security measures and controls across the various parts of an organisation's information systems and networks to protect against threats and unauthorised access. Inspired by military tactics, this approach is predicated on the principle that if one layer of defence fails, additional layers will provide continued protection.


![defence in depth](https://pronto-core-cdn.prontomarketing.com/2/wp-content/uploads/sites/3415/2015/11/ProactiveProtection_CircleChart.jpg)

### Zero trust

The zero-trust security model is a cybersecurity approach that denies access to an enterprise's digital resources by default and grants authenticated users and devices tailored, siloed access to only the applications, data, services and systems they need to do their jobs. Gartner has predicted that by 2025, 60% of organisations will embrace a zero-trust security strategy. Historically, enterprises have relied on a castle-and-moat cybersecurity model, in which anyone outside the corporate network perimeter is suspect and anyone inside gets the benefit of the doubt. The assumption that internal users are inherently trustworthy, known as implicit trust, has resulted in many costly data breaches, with attackers able to move laterally throughout the network if they make it past the perimeter.

![Zero trust](https://network-insight.net/wp-content/uploads/2022/07/AdobeStock_657436912-scaled.jpeg)

Instead of focusing on user and device locations relative to the perimeter -- i.e., inside or outside the private network -- the zero-trust model grants users access to information based on their identities and roles, regardless of whether they are at the office, at home or elsewhere. In zero trust, authorisation and authentication happen continuously throughout the network, rather than just once at the perimeter. Zero Trust networking is centred on the belief that organisations should not automatically trust anything inside or outside their perimeters and instead must verify anything and everything trying to connect to its systems before granting access. This is a logical continuation of DID.  


#### Utilising Micro-Segmenting and Advanced Security Layers

Micro-segmenting and advanced security layers are crucial for protecting data pipelines in modern network architectures. This lesson explores how these techniques can enhance security by providing fine-grained control over network traffic and isolating sensitive data. Traditional network segmentation methods, such as VLANs and subnets, are no longer sufficient to address the sophisticated threats faced by modern networks. Micro-segmenting offers a higher level of security by creating smaller, more manageable segments, while advanced security layers add depth to the defence strategy.

Micro-segmenting involves using software-defined networking (SDN) to create very small, isolated segments within a network. This allows for precise control over traffic flows and limits the lateral movement of threats. In contrast, VLANs operate at the data link layer (Layer 2) and are used to segment networks into broadcast domains, which helps in managing traffic and improving security but does not provide the same level of granularity as micro-segmenting. Subnets operate at the network layer (Layer 3) and are primarily used for IP address management and routing efficiency, but they also fall short in providing the fine-grained control that micro-segmenting offers.

**Advanced Security Layers**

Implementing zero trust architecture, which requires verification for every access request, and endpoint security solutions that protect devices from malware and other threats, adds another layer of defence. Open-source frameworks such as Apache Kafka for real-time data processing, Istio for managing microservices traffic, and Calico for network security in Kubernetes, provide tools that can enhance security in micro-segmented environments.

## Firewalls and DMZ

*An ounce of prevention is worth a pound of cure*

### What are network firewalls?

Network firewalls are critical components of network security, acting as barriers between internal networks and external threats. They monitor and control incoming and outgoing network traffic based on predetermined security rules. Over time, different types of firewalls have been developed to address various security needs. Some prominent modern firewall types include the following:

**Proxy Firewalls (Application-Level Gateways)**
Proxy firewalls act as intermediaries between users and the internet, making network requests on behalf of users. They provide high levels of security by separating end-users from the external network, inspecting and filtering traffic at the application layer.

**Next-Generation Firewalls (NGFW)**
These combine the capabilities of traditional firewalls with additional features like application awareness and control, integrated intrusion prevention, and cloud-delivered threat intelligence. NGFWs are designed to offer more granular control and protection against advanced threats.

**Unified Threat Management (UTM)**
UTM devices consolidate multiple security and networking functions all in one appliance. This includes antivirus, anti-spam, network firewall functions, intrusion detection and prevention, content filtering, and VPN capabilities. UTMs are appreciated for their simplicity and ease of use, making them suitable for small to medium-sized businesses.

**Web Application Firewalls (WAF)**
WAFs specifically protect web applications by monitoring and filtering HTTP traffic between a web application and the Internet. They apply a set of rules to HTTP conversation to cover common attacks such as cross-site scripting (XSS) and SQL injection, thereby protecting against web application attacks.

#### Common firewall designs

There are also three common firewall designs including Public and Private, DMZ Security Architecture, and DMZ. Let's explore these now:

**Public and private**

This architecture is used in SOHO and small branch office environments. As shown in the figure, the public network (or outside network) is untrusted, and the private network (or inside network) is trusted. Typically, a firewall with two interfaces is configured as follows:

- Traffic originating from the private network is permitted and inspected as it travels toward the public network. Inspected traffic returning from the public network and associated with traffic that originated from the private network is permitted.
- Traffic originating from the public network and travelling to the private network is generally blocked.

#### DMZ Security Architecture

A DMZ is a physical or logical subnet that separates an internal local area network (LAN) from untrusted external networks, usually the internet. The DMZ adds an additional layer of security to an organisation's local network by segregating public-facing services and systems from the internal network, reducing the risk of external attacks reaching internal resources.

- **Interesting Fact:** The concept of a DMZ originated from military terminology, where it describes a buffer zone between hostile forces.
- **Technique:** Use multiple layers of firewalls to create a robust DMZ.
- **Consideration:** Regularly update and patch systems in the DMZ to mitigate vulnerabilities.

A demilitarized zone (DMZ) firewall design has typically one inside interface connected to the private network, one outside interface connected to the public network, and one DMZ interface. This architecture is used in classic network security for Small to medium enterprise (SME).  

![DMZ](https://www.techtarget.com/rms/onlineimages/sdn-dmz_network_architecture_mobile.png)

#### How does this work?

- Traffic originating from the private network is inspected as it travels toward the public or DMZ network. This traffic is permitted with little or no restriction. Inspected traffic returning from the DMZ or public network to the private network is permitted.
- Traffic originating from the DMZ network and traveling to the private network is usually blocked.
- Traffic originating from the DMZ network and traveling to the public network is selectively permitted based on service requirements.
- Traffic originating from the public network and traveling toward the DMZ is selectively permitted and inspected. This type of traffic is typically email, DNS, HTTP, or HTTPS traffic. Return traffic from the DMZ to the public network is dynamically permitted.
- Traffic originating from the public network and traveling to the private network is blocked.

#### Zone-Based Policy Firewalls

Zone-based policy firewalls (ZPFs) use the concept of zones to provide additional flexibility. A zone is a group of one or more interfaces that have similar functions or features. Zones help you specify where a firewall rule or policy should be applied. In the figure, security policies for LAN 1 and LAN 2 are similar and can be grouped into a zone for firewall configurations. By default, the traffic between interfaces in the same zone is not subject to any policy and passes freely. However, all zone-to-zone traffic is blocked. In order to permit traffic between zones, a policy allowing or inspecting traffic must be configured.

## Additional security considerations

#### Intrusion Detection System (IDS)
**Description**
An IDS monitors network traffic for suspicious activity and signs of possible attacks. It's designed to detect and alert on potential security breaches but does not take action to block them.

IDS appliances can be signature-based (detecting known patterns of malicious activity) or anomaly-based (detecting deviations from normal traffic patterns).

#### Intrusion Prevention System (IPS)
**Description**
Similar to an IDS, an IPS monitors network and/or system activities for malicious activities or policy violations. The key difference is that an IPS is placed in-line and can automatically block or prevent such activities as they are detected, offering proactive protection.

#### Virtual Private Network (VPN) Appliance
**Description**
VPN appliances provide secure remote access to a network or between networks over the Internet by encrypting connections. They are used to enable secure remote access for users or secure connections between sites, ensuring that data transmitted over public networks is protected.

#### Secure Web Gateway (SWG)
**Description**
SWGs protect users from web-based threats and enforce company policies through web filtering, application control, and malware inspection. They are deployed to monitor and control user web traffic, preventing access to malicious websites or content that does not comply with policy. (See FortiGuard and cisco Talos for examples)

#### Data Loss Prevention (DLP)
**Description**
DLP appliances are focused on detecting and preventing the unauthorized use and transmission of confidential information. They monitor, detect, and block sensitive data while in use (endpoint actions), in motion (network traffic), and at rest (data storage).

#### Private VLANs (PVLANs)
**Description**
PVLANs are used to segment the network at the data link layer (Layer 2). They allow for isolation between hosts within the same VLAN, preventing direct communication between devices in the same broadcast domain which is useful for limiting access to sensitive devices.

#### Storm Control
**Description**
Storm Control prevents disruptions on a switch port caused by broadcast, multicast, or unicast storms. It automatically shuts down or limits the rate of these types of traffic when they exceed configured thresholds.

## Advanced encryption

Encryption is a cornerstone of data security, ensuring that sensitive information remains confidential and protected from unauthorised access.  With the increasing frequency and sophistication of data breaches, applying robust encryption techniques is crucial for protecting personal, financial, and business information. Compliance with security standards ensures that encryption methods meet industry best practices and regulatory requirements. Encryption is used in various scenarios, such as securing online transactions, protecting personal data stored on devices, and safeguarding communication channels. Symmetric encryption, like AES, is often used for its efficiency in encrypting large amounts of data quickly. Asymmetric encryption, such as RSA, is widely used in securing communications and digital signatures due to its strong security properties. For data at rest, tools like BitLocker and FileVault provide full disk encryption, while TLS is a standard for securing data in transit over the internet.

**Why Secure Key Management is Essential**

Here's why:

1. Prevent Unauthorised Access: Encryption keys are the keys to the kingdom.

2. Maintain Data Integrity and Confidentiality: Proper key management ensures that data remains secure, preserving its integrity and confidentiality. This is particularly important for sensitive information such as financial records, personal data, and intellectual property.

3. Compliance with Regulations: Many industries are subject to strict regulatory requirements regarding data protection. Secure key management helps organisations comply with standards which mandate stringent measures for protecting encryption keys.

#### Hardware Security Modules (HSMs)

An HSM is a dedicated hardware device designed to generate, store, and manage cryptographic keys securely. HSMs are tamper-resistant and provide a high level of security for key management operations. Advantages of HSMs include:

- **Physical Security:** HSMs are designed to resist physical tampering. If someone tries to tamper with the device, it can automatically destroy the keys it holds.
- **High Assurance:** HSMs are certified to high security standards (e.g., FIPS 140-2 Level 3 or 4), providing confidence in their ability to protect keys.
- **Performance:** HSMs can handle cryptographic operations quickly and efficiently, making them suitable for high-performance environments.
- **Integration**: Integrate HSMs with your encryption software to offload key management operations to the secure hardware device. Most HSMs provide APIs and SDKs for seamless integration.
- **Key Generation and Storage:** Use the HSM to generate encryption keys. Store the keys within the HSM to ensure they are never exposed outside the secure hardware environment.
- **Access Control:** Configure strong access controls on the HSM to ensure that only authorized personnel can perform key management operation

### Key Management Services (KMS)

A KMS is a cloud-based service that provides secure key management capabilities. KMS solutions, such as AWS Key Management Service (AWS KMS) or Azure Key Vault, offer a scalable and convenient way to manage encryption keys without the need for dedicated hardware. The advantages of KMS include:

- **Scalability:** KMS solutions can scale to manage a large number of keys, making them suitable for dynamic and growing environments.
- **Ease of Use:** Cloud providers offer integrated key management services that are easy to set up and use, with features like automated key rotation and lifecycle management.
- **Cost-Effective:** KMS solutions eliminate the need for upfront investment in hardware, making them a cost-effective option for secure key management.

**Practical Implementation:**

**Setup:** Create and configure a KMS instance through your cloud provider's management console. Define key policies that specify who can use and manage the keys.

**Key Management:** Use the KMS to create, rotate, and retire keys as needed. Take advantage of automated key rotation features to regularly update keys without manual intervention.

**Integration:** Integrate your applications and services with the KMS using provided APIs. This allows your applications to securely use the keys for encryption and decryption operations without exposing them.

**Monitoring and Auditing:** Enable logging and monitoring features to track key usage and management activities. Regularly review audit logs to ensure compliance and detect any unauthorised access attempts.

## Visual methods for secure architectures and full stack systems

Visual methods, such as diagrams and flowcharts, are used to represent and communicate the design of secure architectures. These visual tools help in understanding complex systems, identifying potential security vulnerabilities, and ensuring that all stakeholders have a clear and consistent understanding of the security measures in place.

**Interesting Fact:** Visual representations can reduce the time required to understand a complex architecture by up to 40%.

**Technique:** Use standard symbols and consistent notation for clarity.

**Consideration:** Keep diagrams up-to-date to reflect the current architecture accurately.

### How to design secure architectures

When designing a secure network for a financial institution, creating detailed network diagrams that highlight the placement of firewalls, DMZs, and intrusion detection systems can help in ensuring comprehensive protection. Network diagrams visualise network components and their connections, helping to understand the overall structure and identify weak points. System architecture diagrams show the different layers of an application stack and the security measures implemented at each layer. Flowcharts map out processes and data flows, ensuring that all steps are secure and efficient.

### Best practices for effective security architecture

Creating a security architecture diagram is not enough; it needs to be regularly maintained for it to be effective. Regular updates also help in reflecting the current state of the organisation’s security posture, ensuring that any new systems or technologies are appropriately represented in the diagram. Additionally, conducting reviews with key stakeholders can provide valuable insights and perspectives for enhancing the diagram’s effectiveness.

#### Managing attack surfaces in full-stack systems

Full-stack systems encompass all the technologies and layers involved in the development and operation of a comprehensive application. This includes the front-end, back-end, database, and infrastructure components. Given the complexity of these systems, ensuring robust security across all layers is crucial to defend against various cyber threats.

#### Understanding attack surfaces in full-stack systems

An attack surface refers to all the points where an unauthorized user can try to enter data to or extract data from an environment. Every layer of a full-stack system can potentially expand the attack surface, and a vulnerability in any layer could compromise the entire application. Therefore, it is essential to implement stringent security measures at each stage of development and operation.

Key practices for secure full-stack systems:

- **Secure coding practices:** Ensure that secure coding guidelines are followed to prevent common vulnerabilities such as SQL injection, XSS, etc.
- **Regular security audits:** Conduct comprehensive audits to identify and rectify security flaws within the system.
- **Frequent updates:** Keep all components updated to protect against known vulnerabilities.
  
# Lecture

**Authentication**
verifying who someone is

**Authorization**
Dictating what someone can do

**Service**
Special software interface that enables access to a particular functionality

**Service account**
A special account with escalated privileges. Like a backstage pass at a festival

**Open Design**
Hiding methods of design does not secure your system

#### Practical Security Principals

**Secure Communication:**
Ensure data transmitted is encrypted and authenticated 

**Secure configuration:**
Setting up system components follow best practices

**Anti-patterns:**
Common but flawed approaches. 
- Example: Hardcoding API keys in Git repo or something

#### Key Secure Networking Protocols 

**SSL/TLS** - Secure sockets layer/transport layer security
- Cryptographic protocol designed to provide secure communication over a computer network
- Protects data during transmission
- Vunerable to "man in the middle" attacks where unautorised parties can intercept traffic

![SSL Handshake](https://www.clickssl.net/wp-content/uploads/2020/10/ssl-handshake-explained.jpg)

**Downgrade attacks**
Forces a connection to use older less secure versions making them vunerable
To mitigate you can force use of the latest version

**VPN** - Stop people ease dropping e.g. PPTP, L2TP, OpenVPN, IPsec

![VPN](https://blog-api.hidemyacc.com/posts/content/images/ex0inb4v54benl4ojuhqwgmwhnra8uows7thd8k3sgjj5nhjtnvirvhbubweeigrr4mt.png)

## Understanding VPNs

### What is a VPN?

A **VPN (Virtual Private Network)** is a service that creates a secure, encrypted connection between your device (like your computer or smartphone) and the internet. It acts like a private tunnel for your online activities, keeping your data safe from prying eyes.

### How Does a VPN Work?

1. **Establishing a Secure Connection:**  
   When you activate a VPN, your device connects to a VPN server. This connection forms a private "tunnel" that your data travels through.

2. **Encryption:**  
   The VPN encrypts your data, which means it scrambles your information so that anyone who intercepts it (like hackers or your internet service provider) cannot read it.

3. **Data Transmission Through a Tunnel:**  
   Your internet traffic (websites you visit, emails you send, etc.) travels through this secure tunnel to the VPN server. Because the data is encrypted, it stays private and secure.

4. **IP Address Masking:**  
   After passing through the VPN server, your data goes out onto the internet. The websites you visit see the IP address of the VPN server, not your real IP address. This helps keep your location and identity hidden.

### Why Use a VPN?

- **Enhanced Security:**  
  Using a VPN, especially on public Wi-Fi networks (like in cafés or airports), helps protect your sensitive information from hackers.

- **Increased Privacy:**  
  By masking your IP address and encrypting your data, a VPN makes it much harder for websites and online services to track your activities.

- **Access to Restricted Content:**  
  VPNs allow you to appear as if you're browsing from a different location. This can help you access websites or streaming services that might be restricted or censored in your area.

### Summary

A VPN is a valuable tool that safeguards your online privacy and security by:
- Creating a secure, encrypted tunnel for your data.
- Hiding your real IP address and location.
- Helping you bypass content restrictions.

Whether you're looking to protect your personal information on public Wi-Fi or simply want to browse the internet with more privacy, a VPN is a practical solution for maintaining online security.

## SSH Tunnelling Explained

SSH tunnelling is a technique that uses the SSH (Secure Shell) protocol to create an encrypted "tunnel" between your computer and a remote server. This tunnel securely transports data across an insecure network, such as the internet, protecting it from eavesdropping or tampering.

### Why Use SSH Tunnelling?

- **Security:** All data passing through the tunnel is encrypted, which helps protect sensitive information.
- **Bypassing Restrictions:** It can help you bypass firewalls or network restrictions by routing traffic through a secure connection.
- **Remote Access:** It allows you to access services on a remote server securely, as if they were on your local machine.

### How Does SSH Tunnelling Work?

1. **Establish an SSH Connection:** You begin by connecting to a remote server using the SSH protocol.
2. **Create an Encrypted Tunnel:** Once connected, SSH establishes an encrypted pathway (the tunnel) between your local machine and the remote server.
3. **Forward Data:** Data sent from your local machine is securely "forwarded" through the tunnel to the remote server, and vice versa.

### Types of SSH Tunnelling

There are three common types of SSH tunnelling:

#### 1. Local Port Forwarding

- **Description:** Redirects traffic from a port on your local machine to a specified remote address and port.
- **Use Case:** Accessing a web server running on a remote machine as if it were running locally.

#### 2. Remote Port Forwarding

- **Description:** Forwards traffic from a port on the remote server to a port on your local machine.
- **Use Case:** Allowing someone on the remote server to access a service running on your local machine.

#### 3. Dynamic Port Forwarding

- **Description:** Sets up a SOCKS proxy that dynamically forwards traffic to any destination.
- **Use Case:** Securely browsing the internet by routing your web traffic through the SSH server.

---

**RDP** - Remote Desktop Protocol
**SNMP** - Simple Network Management Protocol
**SSH** - Secure shell. Command line

**HTTPS** Hypertext transfer protocol secure
Comines HTTP with SSL/TLS to provide encrypted transmission of data

### APIs

Rest API - Set of rules that allow things to communicate

![Rest API](https://images.ctfassets.net/vwq10xzbe6iz/5sBH4Agl614xM7exeLsTo7/9e84dce01735f155911e611c42c9793f/rest-api.png)

## What is an API?

API stands for Application Programming Interface. It acts as a bridge that allows different software applications to communicate with each other.

Think of an API like a waiter in a restaurant:
- You (the user) request food from the menu (send a request to the API).
- The waiter (API) takes your order to the kitchen (the system/server).
- The kitchen prepares the food (processes the request).
- The waiter brings the food back to you (returns the response).

**Why Are APIs Important?**

APIs allow developers to:
- Access services and data from other applications.
- Automate processes.
- Integrate different systems easily.

**Types of APIs**

There are several types of APIs:
- **REST (Representational State Transfer)** - Uses HTTP requests (GET, POST, PUT, DELETE) to interact with data.
- **SOAP (Simple Object Access Protocol)** - Uses XML messaging for communication.
- **GraphQL** - Allows clients to request only the specific data they need.
- **WebSockets** - Enables real-time, two-way communication.

**How Does an API Work?**

APIs usually follow a request-response cycle:
- The client (a web app, mobile app, or another system) sends a request.
- The API processes the request and communicates with the server.
- The server sends back a response (data or an action confirmation).

--- 

### General best practices

- Regularly update software and libraries
- Use strong unqiue certificates and keep private keys secure
- Monitor for anomolies

# OWASP Top 5 Vulnerabilities

The **Open Web Application Security Project (OWASP)** publishes a list of the most critical security risks for web applications. Here are the top five vulnerabilities explained in simple terms:

### 1. Broken Access Control
**What it is:**
- Users can access parts of a website they shouldn’t, like admin panels or other users’ data.

**Example:**
- A normal user can visit `example.com/admin` and access admin controls without permission.

**How to prevent:**
- Enforce proper user roles and permissions.
- Restrict direct access to sensitive resources.

### 2. Cryptographic Failures
**What it is:**
- Sensitive data (passwords, credit card numbers) is not properly encrypted, making it easy for hackers to steal.

**Example:**
- A website stores passwords in plain text instead of hashing them.

**How to prevent:**
- Use strong encryption (e.g., AES for data, bcrypt for passwords).
- Avoid exposing sensitive data in URLs or logs.

### 3. Injection Attacks
**What it is:**
- Hackers insert malicious code into a website’s database or commands by tricking input fields.

**Example:**
- Entering `'; DROP TABLE users; --` into a login form deletes the user database (SQL Injection).

**How to prevent:**
- Use parameterized queries and prepared statements.
- Sanitize and validate user inputs.

### 4. Insecure Design
**What it is:**
- The application itself is poorly designed, making it vulnerable to attacks.

**Example:**
- A website allows unlimited password guesses without locking the account (brute force attack).

**How to prevent:**
- Follow secure coding principles.
- Implement security from the start, not as an afterthought.

### 5. Security Misconfiguration
**What it is:**
- Default settings, exposed error messages, or unnecessary features that create security risks.

**Example:**
- A website shows detailed error messages that reveal database information.

**How to prevent:**
- Disable unnecessary features and services.
- Keep software and frameworks updated.
- Hide detailed error messages from users.

### Conclusion
Understanding and fixing these vulnerabilities can greatly improve web security. Always validate input, secure user access, and follow best security practices!


---

# Reflections

Do more diagrams to explain security concepts
