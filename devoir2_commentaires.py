### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

### Bravo pour un autre script très bien documenté! :)

'''
Script Python sur le Fonds du Canada pour les périodiques de Patrimoine canadien
Titre: EDM5240-devoir2_GGelinas
Réalisé par Geneviève Gélinas / GELG19608607 / dans le cadre du cours EDM5240 - Technologie de l'information appliquée au journalisme
Date de réalisation: Lundi 19 février 2017
Description général du script: 
  - Lire le fichier grants.csv et afficher uniquement les lignes relatives aux subventions octroyées 
  dans le cadre des différents programmes du Fonds du Canada pour les périodiques.
  - Ensuite, ajouter, au passage, une colonne correspondant à l'année au cours de laquelle la subvention a été octoyée.
'''

#coding: utf-8

import csv

### L'import ci-dessous fait planter ton script; je le mets en commentaire...
# from devoir2 import grants.csv

### L'import ci-dessous est intéressant... mais «.append()» fait le même travail
from collections import deque #Permettra d'intégrer une nouvelle colonne positionnée en début d'une liste.

### Je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

fichier="../grants.csv"

f1=open(fichier, newline='', encoding="utf8")
reader=csv.reader(f1)
next(reader)#Permet de sauter la première ligne du fichier csv car souvent elle contient les entêtes des colonnes.

#header=next(reader)
#print (header)
'''
# row = ['\ufeffref_number', 'prog_number', 'prog_name_en', 'prog_name_fr', 'proj_number', 'proj_name_en', 'proj_name_fr', 
    'recipient_name_en', 'recipient_name_fr', 'recipient_business_number', 'recipient_country', 'recipient_region_en', 
    'recipient_region_fr', 'date', 'value', 'type', 'purpose_en', 'purpose_fr', 'comments_en', 'comments_fr', 'additional_info_en',
    'additional_info_fr', 'owner_org', 'owner_org_title']
'''
#print(len(header)) #Permet de compter le nombre d'index du header.

#Une boucle avec une condition intégrée qui permet de lire le fichier complet en demandant de chercher, à partir de l'index 17, les mots 'Fonds', 'Canada' et 'périodiques'
#pour ainsi cibler seulement les lignes qui relatent le Fonds du Canada pour les périodiques.
#Ensuite, un compteur a été ajouté pour faire le décompte total de ces dernières lignes et sera ajouté à l'affichage final.
#Un .appendleft() a été ajouté en utilisant le module 'deque' pour ajouter une colonne en début de fichier qui indique l'année au cours de laquelle la subvention a été octoyée.
#Un .join() permet de transformer une liste en string en faisant une concaténation des éléments pour faciliter la lecture en éliminant les guillemets, espaces, virgules, etc.
#Ce qui permet de peaufiner l'affichage en y insérant l'index[0] de row qui correspond à l'année en début d'affichage et ensuite y insérer les lignes "nettoyées".
#Un dernier print permet d'afficher le décompte total mentionné ci-dessus.

n=0

for row in reader:

### Intéressante méthode pour trouver les lignes relatives au Fonds du Canada pour les périodiques
### Pourquoi tester trois mots différents, alors que tu aurais pu écrire:
### «joly (ou n'importe quel autre nom de variable) = row[17].find("Fonds du Canada pour les périodiques")»

    findfonds=row[17].find("Fonds")
    findcanada=row[17].find("Canada")
    findperiodiques=row[17].find("périodiques")

### J'ai écrit la ligne ci-dessous pour tester
    joly  = row[17].find("Fonds du Canada pour les périodiques")
    # print(findfonds,findcanada,findperiodiques)



    if findfonds != -1 and findcanada != -1 and findperiodiques != -1:

### Toujours mon test. Il est concluant.
    # if joly != -1:
        n+=1
        row=deque(row)

### Tu as la bonne façon d'isoler l'année
### Intrigante façon de l'ajouter à ta «row».
### «annee = row[13][:4]»
### «row.append(annee)»
### pourraient plus simplement faire le travail

        row.appendleft(row[13][0:4])
        nettoyage=' '.join(row)
        print(row[0], "/", nettoyage[5:])

print ("\nIl y a", n, "lignes relatives aux subventions octoyées dans le cadre des différents programmes du Fonds du Canada pour les périodiques.")

### Très bonne idée que de nous dire combien de subventions ton script trouve: 2494.
### Il en manque cependant. Des subventions étaient identifiées par l'acronyme FCP.
### Ici, un if double, à l'aide d'un «or», permettait de trouver ce qu'on cherchait:
### «if "Fonds du Canada pour les périodiques" in row[17] or "FCP -" in row[17]:»