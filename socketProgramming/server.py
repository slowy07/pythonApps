import socket

s = socket.socket()
ipAddress = socket.gethostbyname(socket.gethostname())

s.bind((ipAddress, 12345))
s.listen(3)
print("server ip address :", ipAddress)

while True:
    print('waiting connection')
    connection, clientAddress = s.accept()
    try:
        print("connected ", clientAddress)
        connection.send(str("now you are connected").encode("utf-8"))
        while True:
            data = connection.recv(1024).decode("utf-8")
            if data:
                print(list(clientAddress)[0], end="")
                print(": %s" % data)

                newData = str(input("you: ")).encode("utf-8")
                connection.send(newData)
    finally:
        connection.close()
