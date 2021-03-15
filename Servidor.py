import socket 
x=socket.socket ()
print("[*...]Esperando a conexao:[*...]")
IP=""# digite o seu ip aqui 
PORT=443
x.bind((IP,PORT))
x.listen (2)
r,t=x.accept ()
v=x.recv (2048)
print (v)
m= input()
x.send (m)