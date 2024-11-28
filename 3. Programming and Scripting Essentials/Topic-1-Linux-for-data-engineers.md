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

- **Data processing**: Engineers use CLI tools to process raw data from space missions. Commands such as **grep, awk, and sed** help in filtering and transforming data efficiently, which is essential for extracting meaningful information from vast datasets.

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

Video explaining the Linux file system - https://www.youtube.com/watch?v=bbmWOjuFmgA

## Key Linux utilities for data engineers
Utilities for manipulating and analysing text files, include tools such as grep, sed, and awk. These tools are vital for parsing log files, transforming data, and extracting insights. Here is a brief overview of these tools: 

- **Global regular expression print (grep):** These search for patterns within files.
- **Stream editor (sed):** The stream editor is used for modifying file content
- **awk:** This is used for pattern scanning and processing language

**A Netflix case study**
Netflix ensures service reliability by meticulously monitoring its log files using the powerful Unix command-line utility grep. 
This tool, integral to their system administration toolkit, allows them to search through massive log files for specific patterns that indicate errors or anomalies. 
By automating the use of grep, Netflix can swiftly identify and respond to potential issues, maintaining the seamless streaming experience their users expect.

The primary function of **grep** is to search for and highlight specific text patterns within files. Netflix uses grep to scan logs for common error keywords such as "error," "fail," and "exception." This is often done in a case-insensitive manner to ensure no relevant log entry is missed. The ability to search through logs efficiently helps Netflix quickly isolate errors and understand the context in which they occur, which is crucial for rapid troubleshooting and maintaining service uptime. 

Moreover, Netflix combines grep with other command-line tools to enhance its log analysis capabilities. By using grep alongside utilities for sorting, counting, and aggregating data, they can track error frequencies and identify recurring issues. This comprehensive approach not only aids in immediate problem resolution but also helps in proactive maintenance, allowing Netflix to preemptively address issues before they escalate, thus ensuring consistent and reliable service for its global user base 

### Mastering grep: Efficient log file analysis for error detection
grep is a powerful command-line tool in Unix-like systems that allows you to search for specific patterns (regular expressions) within text files. When it comes to analysing log files, grep becomes an indispensable ally. In this section, we will explore various grep commands and examples to efficiently detect errors, failures, and exceptions in log files. Whether you are troubleshooting system issues or monitoring application logs, mastering grep will significantly enhance your productivity. Here are examples of how to use grep to scan log files for common error keywords such as "error," "fail," and "exception" in a Unix-like system:

**Basic usage**
To search for the keyword "error" in a log file named application.log, you would use: grep "error" application.log

**Case insensitive search**
To search for "error" in a case-insensitive manner, which also captures "Error" and "ERROR":

  grep -i "error" application.log

**Multiple keywords**
To search for multiple keywords such as "error," "fail," and "exception":

grep -E "error|fail|exception" application.log
Alternatively, you can use the -e option to specify multiple patterns:

  grep -e "error" -e "fail" -e "exception" application.log

**Contextual search**
To display lines containing "error" along with 2 lines of context before and after each match:

grep -C 2 "error" application.log

**Count matches**
To count the number of lines that match the keyword "error":

  grep -c "error" application.log

**Display line numbers**
To display line numbers along with matching lines:

  grep -n "error" application.log

For a comprehensive search that is case-insensitive, looks for multiple keywords, displays context, and shows line numbers:

  grep -i -n -C 2 -E "error|fail|exception" application.log

**Data transfer and compression**
Efficient data transfer and compression are crucial for managing large datasets across different systems. Tools for transferring and compressing data, such as rsync, scp, tar, and gzip. 

Explanation and examples include the following:
- **rsync:** Synchronizes files and directories between two locations
- **tar and gzip:** Archiving and compressing files

**Grep by example interactive guide** https://antonz.org/grep-by-example/

## Job scheduling and automation

### cron jobs
A cron job is a scheduled task that runs automatically at specified intervals. The syntax for defining a cron job consists of five fields, which represent the minute, hour, day of the month, month, and day of the week when the task should execute. These fields are separated by spaces and use special symbols to denote specific values, as follows:

- Minute (0-59): The minute when the task should run.
- Hour (0-23): The hour when the task should run.
- Day of the Month (1-31): The day of the month when the task should run.
- Month (1-12): The month when the task should run.
- Day of the Week (0-6, where 0 represents Sunday): The day of the week when the task should run. For example, the following cron job runs a backup script every day at 2:30 AM: 30 2 * * * /path/to/backup-script.sh.

Cron jobs are commonly used for various technical tasks, including: 
- Scheduling data backups: Automating regular backups of databases, files, or other critical data.
- Extract, transform, load (ETL) processes: Running data extraction, transformation, and loading tasks at specific intervals.
- System maintenance tasks: Performing system cleanup, log rotation, or other maintenance activities automatically.

**Using cron for Job Scheduling**
In addition to advanced orchestration tools, Airbnb also uses cron, a standard Unix-like operating system utility, to schedule tasks. 
cron jobs are scheduled commands or scripts that run at specific times or intervals. 
These jobs are defined in the crontab (cron table) file.

**Understanding crontab**
crontab is a command-line utility used to schedule cron jobs. Each user can have their own crontab file, and there is also a system-wide crontab for tasks that need to be run by the system.
To submit a cron job, you use the crontab command with the -e flag, which opens the crontab file for editing. 

**crontab entry format**
Here’s a breakdown of how to set up a cron job:

* * * * * command_to_run 

Explanation:
Each asterisk (*) represents a time value:

Minute (0 - 59)
Hour (0 - 23)
Day of the month (1 - 31)
Month (1 - 12)
Day of the week (0 - 6) (Sunday to Saturday)

**example crontab entries**
Running a Script Every Day at Midnight:

0 0 * * * /usr/local/bin/daily_job.sh 

Explanation: This line schedules the daily_job.sh script to run at midnight every day. The 0 0 at the beginning specifies the minute and hour (0 minutes past 0 hours, or midnight).

**Running**
To count the number of lines that match the keyword "error":

grep -c "error" application.log

**Running a script every hour**
0 * * * * /usr/local/bin/hourly_job.sh 

This line schedules the hourly_job.sh script to run at the start of every hour. 
The 0 * specifies the job runs at the 0th minute of every hour.

**Submitting a cron job**
To submit a cron job, you edit the crontab file by running:

crontab -e 
This opens the user's crontab file in a text editor, where you can add, remove, or edit cron jobs.

Explanation:nBy using cron and crontab, Airbnb ensures that data processing tasks are automated and executed reliably at specified times, contributing to efficient and timely data reporting. 

This automation is crucial for maintaining the smooth operation of their data infrastructure.

### Writing and executing simple scripts in Linux
**Creating a script file**
Begin by opening a text editor and creating a new file with a .sh extension. For example, you can use nano:
nano myscript.sh 

**Give it some 'shebang'!**
The first line of your script should specify the shell interpreter, known as the shebang. 

For a typical Bash script, you would write:
#!/bin/bash 
This line tells the system to use the Bash shell to execute the script.

**Writing commands**
Add the commands you want the script to execute. 

For example, a simple script to print "Hello, World!" and list the files in the current directory might look like this:
#!/bin/bash
 echo "Hello, World!"
 ls -l 

**Saving and exiting**
Finally, you should save the file and exit the text editor (in nano, you would press Ctrl+X, then Y to confirm, and Enter to save).

### Making the code executable
**Make script executable**
Before running the script, you need to make it executable. This is done using the chmod command:
chmod +x myscript.sh 

**Execute the scipt**
Once the script is executable, you can run it from the terminal by specifying the path to the file. 

If the script is in the current directory, use:
./myscript.sh 

**The script execution process**
When executed, the shell reads the script file line by line, interpreting and running each command sequentially. 
This allows for complex operations to be automated simply by running the script.

### Practical applications
**Automating Backups:** A script can be scheduled to run daily backups of critical data, using the following code:
#!/bin/bash
tar -czf backup_$(date +%Y%m%d).tar.gz /path/to/data 

**System Monitoring:** Scripts can check system health and log the status, alerting administrators if necessary, using the following code:
#!/bin/bash
echo "System Load:" > /var/log/sysload.log
uptime >> /var/log/sysload.log 

### Redirection operators
**>:** This is the redirection operator. It directs the output of the echo command to a file instead of the terminal.
Types of redirection operators:

**> (Single Redirect):**
This redirects the output of a command to a file
If the file exists, its content is overwritten
If the file does not exist, it is created

**>> (Append Redirect):**
This redirects the output of a command to a file
If the file exists, the new output is appended to the end of the file
If the file does not exist, it is created

### Pipes
Similar to redirects, pipes (|) are used in Unix-like systems to pass the output of one command as the input to another. 

This is useful for chaining commands together to perform more complex operations. 

Example:
ls -l | grep "txt"
Lists detailed information about files and directories, then filters the output to show only those containing "txt".

## Advanced text processing and log management
### Advanced grep usage
Global regular expression print (Grep) is a versatile tool that allows you to search for patterns, extract relevant information, and manipulate text effortlessly. 
Whether you are dealing with voluminous log files, intricate configuration data, or streaming information, Grep becomes your trusted companion.

By mastering advanced Grep usage, you will acquire the ability to: 
Fine-tune your search: The minute when the task should run
Utilise options like -E, -v, and -c to tailor your searches
Filter out superfluous log entries, zero in on specific patterns, and count occurrences

**Examples**
Filtering errors:
Hunt down error messages in log files: grep "error" application.log

Counting occurrences:
Tally how many times a specific pattern appears: grep -c "warning" access.log

### Log management and monitoring
Log management plays a pivotal role in maintaining system health, diagnosing issues, and ensuring compliance. 
As professionals responsible for data infrastructure, we face the challenge of efficiently managing logs, detecting anomalies, and responding promptly to potential threats. 
Whether you are overseeing logs for a small application or a complex network, mastering these skills ensures smoother operations. 

**Examples**
Real-time monitoring:
Keep a vigilant eye on incoming logs: tail -f application.log

Automated rotation: 
Rotate logs to prevent overload: logrotate -v /etc/logrotate.conf

**For more details see Linux command cheat sheet in this repo**

## Lecture notes
CLI, Shell and terminal are all the same thing

Linux OS is open source, so unlike MacOS and Windows you can fork the OS and edit/customise it

Mac is POSIX. POSIX means that it can run linux, unix, bsd and recompile and run the code

Linux was created by Linus Torvids

In Linux - "Everything is a file"

A directory is a special type of file

Every file can be four types:
1. Ordinary file (contains data/info)
2. Directories (holds files and other directories
3. Devices (accessing the hardware)
4. Links (Pointer to another file)

Linux is more efficient because it can write straight to the hardware. Whereas windows for example you write a script to windows that then accesses the hardware

Important directories
/etc - Configuration files
/dev - Devices
/tmp - Temporary files
/mnt - Mount directory

![Linux file system](https://miro.medium.com/v2/resize:fit:1400/0*bFnHaO8eYpW3dSuz)

bin are the binaries, whaich are the system files

linux rarely ever reboots - another benefit for using it for data transfering 

linux has a GUI for the OS to use it graphically but you can also use via CLI

It's the mantra of superusers to use terminal because you have more control over what you're trying to do

![Ubuntu OS](https://149366088.v2.pressablecdn.com/wp-content/uploads/2017/04/gnome-ubuntu-desktop.jpg)

**Don't do anything as root**
Root is the all powerful account and shouldn't be used when browsing internet etc. Only for admin tasks (installing software, configuring servers)

**sudo (super user do)**
this allows you to temporarily become the root user to have extra privileges. Called privilege escallation 

Remember with passwords etc in linux you won't see *'s or any characters

### Linux security model

Attackers will want to get "root" privileges 

crux of problem is use Discretionary access control (DAC) - basically all files have their own permissions

There's a special syntax to this:
**rwx**: read, write and execute 
**rw-**: read and write 
**r--**: read only 

There is a character at the front to show what kind of file it is. For example directory is d and the file might be **drwx**

Regular file is - so **-rwx** is a regular file with those privileges

Set this using **chmod** command

Commands are case sensitive. Lower case

### Linux commands
**ls** - list dir contents
**cd** - change dir
**pwd** - display present working dir
**cat** - concatenates and displays files
**echo** - display arguments to the screen
**man** - display the online manual
**exit** - exits the shell or session
**clear** - clears screen

you can string these together. **man cat** for example will sho the manual for the cat command 

Any command with -h or --help will give more info

If you don't know the command you can try **man -k [SEARCH TERM]** to try and search by keyword

**Navigating**
cd.. - goes up a level
cd ~/mydir - goes to currently using user dir. (~ pronounced tild e)
su - switch user
passwd - change password
(The below were created before mouses but it's still the way to navigate)
Enter - moves down a line
Space - move down one page
g - moves to top of a page
G - moves to top of the page
q - quit

![Linux command cheat sheet](https://images.ctfassets.net/aw6mkmszlj4x/2oDcVTRgDK6KIVBshsKuO8/54d205b6c365cd181430565f3706be9c/linuxthree.png)

### Shell scripting basics
#!bin/sh
echo "Welcome to Linux --"$USER
ehco "Today is: "$(date)
echo "You're working in: "'pwd'
echo "Enter your last name:"
read LNAME 
echo "Hello " $LNAME

**To practice Linux use this website**
https://shell.segfault.net/#/dashboard

**nano** is text editor
can use tab for auto complete (this gives blank editor)

To run something is **./scriptname** ./ is the current directory

remember to change file to executable before running a script
**chmod +x FILENAME**

## Topic 1 Reflections
Try and find area in the business using Linux and speak to the engineers about it

