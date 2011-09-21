#listen on socket, echo double
import sys, time, socket

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print "test python server, waiting for connection"
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1)
    if len(data):
        cnt = ord(data[0])
        if cnt==0:
            break
        data = conn.recv(cnt)
        print "received msg-->" + repr(data) + "<--"
        if data == "ack":
            conn.send(chr(3) + "ACK")
    else:
        print ".",
        sys.stdout.flush()
##    time.sleep(.1)
print "closing connection"
conn.close()
