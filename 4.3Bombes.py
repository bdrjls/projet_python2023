#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:43:13 2023

@author: baderjelassi
"""
p={"char":"o", "x":0, "y":0}
dico = {0:' ',1:'#',2:' ',3:'X'}
objet={(0, 2),(3,1),(3,2),(2,3)}
map = [[0,0,0,1,1],
        [1,0,0,0,1],
        [1,1,0,0,0],
        [3,2,0,0,1]]
import random
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

def update_objects_bis(p, objet):
    position = (p["y"], p["x"])
    if position in objet: 
        p['score']+=1 
        objet.remove(position)
def create_new_level(p,m,obj,size_map,proportion_wall):
        m[:]=generate_random_mapbis(size_map,proportion_wall)
        nb_objets=random.randint(0,size_map[0]*size_map[1]-round((size_map[0]*size_map[1])*proportion_wall)) 
        obj=create_objects(nb_objets,m)
        for i in range(len(m)-1):
                for j in range(len(m[0])-1):
                    if m[i][j]==2: 
                        p['x']=j 
                        p['y']=i
        return 
def create_objects(nb_objets,m):
    s=set()  
    for i in range(nb_objets):  
        n=random.randint(0,len(m)-1) 
        v=random.randint(0,len(m[0])-1) 
        if m[n][v]==0: 
            s.add((n,v)) 
    return(s)
def generate_random_mapbis(size_map,proportion_wall):
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


        
###### 4.3 Ajout de bombes 

def delete_all_walls(m, pos): 
    proxi= {(pos[0]-1, pos[1]-1), (pos[0], pos[1]-1), (pos[0]+1, pos[1]-1)
            ,(pos[0]-1, pos[1]),(pos[0]+1, pos[1]),(pos[0]-1, pos[1]+1),
            (pos[0], pos[1]+1), (pos[0]+1, pos[1]+1)}

    for i in proxi:  
        if 0 <= i[0] < len(m[0]) and 0 <= i[1] < len(m) and m[i[1]][i[0]]!=3: 
            m[i[1]][i[0]]=0 
    return 
            
def updtate_bisbombes(letter, p, m):
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
    
def infini_objet_terbombes(m,d,p,objet):
    p['score']=0 
    while True: 
        display_map_and_char_objets(m,d,p,objet) 
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ") 
        updtate_bisbombes(letter,p,m)
        update_objects_bis(p, objet) 
        if m[p['y']][p['x']]==3: 
            size_map=(random.randint(1,50),random.randint(1,50))
            x=1
            while x>0.5:
                x=random.random()
                if x<0.5:    
            proportion_wall=random.random()
            create_new_level(p,m,objet,size_map,proportion_wall) 
            continue
