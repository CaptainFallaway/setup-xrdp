from os import *
from time import sleep
import socket

# Side
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

ip = s.getsockname()[0]
x = "-------------------------------------------------------------------------------------------------------------------"

# Main
print(x)
print("")
system("service xrdp start")
print("")
print(x)
print("")
sleep(1)
system("service xrdp status")
print("")
print(x)
print("""
# For adding a new port rule (Check if port is open in windows firewall!)
netsh interface portproxy add v4tov4 listenport= listenaddress=0.0.0.0 connectport= connectaddress="""+ ip + """

# For modifying a port rule
netsh interface portproxy set v4tov4 listenport= listenaddress=0.0.0.0 connectport= connectaddress="""+ ip + """

# Viewing all the port rules
netsh interface portproxy dump

# You need to renew the portforwarding if the ip has changed, the easiest way to do this is type
netsh interface portproxy reset

#Comments:
If you need to make this public then you'll need to portforward in the router with the Windows pc ipv4
""")
print(x)