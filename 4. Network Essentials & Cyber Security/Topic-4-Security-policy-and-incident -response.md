# Topic 4 Security Policy and Incident Responce 27/02/2025

## Developing an evaluating security policies

#### Why companies need security policies and procedures

Security policies cover various aspects of information security, including access control, data protection, and incident response. For instance, an access control policy defines who can access what information and under what conditions. A data protection policy outlines how data should be handled, stored, and transmitted to ensure its security. An incident response policy provides a roadmap for handling security breaches and mitigating their impact. IT policies and procedures complement each other. Policies highlight areas within security that need assistance, while procedures explain how that security area will be addressed.

### Example Security Policies

**General information security policy**

Provides a holistic view of the organisation's need for security and defines activities used within the security environment.

**Access security policy**

Addresses how users are granted access to applications, data, databases and other IT resources. This policy is particularly important for audits.

**Authentication policy**

Governs how users are verified to access a system's resources.

**Password policy**

Defines how passwords are configured and managed.

**Perimeter security policy**

Defines how an organisation protects its network perimeter from unauthorized access and the technologies used to minimise perimeter porosity.

**Cybersecurity policy**

Defines how an organisation prepares and responds to malware, phishing, viruses, ransomware and other attacks.

**Cloud security policy**

Defines the security parameters for situations involving cloud-based technology, such as data storage and applications.

**Patching policy**

Defines the process for installing and managing patches for various systems, including security systems.

**Physical access policy**

Addresses how company assets, such as data centres, office buildings, parking garages and other physical facilities, are protected from unauthorized access.

### How to prepare a security policy

Discrepancies and weaknesses in policies are often brought up during audits, so it's best to prepare in advance. It's also common for users to have safety concerns about their data and systems, so it's advised to disseminate security policies to employees and clients to alleviate their concerns. Businesses normally follow these steps when preparing a security policy:

1. Identify the business purpose for having a specific type of IT security policy.
2. Secure approval from senior management to develop the policy.
3. Adapt existing security policies to maintain policy structure and format, and incorporate relevant components to address information security.
4. Establish a project plan to develop and approve the policy.
5. Create a team to develop the policy.
6. Schedule management briefings during the writing cycle to ensure relevant issues are addressed.
7. Invite internal departments to review the policy, particularly the legal team and HR.
8. Invite the risk management team to review the policy.
9. Distribute the draft for final review before submitting to management.
10. Secure management approval and disseminate the policy to employees.
11. Establish a review and change process for the policy using change management procedures.
12. Schedule and prepare for annual audits of the policy.
13. Make policy widely accessible via multiple channels.

## Implementing risk mitigation strategies

#### How do you implement policies?

The steps to take:

1. **Assess Needs:** Determine which systems and data require MFA (multi factor authentication).
2. **Select Methods:** Choose appropriate authentication factors (e.g., SMS codes, authentication apps, biometrics). A successful MFA approach uses a combination of something you know (password), something you have (smartphone), and something you are (biometrics) for MFA. Ensure user convenience while implementing MFA to avoid resistance to adoption.
3. **Rollout:** Implement MFA across the organization, starting with high-risk areas.
4. **Monitor and adjust:** Continuously monitor the effectiveness of MFA and make adjustments as needed.

#### How do you implement security control?

The steps to take:

1. **Draft policy** that mandates MFA for all employee and customer logins, and extra training to be scheduled.
2. **Invite** internal departments to review the policy, particularly the legal team and HR.
3. **Educate Users:** Provide training to ensure users understand how to follow this polict effectively.
4. **Publish** and make policy widely accessible via multiple channels.

### Conducting security assessments

Security assessments are a fundamental part of risk mitigation. They help identify vulnerabilities that could be exploited by attackers. Regular assessments enable organizations to address weaknesses before they can be leveraged for malicious purposes.

- **Interesting Fact:** The average cost of a data breach in 2021 was $4.24 million, emphasizing the importance of proactive security measures.
- **Best Practice:** Use automated tools to regularly scan for vulnerabilities.
- **Key Consideration:** Combine automated scans with manual testing to uncover less obvious vulnerabilities.

#### Types of security assessments

**Vulnerability scanning**
Automated tools scan systems for known vulnerabilities. Examples include **OpenVAS** and **Nessus**.

**Penetration testing**
Ethical hackers simulate attacks to uncover potential security weaknesses. Tools like **Metasploit** can assist in this process.

**Risk assessments**
Comprehensive evaluations that consider the likelihood and impact of different threats. Frameworks like NIST SP 800-30 guide this process.

#### Applying security patches

Regularly applying security patches is critical for protecting systems from known vulnerabilities. Cybercriminals often exploit unpatched systems, making timely updates essential.

```
Best Practice:
Implement a patch management policy that includes regular updates and emergency patching for critical vulnerabilities.
Ensure compatibility and test patches in a staging environment before deployment.
```

#### The patch management process

The patch management process is as follows:

1. **Inventory Systems:** Maintain an up-to-date inventory of all software and hardware.

2. **Monitor for Updates:** Regularly check for patches and updates from vendors.

3. **Test Patches:** Test patches in a controlled environment to ensure they do not disrupt operations.

4. **Deploy Patches:** Apply patches to production systems promptly.

5. **Verify and Document:** Verify that patches are applied correctly and document the process.

#### Open-source resources for risk mitigation

Open-source tools offer cost-effective solutions for implementing robust security measures. Regularly update and maintain open-source tools to benefit from the latest security features and patches. Evaluate the security and reliability of open-source tools before deployment.

Here's some you should be aware of:

1. **OpenVAS:** An open-source vulnerability scanner that helps in identifying security issues in systems and applications. It provides comprehensive reports and recommendations for remediation.
2. **Metasploit:** A powerful penetration testing framework that allows security professionals to test the effectiveness of their defences and identify potential vulnerabilities.
3. **OWASP ZAP (Zed Attack Proxy):** A tool for finding security vulnerabilities in web applications during development and testing. It is widely used for dynamic application security testing (DAST).
4. **CIS-CAT:** The Center for Internet Security Configuration Assessment Tool helps organizations assess and improve their security posture based on CIS benchmarks.
5. **Snort:** An open-source intrusion detection and prevention system (IDPS) that monitors network traffic for suspicious activities and generates alerts.

#### The importance of security monitoring and incident response in risk mitigation

In an increasingly digital world, where cyber threats are becoming more sophisticated and frequent, the importance of robust security monitoring and an effective incident response plan cannot be overstated. Organisations of all sizes and across all sectors are potential targets for cybercriminals, and the ability to detect and respond to security incidents in real-time is crucial for safeguarding sensitive data and maintaining trust with stakeholders.

### Continuous Monitoring

Continuous network monitoring is the foundation of a proactive security strategy. Unlike traditional monitoring, which may involve periodic checks, continuous monitoring involves the real-time surveillance of network traffic, system logs, and user activity. This approach is vital because it allows organisations to detect and respond to threats as they occur, significantly reducing the time between detection and response, known as the 'dwell time'. The shorter the dwell time, the less opportunity there is for an attacker to cause damage.

A key tool in continuous monitoring is the Security Information and Event Management (SIEM) system. SIEM systems aggregate and analyse log data from across an organisation's IT environment, providing a comprehensive view of security events. By correlating data from various sources, SIEM systems can identify patterns indicative of potential threats, such as unusual login attempts, unauthorised access to sensitive files, or anomalies in network traffic.

The benefits of continuous monitoring extend beyond mere threat detection. It also enables organisations to maintain compliance with regulatory requirements, such as the General Data Protection Regulation (GDPR) in the UK and Europe. These regulations often require organisations to demonstrate that they have implemented adequate security measures to protect personal data. Continuous monitoring provides the necessary audit trails and reports to fulfil these obligations.

Moreover, continuous monitoring supports the principle of 'defence in depth', where multiple layers of security controls are implemented to protect an organisation's assets. By providing ongoing visibility into the effectiveness of these controls, continuous monitoring helps organisations to identify weaknesses and areas for improvement in their security posture.


### Incident Responce Plan

While continuous monitoring is essential for detecting threats, having a well-defined incident response plan is equally crucial for effectively addressing and mitigating security breaches. An incident response plan outlines the procedures that an organisation should follow when a security incident occurs. This plan ensures that responses are timely, coordinated, and effective, minimising the potential impact on the organisation.

A comprehensive incident response plan typically includes several key components: preparation, identification, containment, eradication, recovery, and lessons learned. During the preparation phase, organisations establish the policies, tools, and teams needed for incident response.

The identification phase involves recognising that an incident has occurred, often triggered by alerts from the SIEM system. Containment involves isolating the affected systems to prevent the incident from spreading, while eradication focuses on removing the threat. Recovery entails restoring normal operations, and the lessons learned phase involves reviewing the incident to improve future responses.

The importance of an incident response plan cannot be underestimated. In the event of a security breach, an uncoordinated or delayed response can exacerbate the damage, leading to financial loss, reputational damage, and legal consequences. Conversely, a well-executed incident response can significantly reduce the impact of an incident, ensuring that normal operations are restored quickly and that any legal and regulatory requirements are met.

```
The key message

In summary, mitigating network security risks requires a comprehensive approach that includes a combination of technical, administrative, and procedural measures.

Continuous monitoring provides the real-time visibility needed to detect threats before they can cause significant harm, while an incident response plan ensures that when incidents do occur, they are handled swiftly and effectively.

Together with incident response plans and other practices described in this lesson, risk mitigation strategies help organisations to protect their assets, maintain compliance, and build resilience against the ever-evolving landscape of cyber threats.
```

## Learning from security incidents and near-misses

Documenting and analysing security incidents and near-misses is essential for improving future response strategies. This lesson covers the importance of thorough documentation and how to use incident reports to enhance security measures. By learning from past incidents, organisations can refine their security policies, minimise the impact of future breaches, and ensure continuous improvement. Learning from past incidents helps organisations refine their security policies and response strategies. Detailed documentation provides valuable insights that can prevent future occurrences and improve overall security readiness.

### Why document security incidents?

Its important to document security incidents for the following reasons:

1. **Accountability:** Proper documentation holds individuals and teams accountable for their actions during an incident.
2. **Learning and Improvement:** Detailed records help identify patterns and recurring issues, facilitating continuous improvement.
3. **Compliance:** Many regulations require detailed incident reporting. Compliance ensures that the organisation avoids penalties and maintains trust.
4. **Communication:** Documentation helps communicate the nature and impact of incidents to stakeholders, including management, clients, and regulatory bodies.

### Steps for documenting security incidents

Use a standardised template for incident documentation to ensure consistency and completeness. Include both technical and non-technical details to provide a full picture of the incident.

1. **Incident Detection:** Record the initial detection of the incident, including the time, date, and method of detection (e.g., automated alert, user report).
2. **Initial Response:** Document the immediate actions taken to contain the incident, such as isolating affected systems or shutting down services.
3. **Incident Analysis:** Provide a detailed analysis of the incident, including the type of attack, affected systems, and data compromised. Use tools like Splunk or ELK Stack for log analysis.
4. **Mitigation and Recovery:** Record the steps taken to mitigate the impact of the incident and restore normal operations. Include timelines and responsible personnel.
5. **Post-Incident Review:** Conduct a post-incident review to identify lessons learned and recommend changes to policies or procedures. Document any follow-up actions required.

Guidance for analysing incident reports includes:

1. **Identify Root Causes:** Determine the underlying causes of the incident, such as a misconfigured firewall or unpatched vulnerability. Tools like Root Cause Analysis (RCA) and Failure Mode and Effects Analysis (FMEA) can be helpful.
2. **Assess Impact:** Evaluate the impact of the incident on operations, finances, and reputation. This helps prioritise remediation efforts and resource allocation.
3. **Implement Improvements:** Based on the analysis, implement improvements to prevent recurrence. This could include technical fixes, policy changes, or additional training.
4. **Review Effectiveness:** Continuously monitor and review the effectiveness of the implemented improvements. Make adjustments as needed to ensure ongoing security.

Using incident documentation to enhance future response

Conduct regular incident response drills to test and refine your incident response plan. Involve all relevant stakeholders in the incident response process to ensure a comprehensive and coordinated approach. Here are some strategies for enhancing you future response:

1. **Update Response Plans:** Incorporate lessons learned from past incidents into your incident response plan. Ensure that the plan is practical and actionable.
2. **Train Personnel:** Provide regular training for all employees on updated response procedures. Include scenario-based training to improve readiness.
3. **Improve Communication:** Establish clear communication channels for incident reporting and response. Ensure that all team members know their roles and responsibilities during an incident.
4. **Utilise Technology:** Leverage technology such as Security Information and Event Management (SIEM) systems and automated response tools to enhance detection and response capabilities.
5. **Conduct Regular Reviews:** Regularly review and test your incident response plan to ensure its effectiveness. Adjust the plan based on feedback and new threats.

#### Open-source resources for incident documentation and response

Open-source tools can provide cost-effective and flexible solutions for incident documentation and response. Regularly update and maintain open-source tools to benefit from the latest features and improvements. Remember to evaluate the security and reliability of open-source tools before deployment and check if they are whitelisted by your organisation.

Open-source tools include:

1. **TheHive:** An open-source Security Incident Response Platform (SIRP) designed to help manage and document security incidents. It provides features for case management, collaboration, and reporting.
2. **Cortex:** An open-source tool that works with TheHive to automate the collection and analysis of observables, such as IP addresses and file hashes, during an incident investigation.
3. **MISP:** The Malware Information Sharing Platform (MISP) is an open-source threat intelligence platform that facilitates the sharing of threat data and incident information.
4. **GRR Rapid Response:** An open-source incident response framework focused on remote live forensics and investigation. It helps identify and mitigate threats across large networks.
5. **OSSEC:** An open-source host-based intrusion detection system (HIDS) that can monitor and analyse logs, files, and processes for suspicious activities.

```
By incorporating these open-source tools into your incident response strategy, you can enhance your ability to document, analyse, and respond to security incidents effectively.
Regularly updating and maintaining these tools ensures that you benefit from the latest features and improvements, thereby strengthening your overall security posture.
```

## The impact of downtime

`Interesting Fact: According to Gartner, the average cost of IT downtime is $5,600 per minute, which translates to more than $300,000 per hour.`

### Using the multiple why's framework

The multiple why's framework involves asking 'why' repeatedly (typically five times) to drill down to the root cause of a problem. Each answer forms the basis for the next "why" question.

- **Interesting Fact:** The multiple why's technique, also known as 5 Whys, was developed by Sakichi Toyoda and is used in Toyota’s manufacturing process to uncover root causes.
- **Best Practice:** Apply the multiple why's framework iteratively to explore different dimensions of a problem.
- **Key Consideration:** Ensure that each "why" question is based on factual data to avoid assumptions.

An example

1. **Why did the server fail?** – Because it overheated.
2. **Why did it overheat?** – Because the cooling system was not functioning properly.
3. **Why was the cooling system not functioning properly?** – Because it had not been maintained regularly.
4. **Why was it not maintained regularly?** – Because there was no scheduled maintenance plan.
5. **Why was there no scheduled maintenance plan?** – Because the organisation did not prioritise preventive maintenance.

#### Practical steps for downtime investigation

A survey by Uptime Institute found that 80% of data centre downtime incidents are preventable with proper planning and maintenance. Best Practice: Document each step of the investigation process to ensure a comprehensive review. Involve cross-functional teams to gather diverse perspectives and expertise.

Steps for investigating downtime include:

1. **Initial detection:** Record the exact time and method of detection (e.g., monitoring alert, user report).
2. **Immediate Response:** Document the immediate actions taken to mitigate the impact (e.g., failover procedures, temporary fixes).
3. **Data Collection:** Gather logs, monitoring data, and user reports to get a complete picture of the incident.
4. **Root Cause Analysis:** Use the multiple why's framework to identify the root causes.
5. **Solution Implementation:** Develop and implement solutions to address the root causes.
6. **Review and Document:** Conduct a post-incident review, document the findings, and update policies and procedures as necessary.

#### Implementing preventive measures

Develop a comprehensive maintenance schedule that includes hardware, software, and network components. Regularly review and update preventive measures based on new data and technological advancements.

Preventive measures include the following:

1. **Scheduled Maintenance:** Regularly inspect and maintain hardware and software to prevent failures. Use tools like Nagios or Zabbix for automated monitoring and alerts.
2. **Redundancy:** Implement redundancy in critical systems to ensure availability in case of failure. This includes backup power supplies, failover servers, and redundant network paths.
3. **Training and Awareness:** Provide ongoing training for staff to recognise and respond to potential issues before they escalate.
4. **Patch Management:** Regularly apply security patches and updates to all systems. Use patch management tools like WSUS or Ansible to automate the process.
5. **Disaster Recovery Planning:** Develop and regularly test disaster recovery plans to ensure quick recovery from major incidents.

#### Continuous improvement through analysis

Establish a feedback loop where insights from downtime analyses inform future preventive measures. Foster a culture of continuous improvement by encouraging proactive problem-solving and innovation.

A suggested continuous improvement process is as follows:

1. **Post-Incident Review:** After resolving downtime, conduct a thorough review to analyse what happened and why. Use tools like Root Cause Analysis (RCA) and Failure Mode and Effects Analysis (FMEA).
2. **Implement Recommendations:** Based on the review, implement recommendations to prevent future incidents. This might include technical fixes, policy changes, or additional training.
3. **Monitor Effectiveness:** Continuously monitor the effectiveness of implemented changes. Use metrics and KPIs to measure improvements.
4. **Feedback Loop:** Create a feedback loop where findings from each incident feed into the planning and implementation of preventive measures.
5. **Regular Updates:** Regularly update the incident response plan and preventive measures to reflect new insights and changes in the environment.

---

## Reflections



