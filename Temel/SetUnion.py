# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:27:40 2020

@author: Bartu
"""

setA = {1,2,3,4}
setB= {1,2,4,5,6,7,8}
# Set Union (Eleman tekrarı yapmadan olanları yazıyor !)
print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))
print("**********************")
# Set Intersection (Ortak olanları yazıyor !)
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))
print("**********************")
# Set Difference
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))
print("**********************")
# Set Symmetric Difference
print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
print("**********************")