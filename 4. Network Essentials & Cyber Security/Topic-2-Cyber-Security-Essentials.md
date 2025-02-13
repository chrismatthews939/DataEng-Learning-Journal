# Topic 2 Cyber Security Essentials 13/02/2025

## Understanding the CIA Triad

![CIA Triad Model](https://www.itgovernance.co.uk/blog/wp-content/uploads/2023/02/image-2.png)

Understanding the CIA triad is fundamental to implementing effective security measures. Each component of the triad addresses a critical aspect of data protection. Knowledge of the CIA triad helps in designing comprehensive security strategies that protect sensitive information from various threats. Additionally, this understanding is crucial for your professional discussion in the End Point Assessment (EPA), where demonstrating a deep awareness of security principles is essential.

Explanation of key concepts:

- **Confidentiality**: Ensuring that information is not accessed by unauthorised individuals.
- **Integrity**: Maintaining the accuracy and completeness of data.
- **Availability**: Ensuring that information is accessible to authorised users when needed, in a timely manner.

### The AAA model

The AAA model is complementary to the CIA triad, and highlights the three key functions that need to be performed at all times in a secure system, these are:

- **Authentication**: Verifying the identity of users before granting access to systems.
- **Authorisation**: Determining the level of access or permissions a user has once authenticated.
- **Accounting**: Tracking and logging user activities within the system.

![AAA Model](https://discover.strongdm.com/hubfs/aaa-security.jpg)

### So, how can the CIA Triad be applied?

Applying the CIA triad involves implementing measures that protect data confidentiality, maintain data integrity, and ensure data availability. Effective application of the CIA triad can significantly reduce the risk of data breaches and ensure compliance with regulatory requirements. It helps in building trust with stakeholders by safeguarding sensitive information.

Examples of implementing C, I and A include:

- **Confidentiality Measures**: Encryption, access controls, and authentication protocols.
- **Integrity Measures**: Checksums, hash functions, and version control systems.
- **Availability Measures**: Redundancy, failover mechanisms, and regular backups.

`A real-world example...
Implementing multi-factor authentication (MFA) for accessing sensitive data enhances confidentiality by ensuring that only authorised users can access the data.
Using version control systems like Git helps maintain the integrity of code and data by tracking changes and allowing rollbacks if necessary.
Employing redundancy and failover mechanisms ensures that critical systems remain available even during hardware failures or cyber-attacks.`

### What is Multifactor Authentication?

MFA is a combination of criteria that need to be met in order for the user to gain access to resources

## Vulnerabilities and risks

**Risk** refers to the potential for loss or damage when a threat exploits one of those vulnerabilities. Identifying the risks associated with an outdated operating system being compromised and applying patches would be nowadays classified as an essential security practice.

```
The risk equation

risk = probability x severity
```

### How do organisations protect sensitive customer data?

Usually, organisations will use frameworks to proactively identify and address cybersecurity threats. By systematically evaluating each potential hazard in terms of its severity, probability, and controllability, organisations can prioritise their cybersecurity efforts effectively. Specialised frameworks, like the one given in the chart below, help in documenting existing vulnerabilities, the efficacy of implemented controls, and the overall resilience of the organisation against cyber threats. Such a tool is invaluable not only for IT security teams but also for senior management to understand the cybersecurity posture of their organisation and make informed decisions regarding resource allocation and strategic security enhancements.

![Risk analysis chart](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2TsqxBinC4MR-PQEPFE1avhMMTpeFCrTSKA&s)

**Hazard**: Identifies specific cybersecurity threats or vulnerabilities.

**Severity**: Assesses the potential impact of the hazard should it occur, rated as Low, Medium, or High.

**Probability**: Evaluates the likelihood of the hazard occurring, also rated as Low, Medium, or High.

**Level of Risk**: A derived metric, typically calculated by combining severity and probability to gauge the overall risk level, indicated as Low, Medium, or High.

**Controls to Reduce Risk**: Lists actions or strategies that can be implemented to manage or mitigate the risk.

**Residual Risk**: The level of risk remaining after the control measures are applied, also rated as Low, Medium, or High.

## Understanding threats and attacks

A threat is any circumstance or event with the potential to cause harm to an information system. An attack is an intentional act by a malicious actor to exploit a vulnerability. Understanding threats and attacks is essential for developing effective defence mechanisms. This knowledge helps in anticipating potential security incidents and implementing measures to prevent or mitigate their impact. Being aware of common attack vectors enhances your ability to protect data products and infrastructures. Additionally, it prepares you for discussing these topics in your EPA professional discussion.

### A focus on: Threats

**Malware**: Malicious software designed to damage or disrupt systems, steal data, or perform other unwanted actions. Types of malware include viruses, worms, and spyware. Example: A piece of malware might be downloaded unknowingly from an email attachment, which then spreads through the network, stealing sensitive data.

**Insider Threats**: Risks posed by individuals within the organisation who have access to sensitive information and misuse it. Example: A disgruntled employee who leaks confidential data to a competitor.

**Social Engineering**: Manipulating people into breaking normal security procedures and divulging confidential information. Example: An attacker calls an employee pretending to be from IT support and convinces them to reveal their password.

**Phishing**: A tactic used to trick individuals into divulging confidential information by pretending to be a trustworthy entity in electronic communications. Example: An email that appears to be from a bank, asking the recipient to click on a link and enter their login credentials. The link leads to a fake website controlled by attackers.
  
  - **Spearphishing** is a more targeted form of phishing, where attackers tailor their messages to specific individuals or organisations, often using personal information to make the attack more convincing.
  This could be an email that appears to be from a company’s CEO, targeting a specific employee in the finance department and requesting a wire transfer to a fraudulent account.

### Threat actors

**Hacktivists**
Individuals or groups that use hacking to promote political ends. They often target organisations to protest against actions they disagree with.

**Example**: Anonymous is a well-known hacktivist group that has conducted attacks on government and corporate websites to support their political views.


**Rogue State Actors**
Nation-states that engage in cyber attacks against other nations or entities for espionage, disruption, or damage.

**Example**: The 2014 Sony Pictures hack was attributed to North Korean hackers in retaliation for a film that mocked their leader.


**Script Kiddies and Common Hackers**
Script Kiddies are inexperienced hackers who use existing scripts and tools to launch attacks, often with no clear understanding of the underlying technology.

**Example**: A teenager using a downloaded DDoS tool to take down a friend's gaming server.

Common Hackers are individuals with various skill levels who hack for personal gain, notoriety, or simply to challenge their skills.

**Example**: Kevin Mitnick, once one of the most wanted hackers, who now works as a security consultant.

### Attacks

SQL Injection: An attack where malicious SQL code is inserted into an input field for execution, allowing attackers to interfere with the queries an application makes to its database. Example: An attacker enters SQL code into a login form to bypass authentication and gain unauthorised access to user accounts

**Denial of Service (DoS)**: An attack meant to shut down a machine or network, making it inaccessible to its intended users by overwhelming it with traffic. Example: Flooding a website with requests until it crashes, making it unavailable to users.

**Ransomware**: Malicious software that locks or encrypts files on a victim's computer, demanding a ransom for their release. Example: The WannaCry attack in 2017, which encrypted data on infected computers and demanded ransom payments in Bitcoin.

**Zero-Day**: An attack that exploits a previously unknown vulnerability in software before the vendor has issued a patch. Example: Stuxnet exploited four zero-day vulnerabilities to sabotage Iran's nuclear program.

**DDoS (Distributed Denial of Service)**: A DoS attack where multiple compromised systems attack a single target, causing a denial of service for users. Example: The Mirai botnet used hundreds of thousands of IoT devices to perform a massive DDoS attack in 2016.

**Trojan Horse**: Malicious software that misleads users of its true intent, often appearing as a legitimate program to deceive users into installing it. Example: A fake antivirus program that claims to find infections on the user's computer and prompts them to purchase a full version to remove them.

**Malware**: Any software intentionally designed to cause damage to a computer, server, or computer network. Types of malware include viruses, worms, and Trojan horses. Example: A worm that replicates itself to spread to other computers, often exploiting vulnerabilities in network software.

**Man-in-the-Middle (MITM)**: An attack where the attacker secretly intercepts and relays messages between two parties who believe they are communicating directly with each other. Example: Intercepting communication between a user and a banking website to steal login credentials.

### Security Controls

Security controls are essential measures designed to protect systems from threats, reduce vulnerabilities, and ensure the confidentiality, integrity, and availability of information. This lesson addresses the critical problem of how to effectively implement these controls to maintain a secure environment. By understanding and applying security controls, you will learn how to prevent unauthorized access, detect potential breaches, and respond promptly to incidents.

#### Examples of security controls include the following:

**Preventive Controls**: Firewalls, encryption, and access controls.

**Detective Controls**: Intrusion detection systems (IDS), security information and event management (SIEM) systems, and regular audits.

**Corrective Controls**: Incident response plans, patch management, and disaster recovery plans.

**Firewalls**: Act as a barrier between trusted and untrusted networks, filtering incoming and outgoing traffic based on security rules.

**Security Policies**: Written documents that define an organisation’s security practices and procedures, such as clean desk policies and social media policies.

**Staff Training**: Regular training sessions to educate employees on security best practices and how to respond to security incidents.

#### Demilliarized Zones

**DMZ**: A physical or logical subnetwork that contains and exposes an organisation's external-facing services to an untrusted network, usually the internet.
It adds an extra layer of security by isolating these services from the internal network.
A DMZ also prevents an attacker from being able to scope out potential targets within the network.
Even if a system within the DMZ is compromised, the internal firewall still protects the private network, separating it from the DMZ.
This setup makes external active reconnaissance more difficult.

![DMZ](https://www.techtarget.com/rms/onlineimages/sdn-dmz_network_architecture_mobile.png)

## Evaluating the impact of security breaches

Evaluating the impact of security breaches involves assessing the potential damage caused by a security incident, including financial losses, reputational damage, operational disruptions, legal problems, and loss of trust. Understanding the impact of security breaches helps in prioritising security measures and allocating resources effectively. It enables organisations to prepare for potential incidents and minimise their effects. Demonstrating this capability is crucial during your EPA professional discussion, showcasing your ability to assess and manage the consequences of security breaches. Additionally, it supports the development of more resilient security strategies.

#### Explanation and examples

Understanding the multifaceted impacts of security breaches is crucial for developing effective mitigation strategies. In this section, we will delve into specific examples that illustrate the severe consequences of security breaches.

**Legal problems**

Breaches can lead to legal penalties, fines, and lawsuits due to non-compliance with data protection regulations.

For instance, The Equifax data breach in 2017 exposed sensitive information of 147 million people, leading to significant legal consequences, including a settlement of up to $700 million.

**Loss of trust**

Customers and stakeholders may lose trust in an organisation that cannot protect their data, leading to reputational damage.

For example, The Facebook-Cambridge Analytica scandal in 2018 eroded user trust, resulting in a decline in user engagement and increased scrutiny from regulators.

**Loss of business**

A breach can result in significant financial losses due to disrupted operations, compensation costs, and loss of customers.

For instance, the WannaCry ransomware attack in 2017 affected numerous organisations worldwide, leading to operational disruptions and financial losses estimated at billions of dollars.

**Loss of availability**

Attacks such as denial-of-service attack (DDoS) can render systems unavailable, affecting business continuity and service delivery.

#### Calculating the financial impact of a security breach

Scenario

An organisation experiences a ransomware attack that affects 100 servers. Each server has a replacement cost of £5,000, and the downtime costs the company £10,000 per hour in lost business. The average downtime per server due to the attack is 8 hours.

| **Description**         | **Amount**    |
|----------------------|-----------------------------|
| Number of Servers Affected    | 100 |
| Replacement Cost per Server     | £5,000 |
| Total Replacement Cost | £500,000 |
| Downtime Cost per Hour | £10,000  |
| Average Downtime per Server   | 8 hours |
| Total Downtime Cost per Server  | £80,000 |
| **Total Financial Impact**  | **£8,500,000**  |

  
# Lecture

## Encryption

**Symmetric** 

Based on the premise that both parties knows the pre-shared key to encrypt/unencrypt

Commonly used with VPN traffic because it uses less resources

Well known algorithms for this. Algorithms often classified as block ciphers 

**Asymmetric**

Uses different keys to encrypt/unencrypt

Asymmetric algorithms are used to provide confidentiality without pre-sharing a password. 

![asymmetric encryption](https://www.simplilearn.com/ice9/free_resources_article_thumb/alice.PNG)

`In this example Alice encrypts a message to Bob using her provite key and sends to Bob.
Bob decrypts the message the message using Alice's public key. This authenticates the message from Alice because if the message doesn't decrypt you know it's been tampered with`

# Asymmetric Encryption Explained Simply

## What is Asymmetric Encryption?
Asymmetric encryption is a method of encrypting messages using two keys:
- **Public Key**: Used to encrypt the message.
- **Private Key**: Used to decrypt the message.

Only the person with the private key can read the encrypted message.

---

## Example: Bob and Alice
Imagine Bob wants to send a secret message to Alice. Here's how they do it:

1. **Alice creates two keys**: 
   - A **public key** (which she shares with everyone, including Bob).
   - A **private key** (which she keeps secret).

2. **Bob encrypts the message** using Alice's **public key**.
3. **Alice decrypts the message** using her **private key**.

This way, only Alice can read the message, even if someone intercepts it.

---

## Step-by-Step Example with Simple Phrases

- Alice generates her keys:
  - **Public Key**: `12345`
  - **Private Key**: `67890`

- Bob wants to send the message: **"Hello Alice"**
  - He encrypts it using `12345` (Public Key).
  - The encrypted message looks like: `@&$%!#`

- Alice receives `@&$%!#` and decrypts it using `67890` (Private Key), revealing **"Hello Alice"**.

---

## Why is Asymmetric Encryption Useful?
- **Security**: Only the person with the private key can decrypt the message.
- **No need for secret key exchange**: Unlike symmetric encryption, Bob and Alice don’t need to share a secret key in advance.
- **Used in real-world applications**: Secure websites (HTTPS), digital signatures, and cryptocurrency transactions all rely on asymmetric encryption.

---

This is a fundamental concept in cryptography and is widely used to protect digital communications!

## Understanding Asymmetric Encryption

### What is Asymmetric Encryption?
Asymmetric encryption is a method of encrypting data using a pair of keys:
- **Public Key**: Used for encryption.
- **Private Key**: Used for decryption.

Unlike symmetric encryption (where the same key is used for both encryption and decryption), asymmetric encryption ensures that only the recipient with the private key can decrypt the message.

---

### Example: Asymmetric Encryption in Python
Here’s a simple example using the `cryptography` library:

#### Install Required Library
```bash
pip install cryptography
```

#### Generate Key Pair and Encrypt/Decrypt Data
```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Serialize public key for sharing
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("Public Key:\n", public_pem.decode())

# Encrypt a message
message = b"Hello, this is a secret message!"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Encrypted Message:", ciphertext)

# Decrypt the message
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Decrypted Message:", plaintext.decode())
```

---

### How It Works
1. A key pair (public & private) is generated.
2. The public key is shared and used for encryption.
3. The private key is kept secret and used for decryption.
4. The message is encrypted using the public key.
5. Only the private key can decrypt it back to the original message.

This method is widely used in secure communications, such as HTTPS, SSH, and digital signatures.

---

#### Conclusion
Asymmetric encryption ensures secure data exchange, even over insecure channels. The key advantage is that the private key is never shared, making it more secure than symmetric encryption in certain scenarios.


## Asymmetric Encryption Explained with Padlocks

Imagine Bob and Alice want to send secret messages to each other using padlocks instead of traditional keys. Here's how asymmetric encryption works in simple terms:

### Step 1: Alice's Padlock (Public Key)
- Alice has a special padlock with a unique key that only she owns.
- She makes copies of the padlock and gives them to anyone who wants to send her a message. This padlock is her **public key**.

### Step 2: Bob Locks the Message
- Bob wants to send a private message to Alice.
- He takes one of Alice's **public padlocks** and locks the message inside a box.
- Once locked, the padlock **cannot be opened** without Alice’s unique key.
- Bob sends the locked box to Alice.

### Step 3: Alice Unlocks the Message
- Since only Alice has the key to her own padlock (**private key**), she can unlock the box and read Bob’s message.

### Why is This Secure?
- Anyone can get Alice's **public padlock**, but they **cannot unlock it**—only Alice can.
- Even if someone intercepts the locked box, they cannot open it without Alice's **private key**.

### Real-World Use
- Asymmetric encryption is used in HTTPS, email security, and cryptocurrency transactions.
- Examples: RSA, ECC, and Diffie-Hellman encryption methods.

This is how secure communication works online using **public and private keys** instead of padlocks!

## Public Key Management & PKI Trust System

### Understanding Public Key Cryptography

Public Key Cryptography (PKC) is a method that allows two people (like Bob and Alice) to communicate securely over an insecure network. It involves two keys:

- **Public Key**: Can be shared with anyone.
- **Private Key**: Must be kept secret.

Anything encrypted with one key can only be decrypted with the other.

---

### Scenario: Bob and Alice Secure Communication

Imagine Bob wants to send a secret message to Alice.

1. **Alice generates a key pair:**
   - Public Key (can be shared)
   - Private Key (kept secret by Alice)

2. **Bob gets Alice’s Public Key** and encrypts the message.

3. **Alice uses her Private Key** to decrypt the message.

This ensures that only Alice can read Bob’s message, even if someone intercepts it.

```plaintext
Bob → (Encrypt with Alice's Public Key) → Secret Message → (Decrypt with Alice's Private Key) → Alice
```

---

### PKI (Public Key Infrastructure) & Trust System

In a real-world scenario, how does Bob know that the public key really belongs to Alice and not a hacker? This is where **PKI (Public Key Infrastructure)** comes in.

#### How PKI Works:
1. **Certificate Authorities (CA):** Trusted organizations that verify identities.
2. **Digital Certificates:** A CA signs Alice’s public key, confirming it's really hers.
3. **Trust Chain:** Bob checks Alice’s certificate and trusts her public key if it’s signed by a trusted CA.

#### Example Trust Flow:
- Alice gets her **public key signed** by a CA (e.g., "TrustedCA").
- Bob checks the **CA’s signature** before trusting Alice’s key.
- If the CA is trusted, Bob can securely communicate with Alice.

```plaintext
Trusted CA → Signs Alice’s Public Key → Bob trusts the certificate → Secure Communication
```

---

### Summary
- Public Key Cryptography ensures secure communication using key pairs.
- PKI helps verify identities using **Certificate Authorities**.
- Trust is built through **digital certificates** signed by a CA.

This system enables **secure websites (HTTPS), encrypted emails, and more!** 🚀

## Public Key Infrastructure (PKI) Trust System Explained

### Simple Explanation with Bob and Alice

Imagine Bob wants to send a secret message to Alice securely. They use a system called **Public Key Infrastructure (PKI)** to do this safely.

#### 1. The Role of a Trusted Authority
Bob and Alice don’t trust each other blindly. Instead, they trust a **Certificate Authority (CA)**, which is like a trusted official who verifies identities.

#### 2. How Certificates Are Obtained
1. Alice generates a pair of keys: a **public key** and a **private key**.
2. Alice sends her **public key** to the CA.
3. The CA verifies Alice’s identity and gives her a **certificate** (which contains her public key and is signed by the CA).

#### 3. How Bob Verifies Alice’s Certificate
1. Bob receives Alice’s certificate.
2. He checks if the certificate was signed by a trusted CA.
3. If valid, Bob trusts that the public key inside the certificate **really belongs to Alice**.
4. Bob then uses Alice’s public key to encrypt a message and send it to her.
5. Only Alice can decrypt the message using her **private key**.

#### 4. Why This Works
- Bob trusts the CA.
- The CA verified Alice.
- The certificate proves Alice’s identity.
- Only Alice’s **private key** can decrypt messages meant for her.

#### 5. Summary
PKI ensures that Bob and Alice can communicate securely, even if they have never met before. The **Certificate Authority (CA) acts as a trusted middleman** to verify identities.

---

Now Bob and Alice can exchange messages securely without worrying about imposters!

### 5. Why Do We Need PKI if Asymmetric Encryption Works?
Asymmetric encryption allows secure communication, but it does not prove **who owns the key**. Without PKI:
- An attacker could create a fake key and pretend to be Alice.
- Bob might encrypt messages for the wrong person.
- There would be no way to verify identities securely.

PKI solves this by using **certificates issued by a trusted CA** to prove that a public key truly belongs to its owner.

*You can go into your browser for example and check the certificates*

---

## NIST Access Control Mechanism Explained

### Simple Example: User and Object

Access control is like a door lock. Only people with the right key can open the door. In NIST’s model, access control follows these main rules:

1. **Subject (User)** – The person or system that wants access.
2. **Object** – The thing the user wants to access (like a file, a door, or a system).
3. **Access Policy** – The rules that decide who can access what.

#### Example:
Imagine a library system where users (students and staff) want to access books.

#### Step 1: Define Users and Objects
```yaml
users:
  - name: "Alice"
    role: "student"
  - name: "Bob"
    role: "staff"

objects:
  - name: "Science Book"
    access_roles: ["staff", "student"]
  - name: "Restricted Research Paper"
    access_roles: ["staff"]
```

#### Step 2: Check Access
```python
def check_access(user, object_name, objects):
    for obj in objects:
        if obj["name"] == object_name:
            return user["role"] in obj["access_roles"]
    return False

users = [
    {"name": "Alice", "role": "student"},
    {"name": "Bob", "role": "staff"}
]

objects = [
    {"name": "Science Book", "access_roles": ["staff", "student"]},
    {"name": "Restricted Research Paper", "access_roles": ["staff"]}
]

# Example Checks
print(check_access(users[0], "Science Book", objects))  # True
print(check_access(users[0], "Restricted Research Paper", objects))  # False
print(check_access(users[1], "Restricted Research Paper", objects))  # True
```

#### How It Works
- Alice (a student) can access the Science Book.
- Alice cannot access the Restricted Research Paper because it is only for staff.
- Bob (a staff member) can access both.

This is a very simple version of NIST access control, where rules define who can access what. In real-world systems, this is done with Role-Based Access Control (RBAC), Mandatory Access Control (MAC), or Discretionary Access Control (DAC).

## Preserving Data Integrity: A Beginner's Guide

Data integrity refers to the accuracy, consistency, and reliability of data over its lifecycle. Preserving data integrity means ensuring that data remains correct, unaltered, and reliable throughout its use.

### Why is Data Integrity Important?

When data is collected, stored, or transmitted, it can become corrupted or altered unintentionally due to various reasons such as:

- Human errors
- System malfunctions
- Security breaches

This can lead to incorrect information, which could cause businesses or systems to make wrong decisions, impacting productivity, trust, and even security.

### Key Aspects of Data Integrity

1. **Accuracy**: Data must be correct and reflect real-world values.
2. **Consistency**: Data must be uniform across different systems and platforms.
3. **Reliability**: Data should always be available and usable when needed, without degradation.
4. **Completeness**: All required data must be present, without missing values.
5. **Security**: Protecting data from unauthorized access or modification.

### Methods to Preserve Data Integrity

Here are some ways to preserve data integrity:

- **Validation**: Ensuring that only valid data is entered into a system.
- **Checksums**: A checksum is a calculated value used to verify the integrity of data during transfer or storage.
- **Redundancy**: Storing copies of data in different locations or systems to ensure availability in case of failure.
- **Encryption**: Securing data with encryption to prevent unauthorized access or tampering.
- **Access Control**: Restricting who can view or alter data, ensuring that only authorized users can modify it.

### Conclusion

Preserving data integrity is essential for maintaining trustworthy and accurate information in any system. Implementing practices like validation, redundancy, and encryption helps ensure that data remains correct and secure throughout its lifecycle.

By prioritizing data integrity, businesses and individuals can reduce the risk of errors, protect sensitive information, and make more informed decisions.

---

## Understanding Hash Functions for Beginners

### What is a Hash Function?

A **hash function** is a special function used in computing to take an input (or 'message') and turn it into a fixed-size string of numbers and letters. The result is known as the "hash value" or "hash code."

Think of it like a fingerprint for data. Just like how a fingerprint can uniquely identify a person, a hash value can uniquely represent any input data, but in a fixed-length format. This is useful for many things like checking data integrity, storing passwords securely, and more.

#### Key Properties of Hash Functions:
1. **Deterministic**: This means that if you hash the same input multiple times, you will always get the same output.
2. **Fixed Length**: No matter how big or small the input is, the output (the hash) is always of the same length.
3. **Fast to Compute**: Hash functions are designed to be fast, even when dealing with large amounts of data.
4. **One-Way**: It’s practically impossible to reverse a hash to get the original input back. This is crucial for security purposes.
5. **Collision-Resistant**: A good hash function ensures that it's unlikely for two different inputs to produce the same hash value.

### Example: Hashing in Python

Here's an example of how to use a hash function in Python to generate a hash for a string:

```python
import hashlib

# Input string
input_string = "hello, world"

# Create a hash object using SHA-256 (a popular hash function)
hash_object = hashlib.sha256()

# Update the hash object with the input string (must be encoded into bytes)
hash_object.update(input_string.encode())

# Get the hexadecimal representation of the hash
hash_value = hash_object.hexdigest()

# Print the hash value
print("The hash value of '{}' is: {}".format(input_string, hash_value))
```

## Digital Signatures Explained

A **digital signature** is like a virtual fingerprint for your documents or messages. It verifies the authenticity of the sender and ensures that the content hasn't been tampered with.

### How It Works:
1. **Signing**: When you send a message or document, your private key (a secret code) is used to create a digital signature.
2. **Verification**: The recipient uses your public key (a code that everyone can see) to verify the signature. If the signature is valid, they know the message came from you and hasn't been altered.

### Why Use Digital Signatures?
- **Security**: Prevents tampering.
- **Authentication**: Confirms who sent the message.
- **Non-repudiation**: The sender can't deny sending the message.

In short, digital signatures help keep online communication secure, just like a real signature on paper!

---

## Best Practices for High Availability

High availability (HA) refers to the ability of a system to remain functional and accessible even during failures. Here are some best practices for ensuring HA:

### 1. Redundancy
   - Use **multiple servers** or **instances** for critical components.
   - Spread them across **different data centers** or **regions** to prevent localized failures.

### 2. Load Balancing
   - Distribute incoming traffic across multiple servers using a **load balancer**.
   - This helps avoid overloading a single server and provides automatic failover.

### 3. Failover Mechanisms
   - Implement **automatic failover** to switch to a backup system in case of failure.
   - Ensure database and service replication for backup availability.

### 4. Monitoring & Alerts
   - Continuously monitor system health and set up **alerts** for failures.
   - Monitor server CPU, memory, disk space, and network performance.

### 5. Backup and Recovery
   - Regularly back up your data, including databases and configurations.
   - Test recovery procedures to ensure you can restore from backups quickly.

### 6. Scalability
   - Plan for horizontal scaling: add more resources (e.g., servers, storage) when needed.
   - Use cloud services with autoscaling features for dynamic resource allocation.

### 7. Fault Tolerance
   - Design systems to tolerate failures without affecting the user experience.
   - For example, use **caching** or **replication** to reduce single points of failure.

### Conclusion
   - High availability is about minimizing downtime and ensuring that your systems are reliable and resilient.

---

## Calculating SLE and ALE for Data Breaches

### Key Concepts:
1. **SLE (Single Loss Expectancy)**: This is the expected monetary loss from a single data breach incident.
   - Formula: 
     ```
     SLE = Asset Value (AV) * Exposure Factor (EF)
     ```
   - **Asset Value (AV)**: The value of the asset being lost (e.g., company data).
   - **Exposure Factor (EF)**: Percentage of the asset value lost in the event (e.g., 50% loss from a data breach).

2. **ALE (Annual Loss Expectancy)**: This is the expected loss for the entire year from the risk of data breaches.
   - Formula:
     ```
     ALE = SLE * Annual Rate of Occurrence (ARO)
     ```
   - **Annual Rate of Occurrence (ARO)**: How often you expect a data breach to happen in a year.

---

### Example:

Let’s say:
- **Asset Value (AV)**: $1,000,000 (Value of sensitive customer data)
- **Exposure Factor (EF)**: 30% (30% of the data is compromised in the breach)
- **ARO (Annual Rate of Occurrence)**: 0.05 (This means a breach happens 5% of the time each year)

#### SLE = AV * EF SLE = $1,000,000 * 0.30 SLE = $300,000
#### SLE = AV * EF SLE = $1,000,000 * 0.30 SLE = $300,000
#### ALE (new) = SLE * ARO (new) ALE (new) = $300,000 * 0.01 ALE (new) = $3,000
#### ROI = (ALE (before controls) - ALE (after controls) - Cost of Controls) / Cost of Controls ROI = ($15,000 - $3,000 - $50,000) / $50,000 ROI = -$38,000 / $50,000 ROI = -0.76 or -76%

---

# Reflections

What data security meansures do we have in place

IAM
Encryption
Interval VPC





