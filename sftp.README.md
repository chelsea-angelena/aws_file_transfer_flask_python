## References and Resources

[Leiland - Medium Article](https://medium.com/@lejiend/create-sftp-container-using-docker-e6f099762e42)

[Edward S. - Hostinger-Tutorial](https://www.hostinger.my/tutorials/how-to-use-sftp-to-safely-transfer-files/)

## Using SFTP:

#### **_All_ of these instructions have been directly taken and condensed from Edward S's tutorial:**

#### [Edward S. - Hostinger-Tutorial](https://www.hostinger.my/tutorials/how-to-use-sftp-to-safely-transfer-files/)

### Connect

connect to the sftp server:
`sftp -oPort=32768 sftp_user@127.0.0.1`

### Transferring Remote Files From a Server to the Local System

- Local directory:
  `sftp > lpwd`

- Remote directory:
  `sftp > pwd`

#### Transfer file from remote server to your local:

- Get + filepath
  `get /RemoteDirectory/filename.txt`

- For example, to copy the file /etc/xinetd.conf from the remote server to your local machine, you would use:
  `get /etc/xinetd.conf`

- Once the download is complete, you can now find that the file xinetd.conf is in the /user/home directory of your local machine.

- To download multiple files with SFTP, use the mget command.
- To download all files in a directory called /etc that have the .conf extension to your current working directory, you will use the following command:

  `mget /etc/*.conf`

- After the download, you can find all \*.conf files in /user/home directory of your local machine.

### Transferring Files From the Local Machine to a Remote Server

- Copy a file from local to the remote server:
  `get file.txt /RemoteDirectory`

- To move the file example.txt from a local machine to the remote machine, enter the following command:
  `put /home/user-name/example.txt /root`

- Find the file in the remote server’s root directory: (You can also try transferring multiple files using the mput command. It works nearly the same as mget):
  `mput /home/user-name/*.txt /root`

- This command would move all files with the .txt extension in the /home/user-name from the local machine to the remote /root directory.

_Pro Tip:_ Keep in mind that to download and upload the files with SFTP, you will need to type the command put or get and press the TAB key.

#### Commands for Navigating With SFTP

- Remote directory: /RemoteDirectory
  `sftp> pwd`

- Local directory: /LocalDirectory
  `sftp> lpwd`

- You can also display the list of files and directories you’re using for the remote directory:
  `ls`

- Similarly, for the local working directory:
  `lls`

- For instance, the output will look similar to this:
  Pictures Templates Media Text.txt Documents

- To switch from one remote working directory to another local working directory, enter the following commands:
  `cd name_of_directory`
  `lcd name_of_directory`

- Finally, use the ! and exit commands to go back to the local shell and quit SFTP.

#### Basics of File Maintenance Using SFTP

- With SFTP, you can also manage directories and files using specific commands.

- To check the remote server’s disk space in gigabytes, use the df function like so:
  `df -h`
- Here’s an output example:

        Filesystem         Size  Used Avail Use% Mounted on
        /dev/ploop29212p1   59G  2.5G   56G   5% /
        none               1.5G     0  1.5G   0% /sys/fs/cgroup
        none               1.5G     0  1.5G   0% /dev
        tmpfs              1.5G     0  1.5G   0% /dev/shm
        tmpfs              1.5G  568K  1.5G   1% /run
        tmpfs              308M     0  308M   0% /run/user/0

- Use the mkdir command to create a new directory on either the remote and local server :
  `mkdir name_of_directory`
  `lmkdir name_of_directory`

- You can delete one from the remote server using the rmdir command:
  `rmdir name_of_directory`

- Meanwhile, renaming a remote file is also rather straightforward:
  `rename filename new_filename`

- If you want to remove a remote file, use the rm command:
  `rm filename`

- While the chown command is used to replace a file’s owner:
  `chown userid filename`

- userid can either be a username or a numeric user ID. For instance:
  `chown UserOne FileExample`
  `chown 1234 FileExample`

- chgrp is used for changing a file’s group owner:
  `chgrp groupid filename`

- For instance:
  `chgrp NewGroup FileExample`

- Finally, you will need to use the chmod interactive command to change a file’s permission:
- In this example, the three-digit value stands for the file’s user, group, and other users.
- As for the permissions to read (r), write (w), and execute (x), their values are 4, 2, 1, respectively. 0 can also be used to provide no permissions.
- `chmod 764 FileExample`

- To assign permissions, simply calculate the total values for each user class. Here’s a breakdown of the example:
  `chmod ugo FileExample`

**_u_** represents the User who'll be able to read, write and execute the file.
**_g_** is for Groups, here we've given the permission to write and execute the file.
**_o_** or Others will only be able to read the file.

### List of Useful SFTP Commands

- Enter the help or ? command — both will prompt the same result - to produce this sheet:

        bye                                Quit sftp
        cd path                            Change remote directory to 'path'
        chgrp [-h] grp path                Change group of file 'path' to 'grp'
        chmod [-h] mode path               Change permissions of file 'path' to 'mode'
        chown [-h] own path                Change owner of file 'path' to 'own'
        df [-hi] [path]                    Display statistics for current directory or
                                           filesystem containing 'path'
        exit                               Quit sftp
        get [-afpR] remote [local]         Download file
        help                               Display this help text
        lcd path                           Change local directory to 'path'
        lls [ls-options [path]]            Display local directory listing
        lmkdir path                        Create local directory
        ln [-s] oldpath newpath            Link remote file (-s for symlink)
        lpwd                               Print local working directory
        ls [-1afhlnrSt] [path]             Display remote directory listing
        lumask umask                       Set local umask to 'umask'
        mkdir path                         Create remote directory
        progress                           Toggle display of progress meter
        put [-afpR] local [remote]         Upload file
        pwd                                Display remote working directory
        quit                               Quit sftp
        reget [-fpR] remote [local]        Resume download file
        rename oldpath newpath             Rename remote file
        reput [-fpR] local [remote]        Resume upload file
        rm path                            Delete remote file
        rmdir path                         Remove remote directory
        symlink oldpath newpath            Symlink remote file
        version                            Show SFTP version
        !command                           Execute 'command' in local shell
        !                                  Escape to local shell
