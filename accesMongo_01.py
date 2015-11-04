import pymongo
import time
import datetime
#from datetime import date
import subprocess
import os
import os.path
import re

from pymongo import MongoClient

class Connexion():
    def __init__(self):
        
        self.client = MongoClient()
        self.db = self.client.test_rep_0
        self.collection = self.db.test10
        
mongo = Connexion()

def creerFichier(rep, fichier):
    disque = rep.split("/")[4]
    nom = fichier.split('.')[0]
    try:
        extension = fichier.split('.')[1]
    except IndexError :
        extension = ""
    parents = rep.split("/")[4:]
    taille = getTailleFichier("/".join((rep, fichier)))
    date = getDateCreation("/".join((rep, fichier)))
    scan = date.today()
    return {"disque" : disque,
            "scan" : scan,
            "fichier" : True,
            "nom" : nom,
            "extension" : extension,
            "parents" : parents,
            "taille" : taille,
            "date" : date}
    
def creerDossier(rep, dossier):
    disque = rep.split("/")[4]
    nom = dossier
    extension = ""
    parents =rep.split("/")[4:]
    taille = getTailleFichier("/".join((rep, dossier)))
    date = getDateCreation("/".join((rep, dossier)))
    scan = date.today()
    return {"disque" : disque,
            "scan" : scan,
            "fichier" : False,
            "nom" : nom,
            "extension" : extension,
            "parents" : parents,
            "taille" : taille,
            "date" : date}
    
def getTailleFichier(chemin):
    
    try :
        taille = os.stat(chemin).st_size
    except OSError :
        taille = 0
        
    return taille
    
    
def getDateCreation(chemin):

    try :
        date = datetime.datetime.fromtimestamp(os.path.getctime(chemin))
    except OSError :
        date = None
        
    return date



def ajouter(atome) :
    atome_id = mongo.collection.insert(atome)
    
    
def nouveauDisque(rep):
    
    disque_base = rep.split("/")[4]
    disque = disque_base
    try:
        disque_archive = mongo.collection.find({"disque" : re.compile(disque_base + "#", re.IGNORECASE)}).sort("$natural", pymongo.DESCENDING)[0]
        
        coupe = disque_archive["disque"].split("#")
        
        if coupe[1] != "":
            disque = disque + "#%04d" % (int(coupe[1]) + 1)
        else :
            disque = disque + "#%04d" % 1
            
    except IndexError:
        disque = disque + "#%04d" % 1
        
 
    mongo.collection.update({"disque": disque_base}, {"$set": {"disque": disque}})




