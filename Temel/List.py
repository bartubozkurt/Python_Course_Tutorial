# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:27:40 2020

@author: Bartu
"""

ogrenciler = ["Bartu","Fatih","Hasan"]
ogrenciler[0] = "Veli"
print(ogrenciler[1])
ogrenciler.append("Osman")
ogrenciler.remove("Fatih")
print(ogrenciler)
sehirler = list(("Ankara", "İstanbul"))
print(sehirler)
print(len(sehirler))
print(len(ogrenciler))
print("-------------------------")

print (str(sehirler.count("İstanbul")))  # kaç adet istanbul var
print (str(sehirler.index("İstanbul"))) # kaçıncı indiste istanbul var
sehirler.pop(1) # O indisi çıkarır!
sehirler.insert(0,"İstanbul") # o indise ekle
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()
sehirler2 = sehirler
sehirler2[0] = "İzmir"

print(sehirler)             # ['Ankara', 'İstanbul']
print(sehirler2)            # ['İzmir', 'İstanbul']
print(sehirler3)            # ['Ankara', 'İstanbul']
                            


sehirler.extend(sehirler3) # ['İzmir', 'İstanbul', 'Ankara', 'İstanbul']
print(sehirler)

sehirler.sort() # sırala
sehirler.reverse() #ters çevir
print(sehirler)
