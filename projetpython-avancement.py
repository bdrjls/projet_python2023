#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:38:33 2023

@author: baderjelassi
"""

#######  2.1 map

def display_map(m,d):
    for i in m:
        for j in i:
           print(d[j],end='')

        print()
    return


map = [[1,0,0,1,1],
        [1,0,0,0,1],
        [1,1,0,0,0],
        [3,2,0,0,1]]


dico = {0:' ',1:'#',3:'X',2:' '}



###### 2.2 personnage

def create_perso(depart):
    perso={}
    perso['char']='o'
    perso['x']=depart[0]
    perso['y']=depart[1]
    print(perso)
    return 



def display_map_and_char(m,d,p):
    for i in range(len(m)):  ## cest des ccordonnees on parcours les coordonnees de la liste pour comparer
        for j in range(len(m[i])):
            if i==p["y"] and j==p["x"]: ### si nos coordonnes correspondee avc les x pour chaque colonnes et y pour chaque ligne du personnage on print le personnage (les coordonnes de x cest les colonnes et celle de y cest les lignes)
            
                print(p['char'],end='')
            else:
                print(d[m[i][j]],end='') #### sinon on print les caracteres du dico sans prendre en compte le personnage pour pas decaler
        print()### saut de ligne quand on a fini une ligne 
    return
    
p={"char":"o", "x":3, "y":1}   



##### 2.3 deplacement 

def updtate_p(letter,p): #### inversion des x et y pour nous 


    x=p['x']
    y=p['y']
    if letter=='d': #### pour aller a droite on ajoute 1 a x
        x+=1
    elif letter=='q': #### pour aller a gauche on enelve 1 
        x-=1
    elif letter=='s': ####pour descendre on ajoute a y 1 et pour monter on lui enleve 1
        y+=1
    elif letter=='z': ### pour pour monter on enleve 1 a y car il sagit des lignes pour remonter dans la matrice lindice diminue 
        y-=1
    else:
        print("erreur")
    p['x']=x ### MAJ du dico 
    p['y']=y
    print(p)
    return()
   

##### jouer a l'infini

def infini(m,d,p):
    while True:
        display_map_and_char(m,d,p)
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ")
        updtate_pbis(letter,p,m)
        
    return


#### 3.1 Sortir de la carte

def updtate_pbis(letter,p,m):
    #### inversion des x et y pour nous 
    x=p['x']
    y=p['y']
    if letter == "q" and x > 0: ### on verifie si on va a gauche quon est bien strictementsuperieur a 0 sinon on sort de la map en enlevant 1
        x -= 1
    elif letter == "z" and y > 0:  #### on va en haut on verifie la ligne a laquel on se situe avant de bouger 
        y -= 1
    elif letter == "d" and x < len(m[0])-1:  ###de meme si on veut alle a droite on verifie que la fin de la colonne nest pas atteinte mais le len(m[0]) etant superieur a lindice de la fin on lui enleve 1 
        x += 1
    elif letter == "s" and y< len(m)-1: ### de meme on verifie que lidnice y soit inferieur strictement a la longueur de la matrice(la ligne où on descend)
        y += 1

    p["x"]=x
    p["y"]=y

####  3.2 murs infranchisable

def updtate_bismurs(letter, p, m):
    x = p['x']
    y = p['y']

            

    if letter == "q" and x > 0 and m[y][x - 1] != 1: ### on va gauche et on verifie quil ny a pas de 1 dans la matrice une colonne avant dans la meme ligne 
        x -= 1
    elif letter == "z" and y > 0 and m[y - 1][x] != 1:  #### on va en haut et on verifie si lelement de la matrice une ligne au dessus dans la meme colonne ne contient pas de 1(mur)
        y -= 1
    elif letter == "d" and x < len(m[0])-1 and m[y][x + 1] != 1:  ### on verfie que que dans la meme ligne une colonne a droite on a pas de 1(mur) avant de bouger 
        x += 1
    elif letter == "s" and y < len(m)-1 and m[y + 1][x] != 1: ## de meme pour le bas avec une ligne en plus dans la mettrice pour la meme colonne 
        y += 1

    p["x"] = x
    p["y"] = y
    
def infini_bis(m,d,p):
    while True:
        display_map_and_char(m,d,p)
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ")
        updtate_bismurs(letter,p,m)
 ###### on reprend notre boucle infini avec notre focntion deux fois modifie updtate_bismur
 
 
 #### 3.4 objets a recolter
 
import random
def create_objects(nb_objets,m):
    s=set()  ### on declare un ensemble ppour y ajouter nos objets sous forme de tuple 
    for i in range(nb_objets):  ###on a un nombre dobjet (nb`_objet ) et on fais une boucle for pour en avoir autant
        n=random.randint(0,len(m)-1) #### on prend une valeur aleatoire pour les lignes comprise entre 0 e tla taille de la matrice -1 pour pas aller trop loin 
        v=random.randint(0,len(m[0])-1) #### on prend une valeur aleatoire pour les colonnes comprise entre 0 et la taille de la premiere colonne qui sera la meme taille que les autres -1 tjr pour pas aller trop loin 
        if m[n][v]==0: #### on verifie alors si dqns la matrice (map) on trouve un 0 on attribue cette coordonnees a notre objet 
            s.add((n,v)) ### on ajoute alors cette coordonnes dobjet a notre ensemble dobjet 
    return(s)


def display_map_and_char_objets(m,d,p,objet):
    d[3]="X"
    for i in range(len(m)):  ## cest des ccordonnees on parcours les coordonnees de la liste pour comparer
        for j in range(len(m[i])):
            if i==p["y"] and j==p["x"]:### si nos coordonnes correspondee avc les x pour chaque colonnes et y pour chaque ligne du personnage on print le personnage (les coordonnes de x cest les colonnes et celle de y cest les lignes)
                print(p['char'],end='')
            else:
                if m[i][j]==3:
                    print(d[3],end='')
                elif (i,j) in objet:
                    print('.',end='') #### on print lobjet 
                    
                else:
                    print(d[m[i][j]],end='')#### sinon on print les caracteres du dico sans prendre en compte le personnage pour pas decaler
        print()
    print("score",p['score'])
    return

#### 3.5 Ramasser les objets

def update_objects(p, objet):
    position = (p["y"], p["x"])##### on declare position dans la localisation du personnage 
    if position in objet: ### si cette position correspond a un des tuple dans objet alors on lenleve des objet car on est passé dessus 
        objet.remove(position)
        
def infini_objet(m,d,p,objet):#### on lance alors une boucle  infini tant quon larrrete pas, 
    while True:
        display_map_and_char_objets(m,d,p,objet)
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ")
        updtate_bismurs(letter,p,m)       
        update_objects(p, objet)
             
        
        
objet={(0, 1), (1, 3), (3, 1), (3, 2)}

#### 3.6 Afficher le score 

def create_persobis(depart):
    perso={}
    perso['score']=0
    perso['char']='o'
    perso['x']=depart[0]
    perso['y']=depart[1]
    return perso

def update_objects_bis(p, objet):
    position = (p["y"], p["x"])##### on declare position dans la localisation du personnage 
    if position in objet: ### si cette position correspond a un des tuple dans objet alors on lenleve des objet car on est passé dessus 
        p['score']+=1 ### on ajoute a notre score 1 comme on vient de ramasser
        objet.remove(position)###et on enelve lobjet
    print(p['score'])

def infini_objet_bis(m,d,p,objet):#### on lance alors une boucle  infini tant quon larrrete pas, 
    p['score']=0 ### on initialise si le score nexiste pas dans p en dehors de la boucle et pas directment dans (update_objects_bis) car la boucle ferait que a chaque fois le score soit 0 
    while True:
        display_map_and_char_objets(m,d,p,objet)
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ")
        updtate_bismurs(letter,p,m)       
        update_objects_bis(p, objet)


##### 4.1 Generation de la map 

def generate_random_map(size_map,proportion_wall):
    matrice=[]
    if proportion_wall<0 or proportion_wall>1:  ### on recommence dans la cas ou le nombre a virgule ne peu pas etre traité comme proportion 
        print("veuillez rentrer une valeur comprise entre 0 et 1")
        return #### on sarrete
    for i in range(size_map[0]):   #### on creer size_map[0] sous matrice avec rien dedans 
        matrice.append([])
    for i in matrice:
        for j in range(size_map[1]): ### on creer size_map[1] colonne dans chaque ligne 
            i.append(0) #### on y ajt des zeros 
    nombre_mur=round((size_map[0]*size_map[1])*proportion_wall) #### pour traiter le nombre de case ou il y aura des murs on arrondi pour avoir un entier 
    s=set() ### on creer un ensemble pour y ajouter nos tuple pour poouvoir disitnguer ceux quon a deja utiliser de ceux encore libre 
    for k in range(nombre_mur):
        while True: ### on se lance sur une boucle pour bien avoir le nombre exact de mur que lon veut 
            i=random.randint(0,len(matrice)-1)
            j=random.randint(0,len(matrice[0])-1)
            if (i,j) not in s:   ### la condition permet de continuer la boucle ou de la arreter pour chaque k jsuqua le nombre de mur 
                matrice[i][j]+=1 ### on ajoute 1 soit le mur en question 
                s.add((i,j)) ### on lajoute a lensemble pour ne plus utiliser la coordonnes 
                break ### on sarrete 

    return matrice ### en dehors e tt ca quand tout est ifni on retourne la matrice 
    
###### 4.2 Entrée et sortie du niveau 

def generate_random_mapbis(size_map,proportion_wall):
    matrice=[]
    if proportion_wall<0 or proportion_wall>1: #### on verifie que le proportion wall est compris entre 0 et 1 
        print("veuillez rentrer une valeur comprise entre 0 et 1") #### sinon on exige quil le soit 
        return ## on quitte 
    for i in range(size_map[0]): #### on prend la premiere valeur du tuple qui sera les lignes 
        matrice.append([]) ### on met autant de sous matrice vide quil ya de ligne 
    for i in matrice: #### la matrice etant cree avec ses sous matrices 
        for j in range(size_map[1]): ### pour chaquee colonne dont le nombre est size_map[1] 
            i.append(0) ###on ajoute dans la sous matrice autant de zero 
    n=random.randint(0,len(matrice)-1)  #### on prend un point aleatoire compris entre 0 et taille de la matrice pour les lignes 
    m=random.randint(0,len(matrice[0])-1) ### on prend un point aleatoire pour laes colonnes compris entre 0 et la taille de la premiere sous matrice 
    matrice[n][m]+=2 ### on lui ajoute 2 lentrée
    while True: #### on ouvre une boucle pour la sortie 
        n=random.randint(0,len(matrice)-1) ### on repete la meme operation 
        m=random.randint(0,len(matrice[0])-1) #### de meme 
        if matrice[n][m]!=2: ### on verifie que les coordonnes ne correspondent pas a lentrée 
            matrice[n][m]+=3 ### si cest le cas on y ajoute 3 poyr la sortie 
            break ### on sarrete on a alors une matrice rempli de 0 un 2 et un 3 
    nombre_mur=round(size_map[0]*size_map[1]*proportion_wall) #### on introduit le nombre de mur avec une multiplication et on larrondi pour avoir un nombre de mur exact 
    s=set() ###on introduit un ensemble vide pour y mettre les tuples quon va utiliser pour chaque mur 
    for k in range(nombre_mur): ### une boucle for pour k range(nombre mur)
        while True: ### on ouvree une boucle while pour chaque k pour nen laisser aucunet avoir exactement le nombre de mur voulu 
            i=random.randint(0,len(matrice)-1) #### on repars sur un choix aleatoire pour les lignes 
            j=random.randint(0,len(matrice[0])-1) #### on repars sur un choix aleatoire pour les colonnes 
            if (i,j) not in s and matrice[i][j]==0: ### on emet une condition sur le tuple quon a eu aleatoirement et son appartenance a lensemble ou non avec la condititon en plus les coordonnes dans la matrice pour avoir une case "vide"
                matrice[i][j]+=1 ### si tout ca est verifié on ajoute 1 a la case pour un mur sinon on recommence le choix aleatoire pour un meme k 
                s.add((i,j)) ### on ajoute nos coordonnees a s pour les vereouillés 
                break ### et on arrete cette boucle seulement pour le k donnée le reste veant apres 

    return matrice #### on retourne notre nouvelle matrice quon va utiliser 

def create_new_level(p,m,obj,size_map,proportion_wall):
    m[:]=generate_random_mapbis(size_map,proportion_wall) ### on modifie alors la matrice de base (celle de lancien niveau) par une autre 
    nb_objets=random.randint(0,size_map[0]*size_map[1]-round((size_map[0]*size_map[1])*proportion_wall)) #### pour creer un nouveau niveau on a besoin dun nombre dobjet quon va avoir aleatoirement qui sera le reste parce que les murs sont deja inclus dans le nombre de case de la matrice 
    obj=create_objects(nb_objets,m)#### on cree a nouveau des objet on modifie alors la valeur de obj 
    for i in range(len(m)-1):
        for j in range(len(m[0])-1):
            if m[i][j]==2: #### pour les coordonnes dans la matrice si a un moment on trouve un 2 qui est unique 
                p['x']=j #### il devient alors les coordonnes du personnage
                p['y']=i
    return ### on retourne simplememnt 

def infini_objet_ter(m,d,p,objet):#### on lance alors une boucle  infini tant quon larrrete pas, 
    p['score']=0 ### on initialise si le score nexiste pas dans p en dehors de la boucle et pas directment dans (update_objects_bis) car la boucle ferait que a chaque fois le score soit 0 
    while True: ##### tant quon ne sarrete pas 
        display_map_and_char_objets(m,d,p,objet) #### on utilise la fonction qui va nous afficher la map avec les objets etc 
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ") #### on laisse lutilisateur
        updtate_bismurs(letter,p,m)       #### on regarde pour les murs et on met a jour 
        update_objects_bis(p, objet) ### pour la collecte des objets ausssi on maj
        if m[p['y']][p['x']]==3: #### si on atteint la sortie 
            size_map=(random.randint(1,50),random.randint(1,50)) ### on recupere une nouvelle taille de map aleatoire 
            proportion_wall=random.random()### une proportion de murs aleatoire comprise entre 0 et 1 
            create_new_level(p,m,objet,size_map,proportion_wall) ### et avec on cree un nouveau niveau avec les objets etc 
            continue #### et on continue 
        
        
###### 4.3 Ajout de bombes 

def delete_all_walls(m, pos): 
    proxi= {(pos[0]-1, pos[1]-1), (pos[0], pos[1]-1), (pos[0]+1, pos[1]-1) ##### on creer un ensemble contenant toutes les valeurs a proximite du personnage 
            ,(pos[0]-1, pos[1]),(pos[0]+1, pos[1]),(pos[0]-1, pos[1]+1),
            (pos[0], pos[1]+1), (pos[0]+1, pos[1]+1)}

    for i in proxi: #### pour chaque tuple qui entoure le personnage on emet des conditions 
        if 0 <= i[0] < len(m[0]) and 0 <= i[1] < len(m) and m[i[1]][i[0]]!=3: #On test si il s'agit d'un mur ou non et il ne faut pas suppimer la sortie 
            m[i[1]][i[0]]=0 ####on remplace la valeur par 0  
    return 
            
def updtate_bisbombes(letter, p, m):
    x = p['x']
    y = p['y']

            

    if letter == "q" and x > 0 and m[y][x - 1] != 1: ### on va gauche et on verifie quil ny a pas de 1 dans la matrice une colonne avant dans la meme ligne 
        x -= 1
    elif letter == "z" and y > 0 and m[y - 1][x] != 1:  #### on va en haut et on verifie si lelement de la matrice une ligne au dessus dans la meme colonne ne contient pas de 1(mur)
        y -= 1
    elif letter == "d" and x < len(m[0])-1 and m[y][x + 1] != 1:  ### on verfie que que dans la meme ligne une colonne a droite on a pas de 1(mur) avant de bouger 
        x += 1
    elif letter == "s" and y < len(m)-1 and m[y + 1][x] != 1: ## de meme pour le bas avec une ligne en plus dans la mettrice pour la meme colonne 
        y += 1
    elif letter =='e': ### on applique la focntion delete
        delete_all_walls(m,(x,y)) 
    p["x"] = x #### maj des coordonnees
    p["y"] = y
    
def infini_objet_terbombes(m,d,p,objet):#### on lance alors une boucle  infini tant quon larrrete pas, 
    p['score']=0 ### on initialise si le score nexiste pas dans p en dehors de la boucle et pas directment dans (update_objects_bis) car la boucle ferait que a chaque fois le score soit 0 
    while True: ##### tant quon ne sarrete pas 
        display_map_and_char_objets(m,d,p,objet) #### on utilise la fonction qui va nous afficher la map avec les objets etc 
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ") #### on laisse lutilisateur
        updtate_bisbombes(letter,p,m)       #### on regarde pour les murs et on met a jour 
        update_objects_bis(p, objet) ### pour la collecte des objets ausssi on maj
        if m[p['y']][p['x']]==3: #### si on atteint la sortie 
            size_map=(random.randint(1,50),random.randint(1,50)) ### on recupere une nouvelle taille de map aleatoire 
            x=1
            while x>0.5: #### on force le nombre de mur a etre inferieur a 0,5 pour ne pas en abuser 
                x=random.random()
                if x<0.5:
                    proportion_wall=x### une proportion de murs aleatoire comprise entre 0 et 1 
            create_new_level(p,m,objet,size_map,proportion_wall) ### et avec on cree un nouveau niveau avec les objets etc 
            continue #### et on continue 


