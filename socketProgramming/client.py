import socket

s = socket.socket()
server = input("enter server ip ") #port 12345
s.connect((server, 12345))

data = s.recv(1024).encode("utf-8")
print(server +":"+data)

while True:
    newData = str(input("you :")).encode("utf-8")
    s.sendall(newData)
    data = s.recv(1024).decode("utf-8")
    s.sendall(newData)

    data = s.recv(1024).decode("utf-8")
    print(server + ":" + data)

s.close()
