#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:25:59 2023

@author: baderjelassi
"""
map = [[0,0,0,1,1],
        [0,0,0,0,1],
        [1,1,0,0,0],
        [0,0,0,0,0]]


dico = {0:' ',1:'#'}
p={"char":"o", "x":0, "y":0} 
def display_map_and_char(m,d,p):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i==p["y"] and j==p["x"]:
            
                print(p['char'],end='')
            else:
                print(d[m[i][j]],end='') 
        print()
    return
def updtate_p(letter,p): 
    x=p['x']
    y=p['y']
    if letter=='d': 
        x+=1
    elif letter=='q': 
        x-=1
    elif letter=='s': 
        y+=1
    elif letter=='z':  
        y-=1
    else:
        print("erreur")
    p['x']=x 
    p['y']=y
    return()

##### jouer a l'infini

def infini(m,d,p):
    while True:
        display_map_and_char(m,d,p)
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ")
        updtate_p(letter,p)
        
    return

infini(map,dico,p)






