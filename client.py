import time, socket

HOST = 'localhost'    # The remote host
PORT = 50007             # The same port as used by the server
g_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
g_sock.connect((HOST, PORT))

def sendMsg(s):
    s = chr(len(s)) + s
    print "sending-->" + repr(s) + "<--"
    g_sock.send(s)

def getMsg():
    cnt = 0
    while cnt == 0:
        data = g_sock.recv(1)
        if len(data):
            cnt = ord(data[0])
            data = g_sock.recv(cnt)
    return data
        

sendMsg('abc')
sendMsg('ack')
x = getMsg()
print "received:", x
sendMsg('Holy Cow Batman!')
sendMsg('')
time.sleep(1)
g_sock.close()
