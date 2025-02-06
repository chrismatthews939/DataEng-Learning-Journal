# Topic 1 Networks for Data Engineers 06/02/2025

## Networks

**Key definitions**

Here are the definitions for some key concepts referred to in this module:

1. **Router**: A device that forwards data packets between computer networks, creating an overlay internetwork.

2. **Local Area Network (LAN)**: A network that connects computers within a limited area such as a residence, school, or office building.

3. **Access Point**: A device that allows wireless devices to connect to a wired network using Wi-Fi or related standards.

4. **Firewall**: A network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.

## TCP / IP and the OSI layer model

`In the digital age, understanding network models such as TCP/IP and OSI is not just beneficial, it’s essential. These models serve as the backbone of internet communication, enabling data to be transmitted efficiently across diverse networks. The layered design of these models allows for systematic troubleshooting, speeding up the problem-solving process by isolating network issues effectively. By understanding these models, we ensure compatibility and interoperability between different network systems and devices, which is crucial for diagnosing network issues and designing network solutions.`

**So, what is TCP/IP?**
TCP/IP (Transmission Control Protocol/Internet Protocol) is a set of rules that allows computers to communicate over the internet. Think of it as the language that computers use to talk to each other, ensuring that data sent from one computer arrives accurately and in the right order at another computer.

**1970s**
Developed by the U.S. Department of Defence to ensure robust, reliable communication.

**1983**
Officially adopted for ARPANET (the predecessor of the internet).

**1990S and beyond**
Became the foundation of the modern internet, connecting millions of devices worldwide.

### How does TCP work?**

**Analogy**: Imagine you're sending a letter to a friend.

**Letter Pieces**: Your letter (**data**) is too big to send in one envelope, so you break it into multiple smaller pieces (**packets**).

**umbering**: You number each piece to ensure they can be reassembled in the correct order.

**Confirmation**: When your friend receives each piece, they send you a confirmation (**acknowledgment**) to let you know it arrived safely. If a piece is missing or damaged, you resend it.

**Example**: Downloading a file from the internet. TCP ensures all parts of the file arrive correctly, even if they take different routes to get to you.

### How does IP (Internet Protocol) work?

**Addresses**: Every computer on the internet has a unique address (IP address), like a home address.

**Routing**: The IP ensures that each piece of your letter knows where to go and can find the best route to get there.

**Example**: Sending an email.

IP ensures the email reaches the recipient's email server, no matter where it is in the world. The IP address is like a phone number but for your computer.

There are two types of IP addresses: IPv4 (e.g., 192.168.1.1) and IPv6 (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334), with IPv6 being the newer, longer version because we're running out of the shorter IPv4 addresses. We will explore IP addresses in the webinar.

### Combining TCP and IP - an example

![Combining TCP and IP](https://www.simplilearn.com/ice9/free_resources_article_thumb/TCP_Model_1.png)

**What can we learn from this diagram?**

**Analogy**: Throwing a party using the Internet.

**Invitations (Packets)**: You send out invitations to friends (data).

**Addresses (IP)**: You need their home addresses to send invitations (IP addresses).

**Responses (TCP)**: Friends RSVP to let you know they received the invite and will attend (acknowledgments). If someone doesn't reply, you might follow up (resend lost packets).

### Why should this all matter to you?

Here's some important reasons:

1. **TCP/IP**

Understanding TCP/IP helps you become more tech-savvy and better at troubleshooting connectivity issues.

The TCP/IP model is fundamental in ensuring reliable data transmission across diverse networks.

It serves as the backbone for internet communication by defining how data should be packetized, addressed, transmitted, routed, and received.

2. **OSI Model**

Understanding the broader scope of network interactions necessitates the OSI model.

The OSI model provides a more detailed and structured framework for network architecture.

It divides network communication into seven distinct layers, from physical transmission to application-specific functionalities.

This allows for a clearer delineation of roles and facilitates easier troubleshooting and network management.

3. **Complementarity of OSI and TCP/IP**

By compartmentalising network functions into layers, the OSI model complements the practical framework of TCP/IP.

This enhances our conceptual understanding and enables more robust, adaptable network design and operation.

This comprehensive approach ensures that professionals can isolate issues, implement new technologies, and maintain network integrity more efficiently.

```The OSI comprises seven layers - Physical, Data Link, Network, Transport, Session, Presentation, and Application```

**1970s**
Developed by the International Organization for Standardisation (ISO).

**1984**
Officially adopted as a standard to facilitate interoperability between different networking systems.

**Today**
While not always directly used, it remains a fundamental concept for understanding and designing network protocols.

*The OSI Model helps network engineers and IT professionals understand the complex interactions in network systems, making it easier to design, manage, and troubleshoot networks.*

### What else do you need to know about OSI?

The OSI Model is often referred to by its **layers'** numbers or names, making it easier to pinpoint where an issue might occur in network troubleshooting.

Imagine planning a road trip:

**Physical Layer**: The actual roads and vehicles (physical cables like ethernet).

**Data Link Layer**: Traffic lights ensuring orderly driving (mac addresses).

**Network Layer**: Network Layer: a map with all intersections, junctions and building numbers clearly marked (IP addresses).

**Transport Layer**: The traffic light system and the smart motorway traffic updates (TCP).

**Session Layer**: Your phone keeping the GPS session active (NetBIOS, RPC)

**Presentation Layer**: Your GPS app translating satellite data into readable maps (SSL/TLS, JPEG, ASCII).

**Application Layer**: The GPS app itself that you interact with (HTTP, FTP, SMTP).

### In Summary

- **Physical Layer**: Physical hardware connections.
- **Data Link Layer**: Direct data transfer and error correction.
- **Network Layer**: Routing data to its destination.
- **Transport Layer**: Ensuring complete data transfer.
- **Session Layer**: Managing sessions between applications.
- **Presentation Layer**: Translating and encrypting data.
- **Application Layer**: Interacting with user applications.

## Modern networking practices

In the ever-evolving field of network technology, the shift from physical to logical networking has transformed the landscape of how organisations manage their data flow and security. Virtualisation and other logical networking practices are at the forefront of this transformation, offering unprecedented flexibility and efficiency. Understanding these concepts is crucial for any data engineer tasked with managing a modern network.

### Logical Networking

Logical networking involves the configuration of networks that are largely independent of the physical setup. Instead of relying on hardware alone, logical networks utilise software to manage, segment, and secure network traffic. This approach not only simplifies physical infrastructure but also enhances scalability and adaptability.

### What are distributed data products?

Distributed data products involve storing and processing data across multiple nodes in a network, enhancing performance and reliability. They can use client-server, peer-to-peer or clustered master-worker architectures.

![client server vs peer to peer](https://systemdesignschool.io/blog/peer-to-peer-architecture/client-server-vs-p2p.png)

**Client/server and master/worker**
In Computer Networking, Client/Server describes the relationship between two computer programs in which one program, the client, makes a service request from another program, the server, which fulfills the request (e.g., database access per SQL).

Although the client/server idea can be applied to programs within a single computer, the most popular perception is that of nodes in a network.

A Client/Server configuration is used for accessing but not modifying data in the Server since there could be unpredictable results if multiple Clients modified the data in an unsynchronised way.

In contrast, Master/Worker is a model of communication where one device or process has unidirectional control over one or more devices. This is common in clusters.

**Clusters**

A cluster is a set of loosely or tightly connected computers that work together, so they can be viewed as a single system.

Clusters are used to improve performance and availability, providing a scalable solution for data-intensive applications.

They allow for load balancing and high availability, ensuring that services remain operational even if some nodes fail.

Clusters also enable parallel processing, significantly speeding up data processing tasks. Understanding clusters is essential for designing robust and scalable data processing systems.

## Costs and Sustainability

**Energy-Efficient Hardware**: Utilising low-power devices and optimising resource utilisation to reduce energy consumption.

**Network Design**: Implementing efficient network topologies and protocols to minimise energy use.

**Green Data Centres**: Data centres designed for energy efficiency and environmental sustainability. These centres use advanced cooling systems, renewable energy sources, and AI to optimise operations.

## Evaluating infrastructure costs

Infrastructure costs encompass the total financial commitments required for establishing and maintaining robust network systems. These expenses are broadly categorised into capital expenditure, which includes the initial expenditure on hardware and software, and operational expenditure, which covers ongoing costs such as maintenance, upgrades, and energy consumption. Such comprehensive accounting ensures that all factors contributing to the total cost of ownership (TCO) are considered.

1. Grasping infrastructure costs is key for budgeting, strategic planning, and making network investments.
2. This understanding enables IT professionals to make well-informed decisions about deploying cost-effective technologies and solutions, predict future financial obligations, and allocate resources judiciously.
3. Demonstrating a thorough grasp of these costs, particularly during your professional discussion in the EPA, showcases your ability to manage and enhance network infrastructure efficiently.
4. Reflecting on the sustainability of these choices also becomes crucial, ensuring that long-term environmental impacts are considered alongside economic benefits.

**Cost components**

The main components of infrastructure costs are:

- **Hardware**: Servers, routers, switches, and other physical equipment.
- **Software**: Operating systems, management tools, security software, and application licenses.
- **Maintenance**: Regular updates, repairs, and technical support to ensure optimal system performance.
- **Energy Consumption**: Power usage of the equipment and cooling systems, which can be significant, especially in data centres.

**Optimisation strategies**

Key strategies for cost optimisation include:

- **Adopting Energy-Efficient Technologies**: Implementing green technologies that reduce power consumption.
- **Regular System Updates and Maintenance**: Ensuring that systems are running efficiently and securely, which can save costs related to security breaches and downtime.
- **Scalable Solutions**: Employing modular systems that can be expanded as needed, avoiding the initial expense of oversized infrastructures.Optimisation strategies
  
# Lecture

## Peer-to-Peer (P2P) Networking: A Beginner's Guide

### What is Peer-to-Peer (P2P) Networking?
Peer-to-peer (P2P) networking is a type of computer network where devices (known as "peers") communicate and share resources directly with each other without requiring a central server.

In a P2P network:
- Each device has equal status.
- Devices can act as both clients (requesting resources) and servers (providing resources).
- The network is decentralized, meaning there is no single point of control.

### How It Works
When a peer wants to share or retrieve data, it establishes a direct connection to one or more peers in the network. Peers exchange information, such as files or computing tasks, directly without routing through a central authority.

## Examples of P2P Applications
1. **File Sharing:**
   - Applications like BitTorrent and eMule use P2P technology to share large files efficiently by distributing file chunks across multiple peers.

2. **Streaming:**
   - Platforms like decentralized video streaming services may use P2P to distribute video streams across users.

3. **Blockchain and Cryptocurrency:**
   - Cryptocurrencies such as Bitcoin and Ethereum use P2P networks for transaction validation and data distribution.

4. **Communication Applications:**
   - Some VoIP applications and chat platforms, like Skype (in its early versions), rely on P2P technology for direct communication between users.

5. **Distributed Computing:**
   - Projects like Folding@home and BOINC harness the computing power of many individual devices to perform complex computations.

### Advantages of P2P Networking
- **Scalability:** As more peers join, the network can handle more traffic and resource sharing.
- **Cost-Efficiency:** Reduces the need for costly centralized infrastructure.
- **Fault Tolerance:** The network continues to function even if some peers go offline.
- **Efficiency:** Direct connections between peers improve data transfer speeds.

### Disadvantages of P2P Networking
- **Security Risks:** Without a central authority, it's harder to enforce security measures.
- **Data Integrity:** Maintaining data accuracy and integrity can be challenging.
- **Network Performance:** Performance can degrade if peers have slow or unstable connections.

### When to Use P2P Solutions
P2P networking is best suited for scenarios where:
- A decentralized architecture is required.
- Scalability and cost-efficiency are priorities.
- Direct and fast data exchanges are preferred.

### Practical Use Cases
| **Use Case**         | **P2P Solution Example**    |
|----------------------|-----------------------------|
| File Distribution    | BitTorrent                  |
| Cryptocurrency       | Bitcoin, Ethereum           |
| Distributed Storage  | IPFS (InterPlanetary File System) |
| Collaborative Computing | Folding@home            |
| Decentralized Web    | Web3 Applications            |

### Conclusion
P2P networking is a powerful and versatile technology for decentralized communication and resource sharing. Understanding its advantages and limitations can help you decide where it fits best in your computing solutions.

---

### Network Components
| **Media Type**         | **Description**    |
|----------------------|-----------------------------|
| Metal wires   | Uses elecrical impulses                |
| Glass or plastic fibres within cables (fibre-optic      | Pulses of light           |
| Wireless  | Specific frequency of magnetic waves |


### Network Local Area Network (LAN)

Most LANs are Ethernet based.

### IP Addressess

An identifier for a computer or device on a TCP/IP network.

99% of the world use (IPv4) version 4

- IPv4 address is four bytes (octets). Total 32 bits.
- Each byte is a number from 1 to 254
- Written in dotted notation e.g 192.168.21.76

### Maths RevisionConvert Number to Binary

**Convert Number to Binary**

![convert to binary](https://i.ytimg.com/vi/LFmlStBx6nw/hqdefault.jpg)

**Convert Number to Hexadecial**

![Convert Number to Binary](https://mathmonks.com/wp-content/uploads/2024/04/Binary-to-Hexadecimal.jpg)


## LAN Infrastructure 

### What is a LAN?
A **Local Area Network (LAN)** is a network that connects computers and devices within a limited area, such as a home, office, or school. It allows devices to share data, resources (like printers), and internet connections.

### Components of LAN Infrastructure
To understand LAN architecture, let's break down the essential components involved:

#### 1. **End Devices (Clients)**
These are the devices that access the network to communicate and share data.
- Examples: Computers, smartphones, printers, and IoT devices.

#### 2. **Network Interface Card (NIC)**
Each device in the LAN must have a **NIC**, which allows it to connect to the network.
- NIC can be wired (Ethernet) or wireless (Wi-Fi).

#### 3. **Switches**
Switches connect multiple devices within the LAN and manage data traffic efficiently.
- They operate at Layer 2 (Data Link Layer) of the OSI model.
- Use MAC addresses to forward data to the correct device.

#### 4. **Routers**
Routers connect multiple networks and direct data packets between them.
- They are essential for LANs that connect to the internet.
- Operate at Layer 3 (Network Layer) of the OSI model.

#### 5. **Cabling**
Physical cables form the backbone of a wired LAN.
- Common types: **Ethernet cables (Cat5e, Cat6)**.
- Fiber optic cables are used for higher speeds and longer distances.

#### 6. **Wireless Access Points (WAPs)**
WAPs enable wireless communication between devices within the LAN.
- Often built into routers.

#### 7. **Firewall**
Firewalls protect the LAN by filtering incoming and outgoing traffic.

---

### LAN Architecture Types
The architecture defines how devices in the LAN are arranged and communicate with each other.

#### 1. **Bus Topology**
- All devices are connected to a single central cable (the bus).
- Pros: Simple and cost-effective.
- Cons: Limited scalability and prone to collisions.

#### 2. **Star Topology**
- Devices are connected to a central switch or hub.
- Pros: Easy to manage and troubleshoot.
- Cons: Failure of the central switch can affect the entire network.

#### 3. **Ring Topology**
- Devices are connected in a circular manner.
- Pros: Data flows in one direction, reducing collisions.
- Cons: A single failure can disrupt the entire network.

#### 4. **Mesh Topology**
- Devices are interconnected, allowing multiple paths for data.
- Pros: High redundancy and reliability.
- Cons: Expensive and complex.

#### 5. **Hybrid Topology**
- A combination of two or more topologies.
- Pros: Flexible and scalable.

---

### How Data Flows in a LAN
1. **Data Transmission**: When a device sends data, the NIC formats it into packets.
2. **Switch Operation**: The switch reads the destination MAC address and forwards the packet to the correct device.
3. **Router Role (if internet is involved)**: If the destination is outside the LAN, the router directs the packet to the internet.

---

### Example Scenario
Imagine a small office with the following setup:
- **5 Computers** connected via Ethernet cables to a **central switch**.
- A **router** connects the switch to the internet.
- A **printer** and **WAP** are also connected to the switch.

Here, the switch manages data traffic internally, while the router handles communication between the office LAN and the internet.

---

### Benefits of LANs
- **High Speed:** Faster data transfer within the network.
- **Resource Sharing:** Printers, files, and storage can be shared.
- **Cost-Effective:** Shared internet connections reduce expenses.
- **Scalability:** Easy to add new devices.

### Summary
Understanding LAN infrastructure and architecture is crucial for setting up and managing small networks. Key components like switches, routers, and NICs work together to ensure smooth communication between devices.

**High availability**
A mode for mitigating a single point of failure

## Introduction to VLAN Infrastructure and Architecture

### What is a VLAN?
VLAN stands for **Virtual Local Area Network**. It is a logical subdivision of a physical network. By creating VLANs, you can segment network devices into different groups, regardless of their physical location. VLANs help improve network performance and security by isolating traffic.

#### 1. **Physical Network vs. Virtual Network**
A physical network consists of all devices connected to switches and routers. VLANs introduce a virtual layer where devices connected to the same physical switch can behave as if they belong to different networks.

#### 2. **Why Use VLANs?**
- **Traffic Segmentation:** Organize traffic for better performance.
- **Security:** Isolate sensitive devices and users.
- **Efficient Network Management:** Simplify the logical organization of devices.

#### 3. **Tagging and Trunking**
- **Tagged Traffic:** VLAN-tagged traffic uses a header to indicate which VLAN the packet belongs to.
- **Untagged Traffic:** Regular traffic without VLAN-specific tagging.
- **Trunk Ports:** Ports configured to carry traffic from multiple VLANs using tagging.
- **Access Ports:** Ports assigned to a single VLAN, typically for end-user devices.

### VLAN Architecture
A typical VLAN architecture consists of:

#### 1. **Access Layer**
- Devices such as PCs, printers, and VoIP phones connect to access switches.
- Access ports are configured to assign a VLAN to each device.

#### 2. **Distribution Layer**
- Intermediate switches that aggregate traffic from access switches.
- Responsible for routing traffic between VLANs.

#### 3. **Core Layer**
- High-performance switches for fast data forwarding.
- Ensures efficient routing and network backbone operations.

### Best Practices for VLAN Design
1. **Use Descriptive VLAN Names:** Easier network management.
2. **Limit VLAN Spanning:** Reduce broadcast domains to avoid network congestion.
3. **Use Trunks Wisely:** Configure trunk ports only where necessary.
4. **Security:** Disable unused ports and restrict VLAN access.

### Conclusion
VLANs are essential for efficient and secure network design. By understanding VLAN infrastructure and architecture, network administrators can create scalable and organized network environments.

---

**Captial Expenditure CapEx** Long term costs - Physical Hardware

**Operational Expenditure OpEx** Day to day costs - Energy consumption








