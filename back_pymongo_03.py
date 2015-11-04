# -*- coding: utf-8 -*-

from pymongo import MongoClient
import re

connexion = MongoClient()
base = connexion.LequelFX
session = base.Lequel_V04
print("Connecté à Lequel_V04 : %d fichiers référencés dans la base\n" % session.count())

def requete(champ1) :
    return session.find({"$and" : [{"scanned.rang" : 0}, {"nom" : re.compile(champ1, re.IGNORECASE)}]}).sort("disque" ,1)

def requeteEt(champ1, champ2) :
    return session.find({"$and" : [{"scanned.rang" : 0}, {"nom" : re.compile(champ1, re.IGNORECASE)}, {"nom" : re.compile(champ2, re.IGNORECASE)}]})

def requeteOu(champ1, champ3) :
    return session.find({"$and" : [{"scanned.rang" : 0}, {"$or" : [{"nom" : re.compile(champ1, re.IGNORECASE)}, {"nom" : re.compile(champ3, re.IGNORECASE)}]}]})

def requeteSauf(champ1, champ7) :
    return session.find({"$and" : [{"scanned.rang" : 0}, {"nom" : re.compile(champ1, re.IGNORECASE)}, {"nom" : {"$not" : re.compile(champ7, re.IGNORECASE)}}]})
  
def requeteEtOu(champ1, champ2, champ3) :
    return session.find({"$and" : [{"scanned.rang" : 0}, {"$or" : [{"nom" : re.compile(champ1, re.IGNORECASE)}, {"nom" : re.compile(champ3, re.IGNORECASE)}]}, {"nom" : re.compile(champ2, re.IGNORECASE)}]})
  
def requeteEtsauf(champ1, champ2, champ7) :
    return session.find({"$and" : [{"scanned.rang" : 0}, {"$and" : [{"nom" : re.compile(champ1, re.IGNORECASE)}, {"nom" : {"$not" : re.compile(champ7, re.IGNORECASE)}}]}, {"nom" : re.compile(champ2, re.IGNORECASE)}]})
  
def requeteOuSauf(champ1, champ3, champ7) :
    return session.find({"$and" : [{"scanned.rang" : 0}, {"$or" : [{"$and" : [{"nom" : re.compile(champ1, re.IGNORECASE)}, {"nom" : {"$not" : re.compile(champ7, re.IGNORECASE)}}]}, {"nom" : re.compile(champ3, re.IGNORECASE)}]}]})
  
def requeteEtOuSauf(champ1, champ2, champ3, champ7) :
    return session.find({"$and" : [{"scanned.rang" : 0}, {"$or" : [{"$and" : [{"nom" : re.compile(champ1, re.IGNORECASE)}, {"nom" : {"$not" : re.compile(champ7, re.IGNORECASE)}}]}, {"nom" : re.compile(champ3, re.IGNORECASE)}]}, {"nom" : re.compile(champ2, re.IGNORECASE)}]})
    
