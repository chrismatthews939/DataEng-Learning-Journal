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

**Analog**y: Imagine you're sending a letter to a friend.

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


