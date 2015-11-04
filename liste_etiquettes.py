#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, os.path

def etiquette(disque):
    
    num_disque = int(disque[:3])%10

    top = "/Volumes"
    
    motif_disque = '     <text:s text:c="3"/><text:span text:style-name="T1">%02d</text:span></text:p>\n' % num_disque
    motif_disque_ok = '     <text:s text:c="3"/><text:span text:style-name="T1">%s</text:span></text:p>\n     <text:p text:style-name="P4"><text:span text:style-name="T1"><text:s text:c="5"/>%s</text:span></text:p>\n     <text:p text:style-name="P4"><text:span text:style-name="T1"/></text:p>\n' % ("_".join(disque.split("_")[:-2]), "_".join(disque.split("_")[-2:]))
    
    motif_disque_foot = '     <text:p text:style-name="P4"><text:span text:style-name="T1"><text:s text:c="5"/>%s</text:span></text:p>\n     <text:p text:style-name="P4"><text:span text:style-name="T1"><text:s text:c="5"/>%s</text:span></text:p>\n' % ("_".join(disque.split("_")[:-2]), "_".join(disque.split("_")[-2:]))
    
    motif_rep = """       <text:list-item>
        <text:p text:style-name="P1">%s</text:p>
       </text:list-item>\n"""
     
    bourrage = """     <text:p text:style-name="P3"/>\n"""
    
    if num_disque == 1 :
	fichier = open("/Volumes/PUBLIC/pour melissa/etiquettes/MODELE_DIX_V5.fodt", "r")
    else :
	fichier = open("/Volumes/PUBLIC/pour melissa/etiquettes/feuille_01.fodt", "r")    

    f = fichier.readlines()
    fichier.close()
    fichier_out = open("/Volumes/PUBLIC/pour melissa/etiquettes/feuille_01.fodt", "w")
    
    tab_modifs = []
    
    liste = sorted(os.listdir("/".join((top, disque))))
    for l in liste :
	if os.path.isdir("/".join((top, disque, l))) and l[0] != "." and l != "TheVolumeSettingsFolder" :
	    tab_modifs.append(l)
	    
    print(tab_modifs)
    
    i = 0
    compteur = 0
	    
    while i < len(f) :
	if f[i] == motif_disque :
	    fichier_out.write(motif_disque_ok)
	    i = i + 1
	    fichier_out.write(f[i])
	    for t in tab_modifs :
		if compteur < 12 :
		    fichier_out.write(motif_rep % t)
		    compteur = compteur + 1 + (len(t) / 20)
		
	    i = i + 1
	    fichier_out.write(f[i])
	    while compteur < 13 :
		fichier_out.write(bourrage)
		compteur = compteur + 1
	    fichier_out.write(motif_disque_foot)
	else :
	    fichier_out.write(f[i])
	i = i + 1
     
    fichier_out.close()
    
	    
	
    
