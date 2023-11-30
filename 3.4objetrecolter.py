#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:55:08 2023

@author: baderjelassi
"""
map = [[0,0,0,1,1],
        [0,0,0,0,1],
        [1,1,0,0,0],
        [0,0,0,0,0]]
p={"char":"o", "x":0, "y":0}
dico = {0:' ',1:'#'}

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
    
def infini_objet(m,d,p,objet):
    while True:
        display_map_and_char_objets(m,d,p,objet)
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ")
        updtate_bismurs(letter,p,m)

#### 3.4 objets a recolter

import random
def create_objects(nb_objets,m):
    s=set()  
    for i in range(nb_objets):  
        n=random.randint(0,len(m)-1) 
        v=random.randint(0,len(m[0])-1) 
        if m[n][v]==0: 
            s.add((n,v)) 
    return(s)


def display_map_and_char_objets(m,d,p,objet):
    for i in range(len(m)):  
        for j in range(len(m[i])):
            if i==p["y"] and j==p["x"]:
                print(p['char'],end='')
            else:
                if (i,j) in objet:
                    print('.',end='') 
                    
                else:
                    print(d[m[i][j]],end='')
        print()
    return

objet={(0, 1), (1, 3), (3, 1), (3, 2)}
infini_objet(map, dico, p,objet)

