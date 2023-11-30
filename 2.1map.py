#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:52:35 2023

@author: baderjelassi
"""

####        2.1 map
def display_map(m,d):
    for i in m:
        for j in i:
           print(d[j],end='')

        print()
    return


map = [[0,0,0,1,1],
        [0,0,0,0,1],
        [1,1,0,0,0],
        [0,0,0,0,0]]


dico = {0:' ',1:'#'}

display_map(map, dico)
