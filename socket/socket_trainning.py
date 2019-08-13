#!D:\Python\Projects\Socket\venv\Scripts\python.exe

import socket,sys,time
reload(sys)

host=sys.argv[1]
textport =sys.argv[2]
filename = sys.argv[3]

print("Creating socket...")
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
    print("Strange error creating socket : {}".format(e))
    sys.exit(1)



print("done.")

print("Looking up port number...")
try:
    port = int(textport)
except ValueError:
    try:
        port =socket.getservbyname(textport,'tcp')
    except socket.error as e:
        print("Couldn't find your port:{}".format(e))
        sys.exit(1)

print('done')

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
print("Sleeping...")
time.sleep(1)
print("Continuing.")

try:
    s.sendall("GET {} HTTP/1.0\r\n\r\n".format(filename))
except socket.error as e:
    print("Error sending data:{}".format(e))
    sys.exit(1)

try:
    s.shutdown(1)
except socket.error as e:
    print("Error sending data (detected by shutdown):{}".format(e))
    sys,exit(1)

sys.setdefaultencoding("utf-8")
while 1:
    try:
        buf = s.recv(2048)
    except socket.error as e:
        print("Erorr receiving data : {}".format(e))
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)



