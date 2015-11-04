# -*- coding: utf-8 -*-

from pymongo import MongoClient
import re
import datetime

connexion = MongoClient()
base = connexion.Lequel
session = base.Lequel_V02
print("Connecté à Lequel_V02 : %d fichiers référencés dans la base\n" % session.count())

def requete(champ1) :
    return session.find({"nom" : re.compile(champ1, re.IGNORECASE)}).sort("disque" ,1)
    
    


for x in requete("clementville"):
    for y in x.keys():
        print(y + " :"  + str(x[y]))
    print("\n")
