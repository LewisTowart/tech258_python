# Scripting

### What is scripting? How is it different to programming?

Scripting is a way of providing instructions to a computer so you can tell it what to do and when to do it.

It is generally used to automate singular or smaller in scope.

On the other hand programming helps build large and complex software applications, such as operating systems and 
enterprise-level software. The scope is much larger.

An example could be the program photoshop vs a script to specifically save images at a specific resolution.

### What are the packages in the standard Python library?

The packges that are included in Pythons standard library are ones that were very commonly used and were useful enough
to be added to base Python.

Some examples of these are:
* sys
* os
* math
* random
* datetime

Below you can see some examples of these in action.

#### math
```
num_float = 23.66 # Assigning th varaiable value
print(math.ceil(num_float)) # Output would be 24 as ceil rounds up
print(math.floor(num_float)) # Output would be 23 as floor rounds down
print(math.pi) # Output is 3.141592653589793 which is the value of pi
```

#### os
```
username = os.environ.get("USERNAME") or os.environ.get("USER") # Collecting the user/username of account
print(f"Username is: {username}") # Printing the username in my case the output would be Lewis

cpu_cores = os.cpu_count() # Collecting and assigning the amount of CPU cores in my device
print(f"Cpu cores = {cpu_cores}") # Printing the number of CPU cores in my case 8
```

### Python scripts a DevOps engineer may use/create

#### Here are some examples scripts used/created by DevOps Engineers
* Someone wrote a script to tell them about any new departures from their team
* A script to switch between terraform version on the go
* To check/allocate more disk space
* To restart specific services
* To check current permissions
* Deploy an application to a server
* To pull up various inventory reports
* A script that posts points from the previous days stand up
* Health check - tells you information around current disk and CPU usage
* To ping an IP address (e.g server) to see if it's available

Here is an example of the health check script. It is important to note that they are importing other modules I don't
have the code for but it can give a good example of what the script would look like.

```
import shutil
import psutil
from network import *


def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75


# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")
```
