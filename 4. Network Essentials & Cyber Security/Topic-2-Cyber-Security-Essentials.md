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

Description

Amount

Number of Servers Affected

100

Replacement Cost per Server

£5,000

Total Replacement Cost

£500,000

Downtime Cost per Hour

£10,000

Average Downtime per Server

8 hours

Total Downtime Cost per Server

£80,000

Total Financial Impact

£8,500,000



  
# Lecture







