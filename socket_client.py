import socket, sys

conn_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
	conn_avec_serveur.connect(('192.168.0.201', 12800))
except socket.error :
	print("la connection a echoue")
	sys.exit()
	
print("la connexion a ete etablie avec le serveur")

msgsrv = conn_avec_serveur.recv(1024)

while 1:
	if msgsrv.upper() == "FIN" or msgsrv == "":
		break
	print("S>", msgsrv)
	msgcl = raw_input("C> ")
	conn_avec_serveur.send(msgcl)
	msgsrv = conn_avec_serveur.recv(1024)
	
print("connexion interrompue")
conn_avec_serveur.close() 
