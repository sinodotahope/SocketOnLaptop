#!D:\Python\Projects\Socket\venv\Scripts\python.exe

import socket,sys,time


port = 51423
host = 'localhost'

data = "xxx"

print("Creating socket...")
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
    print("Strange error creating socket : {}".format(e))
    sys.exit(1)



print("done.")






print("Connectiong to remote host on port {}...".format(port) )
try:
    s.connect((host,port))
except socket.gaierror as e:
    print("Address-related error connecting to server:{}".format(e))
    sys,exit(1)
except socket.error as e:
    print("Connection error : {}".format(e))
    sys.exit(1)

print("done.")

byteswritten = 0
while byteswritten<len(data):
    startpos = byteswritten
    endpos = min(byteswritten + 1024,len(data))
    byteswritten+=s.send(data[startpos:endpos].encode())
    sys.stdout.write("Wrote {} bytes\n".format(byteswritten)+str(s.recv(1024)))

    sys.stdout.flush()

s.shutdown(1)

print("All data sent.")
while 1:
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)






