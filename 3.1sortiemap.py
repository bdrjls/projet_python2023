#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:36:59 2023

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
#### 3.1 Sortir de la carte

def updtate_pbis(letter,p,m):
    x=p['x']
    y=p['y']
    if letter == "q" and x > 0: 
        x -= 1
    elif letter == "z" and y > 0:   
        y -= 1
    elif letter == "d" and x < len(m[0])-1:  
        x += 1
    elif letter == "s" and y< len(m)-1: 
        y += 1

    p["x"]=x
    p["y"]=y
#### test 
updtate_pbis('z',p,map)
display_map_and_char(map,dico,p),print("rien ne se passe")
print()
updtate_pbis('q',p,map)
display_map_and_char(map,dico,p),print("la non plus")
print()
updtate_pbis('s',p,map)
display_map_and_char(map,dico,p),print("on bouge dans le carré ")