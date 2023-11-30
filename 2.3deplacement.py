#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:08:57 2023

@author: baderjelassi
"""
map = [[0,0,0,1,1],
        [0,0,0,0,1],
        [1,1,0,0,0],
        [0,0,0,0,0]]


dico = {0:' ',1:'#'}
def display_map_and_char(m,d,p):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i==p["y"] and j==p["x"]:
            
                print(p['char'],end='')
            else:
                print(d[m[i][j]],end='') 
        print()
    return


##### 2.3 deplacement 
p={"char":"o", "x":0, "y":0} 
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


display_map_and_char(map,dico,p)
letter=input("Quel deplacement? : 'z'=haut ,'s'=bas , 'q'=gauche , 'd'=droite : ")
updtate_p(letter,p)
display_map_and_char(map,dico,p)


