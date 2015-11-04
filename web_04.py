# -*- coding: utf-8 -*-

import random
import string

import cherrypy
import back_pymongo_03 as back_pm

class StringGenerator(object):
    
    
    
    def prettify(self, liste):
        if len(liste[1:-1]) == 0:
            return "[RACINE DU DISQUE]"
        sortie = ""
        for l in liste[1:-1] :
            sortie += "[%s] " %l
        return sortie
    
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
              <style>
             
                body
                {
                    font-family: sans-serif;
                }
                
                form
                {
                    font-size: 1.1em;
                }
             </style>

          </head>
          <body>
            <form method="get" action="selection">
              <p>Recherche (dans le nom de fichier uniquement) <input type="text" name="motif" />
              et  <input type="text" name="et" />
               ou  <input type="text"  name="ou" />
               sauf  <input type="text" name="sauf" />
              <button type="submit">Afficher</button></p>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def selection(self, motif, et, ou, sauf):

        if et.strip() != "":
            if ou.strip() != "":
                if sauf.strip() != "":
                    resultat = back_pm.requeteEtOuSauf(motif,et, ou, sauf)
                else :
                    resultat = back_pm.requeteEtOu(motif,et, ou)
            else :
                if sauf.strip() != "":
                    resultat = back_pm.requeteEtSauf(motif,et, sauf)
                else :
                    resultat = back_pm.requeteEt(motif,et)
                
        else :
            if ou.strip() != "":
                if sauf.strip() != "":
                    resultat = back_pm.requeteOuSauf(motif, ou, sauf)
                else :
                    resultat = back_pm.requeteOu(motif, ou)
            else :
                if sauf.strip() != "":
                    resultat = back_pm.requeteSauf(motif, sauf)
                else :
                    resultat = back_pm.requete(motif)
                    
        print "__", resultat.explain(), "__"
        print resultat.explain()["executionStats"]["executionTimeMillis"]
        
        #taille_base = explain["nscannedAllPlans"]
        #taille_retour = explain["n"]    
        #duree_requete = explain["millis"] / 1000.0
        taille_base = resultat.explain()["executionStats"]["totalKeysExamined"]
        taille_retour = resultat.explain()["executionStats"]["nReturned"]    
        duree_requete = resultat.explain()["executionStats"]["executionTimeMillis"] / 1000.0
                    
        print("liste recue")
        
        r_disque_precedent = None
        
        
        tableau = ""
        for r in resultat:
            r_disque_en_cours = r["chemin"].split("/")[1]
            if r_disque_en_cours == r_disque_precedent or r_disque_precedent == None :
                tableau += """
                <tr> 
                <td>%s</td> 
                <td>%s</td> 
                <td>%s</td> 
                <td>%s</td> 
                </tr> 
                """ %(r_disque_en_cours, self.prettify(r["chemin"].split("/")), r["nom"], r["taille"])
                r_disque_precedent = r_disque_en_cours
            else :
                tableau += """
                <tr> 
                <td colspan="4" style="background:#ccc"></td> 
                </tr> 
                <tr> 
                <td>%s</td> 
                <td>%s</td> 
                <td>%s</td> 
                <td>%s</td> 
                </tr> 
                """ %(r_disque_en_cours, self.prettify(r["chemin"].split("/")), r["nom"], r["taille"])
                r_disque_precedent = r_disque_en_cours
                
            
        print("boucle terminee")
        
        return u"""<html>
          <head>
             <style>
             
                body
                {
                    font-family: sans-serif;
                }
                
                form
                {
                    font-size: 1.1em;
                }
                
                table, td, th
                {
                    padding: 5px;
                    height: 15px;
                    border: 1px solid black;
                    border-collapse: collapse;
                    font-size: 0.95em;
                }
                
                th
                {
                    background:#ccc;
                }
                tr:nth-child(even) {
                    /*background-color: #CEECF5;*/
                }
             </style>

          </head>
          <body>
          <form method="get" action="selection">
              <p>Recherche (dans le nom de fichier uniquement) <input type="text" name="motif" value="%s" />
               et  <input type="text" name="et" value="%s" />
               ou  <input type="text"  name="ou" value="%s" />
               sauf  <input type="text" name="sauf" value="%s" />
              <button type="submit">Afficher</button></p>
            </form>
            <p>Taille de la base : <strong>%d</strong> éléments enregistrés (dans LequelFX.LequelFX_V04)</p>
            <p>Résultats de la requête : <strong>%d</strong> réponses trouvées en <strong>%.3f</strong> secondes</p>
            <table> 
                  <tr> 
                 <th> DISQUE </th> 
                 <th> CHEMIN </th> 
                 <th> NOM </th> 
                 <th> TAILLE (en octets) </th> 
                  </tr> 
                  %s
            </table> 
       </body>
        </html> """  % (motif, et, ou, sauf, taille_base, taille_retour, duree_requete, tableau)
        

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator(), config= "tuto.conf")
