import socket, sys

class Socket():
    
    def __init__(self):
	
	self.conn_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try :
		self.conn_avec_serveur.connect(('192.168.0.201', 12800))
	except socket.error :
		print("la connection a echoue")
		sys.exit()

    def envoiDisque(self, disque):

	self.conn_avec_serveur.send(0, disque)
	
    def envoiDossier(self, dossier):

	self.conn_avec_serveur.send(1, dossier)
	
    def envoiFichier(self, fichier):

	self.conn_avec_serveur.send(2, fichier)
	
    def close(self):
	self.conn_avec_serveur.close() 


