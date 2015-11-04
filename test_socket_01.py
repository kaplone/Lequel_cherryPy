import socket, sys

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion_principale.bind(('192.168.0.201', 12800))
except socket.error:
    print("La liaison du socket a l'adresse choisie a Echoue.")
    sys.exit()
    
while 1:
    print("Serveur pret, en attente de requetes ...")
    connexion_principale.listen(5)
    connexion, adresse = connexion_principale.accept()
    print("Client connecte, adresse IP %s, port %s" % (adresse[0], adresse[1]))
    
    connexion.send("Vous etes connecte au serveur Marcel. Envoyez vos messages.")
    msgClient = connexion.recv(1024)
    
    while 1:
        print("C>", msgClient)
        if msgClient.upper() == "FIN" or msgClient =="":
               break
        msgServeur = raw_input("S> ")
        connexion.send(msgServeur)
        msgClient = connexion.recv(1024)
        
        # 6) Fermeture de la connexion :
        connexion.send("Au revoir !")
        print("Connexion interrompue.")
        connexion.close()
        
        ch = raw_input("<R>ecommencer <T>erminer ? ")
        if ch.upper() =='T':
            break
    
