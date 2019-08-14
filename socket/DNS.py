#DNS解析域名成IP地址
'''import sys,socket
result = socket.getaddrinfo("www.jingdong.com",None,0,socket.SOCK_STREAM)

print(result)'''


#反向根据查找域名
import sys,socket
num=1
while 1:
    try:
        #Perform the lookup

        result = socket.gethostbyaddr(input("第{}个IP:".format(num)))

        #Display the looked-up hostname

        print("Primary hostname:")
        print(result)

        #Display the list of available addresses that is also returned
        print("\nAddresser:")
        for item in result[2]:
            print(""+item)

    except socket.herror as e:
        print("Couldn't look up name:",e)
    num+=1