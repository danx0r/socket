#listen on socket, echo double
import socket

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print "test python server, waiting for connection"
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    print "data received:", data
    print "sending back:", data + data
    conn.send(data + data)
print "closing connection"
conn.close()
