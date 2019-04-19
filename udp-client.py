from socket import *


socketKlient=socket(AF_INET,SOCK_DGRAM)

serverName=str(input("Shkruaj emrin e serverit"))
serverPort=int(input("Shkruaj numrin e portit"))

while 1:
    try:
        print("Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI,EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI,,FAKTORETPRIMAR,ISMIRROR)?",end='')
        dataInput=input()
        if dataInput=="":
         socketKlient.sendto(str("Error").encode(),(serverName,serverPort))
        if dataInput!="EXIT":
            socketKlient.sendto(str(dataInput).encode(),(serverName,serverPort))
        else:
            break

        data,serveraddress=socketKlient.recvfrom(128)
        print("Pergjigjja: "+str(data.decode()).strip())
    except Exception as e:
       print(str(e))
       break
