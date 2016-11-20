import socket
import os
import threading
import requests
import webbrowser

Ip = '127.0.0.1'
Porta = 3001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((Ip,Porta))

server.listen(5)

print "[*] Listening on %s:%d" % (Ip,Porta)

def handle_cliente(cliente):
    
    response = ''
    
    request = cliente.recv(1024)
    
    if 'abre url' in request:
        url = request.split(" ")[2]
        response = webbrowser.open_new_tab(url)
        
    print "[*] Received %s" % (request)
    
    cliente.send("STATUS: "+str(response))
    
    cliente.close()

while True:
    
    if server.accept():
        
        try:
            client,add = server.accept()
            print "Accepted connection from %s:%d" %(str(add[0]),int(add[1]))
            handle_cliente= threading.Thread(target=handle_cliente,args=(client,))
            handle_cliente.start()
            
        except Exception as e:
            print e
            server.close()
            import sys
            sys.exit(0)
        
