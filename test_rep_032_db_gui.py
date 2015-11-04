# -*- coding: utf-8 -*-
import os, sys, os.path
import time
import datetime
import shutil
import subprocess
import pygtk, gtk
from gtk import glade
import gobject 

import filtre_count_002 as filtre_count
import client_socket_disque as client_di
import client_socket_dossier as client_do
import client_socket_fichier as client_fi

import liste_etiquettes as etiquettes

class Parcours() :
    
    def __init__(self):
        
        mount = subprocess.Popen("mount | grep /Volumes/", shell = True, stdout = subprocess.PIPE, bufsize = 1 , universal_newlines = True)
        mount_std = mount.stdout.readline()
        self.volume = mount_std.split(" on ")[1].split(" type ")[0]
	
	self.separateur = u'\u0002'
        #self.lancement(self.volume)
        
        
    
    
    def lancement(self, top) :
        
        self.top = '/'.join(("/Volumes", top))
	
	etiquettes.etiquette(top)
	
	sock_di.envoiDisque(self.top)
	print(self.top)
	while sock_di.ecouteDisque() != "OK" :
	    print(u"disque en attente")
	    time.sleep(0.001)
        #accesMongo.nouveauDisque(self.top)
        
        self.dico = {}
    
        self.dico[self.top] = {"dir" : os.listdir(self.top), "time" : time.ctime(os.stat(self.top)[8]), "full_dir" : []}
        for i in self.dico[self.top]["dir"]:
            self.dico[self.top]["full_dir"].append("/".join((self.top, i)))
        
        self.max_len = len(self.dico[self.top]["dir"])
        
        self.compteur = 0
        
        self.compteur_affichage = 0
        
        self.dico_des_done ={} #### s'occupera de fermer toutes les boucles proprement
        self.dico_des_done[self.top] = False
        
        self.dico_des_len = {self.top : [0, self.max_len]}
        self.parcours(self.top)
        
    def parcours(self, rep) :
        
        self.rep = rep
    
        while self.dico_des_done[self.rep] == False :
            
            ### gestion de la sortie de la boucle while generale
            if self.rep in self.dico[self.top]["full_dir"] :
                self.compteur += 1
                if self.compteur == self.max_len :
                    self.dico_des_done[self.top] = True
                
            self.dico_des_len[self.rep] = [0, len(self.dico[self.rep]["dir"])] ## traque la position dans la liste du contenu du repertoire
            
            if self.dico_des_done[self.top] == True :
                pass
            else :
                while self.dico_des_len[self.rep][0] < self.dico_des_len[self.rep][1] : ### tant qu'il y a du contenu a parcourir
  
                    t = self.dico[self.rep]["dir"][self.dico_des_len[self.rep][0]]
                    
                    if t[0] == "." :
                        self.dico_des_len[self.rep][0] +=1
                        
                        while self.dico_des_len[self.rep][0] == self.dico_des_len[self.rep][1]  and self.dico_des_done[self.rep] == False :
                            if self.dico_des_done[self.rep] == True:
                                pass
                            else :
                                self.dico_des_done[self.rep] = True
                                
                                if self.rep == self.top :
                                    break

                                self.rep = "/".join(self.rep.split("/")[:-1])
                                self.dico_des_len[self.rep][0] +=1
                    else :
                        
                        while gtk.events_pending():
                            gtk.main_iteration()
                        
                        self.compteur_affichage += 1
                        gui.progres.set_text("%d/%d" % (self.compteur_affichage, gui.total))
                        if self.compteur_affichage <= gui.total :
                            gui.progres.set_fraction(self.compteur_affichage / gui.total)
                        else :
                            break
                        
                        if os.path.isdir("/".join((self.rep, t))) : ### traitement des dossiers
                            
			    entree = "/".join((self.rep, t))
			    envoi = self.separateur.join((entree, self.getTailleFichier(entree), self.getDateCreation(entree)))
			    sock_do.envoiDossier(envoi)
			    while sock_do.ecouteDossier() != "OK" :
				print(u"dossier %s en attente" % t.decode('utf-8'))
				time.sleep(0.001)
                            #a = accesMongo.creerDossier(self.rep, t)
                            #accesMongo.ajouter(a)
                            
                            self.dico["/".join((self.rep, t))] = {"dir" : os.listdir("/".join((self.rep, t))), "time" : time.ctime(os.stat("/".join((self.rep, t)))[8]), "full_dir" : []}
                                
                            if len(self.dico["/".join((self.rep, t))]["dir"]) == 0 : ### prise en compte des dossiers vides
                                self.dico_des_len[self.rep][0] +=1
                            
                                while self.dico_des_len[self.rep][0] == self.dico_des_len[self.rep][1] and self.dico_des_done[self.rep] == False :
                                    if self.dico_des_done[self.rep] == True:
                                        pass
                                    else :
                                        self.dico_des_done[self.rep] = True
                                        
                                        if self.rep == self.top :
                                            break
    
                                        self.rep = "/".join(self.rep.split("/")[:-1])
                                        self.dico_des_len[self.rep][0] +=1
                        
    
                            else : ### prise en compte des sous-dossiers
                            
                                for i in self.dico["/".join((self.rep,t))]["dir"]:
                                    self.dico["/".join((self.rep, t))]["full_dir"].append("/".join((self.rep, i)))
                                self.dico_des_done["/".join((self.rep, t))] = False
                                if self.compteur == self.max_len :
                                    self.dico_des_done[self.rep] = True
                                else :
                                    self.parcours("/".join((self.rep, t)))
                    
                        elif os.path.isfile("/".join((self.rep, t))) : ### traitement des fichiers
                        
                            self.dico["/".join((self.rep,t))] = {"time" : time.ctime(os.stat("/".join((self.rep,t)))[8])}
                            
			    entree = "/".join((self.rep, t))
			    envoi = self.separateur.join((entree, self.getTailleFichier(entree), self.getDateCreation(entree)))
			    sock_fi.envoiFichier(envoi)
			    while sock_fi.ecouteFichier() != "OK" :
				print(u"fichier %s en attente" % t.decode('utf-8'))
				time.sleep(0.001)
                            #a = accesMongo.creerFichier(self.rep, t)
                            #accesMongo.ajouter(a)
                            
                            self.dico_des_len[self.rep][0] +=1
    
                            while self.dico_des_len[self.rep][0] == self.dico_des_len[self.rep][1]  and self.dico_des_done[self.rep] == False :
                                if self.dico_des_done[self.rep] == True:
                                    pass
                                else :
                                    self.dico_des_done[self.rep] = True
                                    
                                    if self.rep == self.top :
                                        break
    
                                    self.rep = "/".join(self.rep.split("/")[:-1])
                                    self.dico_des_len[self.rep][0] +=1
    
    
    def getTailleFichier(self, chemin):
    
	try :
	    taille = os.stat(chemin).st_size
	except OSError :
	    taille = 0
	    
	return str(taille)
	
	
    def getDateCreation(self, chemin):
    
	try :
	    date = datetime.datetime.fromtimestamp(os.path.getctime(chemin))
	except OSError :
	    date = None
	    
	return str(date)
        
def destroy(obj=None):
    sys.exit()
    
class Gui() :
    
    def __init__(self) :
        
        self.vbox = gui_mirror.get_widget("vbox1")
        self.hbox = gui_mirror.get_widget("hbox1")
        self.entry = gui_mirror.get_widget("comboboxentry1")
        self.bouton = gui_mirror.get_widget("button1")
        self.bouton_raf = gui_mirror.get_widget("button2")
        self.image = gui_mirror.get_widget("image1")
        self.progres = gui_mirror.get_widget("progressbar1")
        self.maj_liste(None)
        
    def maj_liste(self, r) :
        
        self.hbox.remove(self.entry)
        self.entry = gtk.combo_box_new_text()
        self.hbox.pack_start(self.entry, True, True, 2)
        self.hbox.reorder_child(self.entry, 0)
        
        self.dico = {}
        liste_index = 0
        
        for v in sorted(os.listdir("/Volumes")) :
            

            self.dico[liste_index] = v
            self.entry.append_text(v)
            liste_index +=1
            
        self.entry.set_active(0)
        self.vbox.show_all()
        
    def selection(self, t) :
        
        self.selectionne  = self.dico[self.entry.get_active()]
        self.selectionne_full = "/".join(("/Volumes", self.selectionne))

        self.total = float(filtre_count.filtre(self.selectionne_full))
        self.progres.set_text("0/%d" % self.total)
        
        parcours.lancement(self.selectionne)
    
     
gladefile = "/Users/db/MIRROR_V2/rep_mirror_04_.glade"
gui_mirror = glade.XML(gladefile, "window1")   

gui = Gui()
sock_di = client_di.Socket()
sock_do = client_do.Socket()
sock_fi = client_fi.Socket()
parcours = Parcours()


gui.bouton.connect("clicked", gui.selection)
gui.bouton_raf.connect("clicked", gui.maj_liste)

gtk.main()


### python test_socket_disque.py & python test_socket_dossier.py & python test_socket_fichier.py
### python test_3_sockets.py
