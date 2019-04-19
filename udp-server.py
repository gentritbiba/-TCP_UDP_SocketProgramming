from socket import *
import random
import datetime
import sys
import threading
import re
import math

# definohet porti i serverit]
serverName=''
serverPort = 12000
# krijohet soketi i serverit, ngjashem me klientin perdoren IPv4 dhe TCP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# soketit te serverit i rezervohet porti 11000
serverSocket.bind((serverName,serverPort))
print('Serveri startoi ne hostin(kompjuterin) me IP adrese: '+str(gethostbyname(gethostname()))+" ne portin: "+str(serverPort))


print('Serveri eshte gati te pranoje te dhena...')

def BASHKETINGELLORE(fjalia):

    ZANORET = ['A', 'E', 'Ë', 'I', 'O', 'U', 'Y', 'a', 'e', 'ë', 'i', 'o', 'u', 'y']
    fjaliaFormatume = re.sub("[^a-zA-Z]","",fjalia);
    bashtingelloreDyshe=["dh","gj","ll","nj","rr","sh","th","xh","zh","Dh","Gj","Ll","Nj","Rr","Sh","Th","Xh","Zh"]
    bD=0
    for i in bashtingelloreDyshe:
        bD += len(re.findall(i,fjaliaFormatume))

    count=0
    for i in str(fjaliaFormatume):
        if i not in ZANORET:
            count += 1
    return str(count-bD)

def PRINTIMI(teksti):
    teksti = str(teksti).strip()
    return teksti

def KOHA():
    koha=str(datetime.datetime.now()).split(' ');
    KohaOret=koha[1].split(':')
    if(int(KohaOret[0])>12) :
        Parpashtesa="PM"
    else:
        Parpashtesa="AM"
    KohaData=koha[0].split('-')
    return('.'.join(KohaData[::-1])+" " +':'.join(KohaOret)[:8]+ Parpashtesa)


def IPADRESA(address):
    return str(address[0])


def NUMRIIPORTIT(address):
    return str(address[1])

def LOJA():
    numra=[]
    for n in range(7):
        numra.append(random.randint(1,49))
    numra.sort()
    return str(numra)


def isPrime(n):
    if (n % 2 == 0):
        return False

    for i in range(3, int(math.sqrt(n)+1), 2):
        if(n%i==0):
            return False
    return  True

def KONVERTIMI(input,n):
    vlera=0
    try:
        vlera=float(n)
    except:
        return "Error"


    switch={
        "KilowattToHorsepower".upper():str(round(vlera*1.34102,2)),
        "HorsepowerToKilowatt".upper():str(round(vlera*0.7457,2)),
        "RadiansToDegrees".upper():str(round(vlera*57.2958,2)),
        "GallonsToLiters".upper():str(round(vlera*3.78541,2)),
        "LitersToGallons".upper():str(round(vlera*0.264172,2)),
        "DegreesToRadians".upper():str(round(vlera*0.0174533,2))

    }

    return  switch.get(input.upper(),"Error:Shkruaj nje konvertim")

def FaktoretPrimar(numri):
    n=int(numri)
    list=[]
    if(n%2==0):
        list.append(2)
        if(isPrime(n/2)):
            list.append(n/2)

    for i in range(3,int(math.sqrt(n))+1,2):
        if isPrime(i) and n%i==0:
            list.append(i)
            if (isPrime(n / i)):
                list.append(n / i)

    list.sort()
    listString=str(list)
    if len(list)==0:
        return str("Numri: "+ str(n)+" nuk ka faktore numra primar")
    else:
        return str("Numri :"+str(n)+" ka faktore keta numra primar:"+listString)

def EMRIIKOMPJUTERIT(address):
    a, b, c = gethostbyaddr(addr[0])
    # a = emri, b = alias, c = IP adresen e dhene
    if a=="":
        return "Emri i klientit nuk dihet"
    return str(a)

def FIBONACCI(n):
   numri=0
   try:
       numri=int(n)
       if(numri<1):
           return "Bad Input"
       if(numri<3):
            return 1
       array = [1, 1]
       for i in range(2, numri):
           array.append(array[i - 1] + array[i - 2])
       return array[-1]
   except:
       return "Error"


def ISMIRROR(n):
    # Tregon se nje numer a eshte pasqyre. Shembull 123321 eshte pasqyre sepse lexohet njejt nga secila ane,
    # numri 132321 nuk eshte i pasqyre sepse nuk lexohe tnjejt nga secila ane
    try:
        numri = str(n)
        for i in range(0, int(len(numri) / 2)):
            if (numri[i] != numri[-i - 1]):
                return "Numri nuk eshte pasqyre"
        return "Numri eshte pasqyre"

    except:
        return "Error"



#metoda serverResponse tregon qka ka derguar serveri
def serverResponse(response):
    print("Mesazhi i derguar nga serveri eshte :"+str(response))
    print("-----------------------------------------------------")
while 1:
    # deklarohet variabla ndihmese error qe kthehet ne true sahere qe ka gabime
    error = False

    incomingData = (bytes)("empty".encode())
    try:
        while str(incomingData.decode())!="":

            incomingData,ClientAddress = serverSocket.recvfrom(128)

            # dekodojme kerkesen e marre nga klienti e kthejme ne string
            # dhe i largojme whitespace-t nga fillimi dhe fundi
            incomingDatastr = str(incomingData.decode()).strip()
            # ndajme kerkesen me split per te pare se cka ka shenuar klienti
            kerkesaVargu = incomingDatastr.split(' ')
            # krijojme variablen ndihmese emriMetodes qe ka fjalen e pare te shenuar nga klienti
            emriMetodes = kerkesaVargu[0]
            # per te mos krijuar krahasime te kota shnderrojme kerkesen ne fjale me shkronja
            # te medha dhe krahasojme vetem me shkronja te medha
            kerkesaVargu[0] = kerkesaVargu[0].upper()
            #Shenojme se me cilin klient eshte konektuar serveri
            print("Serveri u konektua me klientin :" +str(ClientAddress[0])+" ne portin :" +str(ClientAddress[1]))
            print("Kerkesa e derguar nga klienti: " + str(incomingData.decode().strip()))

            # metoda IPADRESA
            if kerkesaVargu[0]=="IPADRESA":
                # nese ka shenuar dicka tjeter pos IPADRESA, kthehet gabim
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    serverSocket.sendto(("IP adresa e klientit eshte:"+IPADRESA(ClientAddress)).encode(),ClientAddress)
                    serverResponse("IP adresa e klientit eshte:"+IPADRESA(ClientAddress))
            # metoda NUMRIIPORTIT
            elif kerkesaVargu[0]=="NUMRIIPORTIT":
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    serverSocket.sendto(("Klienti eshte duke perdorur portin:"+NUMRIIPORTIT(ClientAddress)).encode(),ClientAddress)
                    serverResponse("Klienti eshte duke perdorur portin:"+NUMRIIPORTIT(ClientAddress))
            # metoda BASHKETINGELLORE
            elif kerkesaVargu[0]=="BASHKETINGELLORE":
                # largojme fjalen BASHKETINGELLORE nga incomingData dhe ate string ia dergojm
                # metodes BASHKETINGELLORE

                 fjaliaShenuar = incomingDatastr.replace(emriMetodes,"",1)
                 serverSocket.sendto(str(BASHKETINGELLORE(fjaliaShenuar)).encode(),ClientAddress)
                 serverResponse(str(BASHKETINGELLORE(fjaliaShenuar)))


            # metoda PRINTIMI
            elif kerkesaVargu[0]=="PRINTIMI":
                fjaliaShenuar = incomingDatastr.replace(emriMetodes,"",1)
                serverSocket.sendto(PRINTIMI(fjaliaShenuar).encode(),ClientAddress)
                serverResponse(PRINTIMI(fjaliaShenuar).encode())
            # metoda EMRIIKOMPJUTERIT
            elif kerkesaVargu[0]=="EMRIIKOMPJUTERIT":
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    if EMRIIKOMPJUTERIT(ClientAddress)=="Emri i klientit nuk dihet":
                        serverSocket.sendto(("Emri i klientit nuk dihet").encode(),ClientAddress)
                        serverResponse(PRINTIMI(fjaliaShenuar))
                    else:
                        serverSocket.sendto(("Emri i klientit eshte: "+EMRIIKOMPJUTERIT(ClientAddress)).encode(),ClientAddress)
                        serverResponse(PRINTIMI(fjaliaShenuar))
            # metoda KOHA
            elif kerkesaVargu[0]=="KOHA":
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    serverSocket.sendto(KOHA().encode(),ClientAddress)
                    serverResponse(KOHA())
            # metoda LOJA
            elif kerkesaVargu[0]=="LOJA":
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    serverSocket.sendto(("Rezultatet nga loja: "+LOJA()).encode(),ClientAddress)
                    serverResponse(str("Rezultatet nga loja: "+LOJA()))
            # metoda FIBONACCI
            elif kerkesaVargu[0]=="FIBONACCI":
                # largojme hapesirat e panevojshme qe jane shenuar ne kerkese
                for i in range(len(kerkesaVargu)):
                    if "" in kerkesaVargu:  #largojme hapesirat e panevojshme
                        kerkesaVargu.remove("")
                # nese nuk jane vetem 2 parametra kthe gabim
                if len(kerkesaVargu)!=2:
                    error = True
                else:
                    if FIBONACCI(kerkesaVargu[1])=="Error":
                        error = True
                    else:
                        serverSocket.sendto(("Numri i "+kerkesaVargu[1]+" ne serine fibonacci eshte: "+str(FIBONACCI(kerkesaVargu[1]))).encode(),ClientAddress)
                        serverResponse(str("Numri i "+kerkesaVargu[1]+" ne serine fibonacci eshte: "+str(FIBONACCI(kerkesaVargu[1]))))
            # metoda KONVERTIMI
            elif kerkesaVargu[0]=="KONVERTIMI":
                for i in range(len(kerkesaVargu)):
                    if "" in kerkesaVargu: #largo hapsirat e panevojshme NULL karakterin
                        kerkesaVargu.remove("")
                # nese nuk jane saktesisht 3 parametra kthe gabim
                if len(kerkesaVargu)>3 or len(kerkesaVargu)<3:
                    error=True
                else:
                    if str(KONVERTIMI(str(kerkesaVargu[1]).upper(),kerkesaVargu[2]))=="Error": #nese kerkesa nuk eshte valide kthe error
                        error = True
                    else:
                        vargu = str(kerkesaVargu[1]).lower().split("to")
                        rezultati = kerkesaVargu[2] + " " + str(vargu[0]).capitalize() + " jane te barabarte me " + KONVERTIMI(str(kerkesaVargu[1]).upper(),kerkesaVargu[2]) + " " + str(vargu[1]).capitalize()

                        serverSocket.sendto(str(rezultati).encode(),ClientAddress)
                        serverResponse(str(rezultati))

            elif kerkesaVargu[0]=="PALINDROMI":
              if kerkesaVargu[1]=="?":
                  serverSocket.send(str("Sheno PALINDROMI {hapsire} fjala ").encode())
              else:
               for i in range(len(kerkesaVargu)):
                   if "" in kerkesaVargu:#largo null karakterin
                       kerkesaVargu.remove("")
               if len(kerkesaVargu)!=2: #nese jipet me shume se nje fjale si argument
                   error=True
               elif bool(re.search(r'\d', kerkesaVargu[1])): #nese fjala ka shifra numerike kthe gabim
                   error=True
                   serverSocket.sendto("Fjala nuk guxon te permbaje shifra numerike".encode(),ClientAddress)
               else:
                   rezultati=kerkesaVargu[1]+" "+str(("eshte palindrom" if PALINDROMI(kerkesaVargu[1]) else "nuk eshte Palindrom"))
                   serverSocket.sendto(str(rezultati).encode(),ClientAddress)


            elif kerkesaVargu[0]=="SHUMASHIFRAVE":
              if len(kerkesaVargu)!=3:
                  serverSocket.sendto(str("Kjo metode pranon 2 numra :"+ str(kerkesaVargu)).encode(),ClientAddress)
              else:
                  serverSocket.sendto(str("Shuma e shifrave te numrit :"+str(kerkesaVargu[1])+" te ngritur ne fuqine :"+str(kerkesaVargu[2])+" eshte:"
                                      +shumaShifrave(kerkesaVargu[1],kerkesaVargu[2])).encode(),ClientAddress)
                  serverResponse(str("Shuma e shifrave te numrit :"+str(kerkesaVargu[1])+" te ngritur ne fuqine :"+str(kerkesaVargu[2])+" eshte:"
                                      +shumaShifrave(kerkesaVargu[1],kerkesaVargu[2])))

            elif kerkesaVargu[0]=="FAKTORETPRIMAR":
                if kerkesaVargu[1]=="?":
                    serverSocket.send(str("Sheno FAKTORETPRIMAR {HAPSIRE} numri -per te pare listen e numrave primar qe jane faktore te numrit te shenuar").encode())
                else:
                    for i in range(len(kerkesaVargu)):
                        if "" in kerkesaVargu:  # largo null karakterin
                            kerkesaVargu.remove("")
                    if len(kerkesaVargu) != 2:  # nese jipet me shume se nje fjale si argument
                        error = True
                        serverSocket.sendto("Ju lutem shenoni vetem 1 numer ".encode(),ClientAddress)
                        serverResponse(str("Ju lutem shenoni vetem 1 numer "))
                    else:
                        serverSocket.sendto(FaktoretPrimar(kerkesaVargu[1]).encode(),ClientAddress)
                        serverResponse(FaktoretPrimar(kerkesaVargu[1]))

            elif kerkesaVargu[0] == "ISMIRROR":

                for i in range(len(kerkesaVargu)):
                    if "" in kerkesaVargu:  # largojme hapesirat e panevojshme
                        kerkesaVargu.remove("")

                if len(kerkesaVargu) != 2:
                    error = True
                else:
                    if FIBONACCI(kerkesaVargu[1]) == "Error":
                        error = True
                    else:
                        serverSocket.sendto((kerkesaVargu[1] + "  eshte: " + str(
                            ISMIRROR(kerkesaVargu[1]))).encode(), ClientAddress)
                        serverResponse(str(kerkesaVargu[1] + " eshte: " + str(
                            ISMIRROR(kerkesaVargu[1]))))







            # asnjera nga metodat lart
            else:
                serverSocket.sendto("kerkesa  eshte jovalide,  provoni perseri!".encode(),ClientAddress)

            # nese ka error kthe mesazhin per korrigjim
            if error==True:
                serverSocket.sendto("kerkesa  eshte jovalide,   rregulloni gabimin!".encode(),ClientAddress)
                error = False


    # nese ka gabim, nuk mbyllet serveri por vetem shkeputet lidhja
    except Exception as e:
        print("-------------An ERROR happenned---------------------")
        print(str(e))
