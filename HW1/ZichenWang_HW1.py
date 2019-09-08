import socket

s = socket.socket()
server = "192.168.200.52"
port = 19001
s.connect((server,port))
print(s.recv(1024))

message = "Zichen Wang, zwang216@jhu.edu, Mr-4000, team6"
s.send(message.encode())
print(s.recv(1024))

message = "YES"
s.send(message.encode())
print(s.recv(1024))

s.close()
