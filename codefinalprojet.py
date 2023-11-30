#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:58:35 2023

@author: baderjelassi
"""

##### Final
import random

#### creation perso:
    
def create_perso(depart):
    perso={}
    perso['char']='o'
    perso['x']=depart[0]
    perso['y']=depart[1]

    return perso
###============================================================================

##### fonction map et display map:
    
def display_map(m,d):
    for i in m:
        for j in i:
           print(d[j],end='')

        print()
    return

def display_map_and_char(m,d,p):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i==p["y"] and j==p["x"]:
            
                print(p['char'],end='')
            else:
                print(d[m[i][j]],end='') 
        print()

def display_map_and_char_objets(m,d,p,objet):
    for i in range(len(m)):  
        for j in range(len(m[i])):
            if i==p["y"] and j==p["x"]:
                print(p['char'],end='')
            else:
                if (i,j) in objet and m[i][j]!=1:
                    print('.',end='') 
                    
                else:
                    print(d[m[i][j]],end='')
        print()
    print(" ______________________ ")
    print("|                      |")
    print("|   objet ramassé:",p['score'],"  |")
    print("|______________________|")
    print()
    return
###============================================================================

##### focntion update:
    
def updtate_p(letter, p, m):
    x = p['x']
    y = p['y']
    if letter == "q" and x > 0 and m[y][x - 1] != 1:
        x -= 1
    elif letter == "z" and y > 0 and m[y - 1][x] != 1:  
        y -= 1
    elif letter == "d" and x < len(m[0])-1 and m[y][x + 1] != 1:  
        x += 1
    elif letter == "s" and y < len(m)-1 and m[y + 1][x] != 1: 
        y += 1
    elif letter =='e': 
        delete_all_walls(m,(x,y)) 
    p["x"] = x 
    p["y"] = y
    
def update_objects(p, objet):
    position = (p["y"], p["x"])
    if position in objet: 
        p['score']+=1 
        objet.remove(position)

###============================================================================
        
#### generer une map:
    
def generate_random_map(size_map,proportion_wall):
    matrice=[]
    if proportion_wall<0 or proportion_wall>1: 
        print("veuillez rentrer une valeur comprise entre 0 et 1") 
        return 
    for i in range(size_map[0]): 
        matrice.append([]) 
    for i in matrice: 
        for j in range(size_map[1]):  
            i.append(0) 
    n=random.randint(0,len(matrice)-1) 
    m=random.randint(0,len(matrice[0])-1) 
    matrice[n][m]+=2 
    while True: 
        n=random.randint(0,len(matrice)-1) 
        m=random.randint(0,len(matrice[0])-1) 
        if matrice[n][m]!=2: 
            matrice[n][m]+=3 
            break 
    nombre_mur=round(size_map[0]*size_map[1]*proportion_wall) 
    s=set() 
    for k in range(nombre_mur): 
        while True: 
            i=random.randint(0,len(matrice)-1) 
            j=random.randint(0,len(matrice[0])-1)  
            if (i,j) not in s and matrice[i][j]==0: 
                matrice[i][j]+=1 
                s.add((i,j)) 
                break 

    return matrice 
###============================================================================

#### focntion pour creer un objet et un nouveau niveau:

def create_objects(nb_objets,m):
    s=set()  
    for i in range(nb_objets):  
        n=random.randint(0,len(m)-1) 
        v=random.randint(0,len(m[0])-1) 
        if m[n][v]==0: 
            s.add((n,v)) 
            
def create_new_level(p,m,obj,size_map,proportion_wall):
    m[:]=generate_random_map(size_map,proportion_wall)
    nb_objets=random.randint(0,size_map[0]*size_map[1]-round((size_map[0]*size_map[1])*proportion_wall)) 
    obj=create_objects(nb_objets,m)
    for i in range(len(m)-1):
        for j in range(len(m[0])-1):
            if m[i][j]==2: 
                p['x']=j 
                p['y']=i

###============================================================================

### focntion supprimer mur:  
         
def delete_all_walls(m, pos): 
    proxi= {(pos[0]-1, pos[1]-1), (pos[0], pos[1]-1), (pos[0]+1, pos[1]-1)
            ,(pos[0]-1, pos[1]),(pos[0]+1, pos[1]),(pos[0]-1, pos[1]+1),
            (pos[0], pos[1]+1), (pos[0]+1, pos[1]+1)}

    for i in proxi:  
        if 0 <= i[0] < len(m[0]) and 0 <= i[1] < len(m) and m[i[1]][i[0]]!=3: 
            m[i[1]][i[0]]=0 
    return 
###============================================================================

##### boucle final: 

def infini(m,d,p,objet):
    p['score']=0 
    while True: 
        display_map_and_char_objets(m,d,p,objet) 
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ") 
        updtate_p(letter,p,m)
        update_objects(p, objet) 
        if m[p['y']][p['x']]==3: 
            size_map=(random.randint(1,50),random.randint(1,50)) 
            proportion_wall=random.random()
            create_new_level(p,m,objet,size_map,proportion_wall) 
            continue
