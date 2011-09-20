import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')
data = s.recv(1024)
print 'Received', repr(data)
s.send('GOODBYE')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
