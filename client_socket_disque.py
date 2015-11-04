# -*- coding: utf-8 -*-
import socket, sys

class Socket:
    
    def __init__(self):
	
	self.conn_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try :
		self.conn_avec_serveur.connect(('192.168.0.201', 12800))
	except socket.error :
		print("la connection au serveur disque a echoue")
		sys.exit()

    def envoiDisque(self, disque):

	self.conn_avec_serveur.send(disque)
	
    def ecouteDisque(self):

	return self.conn_avec_serveur.recv(1024)
	

	
    def close(self):
	self.conn_avec_serveur.close() 
