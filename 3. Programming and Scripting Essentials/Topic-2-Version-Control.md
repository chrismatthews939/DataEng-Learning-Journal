# Topic 2 - Version Control - 05/12/2024
  
## DevOps: Version control for data engineers
DevOps, a combination of "Development" and "Operations," emerged as a set of practices aimed at bridging the gap between software development and IT operations. The term gained traction in the late 2000s as organisations sought to improve their software delivery processes. DevOps advocates for continuous integration, continuous delivery, and continuous deployment, emphasising collaboration, automation, and monitoring throughout the software development lifecycle.

![Distributed version control systems](https://miro.medium.com/v2/resize:fit:1400/1*gPBljo_uRh-IBtHY2oB7ig.png)

**Version control as a DevOps practice**

Version control systems (VCS) like Git enable multiple team members to work on code simultaneously without overwriting each other's changes. This collaborative environment is essential in DevOps, where development and operations teams work together to shorten the development lifecycle and deliver high-quality software continuously. Version control tracks changes, manages versions, and allows rollback to previous states, ensuring that any errors can be swiftly corrected without disrupting the entire system.

### Git
Git is a distributed version control solution. It stores your code in a repository. You can have multiple repositories and share them with colleagues.

**Benefits**
- Collaboration
- Code history
- Branching
- Merging

**Technnical application**
- Using Git to manage code versions and collaborate on data projects

## Mastering CI/CD: A guide for data engineers

### Case study examples: Airbnb and Netflix
Airbnb and Netflix exemplify the effective use of DevOps and CI/CD practices to enhance their data engineering processes and overall operational efficiency. Let's look at each of these in turn and find out more. 

**Airbnb**
Airbnb, a global platform that connects people with unique travel experiences, handles vast amounts of data daily. This data is crucial for providing personalised user experiences, optimising search algorithms, and generating insights for business decisions.

**Here is a breakdown of how Airbnb optimises DevOps principles to maximise the value of this data:**
**DevOps**
- Airbnb manages its data pipeline jobs by adhering to core DevOps principles, including automation, continuous integration, and continuous deployment. 
- The team uses Git for version control, ensuring that all changes are tracked and managed systematically.

**Implementation**
- Job Scheduling: Data pipeline jobs are often defined in scripts executed on Linux systems. These scripts are version-controlled using Git and GitHub, ensuring that any changes are tracked, and historical versions can be restored if necessary.
- Branches and Commits: Developers create branches to work on new features or fixes independently. Once changes are tested and reviewed, they are merged into the main branch through pull requests.
- Continuous Integration: Jenkins is used to automate the testing of new commits. Each commit triggers a series of tests to ensure that changes do not introduce any errors.
- Continuous Deployment: After successful testing, Jenkins automates the deployment of updates to the production environment. Notifications are sent to the team regarding the deployment status, and error logs are monitored for any issues.

**Benefits**
- Timeliness. Automated scheduling ensures that data processing tasks are performed according to the defined schedule, which is critical for generating timely reports and insights.
- Version control. Using Git for pipeline scripts provides a robust framework for managing changes, facilitating collaboration among engineers, and ensuring the production environment's stability.
- Scalability. DevOps practices enable Airbnb to scale its data operations efficiently, accommodating the growing volume of data and increasing complexity of workflows.

**Netflix**
Netflix, a leading streaming service provider, relies heavily on sophisticated algorithms to personalise content recommendations for its users. The accuracy and efficiency of these algorithms are critical to retaining user engagement and satisfaction.
  
**Here is a breakdown of how Netflix optimises DevOps principles to maximise the value of this data:**
**DevOps**
- Netflix leverages Continuous Integration (CI) and Continuous Deployment (CD) to manage and deploy updates to its recommendation algorithms. This approach ensures that updates are thoroughly tested and seamlessly integrated into the production environment.
  
**Implementation**
- Version Control: Every change to the recommendation algorithms is tracked using Git and GitHub. This ensures that all updates are documented, and previous versions can be restored if needed.
- Branches and Commits: Developers work on separate branches for new features or improvements. Changes are committed to these branches and then merged into the main branch after thorough reviews.
- Automated Testing: Jenkins automates the testing of new commits. Automated tests include unit tests, integration tests, and performance tests to validate the changes.
- Continuous Deployment: Jenkins also automates the deployment process. Once the changes pass all tests, they are deployed to the production environment without manual intervention. Notifications are sent to the team about deployment status, and any issues are logged for immediate attention.

**Benefits**
- Quality assurance. Automated testing ensures that only reliable and high-performing updates are deployed, maintaining a high-quality user experience.
- Rapid innovation. Continuous deployment allows Netflix to introduce new features and improvements quickly, keeping the service competitive and engaging.
- Opperational efficiency. The integration of version control and CI/CD practices streamlines the workflow, reducing manual intervention and the risk of errors.

**Jenkins**

Jenkins is an open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration, and continuous delivery. 

![Jenkins](https://cdn.iconscout.com/icon/free/png-256/free-jenkins-logo-icon-download-in-svg-png-gif-file-formats--brand-company-world-logos-vol-3-pack-icons-282385.png)

Both Airbnb and Netflix use Jenkins

### CI/CD
Continuous Integration and Continuous Deployment (CI/CD)

![CI/CD](https://www.mabl.com/hubfs/CICDBlog.png)

**Example version control system**

![version control system](https://www.scaler.com/topics/images/setting-up-jenkins.webp)

## Conducting a code review
In the realm of software development, maintaining code quality and fostering team collaboration are paramount. One of the key practices that serve these objectives is code review. This process involves a systematic examination of a fellow developer’s code, aimed at catching errors, enhancing code quality, and promoting knowledge sharing. This lesson will delve into the concept of code reviews, their importance, and how they can be effectively conducted using GitHub. 

![code review](https://images.ctfassets.net/zsv3d0ugroxu/Z8dtCNdftgdcNAFQEnyYy/bc728a50ec535ed7ff5f062ef532efbd/PR_review_process)

** Pull Requests**
Pull requests (PRs) are a fundamental feature of GitHub that facilitate code reviews. When a developer completes a set of changes in a feature branch, they create a pull request to propose merging these changes into the main branch. 

The PR allows team members to review the code, discuss potential issues, and suggest improvements before the changes are integrated.

An example...
A developer works on a new feature for the data pipeline and pushes their changes to a feature branch in GitHub. They then create a pull request, summarising the changes and why they are necessary. Other team members are notified of the PR and begin reviewing the changes.

**A step-by-step guide to the review process**
1. **Initial Review**
  - Team members check the overall structure of the code, ensuring it adheres to coding standards and project guidelines
2. **Detail review**
  - Reviewers look for specific issues such as bugs, logic errors, and performance inefficiencies.
  - They also ensure that the code is well-documented and readable.
3. **Feedback**
  - Reviewers leave comments on specific lines of code or sections, providing constructive feedback.
  - They may suggest alternative approaches, point out potential bugs, or ask for clarifications.
4. **Discussion**
  - The developer who submitted the PR responds to comments, making necessary changes or explaining their decisions. 
  - This back-and-forth helps improve the code and foster a collaborative environment.
4. **Approval**
  - Once the reviewers are satisfied with the changes, they approve the pull request. 
  - The code can then be merged into the main branch, typically after passing automated tests and continuous integration checks.

** Best practices leaving feedback**
- Be specific
- Be respectful
- Focus on the code not the person

Good Feedback:
*“Consider using a dictionary here instead of a list for faster lookups. This will improve the performance of this function, especially with larger datasets”*

Bad Feedback:
*"This code is slow and inefficient"*

## Lecture Notes
Types of version control:
- Local. Local computer
- Central. Central server 
- Distributed. Git

**Git vs OneDrive/Dropbox**
Basically the same thing.
The jargon is slightly different.
Git pull is Onedrive sync
Git commit/checkout is Onedrive tracking 

**GitLab vs GitHub**

GitHub is Microsoft - GitLab is own company

![GitLab vs GitHub](https://graffersid.com/wp-content/uploads/2023/08/Difference-Between-GitLab-GitHub.jpg)

**Three stages of Git**
1. Modified. Files are changed but not committed
2. Staged. Modified file
3. Committed. Change is safely stored

Git is acyclical - A can point to B or C but can't point back to A. One direction only

git checkout is a way of going back in time to see an old version

**Semantic Versions**

e.g. 1.12.103

**Major** - Changes that break other people work (complete rewrite) 

**Minor** - Changes that don't brake anything

**Patch** - Bug fixes

**Branches**
- Main/Master
- Development branch
- Merged Branches

![git commands](https://miro.medium.com/v2/resize:fit:1400/1*seVNmyFK4RhNy_wVLQKonQ.png)

**git branching diagram**

![git branching diagram](https://www.nobledesktop.com/image/gitresources/git-branches-merge.png)

Use this link to practice git branching
https://learngitbranching.js.org/

git branching mantra is *branch fast and branch often* this is because branches just point to a commit and have no storage. It's better to heave lots of branches for small changes than one big branch with all the changes.

## Topic 2 Reflections
Implement code reviews into our CI/CD process. We currently don't do this with feedback for the developer.

