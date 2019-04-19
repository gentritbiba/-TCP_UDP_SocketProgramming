from socket import *


# krijojme soketin e klientit me IP adrese te llojit IPv4 dhe
# me protokolin TCP
soketiKlientit = socket(AF_INET,SOCK_STREAM)


# deklarojme variablen ndihmese per te shikuar a mund te sigurojme lidhjen
# me serverin e caktuar ne portin e caktuar
notConnected = True
while notConnected:
    notConnected = False
    try:
        serverName = input("Sheno emrin e serverit: ")
        serverPort = int(input("Sheno portin: "))
        soketiKlientit.connect((serverName,serverPort))
    except Exception as e:
        notConnected = True
        print("Serveri nuk eshte i qasshem per momentin, provoni perseri!")
        input()


print("Jeni lidhur ne serverin ",serverName," ne portin ",serverPort)

# unaza qe perseritet gjithmone, perveq nese ka ndonje break brenda saj
# me ane te kesaj unaze sigurohet qe klienti t'i dergoje shume kerkesa
# serverit ne nje lidhje TCP te vetme
while 1:
    try:
        print("Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI,EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI,,FAKTORETPRIMAR,ISMIRROR)?",
            end='')
        dataInput = input()
        data="";
        if dataInput == "":
            soketiKlientit.sendall(str("Error").encode())
        elif dataInput != "EXIT":
                soketiKlientit.sendall(str(dataInput).encode())

        else:
            break

        data= soketiKlientit.recv(128)
        print("Pergjigjja: " + str(data.decode()).strip())

    except Exception as e:
        print(str(e))
        break
soketiKlientit.close()

print("Lidhja me serverin u mbyll")

