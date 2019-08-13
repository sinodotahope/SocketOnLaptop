import socket,sys
import time,struct
host="localhost"
port = 51423

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((host,port))


while 1:
    print("\nEnter anything:")
    data = sys.stdin.readline().strip()
    s.sendall(data.encode())
    buf = s.recv(2048)
    if  len(buf) !=4:
        print("Wrong!")
        sys.exit(1)

    secs = struct.unpack("!I",buf)[0]
    secs-=2208988800
    print(time.ctime(int(secs)))
