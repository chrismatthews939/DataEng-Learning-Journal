# NDG Linux Unhatched Course
https://portal.netdevgroup.com/learn/unhatched/GasK9avLUN/

## Basic Command Syntax
command [options…] [arguments…]

**cd** change directory
**cd ..** goes up a directory level

Listing files
**ls [OPTIONS] [FILE]**

**su** switch user

**sudo** 
The sudo command allows a user to execute a command as another user without creating a new shell. Instead, to execute a command with administrative privilege

File permissions
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

Changing ownership command
**chown**
To switch the owner of the hello.sh script to the root user, use root as the first argument and hello.sh as the second argument
**sudo chown root hello.sh**

Viewing files
UP TO 10
