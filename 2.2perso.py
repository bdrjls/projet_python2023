#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:01:20 2023

@author: baderjelassi
"""

###### 2.2 personnage

def create_perso(depart):
    perso={}
    perso['char']='o'
    perso['x']=depart[0]
    perso['y']=depart[1]

    return perso

create_perso((0,0))


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
    

display_map_and_char(map, dico, p) 

