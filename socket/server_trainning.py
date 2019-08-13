import socket


host=''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
print("Waiting for connections...")
s.listen(5)

while 1 :
    clientsock,clientaddr = s.accept()
    print("Got connection from",clientsock.getpeername())
    clientsock.close()
    print("Socket is closed.")


'''solist=[x for x in dir(socket) if x.startswith('SO_')]
solist.sort()
for x in solist:
    print (x)'''

