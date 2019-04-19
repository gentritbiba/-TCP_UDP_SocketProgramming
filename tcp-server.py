from socket import *
import random
import datetime
import sys
import threading
import re
import math


serverName=''
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))

print('Serveri startoi ne hostin me IP adrese: '+str(gethostbyname(gethostname()))+" ne portin: "+str(serverPort))
serverSocket.listen(5)

print('Serveri eshte gati per kerkesa')

def BASHKETINGELLORE(fjalia):


    ZANORET = ['a', 'e', 'ë', 'i', 'o', 'u', 'y']
    fjaliaFormatume = re.sub("[^a-z]","",fjalia.lower());
    bashtingelloreDyshe=["dh","gj","ll","nj","rr","sh","th","xh","zh"]
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

def isPrime(n):
    if (n % 2 == 0):
        return False

    for i in range(3, int(math.sqrt(n)+1), 2):
        if(n%i==0):
            return False
    return  True


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


# metoda SHTYPDERGESEN , qe ndihmon te tregoje se cka eshte derguar tek cdo klient
def SHTYPDERGESEN(IPKlientit,portiKlientit,mesazhi):
    try:
        print("-----------------------------------MESAZH------------------------------------")
        print("Te dhenat e derguara tek klienti "+str(IPKlientit)+" me numer te portit "+ str(portiKlientit) +" jane:\n\""+mesazhi+"\"")
    except Exception as e:
        print(str(e))




# funksioni qe thirret tek thread
def newClient(connectionSocket,addr):
    # deklarohet variabla ndihmese error qe kthehet ne true sahere qe ka gabime
    error = False

    kerkesa = (bytes)("empty".encode())
    try:
        while str(kerkesa.decode())!="":
            kerkesa = connectionSocket.recv(128)
            # dekodojme kerkesen e marre nga klienti e kthejme ne string
            # dhe i largojme whitespace-t nga fillimi dhe fundi
            kerkesaStr = str(kerkesa.decode()).strip()
            # ndajme kerkesen me split per te pare se cka ka shenuar klienti
            kerkesaVargu = kerkesaStr.split(' ')
            # krijojme variablen ndihmese fjalaePare qe ka fjalen e pare te shenuar nga klienti
            fjalaePare = kerkesaVargu[0]
            # per te mos krijuar krahasime te kota shnderrojme kerkesen ne fjale me shkronja
            # te medha dhe krahasojme vetem me shkronja te medha
            kerkesaVargu[0] = kerkesaVargu[0].upper()

            # metoda IPADRESA
            if kerkesaVargu[0]=="IPADRESA":
                # nese ka shenuar dicka tjeter pos IPADDR, kthehet gabim
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    SHTYPDERGESEN(addr[0],addr[1],"IP adresa juaj eshte: "+IPADRESA(addr))
                    connectionSocket.send(("\033[1m"+"IP adresa e klientit eshte:"+IPADRESA(addr)).encode())
            # metoda NUMRIIPORTIT

            elif kerkesaVargu[0]=="NUMRIIPORTIT":
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    SHTYPDERGESEN(addr[0],addr[1],"Klienti eshte duke perdorur portin:"+NUMRIIPORTIT(addr))
                    connectionSocket.send(("Klienti eshte duke perdorur portin:"+NUMRIIPORTIT(addr)).encode())

            # metoda BASHKETINGELLORE
            elif kerkesaVargu[0]=="BASHKETINGELLORE":
                # largojme fjalen BASHKETINGELLORE nga kerkesa dhe ate string ia dergojm
                # metodes BASHKETINGELLORE
                fjaliaShenuar = kerkesaStr.replace(fjalaePare,"",1)
                rezultati = "Numri i bashketingelloreve ne fjaline \"" + fjaliaShenuar.strip() + "\" eshte: " + BASHKETINGELLORE(fjaliaShenuar.strip())
                SHTYPDERGESEN(addr[0],addr[1],rezultati)
                connectionSocket.send(rezultati.encode())
            # metoda PRINTO
            elif kerkesaVargu[0]=="PRINTIMI":
                fjaliaShenuar = kerkesaStr.replace(fjalaePare,"",1)
                SHTYPDERGESEN(addr[0],addr[1],PRINTIMI(fjaliaShenuar))
                connectionSocket.send(PRINTIMI(fjaliaShenuar).encode())
            # metoda HOST
            elif kerkesaVargu[0]=="EMRIIKOMPJUTERIT":
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    if EMRIIKOMPJUTERIT(addr)=="Emri i klientit nuk dihet":
                        SHTYPDERGESEN(addr[0],addr[1],"Emri i klientit nuk dihet")
                        connectionSocket.send(("Emri i klientit nuk dihet").encode())
                    else:
                        SHTYPDERGESEN(addr[0],addr[1],"Emri i klientit eshte: "+EMRIIKOMPJUTERIT(addr))
                        connectionSocket.send(("Emri i klientit eshte: "+EMRIIKOMPJUTERIT(addr)).encode())
            # metoda TIME
            elif kerkesaVargu[0]=="KOHA":
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    SHTYPDERGESEN(addr[0],addr[1],KOHA())
                    connectionSocket.send(KOHA().encode())
            # metoda LOJA
            elif kerkesaVargu[0]=="LOJA":
                if(len(kerkesaVargu)>1):
                    error=True
                else:
                    SHTYPDERGESEN(addr[0],addr[1],"Rezultatet nga loja: "+LOJA())
                    connectionSocket.send(("Rezultatet nga loja: "+LOJA()).encode())
            # metoda FIBONACCI
            elif kerkesaVargu[0]=="FIBONACCI":
                # largojme hapesirat e panevojshme qe jane shenuar ne kerkese
                for i in range(len(kerkesaVargu)):
                    if "" in kerkesaVargu:
                        kerkesaVargu.remove("")
                # nese nuk jane vetem 2 parametra kthe gabim
                if len(kerkesaVargu)==1 or len(kerkesaVargu)>2:
                    error = True
                else:
                    if FIBONACCI(kerkesaVargu[1])=="Error":
                        error = True
                    else:
                        SHTYPDERGESEN(addr[0],addr[1],"Numri i "+kerkesaVargu[1]+" ne serine fibonacci eshte: "+str(FIBONACCI(kerkesaVargu[1])))
                        connectionSocket.send(("Numri i "+kerkesaVargu[1]+" ne serine fibonacci eshte: "+str(FIBONACCI(kerkesaVargu[1]))).encode())
            # metoda KONVERTO
            elif kerkesaVargu[0]=="KONVERTIMI":
                for i in range(len(kerkesaVargu)):
                    if "" in kerkesaVargu:
                        kerkesaVargu.remove("")
                # nese nuk jane saktesisht 3 parametra kthe gabim
                if len(kerkesaVargu)>3 or len(kerkesaVargu)<3:
                    error=True
                else:
                    if str(KONVERTIMI(str(kerkesaVargu[1]).upper(),kerkesaVargu[2]))=="Error":
                        error = True
                    else:
                        arrayPerShtypje = str(kerkesaVargu[1]).lower().split("to")
                        rezultati = kerkesaVargu[2] + " " + str(arrayPerShtypje[0]).capitalize() + " jane te barabarte me " + KONVERTIMI(str(kerkesaVargu[1]).upper(),kerkesaVargu[2]) + " " + str(arrayPerShtypje[1]).capitalize()
                        SHTYPDERGESEN(addr[0],addr[1],str(rezultati))
                        connectionSocket.send(str(rezultati).encode())


            elif kerkesaVargu[0]=="FAKTORETPRIMAR":
                if len(kerkesaVargu) != 2:  # nese jipet me shume se nje fjale si argument
                    error = True
                    connectionSocket.send("Ju lutem shenoni vetem 1 numer ".encode())

                elif kerkesaVargu[1]=="?":
                    connectionSocket.send(str("Sheno FAKTORETPRIMAR {HAPSIRE} numri -per te pare listen e numrave primar qe jane faktore te numrit te shenuar").encode())
                else:
                    for i in range(len(kerkesaVargu)):
                        if "" in kerkesaVargu:  # largo null karakterin
                            kerkesaVargu.remove("")

                    else:
                        SHTYPDERGESEN(addr[0],addr[1],str(FaktoretPrimar(kerkesaVargu[1])))
                        connectionSocket.send(FaktoretPrimar(kerkesaVargu[1]).encode())

            elif kerkesaVargu[0] == "ISMIRROR":
                if len(kerkesaVargu) != 2:  # nese jipet me shume se nje fjale si argument
                    error = True
                    connectionSocket.send("Ju lutem shenoni vetem 1 numer ".encode())

                elif kerkesaVargu[1] == "?":
                    connectionSocket.send(str(
                        "Sheno ISMIRROR {HAPSIRE} numri -per te pare se a eshte nje numer pasqyre ( a lexohet njejte nga te dy aney)").encode())
                else:
                    for i in range(len(kerkesaVargu)):
                        if "" in kerkesaVargu:  # largo null karakterin
                            kerkesaVargu.remove("")

                    else:
                        SHTYPDERGESEN(addr[0], addr[1], str(ISMIRROR(kerkesaVargu[1])))
                        connectionSocket.send(ISMIRROR(kerkesaVargu[1]).encode())







            # asnjera nga metodat lart
            else:
                connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())

            # nese ka error kthe mesazh
            if error==True:
                connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem rregulloni gabimin!".encode())
                error = False

        connectionSocket.close()

    # nese ka gabim, nuk mbyllet serveri por vetem shkeputet lidhja
    except Exception as e:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxERRORxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(str(e))
        connectionSocket.close()

# pranimi i kerkesave
# unaza eshte e pafundme pasi serveri perderisa eshte funksional
# duhet te jete ne gjendje te pranoj kerkesa tere kohen
while 1:
    # pranohet lidhja nga cilido klient qe i adresohet serverit permes localhost dhe 11000
    connectionSocket, addr = serverSocket.accept()
    print("**********************************LIDHJE***********************************")
    print('Klienti me IP adrese %s dhe numrin e portit %s sapo u lidh' %(addr))
    # startohet nje thread per tu marr me kerkesat e klientit perkates
    threading._start_new_thread(newClient,(connectionSocket,addr))
