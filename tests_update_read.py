# -*- coding: utf-8 -*-

from pymongo import MongoClient
import re
import datetime

connexion = MongoClient()
base = connexion.Lequel
session = base.Lequel_V02
print("Connecté à Lequel_V02 : %d fichiers référencés dans la base\n" % session.count())

for x in session.find({}):  

    session.update(x, {"$set": {"chemin" : "/" + "/".join(x["parents"])}}, upsert=True)
    session.update(x, {"$set": {"chemin_pere" : "/" + "/".join(x["parents"][:-1])}}, upsert=True)

    session.update(x, {"$set": {"pere" : x["parents"][-2]}}, upsert=True)


for x in session.find({}):  
    try :
        session.update(x, {"$set": {"id_pere" : session.find_one({"$and" : [{"chemin" : x["chemin_pere"]}, {"fichier" : False}]})["_id"]}}, upsert=True)
    except TypeError:
        pass    
