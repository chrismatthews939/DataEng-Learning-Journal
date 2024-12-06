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





