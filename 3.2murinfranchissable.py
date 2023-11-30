#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:47:47 2023

@author: baderjelassi
"""
map = [[0,0,0,1,1],
        [0,0,0,0,1],
        [1,1,0,0,0],
        [0,0,0,0,0]]
p={"char":"o", "x":0, "y":0}
dico = {0:' ',1:'#'}
def display_map_and_char(m,d,p):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i==p["y"] and j==p["x"]:
            
                print(p['char'],end='')
            else:
                print(d[m[i][j]],end='') 
        print()
        
####  3.2 murs infranchisable

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
    
def infini_bis(m,d,p):
    while True:
        display_map_and_char(m,d,p)
        letter=input("quel deplacement? (”z” (haut), ”q” (gauche), ”s” (bas), et ”d” (droite)): ")
        updtate_bismurs(letter,p,m)
        
        
infini_bis(map,dico,p)





