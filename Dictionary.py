# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:27:40 2020

@author: Bartu

Aynen set gibi sırasız veri tutar.
Günlük hayattaki sözlük gibi düşünebilirz apple : elma vs."""


engTrDic = {
        "book" : "kitap",
        "table": "masa",
        "apple":"elma"
        }
trEngDic = dict(kitap = "book", masa = "table", elma = "apple", pencil = "kalem")
print(engTrDic)
print(engTrDic["book"]) # Sözlük de book un karşılığı nedir ?
engTrDic["pencil"] = "kalem" # Sözlüğe kelime ekleme
del(engTrDic["book"])  # Sözlükten kelime silme
print(engTrDic)
print(len(engTrDic))


print("***************************")
print(trEngDic)
print(len(trEngDic))
