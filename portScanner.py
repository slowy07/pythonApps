import socket
import subprocess
import sys
from datetime import datetime


subprocess.call('clear', shell=True)

remoteServer = input("enter remote host to start scan: ")
remoteServerIp = socket.gethostbyname(remoteServer)
print("-" * 60)
print("please wait, scanning remote host", remoteServerIp)
print("-" * 60)

