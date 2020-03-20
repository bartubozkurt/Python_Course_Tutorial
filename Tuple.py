# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:27:40 2020

@author: Bartu
"""

# Tuple 
""" Listere benzerdir.
    Tek farkı listelerde elemanları degiştirebiliyorken
    tuple'da degiştirmek söz konusu degildir.
    Bu veri yapısı performanslı bir data saglar.
"""
print("------------------------------------")
tupleListe = (1,3,5,"Bartu",[2,4,6],(),0)
liste = [1,3,5,"Bartu",[2,4,6],(),0]

print(tupleListe[-3]) # Listeye Sağdan -1 den başlar!
print(liste[-3])

liste[1] = 66
#tupleListe[3] = "Bozkurt"      # tuple liste elemanı degişmez !!
                               # ReadOnly !!
print(type(tupleListe))
print(type(liste))
print(liste)
print(tupleListe)
print(len(tupleListe))
print(len(liste))