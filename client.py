import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('https://www.google.co.nz',80))
reply ="GET / HTTP/1.1"
s.send(reply)
data = s.recv(1024)
s.close()
print "received:"
print data