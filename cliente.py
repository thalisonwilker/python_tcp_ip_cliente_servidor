import socket

Ip = '127.0.0.1'
Porta = 3001

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((Ip,Porta))

cliente.send("abre url http://www.google.com")
response = cliente.recv(1024)
print response
cliente.close()
