# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from pymongo.errors import CursorNotFound
import re
import sys
import datetime

connexion = MongoClient()
base = connexion.Lequel
session = base.Lequel_V02
print("Connecté à Lequel_V02 : %d fichiers référencés dans la base\n" % session.count())

compt = 0

for x in session.find({}):  
    print(compt)
    compt += 1
    
    try :

        session.update(x, {"$set": {"chemin" : "/" + "/".join(x["parents"])}}, upsert=True)
        session.update(x, {"$set": {"chemin_pere" : "/" + "/".join(x["parents"][:-1])}}, upsert=True)
    
        session.update(x, {"$set": {"pere" : x["parents"][-2]}}, upsert=True)
        
    except:
        
        print(x["_id"])

#compt = 0

#for x in session.find({"parents" : {"$size" : 4}}): 
    #print("%08d" % compt)
    #compt += 1
     
    #try :
        #session.update(x, {"$set": {"id_pere" : session.find_one({"$and" : [{"chemin" : x["chemin_pere"]}, {"fichier" : False}]})["_id"]}}, upsert=True)
    #except:
        #print(x["_id"])
        ##print(e)    
