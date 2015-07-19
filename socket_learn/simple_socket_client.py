import socket

s=socket.socket()
host=socket.gethostname()
port=5005

s.connect((host,port))
print s.recv(1024)

#1.create socket object
#2.call socket object method 'connect'
#3.call socket object method 'recv'
