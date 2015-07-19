import socket

s=socket.socket()

host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    #conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection
    print 'got connection from',addr
    c.send('Thank you for connecting')
    c.close()

#1.create a socket object
#2.call object method 'bind' at (host,port)
#3.call 'listen' arg:max connect number
#4.while true accept connection
#5.'send'
