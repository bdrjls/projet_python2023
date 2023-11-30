#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:51:00 2023

@author: baderjelassi
"""

##### 4.1 Generation de la map 
import random
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
    nombre_mur=round((size_map[0]*size_map[1])*proportion_wall) 
    s=set() 
    for k in range(nombre_mur):
        while True: 
            i=random.randint(0,len(matrice)-1)
            j=random.randint(0,len(matrice[0])-1)
            if (i,j) not in s:   
                matrice[i][j]+=1 
                s.add((i,j))
                break
    return matrice 

