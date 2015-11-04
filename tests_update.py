# -*- coding: utf-8 -*-

from pymongo import MongoClient
import re
import datetime

connexion = MongoClient()
base = connexion.Lequel
session = base.Lequel_V02_test
print("Connecté à Lequel_V02_test : %d fichiers référencés dans la base\n" % session.count())

session.drop()

session.insert([{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 182000), u'taille': 434206777, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'modif final', u'V3_sommaireS2_43-(1024x576-UFF)_Animation .mov'], u'nom': u'V3_sommaireS2_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 30, 17, 14, 59)},
{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 188000), u'taille': 524237449, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'SOMMAIRE et COMMING NEXT', u'V1', u'S1', u'sommaireS1_43-(1024x576-UFF)_Animation .mov'], u'nom': u'sommaireS1_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 23, 12, 15, 50)},
{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 192000), u'taille': 415293140, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'SOMMAIRE et COMMING NEXT', u'V1', u'S2', u'sommaireS2_43-(1024x576-UFF)_Animation .mov'], u'nom': u'sommaireS2_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 23, 12, 15, 41)},
{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 196000), u'taille': 434620809, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'SOMMAIRE et COMMING NEXT', u'V1', u'S3', u'sommaireS3_43-(1024x576-UFF)_Animation .mov'], u'nom': u'sommaireS3_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 23, 12, 15, 52)},
{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 200000), u'taille': 510279230, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'SOMMAIRE et COMMING NEXT', u'V1', u'S4', u'sommaireS4_43-(1024x576-UFF)_Animation .mov'], u'nom': u'sommaireS4_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 23, 12, 16, 9)},
{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 204000), u'taille': 524124632, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'SOMMAIRE et COMMING NEXT', u'V2', u'S1', u'V2_sommaireS1_43-(1024x576-UFF)_Animation .mov'], u'nom': u'V2_sommaireS1_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 28, 12, 10, 12)},
{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 206000), u'taille': 410677184, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'SOMMAIRE et COMMING NEXT', u'V2', u'S2', u'V2_sommaireS2_43-(1024x576-UFF)_Animation .mov'], u'nom': u'V2_sommaireS2_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 28, 12, 9, 55)},
{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 209000), u'taille': 429700709, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'SOMMAIRE et COMMING NEXT', u'V2', u'S3', u'V2_sommaireS3_43-(1024x576-UFF)_Animation .mov'], u'nom': u'V2_sommaireS3_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 28, 12, 10, 2)},
{u'fichier': True, u'extension': u'mov', u'scan': datetime.datetime(2014, 4, 11, 11, 7, 39, 213000), u'taille': 468422286, u'disque': u'005_CASTO mai_2011', u'parents': [u'005_CASTO mai_2011', u'CONFO', u'EXPRESSO 43', u'SOMMAIRE et COMMING NEXT', u'V2', u'S4', u'V2_sommaireS4_43-(1024x576-UFF)_Animation .mov'], u'nom': u'V2_sommaireS4_43-(1024x576-UFF)_Animation ', u'date': datetime.datetime(2011, 6, 28, 12, 10, 10)},
{u'fichier': False, u'extension': u'', u'scan': datetime.datetime(2014, 4, 8, 18, 9, 18, 364000), u'taille': 238, u'disque': u'006_VALDAURELLE_nov_2012', u'parents': [u'006_VALDAURELLE_nov_2012', u'EDF', u'EDF TERRASSES', u'EDF salon des maires 2013 CAM fixe HDV'], u'nom': u'EDF salon des maires 2013 CAM fixe HDV', u'date': datetime.datetime(2013, 11, 26, 10, 46, 55)},
{u'fichier': False, u'extension': u'', u'scan': datetime.datetime(2014, 4, 8, 18, 9, 18, 368000), u'taille': 714, u'disque': u'006_VALDAURELLE_nov_2012', u'parents': [u'006_VALDAURELLE_nov_2012', u'EDF', u'EDF TERRASSES', u'EDF salon des maires 2013 CAM fixe HDV', u'Capture Scratch', u'EDFsalonmaires2013'], u'nom': u'EDFsalonmaires2013', u'date': datetime.datetime(2013, 11, 26, 10, 46, 55)},
{u'fichier': True, u'extension': u'fcp', u'scan': datetime.datetime(2014, 4, 8, 18, 9, 18, 398000), u'taille': 126196, u'disque': u'006_VALDAURELLE_nov_2012', u'parents': [u'006_VALDAURELLE_nov_2012', u'EDF', u'EDF TERRASSES', u'EDF salon des maires 2013 CAM fixe HDV', u'EDFsalonmaires2013.fcp'], u'nom': u'EDFsalonmaires2013', u'date': datetime.datetime(2013, 11, 26, 10, 46, 55)},
{u'fichier': False, u'extension': u'', u'scan': datetime.datetime(2014, 4, 8, 18, 9, 18, 405000), u'taille': 136, u'disque': u'006_VALDAURELLE_nov_2012', u'parents': [u'006_VALDAURELLE_nov_2012', u'EDF', u'EDF TERRASSES', u'EDF salon des maires cam 2'], u'nom': u'EDF salon des maires cam 2', u'date': datetime.datetime(2013, 11, 26, 10, 58, 27)},
{u'fichier': False, u'extension': u'', u'scan': datetime.datetime(2014, 4, 8, 18, 9, 18, 435000), u'taille': 136, u'disque': u'006_VALDAURELLE_nov_2012', u'parents': [u'006_VALDAURELLE_nov_2012', u'EDF', u'EDF TERRASSES', u'EDF salon des maires cam 2 suite et fin'], u'nom': u'EDF salon des maires cam 2 suite et fin', u'date': datetime.datetime(2013, 11, 26, 11, 4, 49)}])


def requete(champ1) :
    return session.find({"nom" : re.compile(champ1, re.IGNORECASE)}).sort("disque" ,1)
    
    

for x in session.find({}):  
    
    #try :
    #if x["fichier"] :
    session.update(x, {"$set": {"chemin" : "/" + "/".join(x["parents"])}}, upsert=True)
    session.update(x, {"$set": {"chemin_pere" : "/" + "/".join(x["parents"][:-1])}}, upsert=True)
        
    #else :
        #session.update(x, {"$set": {"chemin" : "/" + "/".join(x["parents"])}}, upsert=True)
        #session.update(x, {"$set": {"chemin_pere" : "/" + "/".join(x["parents"][:-1])}}, upsert=True)
    session.update(x, {"$set": {"pere" : x["parents"][-2]}}, upsert=True)
    #except KeyError :
        #pass

for x in session.find({}):  
    print(x)
    #if x["fichier"] :
    try :
        session.update(x, {"$set": {"id_pere" : session.find_one({"$and" : [{"chemin" : x["chemin_pere"]}, {"fichier" : False}]})["_id"]}}, upsert=True)
    except TypeError:
        pass    


for x in session.find({}):
    
    for y in x.keys() :
        print(y + " : " + str(x[y]) + "\n")
    print("\n")

