#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:21:06 2023

@author: baderjelassi
"""
map = [[0,0,0,1,1],
        [0,0,0,0,1],
        [1,1,0,0,0],
        [0,0,0,0,0]]
dico = {0:' ',1:'#'}

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

def updtate_bismurs(letter, p, m):
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

    p["x"] = x
    p["y"] = y
        
#### 3.6 Afficher le score 

def create_persobis(depart):
    perso={}
    perso['score']=0
    perso['char']='o'
    perso['x']=depart[0]
    perso['y']=depart[1]
    return perso

def update_objects_bis(p, objet):
    position = (p["y"], p["x"])
    if position in objet: 
        p['score']+=1 
        objet.remove(position)
    print(p['score'])

def infini_objet_bis(m,d,p,objet):
    while True:
        display_map_and_char_objets(m,d,p,objet)
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ")
        updtate_bismurs(letter,p,m)       
        update_objects_bis(p, objet)
        
objet={(0, 3), (1, 2), (3, 0), (3, 3)}
p=create_persobis((0,0))
infini_objet_bis(map,dico,p,objet)



        
        
        
        
        
        