# parallel SSH demo (without packages)

- 
there can be 2 approaches here :

1 - manually using threading which i have implemented in main.py to count words in a file remotely and it is tested and working by me.
-
2 - second is just use 
   pip install parallel-ssh
   python main_pssh.py
   which is python's lib for this usecase itself
-
# what this does in short??
Runs the same file processing command on multiple servers ips in parallel using SSH.

# files i included
-process_file.py -> dummy processing script\
-main.py ->runs SSH commands in parallel\
-ips.txt -> list of server IPs

-main_pssh.py ->this is the parallel-ssh implementation

# steps for running and ssh

1. making sure ssh works coz this wont work without ssh ,try this command first in powershell:\
   ssh username@127.0.0.1

2. if ssh not working download from github 
https://github.com/PowerShell/Win32-OpenSSH/releases

use this command strictly on the admin powershell coz it needs permissions:\
"""
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0\
Start-Service sshd\
Set-Service -Name sshd -StartupType Automatic
"""

3. once ssh works try this command on any powershell

ssh username@127.0.0.1\
(replace username with your real computer directory username ,my case was avani)

4. then you can run this script in the folder terminal:\
   python main.py

# expected Output
3 servers or 3 threads running at same time for a single task comparison woth single server for same task ,so we expect the parallel exec to have less runtime

the output i got looks like this :

PS C:\parallel_ssh_task_avani> python main.py
>>
running_on 127.0.0.1\
running_on 127.0.0.1\
running_on 127.0.0.1\
15\
15\
15\
time_taken for 3 servers parallely: 0.44978785514831543\
task_completed\
running_on 127.0.0.1\
15\
running_on 127.0.0.1\
15\
running_on 127.0.0.1\
15\
time_taken for 3 servers sequentially: 0.9748907089233398\
task_completed\
PS C:\parallel_ssh_task_avani>\


so we can see that for counting words in the text file it took 0.44978785514831543 seconds in parallel and 0.9748907089233398 seconds in sequential ,so we are saving time in parallel execution 

# difficulties i faced
majorly wrt ssh because it's setup took a long time as it required many permissions before ,so i had to download it from github and then extract it 

# references i used 
#reference - 
ssh -- https://www.geeksforgeeks.org/python/automated-ssh-bot-in-python/
threading -- https://docs.python.org/3/library/threading.html \
time -- https://docs.python.org/3/library/time.html \
os -- https://docs.python.org/3/library/os.html \
open -- https://docs.python.org/3/library/functions.html#open

https://stackoverflow.com/questions/1185855/parallel-ssh-in-python

https://discuss.python.org/t/running-ssh-in-parallel/7404


# main differences in the aprroaches
instead of manually using threads to ssh, ParallelSSHClient handles all the parallelism and SSH connections internally using its own async engine. Same result, so easy work without any additional overhead.
