import os, os.path, sys
import shutil
import subprocess

def filtre(rep) :

    std_filtree = []
    
    filtre = subprocess.Popen('ls -R1 "%s"' %rep, shell =  True, stdout = subprocess.PIPE, bufsize = 1 , universal_newlines = True)
    
    std = filtre.stdout.readlines()
    
    
    hidden = False
    
    for x in std :
        if len(x.split("/")) > 1 :
            for element in x.split("/") :
                if element != "" :
                    if element[0] == "." :
                        hidden = True
                    
        elif x[:5] in ["", ".\n", "..\n"]:
            pass
        else :    
            if hidden == True :
                if x == "\n" :
                    hidden = False

            else:
                if x == "\n" :
                    pass
                else :
                    std_filtree.append(x)
    #print std_filtree
    return len(std_filtree)


