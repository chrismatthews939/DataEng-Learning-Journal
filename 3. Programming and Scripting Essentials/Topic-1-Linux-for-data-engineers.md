# Topic 1 - Linux for Data Engineers - 28/11/2024
  
## What is Linux and why use it?

![Linux](https://images.vexels.com/media/users/3/140692/isolated/lists/72d1f12edf758d24f5b6db73bac4f297-linux-logo.png)

Linux, the open-source operating system, stands as the bedrock of many Big Data solutions. Its robustness, security, and flexibility make it indispensable for data engineers. In this lesson, we will delve into why and how Linux is pivotal for managing and processing large datasets efficiently.

### Why X (formerly Twitter) uses Linux to manage it's data

**An exemplary data-driven enterprise** -
X formerly known as Twitter, a leading social media platform, serves as an exemplary data-driven enterprise. It handles an enormous volume of data daily, including tweets, user interactions, and multimedia content.
To efficiently manage this massive data infrastructure, Twitter relies on Linux. As we discussed, data-driven enterprises leverage vast amounts of data to make informed decisions and drive business strategies. 

**Stability and reliability** -
X/Twitter's data infrastructure must be robust, scalable, and secure to support its global user base and real-time data processing needs. Linux's stability and reliability make it the ideal choice for such demanding environments. 
The operating system's ability to run continuously with minimal downtime ensures that Twitter can provide uninterrupted service to its users, maintaining high levels of performance and user satisfaction. 

**Security and privacy** -
Linux's security features are crucial for protecting user data and maintaining privacy. The open-source nature of Linux allows X/Twitter's engineers to customise the system, optimising it for their specific requirements. 
This flexibility is particularly valuable in a data-driven enterprise, where tailored solutions can significantly enhance efficiency and effectiveness.

### Using the Command Line Interface (CLI) also know as shell
 The shell is a powerful tool that allows users to interact directly with the operating system through text-based commands. For data-driven enterprises like X/Twitter, the shell CLI is indispensable.

### Linux in action (Mars rover mission)
The rovers send back a continuous stream of data, including images, environmental readings, and scientific measurements. This data must be transmitted over vast distances, processed, and analysed quickly. Linux systems manage this entire process, from the initial reception of data at ground stations to its analysis and storage. NASA extensively uses the Linux system for various technical applications, including:

- **Data processing**: Engineers use CLI tools to process raw data from space missions. Commands such as grep, awk, and sed help in filtering and transforming data efficiently, which is essential for extracting meaningful information from vast datasets.

- **System monitoring**: Monitoring the health and performance of computational clusters is critical. CLI tools like top, htop, and dstat provide real-time insights into system resource usage, helping engineers to maintain system stability and performance.

- **Automation**: Automation is key in handling repetitive tasks and managing complex workflows. Shell scripting in Linux allows NASA to automate data processing pipelines, reducing manual intervention and increasing efficiency.
 
Linux systems are known for their stability and reliability, capable of running for extended periods without requiring a reboot. This is crucial in server environments where uptime and consistency are paramount. Imagine the importance of a web server that needs to be accessible 24/7—Linux can handle such demands efficiently. Security is another significant advantage of Linux. Due to its open-source nature, a global community of developers continuously scrutinises the code, identifying and addressing vulnerabilities swiftly. This collaborative approach ensures that security patches and updates are rolled out promptly, helping to protect systems against potential threats. For data engineers handling sensitive information, the security features of Linux provide an added layer of confidence.

![worldwide server operating environments](https://www.redhat.com/rhdc/managed-files/styles/wysiwyg_full_width/private/IDCGraphic2.png.webp?itok=7kR3HR6w)

Flexibility is also a hallmark of Linux. It can be customised to meet specific needs, making it a versatile choice for various applications. From lightweight installations suitable for embedded systems to robust configurations designed for high-performance computing, Linux adapts to diverse requirements. This flexibility extends to the wide range of distributions available, such as Ubuntu, CentOS, and Debian, each offering unique features tailored to different use cases. Moreover, Linux supports a vast array of software tools and frameworks essential for data engineering. Whether it is for data processing, analysis, or visualisation, Linux's compatibility with tools like Hadoop, Apache Spark, and TensorFlow makes it an invaluable asset in the data engineer's toolkit.

### Understanding the Linux system structure

![Linux system structure](https://images.javatpoint.com/linux/images/architecture-of-linux.png)

- **Kernal**: The core part of Linux that manages system resources, such as drivers and power usage

- **Shell**: The interface that allows users to interact with the kernel and with user programs/applications

- **Technical application**: For example Using the terminal to execute commands

## Navigating the Linux filesystem

### filesystem hierarchy standard (FHS)

**Effective filesystems: A Google case study**
Consider how Google’s data centres organise their filesystem to optimise data retrieval and storage. Google’s data centres are renowned for their efficiency, reliability, and innovative use of technology.


To achieve this, they utilise a sophisticated filesystem known as Colossus, which is an evolution of the original Google file system (GFS). This system is integral to handling Google's vast amounts of data and ensuring optimal performance and it follows FHS conventions. Google’s filesystem uses a hierarchical namespace that allows for efficient organisation and retrieval of data. Metadata servers manage the namespace, which includes directories and files, facilitating quick location of data within the system.

**Unpacking FHS**
Every general-purpose computer needs to store data of various types on a hard disk drive (HDD) or something equivalent. There are a couple reasons for this, but mostly because RAM loses its contents when the computer is switched off. There are non-volatile types of RAM that can maintain the data stored there after power is removed but they are pretty expensive. Therefore, we need a logical method of organising and storing large amounts of information in a way that makes it easy to manage. 

![FHS](https://i.imgur.com/gtuIBzE.png)

**What does this diagram tell us?**
- All data in Unix is organised into files. All files are organised into directories. These directories are organised into a tree-like structure called the “Filesystem”. 
- The filesystem hierarchy standard (FHS) is a reference describing the conventions used for the layout of Unix-like systems. 
- It has been made popular by its use in Linux distributions, but it is used by other Unix-like systems as well. It is maintained by the Linux Foundation.

### Understanding key directories
In the intricate world of Unix-like systems, directories play a crucial role in organising and managing data. Imagine a vast library where each shelf holds specific types of books—directories serve a similar purpose. In this section, we will explore essential directories and their purposes, unravelling the logic behind Unix’s orderly structure. 

- **/bin (Binaries)**: The /bin directory contains essential binary executables that are required for the system to boot and run in single-user mode. These are fundamental commands available to all users and necessary for basic system functionality.
  - **Examples of contents:** Common utilities like **ls** (list directory contents), **cp** (copy files), **mv** (move files), **rm** (remove files), and **bash** (Bourne Again SHell)
  - **Purpose:** Provide essential commands and tools for both users and the system for basic operations
 
- **/etc (Configuration files)**: The /etc directory contains all the system-wide configuration files and shell scripts that are used to boot and initialise system settings. This is where system administrators can configure the system's behaviour.
  - **Examples of contents:** Configuration files like fstab (file system table), passwd (user account information), and hosts (static table lookup for hostnames)
  - **Purpose:** Store configuration files that dictate how the system and various services operate

- **/home (Home directories)**: The /home directory is the default location for users' personal directories. Each user on the system has a subdirectory within /home where their personal files, configurations, and documents are stored.
  - **Examples of contents:** User directories like /home/alice, /home/bob, etc
  - **Purpose:** Provide a personal space for each user to store their files and settings, keeping them separate from system files and other users' data

- **/usr (User Binaries & Read-Only Data)**: The /usr directory contains user utilities and applications that are not essential for the system to boot or operate in single-user mode. It is often considered the second major hierarchy and includes various subdirectories.
  - **Subdirectories:**
    - /usr/bin: Non-essential command binaries (like gcc, python)
    - /usr/lib: Libraries for binaries in /usr/bin and /usr/sbin
    - /usr/share: Architecture-independent data (like documentation, icons)
    - /usr/local: Locally installed software and custom scripts
  - **Purpose:** Store the majority of user-space applications and files, separating them from the root filesystem to facilitate easier management and maintenance.

- **/var (Variable Data)**: The /var directory holds variable data files that are expected to grow in size over time. This includes system logs, user data files, caches, and other transient and dynamic files.

  - **Examples of contents:**
    - /var/log: Log files from the system and applications (like syslog, dmesg)
    - /var/spool: Spool directories for tasks like mail, printing
    - /var/tmp: Temporary files that need to be preserved between reboots
  - **Purpose:** Store data that changes frequently, ensuring that the filesystem layout is organised and prevents / from being cluttered with variable data.

### Technical application tips
1. Using commands like ls, cd, pwd to navigate the filesystem.
2. The ls command is used to list the contents of a directory. It provides information about the files and subdirectories within the specified directory.
3. The cd command is used to change the current working directory. It allows you to navigate through the filesystem.
4. The pwd command displays the full path of the current working directory. It is useful to confirm your current location within the filesystem.

### Key file operations
Essential file operations include creating, deleting, moving, and copying files and directories. Mastering file operations is fundamental for automating data engineering workflows.

**touch**
The touch command is used to create an empty file or update the timestamp of an existing file. 
It is a simple way to create new files or modify the access and modification times of files without changing their content.

**rm**
The rm command is used to remove files or directories. When applied to files, it deletes them permanently. 
When used with specific options, it can also recursively remove directories and their contents.

**mv**
The mv command is used to move or rename files and directories. 
It changes the location of a file or directory within the filesystem or changes its name, effectively performing both move and rename operations.

**cp**
The cp command is used to copy files and directories. It creates a duplicate of the specified file or directory in the target location, preserving the original. 
With appropriate options, it can also copy directories recursively.

![Video explaining the Linux file system](https://www.youtube.com/watch?v=bbmWOjuFmgA)

## Key Linux utilities for data engineers











## Lecture notes



## Topic 1 Reflections

