import socket
import subprocess
import sys
from datetime import datetime


subprocess.call("clear", shell=True)

remoteServer = input("enter remote host to start scan: ")
remoteServerIp = socket.gethostbyname(remoteServer)
print("-" * 60)
print("please wait, scanning remote host", remoteServerIp)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIp, port))
        if result == 0:
            print("port {} : Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("exiting program")
    sys.exit()
except socket.gaierror:
    print("hostname could not be resolved, exiting")
    sys.exit()
except socket.error:
    print("couldn't connect to server ")
    sys.exit()
t2 = datetime.now()
total = t2 - t1
print("Scanning complete:", total)
