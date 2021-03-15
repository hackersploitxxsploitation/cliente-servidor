import socket
c=socket.socket()
c.connect (("127.0.0.1",5000))
k=input ("digite a massagem ")
l=c.send(k)
print (l)
p=c.recv (1024)
print (p)