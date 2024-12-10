# NDG Linux Unhatched Course
https://portal.netdevgroup.com/learn/unhatched/GasK9avLUN/

## Basic Command Syntax
command [options…] [arguments…]

**cd** change directory
**cd ..** goes up a directory level

### Listing files
**ls [OPTIONS] [FILE]**

**su** switch user

**sudo** 
The sudo command allows a user to execute a command as another user without creating a new shell. Instead, to execute a command with administrative privilege

### File permissions
**-rwx**
r read w write4 x execute

**-r--rw-rwx. 1 sysadmin staff 999 Apr  10  2013 /home/sysadmin/test**
In this scenario, the user sysadmin ends up having less access to this file than members of the staff group or everyone else. The user sysadmin only has the permissions of r--. It doesn't matter if sysadmin is a member of the staff group; once user ownership has been established, only the user owner's permissions apply.

Changing file permissions
**chmod** change mode of access
The chmod command is used to change the permissions of a file or directory. Only the root user or the user who owns the file is able to change the permissions of a file.
ls -l hel

to change a read file called hello.sh to an execute would be
**chmod u+x hello.sh**
Then **./hello.sh** to run

**./** indicates you want to run from the current directory

### Changing ownership command
**chown**
To switch the owner of the hello.sh script to the root user, use root as the first argument and hello.sh as the second argument
**sudo chown root hello.sh**

### Viewing files
cat [OPTIONS] [FILE]

**cat** command to view files
cd Documents cat animals.txt 
goes into Documents folder and opens the animals file

**head** 
shows top of a file

**tail**
shows bottom of file

For specific number of rows use -n
**head -n 5 file.txt**
shows first 5 records

### Copying Files
cp [OPTIONS] SOURCE DESTINATION

**cp**
Permissions can have an impact on file management commands, such as the cp command. In order to copy a file, it is necessary to have execute permission to access the directory where the file is located and the read permission for the file being copied.

It is also necessary to have write and execute permission on the directory the file is being copied to. Typically, there are two places where you should always have write and execute permission on the directory: your home directory and the /tmp directory.

**dd**
dd [OPTIONS] OPERAND

The dd command is a utility for copying files or entire partitions at the bit level.

This command has several useful features, including:

- It can be used to clone or delete (wipe) entire disks or partitions.
- It can be used to copy raw data to removable devices, such as USB drives and CDROMs.
- It can backup and restore the MBR (Master Boot Record).
- It can be used to create a file of a specific size that is filled with binary zeros, which can then be used as a swap file (virtual memory).


The dd command uses special arguments to specify how it will work. The following illustrates some of the more commonly used arguments:
**if**
Input File: The input file to be read from.
dd **if=/dev/zero** of=/tmp/swapex bs=1M count=50 
The example reads from the /dev/zerofile, a special file containing an unlimited number of zeros.

**of**	
Output File: The output file to be written.
dd if=/dev/zero **of=/tmp/swapex** bs=1M count=50

**bs**	
Block Size: The block size to be used. By default, the value is considered to be in bytes. Use the following suffixes to specify other units: K, M, G, and T for kilobytes, megabytes, gigabytes and terabytes respectively.
dd if=/dev/zero of=/tmp/swapex **bs=1M** count=50
The example uses a block size of one megabyte.

**count**
Count: The number of blocks to be read from the input file.
dd if=/dev/zero of=/tmp/swapex bs=1M **count=50**
The example command reads 50 blocks.

### Moving Files
mv SOURCE DESTINATION

**mv**
mv people.csv Work
Moves people.csv to the Work directory

mv numbers.txt letters.txt alpha.txt School  
Moves mulitple files

### Removing Files
WARNING THIS IS PERMENENT 
rm [OPTIONS] FILE

**rm**
rm linux.txt
removes file

### Filtering Input
grep [OPTIONS] PATTERN [FILE]
More on this from lecture notes

### Regular Expressions
Regular expressions have two common forms: basic and extended. Most commands that use regular expressions can interpret basic regular expressions. However, extended regular expressions are not available for all commands and a command option is typically required for them to work correctly.

Regular expressions specifies a set of strings required for a particular purpose such as an email address.

The following table summarizes basic regular expression characters:
Basic Regex Character(s)	Meaning
.	Any one single character
[ ]	Any one specified character
[^ ]	Not the one specified character
*	Zero or more of the previous character
^	If first character in the pattern, then pattern must be at beginning of the line to match, otherwise just a literal ^
$	If last character in the pattern, then pattern must be at the end of the line to match, otherwise just a literal $
The following table summarizes the extended regular expressions, which must be used with either the egrep command or the -E option with the grep command:

Extended Regex Character(s)	Meaning
+	One or more of the previous pattern
?	The preceding pattern is optional
{ }	Specify minimum, maximum or exact matches of the previous pattern
|	Alternation - a logical "or"
( )	Used to create groups

**grep**
Many more examples of this from lecture

grep 'r$' alpha-first.txt
This finds records that end in r
*B is for Bear*
*F is for Flower*

grep 'r..f' red.txt
letters long starts with r ends with f
*reef*

grep '[0-9]' profile.txt
Any records with a number in

grep '[^0-9]' profile.txt
Any records without a number in

grep '[.]' profile.txt
Records with a full stop

### Shutting Down
shutdown [OPTIONS] TIME [MESSAGE]

The shutdown command requires administrative access, switch to the root

shutdown 01:51 "Goodbye World!" 
This will shutdown at a proposed time and say goodbye world

### Network Configuration
ifconfig [OPTIONS] 
The iwconfig command is similar to the ifconfig command, but it is dedicated to wireless network interfaces.

The ifconfig command can also be used to temporarily modify network settings. Typically these changes should be permanent, so using the ifconfig command to make such changes is fairly rare.

The **ping** command is used to verify connectivity between two computers. It does this by sending packets to another machine on a network. If the sender receives a response it should be possible to connect to that machine.

Information is sent using “packets”; the encapsulated unit of data sent over a network. In order for the packets to find the other computer, they will need an address. The ping command uses IP addresses to identify a computer on the network that it wants to connect to.

By default, the ping command will continue sending packets until the break command (CTL + C) is entered at the console. To limit how many pings are sent, use the -c option followed by the number of pings to be sent. The example below shows ping being limited to 4 iterations with -c 4.

### Viewing processes
ps [OPTIONS]

**ps**
The ps command will display the processes that are running in the current terminal by default. In the example above, the bottom line is the process created by the execution of the ps command. The output includes the following columns of information:

- PID: The process identifier, which is unique to the process. This information is useful for controlling the process by its ID number.
- TTY: The name of the terminal where the process is running. This information is useful for distinguishing between different processes that have the same name.
- TIME: The total amount of processor time used by the process. Typically, this information isn't used by regular users.
- CMD: The command that started the process.

ps -e
This will show all processes

### Package Management
Package management is a system by which software can be installed, updated, queried or removed from a filesystem. In Linux, there are many different software package management systems, but the two most popular are those from **Debian** and **Red Hat**. The virtual machines for this course use Ubuntu, a derivative of Debian.

At the lowest level of the Debian package management system is the **dpkg** command. This command can be tricky for novice Linux users, so the Advanced Package Tool, **apt-get**, a front-end program to the **dpkg** tool, makes management of packages even easier.

**sudo apt-get update**
This will install updates. Need sudo for priviledges needed

**apt-cache search [keyword]**
Search for keywords within these packages

Once you've found the package that you want to install, you can install it with the **apt-get install command**

### Update Packages
The **apt-get** install command can also update a package, if that package is installed and a newer version is available. If the package is not already on the system, it would be installed; if it is on the system, it would be updated.

Updating all packages of the system should be done in two steps. First, update the cache of all packages available with **apt-get update**. Second, execute the **apt-get upgrade** command and all packages and dependencies will be updated.

**apt-get update**
**apt-get upgrade**

### Removing Packages
The **apt-get** command is able to either remove or purge a package. The difference between the two is that purging deletes all package files, while removing deletes all but the configuration files for the package.

An administrator can execute the **apt-get** remove command to remove a package or the **apt-get purge** command to purge a package completely from the system.

**apt-get remove [package]**
**apt-get purge [package]**

### Updating User Passwords

passwd [OPTIONS] [USER]
Updates passwords

**passwd [OPTIONS] [USER]**

The output fields are explained below:

User Name	sysadmin:	The name of the user.
Password Status	P: P indicates a usable password, L indicates a locked password, NP indicates no password.

Change Date	03/01/2015	The date when the password was last changed.
Minimum	0	The minimum number of days that must pass before the current password can be changed by the user.
Maximum	99999	The maximum number of days remaining for the password to expire.
Warn	7	The number of days prior to password expiry that the user is warned.
Inactive	-1	The number of days after password expiry that the user account remains active.

### Redirection

Adding content to files in Linux can be done in a variety of ways. Linux has a few text editors that can be used to add content to a file. However, this method requires some familiarity with Linux text editor commands.

There is a way in Linux to quickly add content to a file using a command line feature called input/output (I/O) redirection. I/O redirection allows for information in the command line to be sent to files, devices, and other commands. The input or output of a command is redirected from its default destination to a different location. I/O redirection is like a series of train tracks, where a switch can be enabled to direct the output of a command on a different track so it goes somewhere else in the shell. In this section, we are writing to files by redirecting the output of a command to a file.

When it comes to command input and output there are three paths, or “tracks”. These paths are called file descriptors. The first file descriptor is standard input, abbreviated as STDIN. Standard input is the information the command receives and processes when it is executed, essentially what a user types on the keyboard. The second file descriptor is standard output, abbreviated as STDOUT. Standard output is the information that the command displays, the output of the command. The last file descriptor is standard error, abbreviated as STDERR. STDERR, are the error messages generated by commands that are not correctly executed. The following are examples of how file descriptors will appear in the terminal:

Example:
**cd ~/Documents**
**cat food.txt**

Now use the > character to redirect the STDOUT of the cat food.txt command above to a new file called newfile1.txt

**cat food.txt > newfile1.txt**

check what's in the file

**cat newfile1.txt**

if you want to add a comment or note to a file? To do this, you can use the **echo** command. The **echo** command is used to print output in the terminal.

Printing comments to the screen is a fun feature but the echo command can be made more useful by using redirection. Using the echo command, content can be added to the newfile1.txt file
To put a comment into a file:
**echo "I like food." > newfile1.txt**

### Text Editor

The premier text editor for Linux and UNIX is a program called **vi**. While there are numerous editors available for Linux that range from the tiny editor **nano** to the massive **emacs** editor, there are several advantages to the **vi** editor:
- The vi editor is available on every Linux distribution in the world. This is not true of any other editor.
- The vi editor can be executed both in a CLI (command line interface) and a GUI (graphical user interface).
- While new features have been added to the vi editor, the core functions have been around for decades. This means that if someone learned the vi editor in the 1970s, they could use a modern version without any problem. While that seems trivial, it may not seem so trivial twenty years from now.

*The correct way to pronounce the vi editor is the vee-eye editor. The letters vi stand for visual, but it was never pronounced this way by the developers, but rather the letter v followed by the letter i.*

In reality, most Linux systems don't include the original vi, but an improved version of it known as **vim**, for vi improved. This fact may be hidden by most Linux distributions. For the most part, vim works just like vi, but has additional features. For the topics that will be covered in this course, either vi or vim will work.

**Using VIM was referenced in the podcasts I've listened to**

### Command Mode Movement

Initially, the program starts in command mode. Command mode is used to type commands, such as those used to move around a document, manipulate text, and access the other two modes. To return to command mode at any time, press the **Esc** key.

Once some text has been added into a document, to perform actions like moving the cursor, the Esc key needs to be pressed first to return to command mode. This seems like a lot of work, but remember that vi works in a terminal environment where a mouse is useless.

Movement commands in vi have two aspects, a motion and an optional number prefix, which indicates how many times to repeat that motion.

The general format is as follows:
- h	Left one character
- j	Down one line
- k	Up one line
- l	Right one character
- w	One word forward
- b	One word back
- ^	Beginning of line
- $	End of the line

*Note: ince the upgrade to vim it is also possible to use the arrow keys ←↓↑→ instead of hjkl respectively.*

These motions can be prefixed with a number to indicate how many times to perform the movement. For example, 5h would move the cursor five characters to the left and 3w would move the cursor three words to the right.

To move the cursor to a specific line number, type that line number followed by the G character. For example, to get to the fifth line of the file type 5G. 1G or gg can be used to go to the first line of the file, while a lone G will take you to the last line. To find out which line the cursor is currently on, use **CTRL+G**.

### Command Mode Actions

cut	**d**	*delete*
copy	**y**	*yank*
paste	**P | p**	*put*

### Delete
Delete removes the indicated text from the page and saves it into the buffer, the buffer being the equivalent of the "clipboard" used in Windows or Mac OSX. The following table provides some common usage examples:
**dd**	Delete current line
**3dd**	Delete the next three lines
**dw**	Delete the current word
**d3w**	Delete the next three words
**d4h**	Delete four characters to the left

### Change
Change is very similar to delete; the text is removed and saved into the buffer, however, the program is switched to insert mode to allow immediate changes to the text. The following table provides some common usage examples:

**cc**	Change current line
**cw**	Change current word
**c3w**	Change the next three words
**c5h**	Change five characters to the left

### Yank
Yank places content into the buffer without deleting it. The following table provides some common usage examples:

**yy**	Yank current line
**3yy**	Yank the next three lines
**yw**	Yank the current word
**y$**	Yank to the end of the line

### Put
Put places the text saved in the buffer either before or after the cursor position. Notice that these are the only two options, put does not use the motions like the previous action commands.

**p**	Put (paste) after cursor
**P**	Put before cursor

### Searching in vi
Another standard function that word processors offer is find. Often, people use CTRL+F or look under the edit menu. The vi program uses search. Search is more powerful than find because it supports both literal text patterns and regular expressions.

To search forward from the current position of the cursor, use the / to start the search, type a search term, and then press the Enter key to begin the search. The cursor will move to the first match that is found.

To proceed to the next match using the same pattern, press the n key. To go back to a previous match, press the N key. If the end or the beginning of the document is reached, the search will automatically wrap around to the other side of the document.

To start searching backwards from the cursor position, start by typing ?, then type the pattern to search for matches and press the Enter key.

###   Insert Mode
Insert mode is used to add text to the document. There a few ways to enter insert mode from command mode, each differentiated by where the text insertion will begin. The following table covers the most common:

**a**	Enter insert mode right after the cursor
**A**	Enter insert mode at the end of the line
**i**	Enter insert mode right before the cursor
**I**	Enter insert mode at the beginning of the line
**o**	Enter insert mode on a blank line after the cursor
**O**	Enter insert mode on a blank line before the cursor

### Ex Mode
Originally, the vi editor was called the ex editor. The name vi was the abbreviation of the visual command in the ex editor which switched the editor to "visual" mode.

In the original normal mode, the ex editor only allowed users to see and modify one line at a time. In the visual mode, users could see as much of the document that will fit on the screen. Since most users preferred the visual mode to the line editing mode, the ex program file was linked to a vi file, so that users could start ex directly in visual mode when they ran the vi link.

Eventually, the actual program file was renamed vi and the ex editor became a link that pointed the vi editor.

When the ex mode of the vi editor is being used, it is possible to view or change settings, as well as carry out file-related commands like opening, saving or aborting changes to a file. In order to get to the ex mode, type a : character in command mode. The following table lists some common actions performed in ex mode:

**:w**	Write the current file to the filesystem
**:w** filename	Save a copy of the current file as filename
**:w!**	Force writing to the current file
**:1**	Go to line number 1 or whatever number is given
**:e** filename	Open filename
**:q**	Quit if no changes made to file
**:q!**	Quit without saving changes to file

*Although the ex mode offers several ways to save and quit, there's also ZZ that is available in command mode; this is the equivalent of :wq. There are many more overlapping functions between ex mode and command mode. For example, ex mode can be used to navigate to any line in the document by typing : followed by the line number, while the G can be used in command mode as previously demonstrated.*





